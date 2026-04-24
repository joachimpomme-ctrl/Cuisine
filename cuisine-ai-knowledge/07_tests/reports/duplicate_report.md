# Rapport de détection de doublons

- Date : 2026-04-24
- Fichiers analysés : 3
- Enregistrements analysés : 8
- Groupes de doublons exacts : 2
- Paires de quasi-doublons : 1
- Seuil de similarité : 0.88

## Doublons exacts

### Groupe 1

- `CUISSON_SAISIR_001` | Saisir développe les arômes et la coloration | 04_rules/raw/cuisson/cuisson_fondamentale_claude_v1.jsonl:1
- `CUISSON_SAISIR_001` | Saisir développe les arômes et la coloration | 04_rules/normalized/cuisson/cuisson_fondamentale_v1.jsonl:1
- `CUISSON_SAISIR_001` | Saisir développe les arômes et la coloration | 04_rules/final/cuisson/cuisson_fondamentale_core_v1.jsonl:1

### Groupe 2

- `CUISSON_SUER_001` | Suer sans colorer concentre les aromatiques | 04_rules/raw/cuisson/cuisson_fondamentale_claude_v1.jsonl:2
- `CUISSON_SUER_001` | Suer sans colorer concentre les aromatiques | 04_rules/normalized/cuisson/cuisson_fondamentale_v1.jsonl:2
- `CUISSON_SUER_001` | Suer sans colorer concentre les aromatiques | 04_rules/final/cuisson/cuisson_fondamentale_core_v1.jsonl:2

## Quasi-doublons

- `CUISSON_RECHAUFFER_001` <-> `CUISSON_RECHAUFFER_001` | score=0.92 | 04_rules/raw/cuisson/cuisson_fondamentale_claude_v1.jsonl:3 | 04_rules/normalized/cuisson/cuisson_fondamentale_v1.jsonl:3
