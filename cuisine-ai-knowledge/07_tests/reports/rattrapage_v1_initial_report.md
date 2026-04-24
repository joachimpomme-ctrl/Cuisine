# Rapport Initial — `rattrapage_v1_raw`

## Résumé

- lot brut créé dans `04_rules/raw/rattrapage/rattrapage_v1_raw.jsonl`
- nombre de règles : 30
- couverture : 10 sous-catégories de rattrapage, avec 3 règles par cas
- statut : structurellement valide, prêt pour audit éditorial et métier
- aucune écriture dans `final`

## Validation JSONL

- commande lancée : `python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py cuisine-ai-knowledge/04_rules/raw/rattrapage/rattrapage_v1_raw.jsonl`
- résultat : validation réussie
- erreurs de validation : 0

## Couverture du lot

- `trop_sale` : 3
- `trop_acide` : 3
- `trop_sucre` : 3
- `trop_epice` : 3
- `sauce_trop_liquide` : 3
- `sauce_qui_tranche` : 3
- `viande_seche` : 3
- `legumes_trop_cuits` : 3
- `pates_collees` : 3
- `riz_rate` : 3

## Détection de doublons

- commande lancée : `python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py cuisine-ai-knowledge/04_rules/raw/rattrapage/rattrapage_v1_raw.jsonl cuisine-ai-knowledge/04_rules/normalized cuisine-ai-knowledge/04_rules/final --report cuisine-ai-knowledge/07_tests/reports/rattrapage_v1_duplicate_report.md`
- groupes de doublons exacts détectés : 41
- quasi-doublons détectés : 0

## Interprétation des doublons

Les doublons exacts détectés proviennent du corpus `cuisson` déjà présent dans le dépôt, notamment des recouvrements entre :

- `04_rules/normalized/cuisson/`
- `04_rules/final/cuisson/`
- `04_rules/normalized/cuisson/cuisson_fondamentale_v1_final_candidate.jsonl`
- `04_rules/final/cuisson/cuisson_fondamentale_v1.jsonl`

Le nouveau lot `rattrapage_v1_raw.jsonl` n'apparaît pas dans les groupes de doublons remontés.

## Forces du lot

- couverture homogène des 10 cas d'erreur demandés ;
- règles majoritairement atomiques ;
- présence de diagnostics, rattrapages, adaptations et limites ;
- bon angle cuisine familiale ;
- plusieurs règles intègrent explicitement l'idée qu'un plat ne retrouve pas toujours son intention initiale.

## Risques et limites

- quelques règles restent proches d'une logique de réorientation d'usage plus que de correction stricte ;
- les sous-catégories `sauce_qui_tranche`, `viande_seche` et `riz_rate` demanderont une review métier attentive ;
- le domaine `rattrapage` n'est pas encore affiné dans la taxonomie comme `cuisson`, ce qui pourra nécessiter une normalisation éditoriale plus forte.

## Points à faire auditer ensuite

- distinguer clairement les règles de rattrapage des règles de simple limitation des dégâts ;
- vérifier si certaines règles relèvent davantage de `anti_gaspillage` ou `gestion_restes` que du coeur `rattrapage` ;
- relire les règles les plus contextuelles sur `sauce_qui_tranche`, `viande_seche`, `pates_collees` et `riz_rate` ;
- vérifier que les règles de dilution ou d'augmentation de volume ne deviennent pas des conseils trop génériques ;
- décider si certaines règles de réorientation doivent être différées lors d'un audit plus fin.
