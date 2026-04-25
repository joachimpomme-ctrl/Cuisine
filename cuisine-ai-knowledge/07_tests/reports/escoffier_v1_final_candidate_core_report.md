# Rapport `escoffier_v1_final_candidate_core`

## Résultat

- fichier candidat créé :
  - `cuisine-ai-knowledge/04_rules/normalized/escoffier/escoffier_v1_final_candidate_core.jsonl`
- nombre total de règles : `115`

## Répartition par type

- `principe` : `33`
- `adaptation` : `58`
- `diagnostic` : `18`
- `erreur_a_eviter` : `6`

## Périmètre inclus

Sous-lots inclus :

- `escoffier_principes_v1_normalized.jsonl`
- `escoffier_associations_v1_normalized.jsonl`
- `escoffier_patterns_v1_normalized.jsonl`
- `escoffier_vocabulaire_v1_normalized.jsonl`

Sous-lots exclus temporairement :

- `escoffier_systemes_v1_normalized.jsonl`

## Validation

- validation JSONL : `OK`
- enregistrements validés : `115`

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py \
cuisine-ai-knowledge/04_rules/normalized/escoffier/escoffier_v1_final_candidate_core.jsonl
```

## Doublons contre `final`

- doublons exacts : `0`
- quasi-doublons : `6`

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py \
cuisine-ai-knowledge/04_rules/normalized/escoffier/escoffier_v1_final_candidate_core.jsonl \
cuisine-ai-knowledge/04_rules/final \
--report cuisine-ai-knowledge/07_tests/reports/escoffier_v1_final_candidate_core_duplicates.md
```

## Lecture des risques

- le noyau `core` est propre structurellement et ne réintroduit pas les éléments différés ;
- les quasi-doublons restants reflètent surtout des proximités naturelles avec :
  - `cuisson` sur `réduction`, `liaison`, `finitions`
  - `assaisonnement` sur certaines logiques d'équilibre et de lisibilité
  - `techniques_cap` sur une partie du vocabulaire culinaire
- le lot reste exploitable car le coeur Escoffier apporte une logique de structure, de sauce et de vocabulaire, pas une simple répétition des bases modernes.

## Risques résiduels

- poids encore élevé de `adaptation` par rapport aux autres types
- possible recouvrement conceptuel ponctuel entre `principes` Escoffier et règles déjà connues de `cuisson`
- vocabulaire à surveiller pour éviter qu'un futur export Gemini ne devienne trop scolaire

## Décision

- décision : `prêt pour final`
- recommandation : publier ce `core` séparément du lot `systemes`, qui devra passer par une sélection plus serrée
