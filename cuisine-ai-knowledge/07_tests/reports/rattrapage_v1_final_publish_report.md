# Rapport de publication `rattrapage_v1`

## Résumé

- Nombre de règles publiées : `27`
- Statut : `stable_initial`
- Domaine : `rattrapage`
- Décision finale : `lot publié`

## Fichiers créés

- `04_rules/final/rattrapage/rattrapage_v1.jsonl`
- `04_rules/final/rattrapage/rattrapage_v1.meta.json`
- `07_tests/reports/rattrapage_v1_final_publish_duplicates.md`

## Règles exclues

Les règles suivantes n'ont pas été publiées dans ce lot `final` :

- `RATTRAPAGE_TROP_SUCRE_003`
- `RATTRAPAGE_SAUCE_QUI_TRANCHE_003`
- `RATTRAPAGE_VIANDE_SECHE_003`

Justification :

- elles avaient été explicitement sorties du `final_candidate` ;
- elles relèvent davantage de la réorientation d'usage ou de la revalorisation que du rattrapage direct ;
- elles ne sont pas réintroduites dans ce lot publié.

## Validation JSONL

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py \
cuisine-ai-knowledge/04_rules/final/rattrapage/rattrapage_v1.jsonl
```

Résultat :

- validation : `OK`
- enregistrements validés : `27`
- erreurs : `0`

## Détection de doublons

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py \
cuisine-ai-knowledge/04_rules/final/rattrapage/rattrapage_v1.jsonl \
cuisine-ai-knowledge/04_rules/final \
--report cuisine-ai-knowledge/07_tests/reports/rattrapage_v1_final_publish_duplicates.md
```

Résultat :

- doublons exacts détectés : `0`
- quasi-doublons détectés : `0`

Le lot est donc isolé proprement dans `final` sans collision avec les autres lots publiés.

## Anomalies restantes

- aucune anomalie structurelle détectée ;
- aucune règle différée réintroduite ;
- aucune fusion avec d'autres lots ;
- aucun impact sur les autres domaines.

## Conclusion

Le fichier `rattrapage_v1.jsonl` a été publié dans `final` conformément au candidate validé.

Décision :

`lot publié`
