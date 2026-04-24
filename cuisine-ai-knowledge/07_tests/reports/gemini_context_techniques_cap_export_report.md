# Rapport export Gemini `techniques_cap`

## Source utilisée

- Fichier source : `04_rules/raw/techniques_cap/techniques_cap_v1_raw.jsonl`
- Niveau de maturité : `raw`

## Fichiers export créés ou modifiés

- `09_exports/gemini_context/gemini_cuisine_techniques_cap.md`
- `09_exports/gemini_context/gemini_instructions.md`
- `09_exports/gemini_context/gemini_cuisine_rules_core.md`

## Nombre approximatif de sections

- `gemini_cuisine_techniques_cap.md` : `9` sections utiles
- `gemini_instructions.md` : `1` section ajoutée
- `gemini_cuisine_rules_core.md` : `1` section ajoutée

## Logique de transformation

- export court, lisible, orienté usage Gemini ;
- suppression des IDs, métadonnées et détails scolaires ;
- regroupement par gestes, découpes, cuissons techniques, liaisons, vocabulaire et points critiques ;
- maintien d'un style direct et actionnable.

## Risques de redondance

- recouvrement partiel avec `gemini_cuisine_cuisson.md` sur :
  - déglacer
  - réduction
  - légumes verts cuits
- recouvrement partiel avec le `core` sur l'idée de point critique avant action

Gestion choisie :

- ne pas recopier les règles de cuisson déjà centrales ;
- garder ici la couche d'exécution technique et de vocabulaire ;
- rappeler que cette couche ne remplace pas le flux principal de diagnostic.

## Recommandations de test Gemini

- tester un besoin de geste :
  - `comment ciseler correctement un oignon ?`
- tester un besoin de vocabulaire :
  - `qu'est-ce que déglacer veut dire ici ?`
- tester une exécution courte :
  - `ma sauce est trop fluide, est-ce que je réduis ou je lie ?`
- tester une limite :
  - `explique vite sans me faire une fiche CAP`

## Décision

- export Gemini : `prêt`
- réserve :
  - la source `techniques_cap` utilisée est encore au niveau `raw`
  - une relecture sera utile si le lot passe ensuite en `normalized` ou `final_candidate`
