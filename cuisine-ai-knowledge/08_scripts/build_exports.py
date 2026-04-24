#!/usr/bin/env python3
"""Construit les exports à partir des règles finales."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FINAL_DIR = ROOT / "04_rules" / "final"
EXPORTS_DIR = ROOT / "09_exports"
BY_DOMAIN_DIR = EXPORTS_DIR / "rules_by_domain"


def load_final_records() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for file_path in sorted(FINAL_DIR.rglob("*.jsonl")):
        with file_path.open("r", encoding="utf-8") as handle:
            for line_number, raw_line in enumerate(handle, start=1):
                if not raw_line.strip():
                    continue
                record = json.loads(raw_line)
                record["_source_file"] = str(file_path.relative_to(ROOT))
                record["_source_line"] = line_number
                records.append(record)
    records.sort(key=lambda item: (item["domaine"], item["sous_categorie"], item["id"]))
    return records


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    lines = [json.dumps(record, ensure_ascii=False) for record in records]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def build_index(records: list[dict[str, Any]]) -> dict[str, Any]:
    index: dict[str, Any] = {
        "generated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "total_rules": len(records),
        "domains": {},
    }
    by_domain: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_domain[record["domaine"]].append(record)

    for domain, items in sorted(by_domain.items()):
        by_sub_category: dict[str, int] = defaultdict(int)
        for item in items:
            by_sub_category[item["sous_categorie"]] += 1
        index["domains"][domain] = {
            "count": len(items),
            "sub_categories": dict(sorted(by_sub_category.items())),
            "rule_ids": [item["id"] for item in items],
        }
    return index


def build_markdown(records: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("# Corpus final des règles")
    lines.append("")
    if not records:
        lines.append("Aucune règle finale disponible.")
        return "\n".join(lines) + "\n"

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[record["domaine"]].append(record)

    for domain, items in sorted(grouped.items()):
        lines.append(f"## {domain}")
        lines.append("")
        for item in items:
            lines.append(f"### {item['id']} — {item['titre']}")
            lines.append("")
            lines.append(f"- Catégorie: `{item['categorie']}`")
            lines.append(f"- Sous-catégorie: `{item['sous_categorie']}`")
            lines.append(f"- Type: `{item['type_regle']}`")
            lines.append(f"- Niveau: `{item['niveau']}`")
            lines.append(f"- Fiabilité: `{item['fiabilite']}`")
            lines.append(f"- Règle: {item['regle']}")
            lines.append(f"- Conditions: {', '.join(item['conditions'])}")
            lines.append(f"- Application: {', '.join(item['application'])}")
            lines.append(f"- Erreurs fréquentes: {', '.join(item['erreurs_frequentes'])}")
            lines.append(f"- Exceptions: {', '.join(item['exceptions'])}")
            lines.append(f"- Usage agent: {', '.join(item['usage_agent'])}")
            lines.append("")
    return "\n".join(lines)


def strip_export_metadata(record: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in record.items() if not key.startswith("_")}


def main() -> int:
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    BY_DOMAIN_DIR.mkdir(parents=True, exist_ok=True)

    records = load_final_records()
    clean_records = [strip_export_metadata(record) for record in records]

    write_jsonl(EXPORTS_DIR / "rules_master.jsonl", clean_records)
    (EXPORTS_DIR / "rules_master.md").write_text(build_markdown(clean_records), encoding="utf-8")
    (EXPORTS_DIR / "rules_index.json").write_text(
        json.dumps(build_index(clean_records), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    by_domain: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in clean_records:
        by_domain[record["domaine"]].append(record)
    for domain, items in by_domain.items():
        write_jsonl(BY_DOMAIN_DIR / f"{domain}.jsonl", items)

    print(f"{len(clean_records)} règle(s) finale(s) exportée(s) dans {EXPORTS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
