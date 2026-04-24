# Rapport de publication `assaisonnement_v1`

## Résumé

- Nombre de règles publiées : `34`
- Statut : `stable_initial`
- Domaine : `assaisonnement`
- Décision finale : `lot publié`

## Fichiers créés

- `04_rules/final/assaisonnement/assaisonnement_v1.jsonl`
- `04_rules/final/assaisonnement/assaisonnement_v1.meta.json`
- `07_tests/reports/assaisonnement_v1_final_publish_duplicates.md`

## Règles exclues

Les règles suivantes n'ont pas été publiées dans ce lot `final` :

- `ASSAISONNEMENT_ALCOOL_001`
- `ASSAISONNEMENT_ALCOOL_002`

Justification :

- ces deux règles avaient été explicitement différées au stade `final_candidate` ;
- elles sont plus contextuelles que le coeur du lot ;
- elles n'ont pas été réintroduites dans le lot publié.

## Validation JSONL

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py \
cuisine-ai-knowledge/04_rules/final/assaisonnement/assaisonnement_v1.jsonl
```

Résultat :

- validation : `OK`
- enregistrements validés : `34`
- erreurs : `0`

## Détection de doublons

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py \
cuisine-ai-knowledge/04_rules/final/assaisonnement/assaisonnement_v1.jsonl \
cuisine-ai-knowledge/04_rules/final \
--report cuisine-ai-knowledge/07_tests/reports/assaisonnement_v1_final_publish_duplicates.md
```

Résultat :

- doublons exacts détectés : `0`
- quasi-doublons détectés : `0`

Le lot est donc publié proprement dans `final` sans collision avec les autres lots déjà publiés.

## Anomalies restantes

- aucune anomalie structurelle détectée ;
- aucune règle différée réintroduite ;
- aucune fusion avec d'autres lots ;
- aucun impact sur les autres domaines.

## Conclusion

Le fichier `assaisonnement_v1.jsonl` a été publié dans `final` conformément au `final_candidate` validé.

Décision :

`lot publié`
