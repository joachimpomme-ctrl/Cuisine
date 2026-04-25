# Plan de Couverture — Cuisson Fondamentale V1

## Objectif

Préparer la première production contrôlée de règles sur les cuissons fondamentales, avec un corpus brut limité, atomique et révisable.

## Périmètre

Le plan couvre les techniques suivantes :

- `saisir`
- `rissoler`
- `revenir`
- `suer`
- `mijoter`
- `braiser`
- `rotir`
- `griller`
- `pocher`
- `bouillir`
- `vapeur`
- `four`
- `basse_temperature`
- `friture`
- `rechauffer`
- `garder_au_chaud`
- `deglacer`
- `reduire`
- `confire`

## Cible de production V1

- 30 à 40 règles maximum ;
- règles atomiques uniquement ;
- pas de recettes ;
- pas de passage en `04_rules/final/` ;
- priorité aux principes robustes, erreurs fréquentes et points de sécurité.

## Répartition prévue des règles candidates

- `saisir` : 2
- `rissoler` : 2
- `revenir` : 1
- `suer` : 2
- `mijoter` : 2
- `braiser` : 2
- `rotir` : 2
- `griller` : 2
- `pocher` : 2
- `bouillir` : 2
- `vapeur` : 2
- `four` : 1
- `basse_temperature` : 1
- `friture` : 2
- `rechauffer` : 2
- `garder_au_chaud` : 1
- `deglacer` : 1
- `reduire` : 1
- `confire` : 1

Total prévu : 31 règles.

## Axes de qualité

- une idée principale par règle ;
- conditions d'application explicites ;
- application praticable en cuisine familiale ;
- erreurs fréquentes distinctes du principe ;
- exceptions non décoratives ;
- prudence renforcée pour `friture`, `rechauffer`, `garder_au_chaud` et `basse_temperature`.

## Ordre de priorité métier

### Priorité 1

- `saisir`
- `suer`
- `mijoter`
- `vapeur`
- `rechauffer`

### Priorité 2

- `rissoler`
- `braiser`
- `rotir`
- `pocher`
- `bouillir`
- `friture`
- `reduire`
- `deglacer`

### Priorité 3

- `revenir`
- `griller`
- `four`
- `basse_temperature`
- `garder_au_chaud`
- `confire`

## Risques connus

- chevauchement entre `saisir`, `rissoler` et `revenir` ;
- confusion entre `mijoter` et `bouillir` ;
- règles de sécurité trop vagues sur `rechauffer` et `garder_au_chaud` ;
- formulations trop générales sur `four` et `basse_temperature` ;
- dérive vers des mini-recettes pour `braiser` ou `confire`.

## Points attendus pour audit Gemini

- cohérence de frontière entre techniques proches ;
- trous de couverture ;
- quasi-doublons ;
- règles trop vagues ;
- règles à faible utilité agentique ;
- prudence suffisante sur la sécurité alimentaire.
