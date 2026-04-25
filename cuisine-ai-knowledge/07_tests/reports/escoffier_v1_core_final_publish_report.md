# Rapport de publication `escoffier_v1_core`

## Fichier publié

- `cuisine-ai-knowledge/04_rules/final/escoffier/escoffier_v1_core.jsonl`

Metadata :

- `cuisine-ai-knowledge/04_rules/final/escoffier/escoffier_v1_core.meta.json`

## Volume

- nombre de règles publiées : `115`

## Lots inclus

- `principes`
- `associations`
- `patterns`
- `vocabulaire`

## Lots exclus

- `systemes`

Le lot `systemes` reste hors publication dans cette étape.

## Validation JSONL

- statut : `OK`
- enregistrements validés : `115`

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py \
cuisine-ai-knowledge/04_rules/final/escoffier/escoffier_v1_core.jsonl
```

## Doublons contre `final`

- doublons exacts : `0`
- quasi-doublons : `6`

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py \
cuisine-ai-knowledge/04_rules/final/escoffier/escoffier_v1_core.jsonl \
cuisine-ai-knowledge/04_rules/final \
--report cuisine-ai-knowledge/07_tests/reports/escoffier_v1_core_final_publish_duplicates.md
```

## Note sur l'auto-correspondance

Le fichier publié fait désormais partie de `04_rules/final`.

Le contrôle n'a pas remonté de doublon exact lié à une auto-comparaison du fichier avec lui-même.
Les `6` quasi-doublons signalés doivent donc être lus comme des proximités inter-lots, pas comme un artefact bloquant de la publication.

## Risques résiduels

- proximité naturelle avec `cuisson` sur :
  - réduction
  - liaison
  - finition
- proximité légère avec `techniques_cap` et `organisation` sur une partie du vocabulaire
- le lot reste riche en `adaptation`, ce qui demande de garder une réponse agent compacte et ciblée

## Décision finale

- décision : `lot publié`
- justification :
  - le lot est valide
  - il n'introduit pas de doublon exact dans `final`
  - il reste distinct du lot `systemes`, volontairement non publié à ce stade
