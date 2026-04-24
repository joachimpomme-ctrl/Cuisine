# Rapport initial `escoffier_v1`

## Source utilisée

- source principale : `documents/Le_guide_culinaire.rtf`
- nature : traité culinaire classique
- auteur : `Auguste Escoffier`
- niveau d'usage dans ce lot : `raw`, extraction massive mais sélective

## Sections exploitées

Sections principalement exploitées dans la source :

- `Sauces` :
  - fonds de cuisine
  - principes généraux
  - fumets
  - essences
  - glaces
  - roux
  - grandes sauces de base
  - sauces dérivées
  - sauces froides
  - beurres composés
  - marinades
  - gelées
- `Potages` :
  - consommés
  - clarifications
- `Œufs`, `Poissons`, `Rôtis`, `Garnitures` :
  - surtout pour les patterns et associations

## Sections volontairement exclues

- recettes complètes ;
- longues proportions historiques ;
- listings exhaustifs de garnitures ;
- dressages et présentations ;
- logiques de grand restaurant inutiles en contexte domestique ;
- procédés sensibles non encadrés, sauf mention prudente de principe.

## Nombre d’entrées par fichier

- `escoffier_principes_v1_raw.jsonl` : `36`
- `escoffier_systemes_v1_raw.jsonl` : `52`
- `escoffier_associations_v1_raw.jsonl` : `38`
- `escoffier_patterns_v1_raw.jsonl` : `24`
- `escoffier_vocabulaire_v1_raw.jsonl` : `46`

Total : `196`

## Validation JSONL

- `principes` : `OK`
- `systemes` : `OK`
- `associations` : `OK`
- `patterns` : `OK`
- `vocabulaire` : `OK`

## Doublons détectés

- doublons exacts : `0` sur tous les lots
- quasi-doublons :
  - `principes` : `51`
  - `systemes` : `124`
  - `associations` : `88`
  - `patterns` : `31`
  - `vocabulaire` : `0`

## Principaux apports nouveaux

- une couche de raisonnement sur les bases, fonds, fumets, glaces et roux ;
- une lecture systémique des sauces mères et dérivées ;
- des patterns de plats classiques réutilisables par agent IA ;
- une modernisation utile des couples produit / sauce / finition ;
- un vocabulaire culinaire classique traduit en langage domestique.

## Risques de bruit

- densité élevée sur les systèmes culinaires ;
- proximité conceptuelle avec les lots `cuisson` et `techniques_cap` ;
- risque de verbosité si le lot est consommé brut sans couche éditoriale.

## Risques de datation

- plusieurs noms de sauces et usages de service restent marqués historiquement ;
- certains procédés sont trop longs pour un usage domestique standard ;
- des éléments comme `saumure`, `gelée` ou `chaud-froid` demandent une forte prudence contextuelle.

## Recommandations avant normalisation

- fusionner ou resserrer certaines familles dans `systemes` ;
- réduire les quasi-doublons les plus évidents autour de `fonds`, `réduction`, `liaison`, `finition` ;
- trier ce qui relève d'une vraie aide domestique de ce qui relève surtout de culture culinaire ;
- garder une vigilance forte sur la traduction Gemini pour ne pas transformer le Gem en manuel ancien.

## Export Gemini

- export créé : `09_exports/gemini_context/gemini_cuisine_escoffier_v1_draft.md`
- mise à jour effectuée : `gemini_instructions.md`

## Décision

- décision : `prêt pour normalisation`
- réserve : lot riche et prometteur, mais encore trop dense pour être promu sans passe éditoriale.
