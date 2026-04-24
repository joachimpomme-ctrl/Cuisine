# Rapport de Publication — `cuisson_fondamentale_v1`

## Résumé

- lot publié : `04_rules/final/cuisson/cuisson_fondamentale_v1.jsonl`
- metadata associé : `04_rules/final/cuisson/cuisson_fondamentale_v1.meta.json`
- nombre de règles publiées : 36
- statut : lot publié

## Validation

- commande : `python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py cuisine-ai-knowledge/04_rules/final/cuisson/cuisson_fondamentale_v1.jsonl`
- résultat : `OK`
- détail : 36 enregistrements JSONL validés

## Doublons vs autres lots `final`

- commande : `python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py cuisine-ai-knowledge/04_rules/final --report cuisine-ai-knowledge/07_tests/reports/cuisson_fondamentale_v1_final_publish_duplicate_report.md`
- doublons exacts : 0
- quasi-doublons : 0

## Anomalies restantes

- aucune anomalie structurelle bloquante ;
- les 3 règles différées n'ont pas été réintroduites ;
- le lot est bien isolé et n'a pas été fusionné avec d'autres lots ;
- le fichier historique `cuisson_fondamentale_core_v1.jsonl` reste présent à côté, sans collision détectée avec le lot publié.

## Règles explicitement exclues de la publication

- `CUISSON_GARDER_AU_CHAUD_001`
- `CUISSON_BASSE_TEMPERATURE_002`
- `CUISSON_POCHER_003`

## Décision

- décision : `lot publié`
- justification : le lot candidat validé a été copié tel quel dans `final`, validé sans erreur et ne présente pas de doublon détecté contre les autres lots `final`.
