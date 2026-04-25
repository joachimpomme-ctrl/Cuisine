# Architecture des couches de knowledge

## Objectif

Clarifier les niveaux de connaissance utilisés dans `cuisine-ai-knowledge` et leur usage.
Le but est d’éviter de mélanger règles canoniques, corpus sources et exports destinés aux agents conversationnels.

## Couche 1 — Canonical rules

Les règles canoniques vivent dans :

```text
04_rules/final/
```

Elles sont atomiques, validées et conformes au schéma officiel :

```text
01_schema/rule.schema.json
```

Cette couche est la base structurée du système.
Elle sert aux validations, aux exports contrôlés et aux décisions éditoriales.

## Couche 2 — Source corpora

Les corpus sources et extractions vivent principalement dans :

```text
04_rules/raw/
04_rules/normalized/
10_research/
```

Ils peuvent venir de Claude, Gemini, Codex, ChatGPT ou d’un travail de recherche.
Ils documentent la production, les choix, les sources et les états intermédiaires.

Ces fichiers ne sont pas tous utilisables directement par un agent final.
Ils doivent être filtrés, harmonisés et validés avant de devenir des règles canoniques.

## Couche 3 — Agent exports

Les exports agent vivent dans :

```text
09_exports/gemini_context/
```

Ils sont conçus pour être chargés dans Gemini Gems ou dans d’autres agents conversationnels.
Ils peuvent être synthétiques, orientés décision et optimisés pour la réponse utilisateur.

Ils ne sont pas forcément conformes au schéma des règles.
Ils représentent une couche d’usage, pas la vérité canonique.

## Couche 4 — Recipes & patterns

Les recettes et patterns servent à l’exécution et à l’inspiration.
Ils complètent les règles, mais ne remplacent pas la couche canonique.

Les patterns peuvent aider l’agent à proposer des idées, des associations ou des structures de plats.
Les recettes doivent rester séparées des règles générales pour éviter de mélanger exécution détaillée et principes culinaires.

## Principe de gouvernance

- raw = production
- normalized = harmonisation
- final = validation
- exports = usage agent

## Décision importante

Tous les fichiers utiles à Gemini ne sont pas des règles canoniques.
Tous les corpus extraits ne doivent pas être injectés tels quels dans Gemini.

## Risques évités

- duplication
- confusion entre source et export
- perte de traçabilité
- sur-normalisation prématurée
