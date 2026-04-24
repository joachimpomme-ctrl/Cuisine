# Rapport `assaisonnement_v1_final_candidate`

## Résumé

- Nombre de règles dans le `final_candidate` : `34`
- Nombre de règles différées : `2`
- Règles révisées : `5`
- Écriture dans `final` : `non`

Le `final_candidate` a été construit à partir de `assaisonnement_v1_normalized.jsonl` en appliquant strictement l'audit Codex :

- inclusion des `29` règles `keep`
- inclusion des `5` règles `revise` après correction éditoriale
- exclusion des `2` règles `move_later`

## Fichiers produits

- `04_rules/normalized/assaisonnement/assaisonnement_v1_final_candidate.jsonl`
- `04_rules/normalized/assaisonnement/assaisonnement_v1_deferred.jsonl`
- `07_tests/reports/assaisonnement_v1_final_candidate_duplicates.md`

## Règles différées

Les règles suivantes ont été sorties du candidat et placées dans `assaisonnement_v1_deferred.jsonl` :

- `ASSAISONNEMENT_ALCOOL_001`
- `ASSAISONNEMENT_ALCOOL_002`

Justification :

- sous-ensemble plus contextuel que le coeur du lot ;
- moins prioritaire pour un premier noyau `final` d'assaisonnement ;
- forte proximité conceptuelle entre les deux règles.

## Règles révisées

### `ASSAISONNEMENT_POIVRE_002`

- Avant : règle encore dépendante du style du plat, formulée de façon un peu générale
- Après : recentrage sur un geste concret, garder une partie du poivre pour la fin
- Effet : règle plus directement actionnable

### `ASSAISONNEMENT_AMERTUME_002`

- Avant : notion trop interprétative de `rondeur`
- Après : levier formulé de façon plus concrète par une petite touche douce ou grasse cohérente avec le plat
- Effet : réduction du flou sans ajout de précision fragile

### `ASSAISONNEMENT_EPICES_001`

- Avant : formulation abstraite autour du `rôle de l'épice`
- Après : recentrage sur deux effets concrets, `réchauffer` ou `relever`
- Effet : meilleure lisibilité agentique

### `ASSAISONNEMENT_EQUILIBRE_003`

- Avant : formulation conceptuelle autour de `détourner l'attention`
- Après : clarification sur le fait qu'un ajout aromatique ne corrige pas à lui seul le défaut principal
- Effet : frontière plus nette entre masquer et corriger

### `ASSAISONNEMENT_DEGUSTATION_001`

- Avant : formulation encore un peu métacognitive
- Après : consigne plus simple, nommer le manque principal avant correction
- Effet : règle plus opérationnelle et moins abstraite

## Validation JSON

Commandes exécutées :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py \
cuisine-ai-knowledge/04_rules/normalized/assaisonnement/assaisonnement_v1_final_candidate.jsonl
```

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py \
cuisine-ai-knowledge/04_rules/normalized/assaisonnement/assaisonnement_v1_deferred.jsonl
```

Résultats :

- `final_candidate` : `34` règles validées, `0` erreur
- `deferred` : `2` règles validées, `0` erreur

## Détection de doublons

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py \
cuisine-ai-knowledge/04_rules/normalized/assaisonnement/assaisonnement_v1_final_candidate.jsonl \
cuisine-ai-knowledge/04_rules/final \
--report cuisine-ai-knowledge/07_tests/reports/assaisonnement_v1_final_candidate_duplicates.md
```

Résultat :

- doublons exacts détectés contre `final` : `0`
- quasi-doublons détectés contre `final` : `0`

Le candidat est donc isolé proprement du corpus déjà publié.

## Recommandations avant passage en `final`

- le lot est prêt du point de vue structurel et de l'unicité contre `final`
- conserver hors du premier lot `final` le sous-ensemble `alcool`
- faire au besoin une dernière relecture métier ciblée sur :
  - `ASSAISONNEMENT_POIVRE_002`
  - `ASSAISONNEMENT_AMERTUME_002`
  - `ASSAISONNEMENT_EQUILIBRE_003`
- garder le coeur du lot centré sur :
  - construction du goût
  - diagnostic précoce
  - assaisonnement progressif
  - distinction claire des leviers

## Décision

`assaisonnement_v1_final_candidate.jsonl` est `prêt` pour une promotion contrôlée vers `final`.
