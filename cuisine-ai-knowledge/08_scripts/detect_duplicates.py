#!/usr/bin/env python3
"""Détecte les doublons exacts et les quasi-doublons dans des fichiers JSONL de règles cuisine."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


def expand_inputs(inputs: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw_input in inputs:
        path = Path(raw_input)
        if path.is_dir():
            files.extend(sorted(candidate for candidate in path.rglob("*.jsonl") if candidate.is_file()))
        elif path.suffix == ".jsonl" and path.is_file():
            files.append(path)
    unique_files: list[Path] = []
    seen: set[Path] = set()
    for file_path in files:
        resolved = file_path.resolve()
        if resolved not in seen:
            unique_files.append(file_path)
            seen.add(resolved)
    return unique_files


def normalize_text(value: str) -> str:
    lowered = value.casefold()
    lowered = re.sub(r"\s+", " ", lowered)
    lowered = re.sub(r"[^\w\s]", "", lowered)
    return lowered.strip()


def load_records(files: list[Path]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for file_path in files:
        with file_path.open("r", encoding="utf-8") as handle:
            for line_number, raw_line in enumerate(handle, start=1):
                if not raw_line.strip():
                    continue
                try:
                    record = json.loads(raw_line)
                except json.JSONDecodeError:
                    continue
                record["_file"] = str(file_path)
                record["_line"] = line_number
                record["_signature"] = normalize_text(record.get("titre", "")) + " || " + normalize_text(record.get("regle", ""))
                record["_title_norm"] = normalize_text(record.get("titre", ""))
                record["_rule_norm"] = normalize_text(record.get("regle", ""))
                records.append(record)
    return records


def exact_duplicates(records: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups[record["_signature"]].append(record)
    return [group for group in groups.values() if len(group) > 1]


def near_duplicates(records: list[dict[str, Any]], threshold: float) -> list[tuple[dict[str, Any], dict[str, Any], float]]:
    matches: list[tuple[dict[str, Any], dict[str, Any], float]] = []
    for index, left in enumerate(records):
        for right in records[index + 1 :]:
            if left["_signature"] == right["_signature"]:
                continue
            title_ratio = SequenceMatcher(None, left["_title_norm"], right["_title_norm"]).ratio()
            rule_ratio = SequenceMatcher(None, left["_rule_norm"], right["_rule_norm"]).ratio()
            average_ratio = (title_ratio + rule_ratio) / 2
            if average_ratio >= threshold:
                matches.append((left, right, average_ratio))
    return sorted(matches, key=lambda item: item[2], reverse=True)


def write_report(
    report_path: Path,
    files: list[Path],
    records: list[dict[str, Any]],
    exact_groups: list[list[dict[str, Any]]],
    near_matches: list[tuple[dict[str, Any], dict[str, Any], float]],
    threshold: float,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# Rapport de détection de doublons")
    lines.append("")
    lines.append(f"- Date : {date.today().isoformat()}")
    lines.append(f"- Fichiers analysés : {len(files)}")
    lines.append(f"- Enregistrements analysés : {len(records)}")
    lines.append(f"- Groupes de doublons exacts : {len(exact_groups)}")
    lines.append(f"- Paires de quasi-doublons : {len(near_matches)}")
    lines.append(f"- Seuil de similarité : {threshold:.2f}")
    lines.append("")

    lines.append("## Doublons exacts")
    lines.append("")
    if not exact_groups:
        lines.append("Aucun doublon exact détecté.")
    else:
        for group_index, group in enumerate(exact_groups, start=1):
            lines.append(f"### Groupe {group_index}")
            lines.append("")
            for record in group:
                lines.append(
                    f"- `{record.get('id', 'UNKNOWN')}` | {record.get('titre', '')} | {record['_file']}:{record['_line']}"
                )
            lines.append("")

    lines.append("## Quasi-doublons")
    lines.append("")
    if not near_matches:
        lines.append("Aucun quasi-doublon détecté.")
    else:
        for left, right, score in near_matches:
            lines.append(
                f"- `{left.get('id', 'UNKNOWN')}` <-> `{right.get('id', 'UNKNOWN')}` | score={score:.2f} | "
                f"{left['_file']}:{left['_line']} | {right['_file']}:{right['_line']}"
            )

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Détecte les doublons dans des règles cuisine.")
    parser.add_argument("paths", nargs="+", help="Fichiers JSONL ou répertoires contenant des fichiers JSONL.")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.88,
        help="Seuil de similarité pour les quasi-doublons. Défaut : 0.88",
    )
    parser.add_argument(
        "--report",
        default="07_tests/reports/duplicate_report.md",
        help="Chemin du rapport Markdown. Défaut : 07_tests/reports/duplicate_report.md",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    files = expand_inputs(args.paths)
    if not files:
        parser.error("Aucun fichier JSONL trouvé.")

    records = load_records(files)
    exact_groups = exact_duplicates(records)
    near_matches = near_duplicates(records, args.threshold)

    report_path = Path(args.report)
    write_report(report_path, files, records, exact_groups, near_matches, args.threshold)

    print(f"Analyse effectuée sur {len(files)} fichier(s) et {len(records)} enregistrement(s).")
    print(f"Groupes de doublons exacts : {len(exact_groups)}")
    print(f"Paires de quasi-doublons : {len(near_matches)}")
    print(f"Rapport écrit dans : {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
