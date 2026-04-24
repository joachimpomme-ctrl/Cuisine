# Rapport initial `assaisonnement_v1`

## Résumé

- Nombre de règles : `36`
- Domaine : `assaisonnement`
- Statut : `raw`
- Décision : `prêt pour normalisation`

Le lot respecte le périmètre demandé :

- pas de recettes ;
- pas de prescriptions nutritionnelles ;
- pas de règles médicales ;
- pas de dosages universels ;
- accent mis sur les principes actionnables, le diagnostic et l'ajustement progressif.

## Fichiers produits

- `10_research/assaisonnement_v1/plan_couverture.md`
- `10_research/assaisonnement_v1/matrice_assaisonnement.md`
- `10_research/assaisonnement_v1/protocole_equilibre_saveurs.md`
- `04_rules/raw/assaisonnement/assaisonnement_v1_raw.jsonl`
- `04_rules/raw/assaisonnement/assaisonnement_v1_raw.meta.json`
- `07_tests/reports/assaisonnement_v1_initial_duplicates.md`

## Couverture par sous-catégorie

- `sel` : `4`
- `acidite` : `3`
- `equilibre_global` : `3`
- `poivre` : `2`
- `sucre` : `2`
- `gras` : `2`
- `umami` : `2`
- `amertume` : `2`
- `herbes_fraiches` : `2`
- `herbes_seches` : `2`
- `epices` : `2`
- `aromates` : `2`
- `bouillon` : `2`
- `alcool` : `2`
- `assaisonnement_progressif` : `2`
- `degustation_ajustement` : `2`

Lecture utile :

- la couverture est large et homogène ;
- le coeur du lot se situe sur `sel`, `acidite`, `equilibre_global`, `assaisonnement_progressif` et `degustation_ajustement` ;
- les sous-catégories périphériques restent volontairement compactes pour un premier lot.

## Validation JSONL

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py \
cuisine-ai-knowledge/04_rules/raw/assaisonnement/assaisonnement_v1_raw.jsonl
```

Résultat :

- validation : `OK`
- enregistrements validés : `36`
- erreurs : `0`

## Doublons

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py \
cuisine-ai-knowledge/04_rules/raw/assaisonnement/assaisonnement_v1_raw.jsonl \
cuisine-ai-knowledge/04_rules/final \
--report cuisine-ai-knowledge/07_tests/reports/assaisonnement_v1_initial_duplicates.md
```

Résultat :

- doublons exacts : `0`
- quasi-doublons : `0`

Le lot RAW `assaisonnement_v1` ne collisionne pas avec les lots déjà publiés dans `final`.

## Règles faibles ou à surveiller

Le lot est globalement propre, mais certaines règles demandent une vigilance éditoriale à la normalisation :

- `ASSAISONNEMENT_POIVRE_002`
  La règle est utile, mais la notion de fin d'ajout dépend du style de plat et devra rester prudente.

- `ASSAISONNEMENT_SUCRE_001`
  Le principe est juste, mais il faudra conserver la limite entre arrondi léger et correction de type `rattrapage`.

- `ASSAISONNEMENT_AMERTUME_002`
  Règle plus abstraite que les autres ; le vocabulaire de rééquilibrage doit rester très lisible.

- `ASSAISONNEMENT_ALCOOL_001`
  Bonne frontière conceptuelle, mais le champ d'application peut vite devenir contextuel.

- `ASSAISONNEMENT_ALCOOL_002`
  À relire pour éviter une répétition trop forte avec `ALCOOL_001`.

## Risques de chevauchement avec `rattrapage`

Les zones de frontière principales sont :

- `acidite` vs `rattrapage/trop_acide`
- `sucre` vs `rattrapage/trop_sucre`
- `epices` / `poivre` vs `rattrapage/trop_epice`
- `equilibre_global` vs règles de correction déjà trop avancées

Le lot reste dans le bon domaine car il traite surtout :

- le diagnostic précoce ;
- les gestes progressifs ;
- la construction de l'équilibre ;
- la prévention de la surcorrection.

Il faudra conserver cette frontière pendant la normalisation :

- `assaisonnement` = construire et ajuster
- `rattrapage` = corriger un défaut déjà installé

## Recommandations avant normalisation

- harmoniser légèrement le vocabulaire entre `principe`, `diagnostic`, `procedure` et `adaptation`
- vérifier que les règles sur `alcool`, `amertume` et `poivre` restent aussi actionnables que celles sur `sel` ou `acidite`
- surveiller les redondances éditoriales potentielles entre :
  - `equilibre_global`
  - `assaisonnement_progressif`
  - `degustation_ajustement`
- garder très visible le principe central du lot : l'assaisonnement se construit progressivement
- préserver la distinction entre :
  - `assaisonner`
  - `corriger`
  - `masquer`
  - `équilibrer`

## Conclusion

Le lot `assaisonnement_v1_raw.jsonl` est structurellement propre, cohérent avec le domaine et suffisamment net pour entrer en phase de normalisation.

Décision :

`prêt pour normalisation`
