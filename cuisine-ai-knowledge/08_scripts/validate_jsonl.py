#!/usr/bin/env python3
"""Valide des fichiers JSONL de règles cuisine selon les conventions du projet."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "id",
    "domaine",
    "categorie",
    "sous_categorie",
    "type_regle",
    "titre",
    "regle",
    "conditions",
    "application",
    "erreurs_frequentes",
    "exceptions",
    "niveau",
    "fiabilite",
    "usage_agent",
]

DOMAINES = {
    "cuisson",
    "ingredient",
    "assaisonnement",
    "sauce",
    "patisserie",
    "hygiene",
    "conservation",
    "substitution",
    "rattrapage",
    "organisation",
    "materiel",
    "nutrition_pratique",
    "enfants_famille",
    "batch_cooking",
    "anti_gaspillage",
}

TYPE_REGLE = {
    "principe",
    "procedure",
    "temperature",
    "temps",
    "erreur_a_eviter",
    "rattrapage",
    "substitution",
    "hygiene",
    "conservation",
    "adaptation",
    "diagnostic",
}

NIVEAU = {"fondamental", "intermediaire", "avance", "expert"}
FIABILITE = {"haute", "moyenne", "contextuelle"}
USAGE_AGENT = {
    "conseil_cuisson",
    "adaptation_recette",
    "generation_menu",
    "diagnostic_erreur",
    "substitution_ingredient",
    "securite_alimentaire",
    "optimisation_temps",
    "repas_enfants",
    "batch_cooking",
    "liste_courses",
    "gestion_restes",
    "anti_gaspillage",
}
STRING_FIELDS = {"id", "domaine", "categorie", "sous_categorie", "type_regle", "titre", "regle", "niveau", "fiabilite"}
ARRAY_FIELDS = {"conditions", "application", "erreurs_frequentes", "exceptions", "usage_agent"}
ID_PATTERN = re.compile(r"^[A-Z0-9]+(?:_[A-Z0-9]+)*_[0-9]{3}$")


@dataclass
class ValidationIssue:
    file_path: Path
    line_number: int
    message: str


def expand_inputs(inputs: list[str]) -> list[Path]:
    jsonl_files: list[Path] = []
    for raw_input in inputs:
        path = Path(raw_input)
        if not path.exists():
            raise FileNotFoundError(f"Chemin introuvable : {path}")
        if path.is_dir():
            jsonl_files.extend(sorted(candidate for candidate in path.rglob("*.jsonl") if candidate.is_file()))
        elif path.suffix == ".jsonl":
            jsonl_files.append(path)
    unique_files: list[Path] = []
    seen: set[Path] = set()
    for file_path in jsonl_files:
        resolved = file_path.resolve()
        if resolved not in seen:
            unique_files.append(file_path)
            seen.add(resolved)
    return unique_files


def validate_record(record: Any, file_path: Path, line_number: int) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if not isinstance(record, dict):
        return [ValidationIssue(file_path, line_number, "Chaque ligne doit contenir un objet JSON.")]

    for field in REQUIRED_FIELDS:
        if field not in record:
            issues.append(ValidationIssue(file_path, line_number, f"Champ obligatoire manquant : {field}"))

    for field in STRING_FIELDS:
        if field in record and not isinstance(record[field], str):
            issues.append(ValidationIssue(file_path, line_number, f"Le champ '{field}' doit être une chaîne."))
        elif field in record and not record[field].strip():
            issues.append(ValidationIssue(file_path, line_number, f"Le champ '{field}' ne doit pas être vide."))

    for field in ARRAY_FIELDS:
        if field in record and not isinstance(record[field], list):
            issues.append(ValidationIssue(file_path, line_number, f"Le champ '{field}' doit être un tableau."))
            continue
        if field in record:
            for index, item in enumerate(record[field], start=1):
                if not isinstance(item, str) or not item.strip():
                    issues.append(
                        ValidationIssue(file_path, line_number, f"L'élément #{index} du champ '{field}' doit être une chaîne non vide.")
                    )

    if record.get("domaine") and record["domaine"] not in DOMAINES:
        issues.append(ValidationIssue(file_path, line_number, f"Domaine inconnu : {record['domaine']}"))
    if record.get("id") and isinstance(record["id"], str) and not ID_PATTERN.match(record["id"]):
        issues.append(ValidationIssue(file_path, line_number, f"Format d'identifiant invalide : {record['id']}"))
    if record.get("type_regle") and record["type_regle"] not in TYPE_REGLE:
        issues.append(ValidationIssue(file_path, line_number, f"type_regle inconnu : {record['type_regle']}"))
    if record.get("niveau") and record["niveau"] not in NIVEAU:
        issues.append(ValidationIssue(file_path, line_number, f"Niveau inconnu : {record['niveau']}"))
    if record.get("fiabilite") and record["fiabilite"] not in FIABILITE:
        issues.append(ValidationIssue(file_path, line_number, f"Fiabilité inconnue : {record['fiabilite']}"))

    if isinstance(record.get("usage_agent"), list):
        invalid_usage = [value for value in record["usage_agent"] if value not in USAGE_AGENT]
        if invalid_usage:
            issues.append(
                ValidationIssue(file_path, line_number, f"Valeurs usage_agent inconnues : {', '.join(sorted(invalid_usage))}")
            )
        if len(set(record["usage_agent"])) != len(record["usage_agent"]):
            issues.append(ValidationIssue(file_path, line_number, "Le champ 'usage_agent' ne doit pas contenir de doublons."))

    return issues


def validate_file(file_path: Path) -> tuple[int, list[ValidationIssue]]:
    issues: list[ValidationIssue] = []
    lines_seen = 0
    with file_path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            if not raw_line.strip():
                continue
            lines_seen += 1
            try:
                record = json.loads(raw_line)
            except json.JSONDecodeError as exc:
                issues.append(ValidationIssue(file_path, line_number, f"JSON invalide : {exc.msg}"))
                continue
            issues.extend(validate_record(record, file_path, line_number))
    if lines_seen == 0:
        issues.append(ValidationIssue(file_path, 0, "Le fichier est vide."))
    return lines_seen, issues


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Valide des fichiers JSONL de règles cuisine.")
    parser.add_argument("paths", nargs="+", help="Fichiers JSONL ou répertoires contenant des fichiers JSONL.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        files = expand_inputs(args.paths)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if not files:
        print("Aucun fichier JSONL trouvé.", file=sys.stderr)
        return 2

    total_lines = 0
    all_issues: list[ValidationIssue] = []
    for file_path in files:
        lines_seen, issues = validate_file(file_path)
        total_lines += lines_seen
        all_issues.extend(issues)

    print(f"Validation effectuée sur {len(files)} fichier(s) et {total_lines} enregistrement(s) JSONL.")
    if all_issues:
        print("")
        for issue in all_issues:
            line_label = f"ligne {issue.line_number}" if issue.line_number else "niveau fichier"
            print(f"[ERREUR] {issue.file_path}:{line_label}: {issue.message}")
        print("")
        print(f"Échec de validation avec {len(all_issues)} problème(s).")
        return 1

    print("Validation réussie sans erreur.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
