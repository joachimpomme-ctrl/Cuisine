# Rapport `rattrapage_v1_final_candidate`

## Résumé

- Nombre de règles dans le `final_candidate` : `27`
- Nombre de règles différées : `3`
- Règles révisées : `5`
- Écriture dans `final` : `non`

Le lot candidat a été construit à partir du fichier `rattrapage_v1_normalized.jsonl` en appliquant strictement les décisions de l'audit Codex :

- inclusion des `22` règles `keep`
- inclusion des `5` règles `revise` après correction éditoriale
- exclusion des `3` règles `move_later`

## Fichiers produits

- `04_rules/normalized/rattrapage/rattrapage_v1_final_candidate.jsonl`
- `04_rules/normalized/rattrapage/rattrapage_v1_deferred.jsonl`
- `07_tests/reports/rattrapage_v1_final_candidate_duplicates.md`

## Règles différées

Les règles suivantes ont été sorties du candidat et placées dans `rattrapage_v1_deferred.jsonl` :

- `RATTRAPAGE_TROP_SUCRE_003`
- `RATTRAPAGE_SAUCE_QUI_TRANCHE_003`
- `RATTRAPAGE_VIANDE_SECHE_003`

Justification :

- ces trois règles relèvent davantage de la réorientation d'usage ou de la revalorisation que du rattrapage direct ;
- elles restent utiles, mais sont moins adaptées à un premier lot `final` centré sur des réponses opérationnelles immédiates.

## Règles révisées

### `RATTRAPAGE_TROP_SUCRE_001`

- Avant : vocabulaire trop abstrait autour du `contraste compatible`
- Après : recentrage sur l'ajout progressif d'une composante moins sucrée et cohérente avec le plat
- Effet : règle plus concrète et plus facile à activer pour un agent

### `RATTRAPAGE_TROP_EPICE_003`

- Avant : formulation éditoriale autour du `geste spectaculaire` et du `correctif miracle`
- Après : reformulation en logique d'ajustements progressifs plutôt qu'en opposition à une correction unique trop forte
- Effet : règle plus technique, moins rhétorique

### `RATTRAPAGE_SAUCE_TROP_LIQUIDE_003`

- Avant : mécanisme d'absorption trop vague via `volume solide`
- Après : recentrage sur l'augmentation ou l'ajout d'un élément solide déjà cohérent avec le plat
- Effet : règle plus compréhensible et moins interprétative

### `RATTRAPAGE_SAUCE_QUI_TRANCHE_002`

- Avant : `reprise douce` trop floue
- Après : règle limitée au cas d'une séparation partielle, avec reprise progressive par petites étapes et sans ajout brutal
- Effet : cadre d'action plus net sans promesse excessive

### `RATTRAPAGE_PATES_COLLEES_002`

- Avant : `relâchement doux` et `environnement compatible` trop ouverts
- Après : recentrage sur une séparation progressive et un desserrage léger sans brassage agressif
- Effet : meilleure actionnabilité sans basculer dans la mini-recette

## Validation JSON

Commandes exécutées :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py \
cuisine-ai-knowledge/04_rules/normalized/rattrapage/rattrapage_v1_final_candidate.jsonl
```

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py \
cuisine-ai-knowledge/04_rules/normalized/rattrapage/rattrapage_v1_deferred.jsonl
```

Résultats :

- `final_candidate` : `27` règles validées, `0` erreur
- `deferred` : `3` règles validées, `0` erreur

## Détection de doublons

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py \
cuisine-ai-knowledge/04_rules/normalized/rattrapage/rattrapage_v1_final_candidate.jsonl \
cuisine-ai-knowledge/04_rules/final \
--report cuisine-ai-knowledge/07_tests/reports/rattrapage_v1_final_candidate_duplicates.md
```

Résultat :

- doublons exacts détectés contre `final` : `0`
- quasi-doublons détectés contre `final` : `0`

Le candidat est donc isolé proprement du corpus déjà publié.

## Recommandations avant passage en `final`

- le lot est prêt pour un passage contrôlé en `final` du point de vue structurel ;
- conserver le périmètre actuel sans réintégrer les trois règles différées ;
- faire au besoin une dernière relecture métier ciblée sur :
  - `RATTRAPAGE_SAUCE_QUI_TRANCHE_002`
  - `RATTRAPAGE_PATES_COLLEES_002`
  - `RATTRAPAGE_SAUCE_TROP_LIQUIDE_003`
- garder la logique actuelle : prioriser le rattrapage direct et l'atténuation réaliste, repousser les règles trop proches de la revalorisation

## Décision

`rattrapage_v1_final_candidate.jsonl` est `prêt` pour une promotion progressive vers `final`.
