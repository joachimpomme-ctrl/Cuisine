# cuisine-ai-knowledge

`cuisine-ai-knowledge` est un atelier de construction de knowledge culinaire pour agents IA. Le dépôt est conçu pour rester lisible par des humains, contrôlable par scripts et exploitable dans des environnements comme ChatGPT Projects, Gemini Gems, Claude Projects ou un pipeline RAG.

La priorité actuelle est la base `rules`, avec une approche prudente : peu d'exemples, un schéma strict, des validations explicites et un workflow clair avant toute production massive.

## Objectif du projet

Le projet vise à produire un corpus culinaire structuré, stable et réutilisable, organisé en trois bases séparées :

- `rules` : règles générales de cuisine, atomiques, actionnables, filtrables et exportables.
- `recipes` : recettes normalisées, adaptables et interrogeables.
- `household_context` : préférences familiales, contraintes, équipements, ingrédients fréquents et habitudes domestiques.

Cette séparation est volontaire. Elle évite de mélanger les règles générales avec des recettes détaillées ou des préférences locales.

## Architecture du dépôt

```text
01_schema/              Schémas JSON officiels
02_taxonomie/           Taxonomie métier et conventions de classification
03_prompts/             Prompts de génération, review, normalisation et gap analysis
04_rules/
  raw/                  Lots bruts produits par les IA contributrices
  normalized/           Lots harmonisés et conformes au schéma
  reviews/              Rapports d'audit qualité, doublons et couverture
  final/                Corpus validé, stable et exportable
05_recipes/             Base réservée aux recettes
06_household_context/   Base réservée au contexte familial
07_tests/
  reports/              Rapports générés par les scripts
08_scripts/             Validation JSONL, doublons et exports
09_exports/             Artefacts de sortie pour Projects, Gems et RAG
10_research/            Recherche documentaire et protocoles de transformation source -> règle
```

## 🧠 Types de knowledge

Le projet distingue plusieurs niveaux de connaissance :

### 1. Règles canoniques

Chemin :
`04_rules/final/`

Ce sont les règles atomiques validées, conformes au schéma officiel `01_schema/rule.schema.json`.
Elles servent de base stable, contrôlée et exportable.

### 2. Extractions et corpus sources

Chemins possibles :
`04_rules/raw/`
`04_rules/normalized/`

Ces fichiers peuvent contenir des formats intermédiaires issus de Claude, Gemini, Codex ou ChatGPT.
Ils ne sont pas tous destinés à être utilisés directement par un agent final.
Ils doivent être normalisés avant passage éventuel en `final`.

### 3. Exports agent

Chemin :
`09_exports/gemini_context/`

Ces fichiers sont optimisés pour l’usage dans Gemini Gems ou autres agents conversationnels.
Ils peuvent être synthétiques, orientés décision, et ne respectent pas forcément `rule.schema.json`.
Ils sont une couche d’usage, pas la source canonique.

### Règle importante

Ne pas confondre :

- `04_rules/final/` = vérité structurée ;
- `09_exports/gemini_context/` = contexte opérationnel pour agent.

## Modules agent actuels

- Core rules : raisonnement général
- Cuisson : techniques de cuisson
- Assaisonnement : équilibre du goût
- Rattrapage : correction des erreurs
- CAP techniques : gestes et bases techniques
- Escoffier : structure des plats
- McGee : science culinaire
- Nosrat : décisions rapides de goût

Les modules McGee, Nosrat et Escoffier existent aussi sous forme d’exports Gemini dans `09_exports/gemini_context/`.

## Rôles des IA

- `Codex` : architecte technique et gardien du repo. Il maintient la structure, les schémas, les scripts, la validation, les exports et la qualité structurelle.
- `Claude` : producteur principal de contenu brut. Il écrit des lots de règles dans `04_rules/raw/`.
- `Gemini` : auditeur et enrichisseur. Il peut produire de nouveaux lots bruts dans `04_rules/raw/` et signaler les manques ou ambiguïtés.
- `ChatGPT` : directeur éditorial et arbitre métier. Il fixe les conventions, tranche les cas ambigus, décide ce qui passe en `final` et maintient la cohérence globale.

## Workflow `raw -> normalized -> final -> exports`

### 1. Production brute

Les IA de production écrivent dans `04_rules/raw/<domaine>/<lot>.jsonl`.

Chaque lot brut doit avoir un fichier jumeau :

```text
04_rules/raw/<domaine>/<lot>.meta.json
```

Le `.meta.json` documente au minimum :

- `source_ai`
- `date`
- `domain`
- `scope`
- `status`
- `reviewed_by`
- `notes`

### 2. Validation initiale

Avant toute normalisation, le lot brut est validé avec `08_scripts/validate_jsonl.py`.

Cette étape vérifie :

- la validité JSON ligne par ligne ;
- la présence des champs obligatoires ;
- les types ;
- les valeurs contrôlées ;
- le format des IDs.

### 3. Normalisation

Codex ou ChatGPT consolide le lot dans :

```text
04_rules/normalized/<domaine>/<lot>.jsonl
```

À cette étape :

- le JSONL est propre ;
- le schéma est respecté ;
- les formulations sont harmonisées ;
- les IDs et classifications sont normalisés ;
- le lot n'est pas encore considéré comme vérité finale.

### 4. Review qualité

Une review est produite dans :

```text
04_rules/reviews/<domaine>/<lot>_review.md
```

Elle doit contrôler :

- la qualité structurelle ;
- les doublons ;
- les quasi-doublons ;
- les contradictions ;
- les règles trop vagues ;
- les risques d'hygiène ;
- les angles morts de couverture ;
- l'utilité pour une cuisine familiale.

### 5. Finalisation

Seules les règles explicitement validées passent dans :

```text
04_rules/final/<domaine>/<lot>.jsonl
```

`final` est le corpus de référence stable. Aucune IA ne doit y écrire directement sans validation explicite.

### 6. Exports

Les exports sont générés depuis `04_rules/final/` vers `09_exports/`.

Sorties prévues :

- `rules_master.jsonl`
- `rules_master.md`
- `rules_index.json`
- `rules_by_domain/*.jsonl`

## Commandes utiles

### Valider un lot brut

```bash
python3 08_scripts/validate_jsonl.py 04_rules/raw/cuisson/cuisson_fondamentale_claude_v1.jsonl
```

### Valider plusieurs zones du dépôt

```bash
python3 08_scripts/validate_jsonl.py 04_rules/raw 04_rules/normalized 04_rules/final
```

### Détecter les doublons

```bash
python3 08_scripts/detect_duplicates.py 04_rules/raw 04_rules/normalized 04_rules/final
```

Le rapport est écrit dans `07_tests/reports/duplicate_report.md`.

### Générer les exports

```bash
python3 08_scripts/build_exports.py
```

## Jeu d'exemples inclus

Le dépôt contient volontairement un petit jeu de démonstration sur `cuisson` avec seulement quelques règles réparties entre `raw`, `normalized` et `final`. Le but est de valider l'atelier, pas de produire encore un corpus massif.

## Prochaine étape

La prochaine étape prévue est la recherche documentaire sur les règles de cuisson fondamentales. Le dossier `10_research/` prépare ce travail avec une grille d'évaluation des sources, des listes de références cibles et un protocole de passage de la source vers une règle exploitable.
