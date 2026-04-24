# Rapport — `cuisson_fondamentale_v1_final_candidate`

## Résumé

- fichier candidat créé : `04_rules/normalized/cuisson/cuisson_fondamentale_v1_final_candidate.jsonl`
- fichier différé créé : `04_rules/normalized/cuisson/cuisson_fondamentale_v1_deferred.jsonl`
- nombre de règles dans le candidat final : 36
- nombre de règles différées : 3

## Règles révisées

- `CUISSON_SUER_003`
- `CUISSON_GRILLER_002`
- `CUISSON_POCHER_001`
- `CUISSON_BASSE_TEMPERATURE_001`
- `CUISSON_CONFIRE_001`
- `CUISSON_FOUR_004`

## Avant / Après synthétique

### `CUISSON_SUER_003`

- avant : astuce formulée comme une petite technique contextuelle centrée sur le sel ;
- après : règle resserrée sur un léger salage comme aide possible à la sortie d'humidité en cuisson douce ;
- effet recherché : rendre la règle plus atomique et moins anecdotique.

### `CUISSON_GRILLER_002`

- avant : formulation un peu scénarisée autour d'une gestion en deux temps ;
- après : règle recentrée sur le principe général applicable aux pièces épaisses grillées ;
- effet recherché : garder l'idée utile sans la sur-détailler.

### `CUISSON_POCHER_001`

- avant : formulation pouvant laisser une ambiguïté sur le niveau d'agitation admissible ;
- après : règle clarifiée autour du frémissement et non de la forte ébullition ;
- effet recherché : renforcer la frontière métier avec `bouillir`.

### `CUISSON_BASSE_TEMPERATURE_001`

- avant : formulation valable mais trop générale ;
- après : règle recentrée sur la primauté de la stabilité de chauffe ;
- effet recherché : garder une règle prudente, plus atomique et moins diffuse.

### `CUISSON_CONFIRE_001`

- avant : formulation large risquant de se confondre avec d'autres cuissons lentes ;
- après : principe simplifié autour d'une cuisson longue et modérée dans un milieu adapté ;
- effet recherché : mieux isoler le coeur de la technique sans fausse précision.

### `CUISSON_FOUR_004`

- avant : formulation utile mais un peu trop générale sur les plats volumineux ;
- après : règle recentrée sur l'intérêt du four pour une cuisson homogène d'un volume important ;
- effet recherché : améliorer l'atomicité et l'actionnabilité.

## Règles différées

- `CUISSON_GARDER_AU_CHAUD_001`
- `CUISSON_BASSE_TEMPERATURE_002`
- `CUISSON_POCHER_003`

## Justification des exclusions

### `CUISSON_GARDER_AU_CHAUD_001`

- règle pertinente mais encore trop vague pour un passage immédiat en `final` ;
- sujet proche d'un futur cluster éditorial plus explicite de sécurité ou de conservation.

### `CUISSON_BASSE_TEMPERATURE_002`

- sujet trop sensible pour promotion sans base documentaire renforcée ;
- prudence correcte, mais encore insuffisante pour une entrée immédiate dans un noyau stable.

### `CUISSON_POCHER_003`

- règle trop spécifique ;
- dépend fortement du cas d'usage et relève davantage d'une adaptation avancée que d'un noyau fondamental.

## Validation JSONL

### Candidat final

- commande : `python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py cuisine-ai-knowledge/04_rules/normalized/cuisson/cuisson_fondamentale_v1_final_candidate.jsonl`
- résultat : validation réussie
- erreurs : 0

### Différé

- commande : `python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py cuisine-ai-knowledge/04_rules/normalized/cuisson/cuisson_fondamentale_v1_deferred.jsonl`
- résultat : validation réussie
- erreurs : 0

## Détection de doublons

- commande : `python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py cuisine-ai-knowledge/04_rules/normalized/cuisson/cuisson_fondamentale_v1_final_candidate.jsonl cuisine-ai-knowledge/04_rules/final --report cuisine-ai-knowledge/07_tests/reports/cuisson_fondamentale_v1_final_candidate_duplicate_report.md`
- groupes de doublons exacts : 0
- quasi-doublons : 0

## Recommandations avant écriture réelle dans `final`

- le candidat à 36 règles est proprement validé et ne présente pas de doublon détecté contre `final` ;
- relire une dernière fois le sous-ensemble `four`, encore plus hétérogène que les autres techniques ;
- relire les 6 règles révisées avec un angle purement métier pour confirmer qu'elles sont désormais assez fondamentales ;
- conserver les 3 règles différées hors `final` tant qu'un cadrage documentaire plus fort n'est pas disponible ;
- procéder à un passage progressif en `final`, de préférence par sous-lots techniques plutôt qu'en un seul bloc.
