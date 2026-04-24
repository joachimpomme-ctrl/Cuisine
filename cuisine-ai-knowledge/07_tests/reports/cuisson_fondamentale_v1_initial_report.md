# Rapport Initial — `cuisson_fondamentale_v1_raw`

## Résumé

- lot brut créé dans `04_rules/raw/cuisson/cuisson_fondamentale_v1_raw.jsonl` ;
- nombre de règles : 39 ;
- couverture : 19 sous-catégories de cuisson fondamentale ;
- statut : structurellement valide, prêt pour audit éditorial ;
- aucun écrit dans `04_rules/final/`.

## Validation JSONL

- commande lancée : `python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py cuisine-ai-knowledge/04_rules/raw/cuisson/cuisson_fondamentale_v1_raw.jsonl`
- résultat : validation réussie ;
- erreurs de validation : 0.

## Détection de doublons textuels

- commande lancée : `python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py cuisine-ai-knowledge/04_rules/raw/cuisson/cuisson_fondamentale_v1_raw.jsonl cuisine-ai-knowledge/04_rules/normalized cuisine-ai-knowledge/04_rules/final --report cuisine-ai-knowledge/07_tests/reports/cuisson_fondamentale_v1_duplicate_report.md`
- groupes de doublons exacts détectés : 2 ;
- quasi-doublons détectés : 0.

## Interprétation des doublons

Les 2 doublons exacts détectés proviennent des fichiers d'exemple historiques déjà présents entre `normalized` et `final` :

- `CUISSON_SAISIR_001` entre `normalized` et `final`
- `CUISSON_SUER_001` entre `normalized` et `final`

Le nouveau lot `cuisson_fondamentale_v1_raw.jsonl` n'introduit pas de doublon textuel exact dans ce contrôle.

## Collisions d'identifiants à arbitrer

Le lot V1 entre en collision d'identifiants avec le corpus d'exemple existant :

- `CUISSON_SAISIR_001`
- `CUISSON_SUER_001`
- `CUISSON_RECHAUFFER_001`

Ces collisions ne sont pas des doublons textuels, mais elles devront être arbitrées avant normalisation pour garantir l'unicité future du corpus.

## Répartition du lot

- `saisir` : 2
- `rissoler` : 2
- `revenir` : 2
- `suer` : 2
- `mijoter` : 2
- `braiser` : 2
- `rotir` : 2
- `griller` : 3
- `pocher` : 3
- `bouillir` : 2
- `vapeur` : 2
- `four` : 5
- `basse_temperature` : 2
- `friture` : 2
- `rechauffer` : 2
- `garder_au_chaud` : 1
- `deglacer` : 1
- `reduire` : 1
- `confire` : 1

## Forces du lot

- couverture large des techniques du plan ;
- structure atomique cohérente ;
- présence de règles de principe, procédure, diagnostic et hygiène ;
- sécurité abordée pour `friture`, `rechauffer`, `garder_au_chaud` et `basse_temperature`.

## Risques et limites

- certaines sous-catégories sont très peu couvertes : `deglacer`, `reduire`, `confire`, `garder_au_chaud` ;
- `four` est plus dense que les autres et devra être relu pour vérifier qu'il n'y a pas de dispersion ;
- la frontière entre `saisir`, `rissoler` et `revenir` devra être auditée ;
- la prudence des formulations `basse_temperature` et `rechauffer` doit être relue métier.

## Points à faire auditer par Gemini

- cohérence des frontières entre techniques proches ;
- collisions d'IDs à résoudre ou stratégie de renumérotation ;
- équilibre de couverture entre techniques ;
- règles possiblement trop abstraites sur `four` ;
- suffisant niveau de prudence sur `rechauffer`, `garder_au_chaud`, `friture`, `basse_temperature` ;
- besoin éventuel de scinder ou fusionner certaines règles ;
- manque de règles de diagnostic sur `braiser`, `rotir`, `bouillir` et `vapeur`.
