# Rapport de normalisation `escoffier_v1`

## Volume initial

- entrées RAW initiales : `196`

## Entrées normalisées par fichier

- `escoffier_principes_v1_normalized.jsonl` : `28`
- `escoffier_systemes_v1_normalized.jsonl` : `40`
- `escoffier_associations_v1_normalized.jsonl` : `29`
- `escoffier_patterns_v1_normalized.jsonl` : `20`
- `escoffier_vocabulaire_v1_normalized.jsonl` : `46`

Total normalisé : `163`

## Entrées différées et exclues

- entrées différées : `33`
- entrées exclues définitivement : `0`

Le différé regroupe surtout :

- des variantes trop proches dans `principes` ;
- des diagnostics redondants dans `systemes` ;
- des diagnostics d associations trop secondaires ;
- quelques erreurs de pattern moins prioritaires au premier passage.

## Principales fusions et réductions

- `principes`
  - resserrage autour de `fonds`, `harmonie produit / sauce`, `réduction`, `liaison`, `finitions`
  - réduction des doublons internes entre principe, erreur et adaptation sur les mêmes idées
- `systemes`
  - conservation des systèmes transférables
  - report d une partie des diagnostics les plus redondants
  - maintien prudent de `saumure` en différé logique
- `associations`
  - conservation des familles réellement modernes et transférables
  - report des signaux d erreur les moins utiles à la décision
- `patterns`
  - maintien des structures de plats utiles à l agent
  - report des patterns d erreur les moins prioritaires
- `vocabulaire`
  - conservation large, car le lot est déjà directement utile et peu bruité

## Principaux retraits

- formulations trop répétitives de type :
  - même principe + même avertissement + même adaptation sans gain réel
- signaux trop proches entre :
  - fonds / qualité des bases
  - réduction / finition
  - associations produit / sauce déjà évidentes
- éléments historiques encore utiles mais non prioritaires pour un premier audit

## Validation JSONL

- `principes` : `OK`
- `systemes` : `OK`
- `associations` : `OK`
- `patterns` : `OK`
- `vocabulaire` : `OK`
- `deferred` : `OK`

## Doublons

Contrôle effectué contre :

- `04_rules/final`

Contrôle `normalized/techniques_cap` :

- non effectué, car ce chemin n existe pas dans le repo à ce stade

Résultats :

- doublons exacts :
  - `principes` : `0`
  - `systemes` : `0`
  - `associations` : `0`
  - `patterns` : `0`
  - `vocabulaire` : `0`

- quasi-doublons restants :
  - `principes` : `0`
  - `systemes` : `128`
  - `associations` : `21`
  - `patterns` : `11`
  - `vocabulaire` : `0`

## Lecture des quasi-doublons restants

Le point de vigilance principal est `systemes`.

Ces quasi-doublons restants viennent surtout :

- de la proximité logique entre plusieurs familles de sauces et de bases ;
- des voisinages naturels avec les lots déjà publiés dans `final` ;
- d un noyau encore dense autour de :
  - fonds
  - fumets
  - glaces
  - réductions
  - liaisons
  - émulsions

Ils ne bloquent pas la validation structurelle, mais ils justifient un audit éditorial serré.

## Risques résiduels

- densité encore forte du lot `systemes`
- recouvrements conceptuels entre logique Escoffier et logique déjà couverte dans `cuisson`
- quelques éléments encore un peu trop proches d un cours de culture culinaire
- risque de sur-explication si le draft Gemini est utilisé sans couche de sélection

## Recommandations avant audit

- auditer en priorité `systemes`
- vérifier si certaines familles doivent être fusionnées avant un futur `final_candidate`
- contrôler que `associations` reste bien moderne et non aristocratique
- vérifier que `vocabulaire` aide vraiment l agent à expliquer un geste au lieu d exhiber du jargon
- tester le draft Gemini sur :
  - `mon plat manque de fond`
  - `quelle famille de sauce pour cette volaille ?`
  - `explique-moi simplement ce qu est un fumet`

## Mise à jour Gemini

- fichier mis à jour depuis les normalisés :
  - `09_exports/gemini_context/gemini_cuisine_escoffier_v1_draft.md`

Le draft a été resserré pour :

- rester court
- éviter le catalogue de sauces nommées
- mettre en avant mécanismes, familles et choix

## Décision

- décision : `prêt pour audit`
- réserve : `systemes` reste le sous-lot le plus fragile et le plus susceptible de fusion supplémentaire
