# Taxonomie Cuisine

## Objectif

Cette taxonomie sert de langage commun pour organiser la base `rules`, limiter les ambiguïtés et faciliter la production distribuée entre plusieurs IA.

## Domaines principaux

- `cuisson`
- `ingredient`
- `assaisonnement`
- `sauce`
- `patisserie`
- `hygiene`
- `conservation`
- `substitution`
- `rattrapage`
- `organisation`
- `materiel`
- `nutrition_pratique`
- `enfants_famille`
- `batch_cooking`
- `anti_gaspillage`

## Sous-domaines prioritaires pour `cuisson`

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

## Conventions d'écriture

- `domaine` : un des domaines principaux ci-dessus.
- `categorie` : groupe métier stable. Exemple : `technique_fondamentale`, `securite_alimentaire`, `organisation_du_poste`.
- `sous_categorie` : sous-domaine plus précis. Exemple : `saisir`, `pocher`, `rechauffer`.
- `type_regle` : nature fonctionnelle de la règle. Exemple : `principe`, `procedure`, `diagnostic`.

## Ligne éditoriale

- Une règle = une idée principale.
- Une règle ne doit pas devenir une mini-recette.
- Les conditions, applications, erreurs fréquentes et exceptions sont obligatoires pour préserver l'utilité agentique.
- Les règles liées à l'hygiène doivent être prudentes, explicites et signaler les limites.

## Priorités de couverture initiale

1. `cuisson`
2. `hygiene`
3. `conservation`
4. `organisation`
5. `rattrapage`

## Frontières métier

- Les règles générales vont dans `04_rules/`.
- Les recettes complètes vont dans `05_recipes/`.
- Les préférences et habitudes familiales vont dans `06_household_context/`.
