# Rapport export Gemini `escoffier_v1`

## Source utilisée

Source principale :

- `cuisine-ai-knowledge/04_rules/final/escoffier/escoffier_v1_core.jsonl`

Metadata de référence :

- `cuisine-ai-knowledge/04_rules/final/escoffier/escoffier_v1_core.meta.json`

Le contenu n'a pas été repris depuis le RAW ni depuis l'ancien draft.

## Fichiers créés / modifiés

Créé :

- `cuisine-ai-knowledge/09_exports/gemini_context/gemini_cuisine_escoffier_v1.md`
- `cuisine-ai-knowledge/07_tests/reports/gemini_escoffier_v1_export_report.md`

Modifiés :

- `cuisine-ai-knowledge/09_exports/gemini_context/gemini_cuisine_escoffier_v1_draft.md`
- `cuisine-ai-knowledge/09_exports/gemini_context/gemini_instructions.md`

## Draft conservé

- oui
- avertissement ajouté en tête :
  - `Fichier obsolète / draft. Utiliser désormais gemini_cuisine_escoffier_v1.md.`

## Sections incluses dans le fichier Gemini final

- `Rôle de ce fichier`
- `Comment utiliser Escoffier dans le Gem`
- `Principes fondamentaux`
- `Logique des sauces`
- `Associations produit / sauce / garniture`
- `Patterns de plats`
- `Vocabulaire utile`
- `Limites et garde-fous`
- `À ne pas faire`

Nombre de sections : `9`

## Niveau de sortie

Le fichier final est :

- plus riche que le draft ;
- basé sur le lot `final` publié ;
- sans JSON ;
- sans identifiants ;
- sans recette complète ;
- orienté diagnostic, décision et action ;
- compatible avec un usage Gem Gemini.

## Limites

- le lot `systemes` Escoffier n'est pas intégré ici, car il n'a pas été publié dans `final`
- certains concepts classiques restent condensés pour garder un format Gem compact
- le fichier vise une aide domestique moderne, pas une couverture exhaustive d'Escoffier

## Risques de sur-utilisation d'Escoffier

- répondre trop souvent par logique de sauce alors qu'un problème simple relève d'abord de `cuisson`, `assaisonnement` ou `rattrapage`
- laisser le vocabulaire classique prendre trop de place dans une réponse courte
- transformer une réponse pratique en mini-cours

## Décision

- décision : `prêt pour chargement dans Gemini`
