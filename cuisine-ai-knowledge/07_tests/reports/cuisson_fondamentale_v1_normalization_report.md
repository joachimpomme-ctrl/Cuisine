# Rapport de Normalisation — `cuisson_fondamentale_v1`

## Résumé

- source normalisée : `04_rules/raw/cuisson/cuisson_fondamentale_v1_raw.jsonl`
- sortie créée : `04_rules/normalized/cuisson/cuisson_fondamentale_v1_normalized.jsonl`
- nombre de règles conservées : 39
- écriture dans `final` : aucune

## Principe de normalisation appliqué

- conservation des 39 règles du lot brut ;
- aucune suppression de règle ;
- aucune fusion de règle ;
- résolution des collisions d'identifiants avec les exemples existants en `normalized` et `final` ;
- ajout d'une section de clarification dans la taxonomie sur les frontières entre techniques proches.

## Règles renommées

- `CUISSON_SAISIR_001` -> `CUISSON_SAISIR_002`
- `CUISSON_SAISIR_002` -> `CUISSON_SAISIR_003`
- `CUISSON_SUER_001` -> `CUISSON_SUER_002`
- `CUISSON_SUER_002` -> `CUISSON_SUER_003`
- `CUISSON_RECHAUFFER_001` -> `CUISSON_RECHAUFFER_002`
- `CUISSON_RECHAUFFER_002` -> `CUISSON_RECHAUFFER_003`

## Règles ajustées

- aucun ajustement sémantique majeur ;
- normalisation centrée sur l'unicité des IDs ;
- clarifications conceptuelles déplacées dans `02_taxonomie/taxonomie_cuisine.md` plutôt que dispersées dans les règles.

## Validation

- commande : `python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py cuisine-ai-knowledge/04_rules/normalized/cuisson/cuisson_fondamentale_v1_normalized.jsonl`
- résultat : validation réussie
- erreurs de validation : 0

## Détection de doublons

- commande : `python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py cuisine-ai-knowledge/04_rules/normalized/cuisson/cuisson_fondamentale_v1_normalized.jsonl cuisine-ai-knowledge/04_rules/normalized/cuisson/cuisson_fondamentale_v1.jsonl cuisine-ai-knowledge/04_rules/final --report cuisine-ai-knowledge/07_tests/reports/cuisson_fondamentale_v1_normalized_duplicate_report.md`
- doublons exacts restants : 2 groupes
- quasi-doublons restants : 0

## Interprétation des doublons restants

Les doublons exacts restants ne proviennent pas du nouveau fichier normalisé. Ils correspondent aux exemples historiques déjà présents entre :

- `04_rules/normalized/cuisson/cuisson_fondamentale_v1.jsonl`
- `04_rules/final/cuisson/cuisson_fondamentale_core_v1.jsonl`

Ils concernent :

- `CUISSON_SAISIR_001`
- `CUISSON_SUER_001`

## Vérification des collisions d'identifiants

Après renumérotation, le nouveau fichier `cuisson_fondamentale_v1_normalized.jsonl` n'entre plus en collision d'identifiant avec le corpus d'exemple existant.

## Taxonomie enrichie

Section ajoutée dans `02_taxonomie/taxonomie_cuisine.md` :

- `saisir` ≠ `rissoler`
- `revenir` ≠ `suer`
- `mijoter` ≠ `bouillir`
- `pocher` ≠ `bouillir`
- `braiser` ≠ `mijoter`

## Recommandations pour audit Gemini

- vérifier que les frontières entre techniques proches sont suffisantes pour éviter des quasi-doublons futurs ;
- relire la densité du sous-ensemble `four`, plus fourni que les autres ;
- relire la prudence de `basse_temperature` et `garder_au_chaud` ;
- confirmer que `pocher_003` et `griller_003` ont une utilité agentique suffisante ;
- évaluer s'il manque des règles de diagnostic pour `braiser`, `vapeur`, `reduire` et `confire` ;
- décider si les exemples historiques doivent être conservés comme fixtures ou normalisés dans une stratégie d'unicité globale.
