# Brief Claude — Génération du lot brut `cuisson_fondamentale_v1_raw`

## Mission

Produire un lot brut de règles JSONL sur les cuissons fondamentales, dans un style strictement atomique et exploitable par agent IA.

## Contraintes

- écrire uniquement dans `04_rules/raw/cuisson/` ;
- produire entre 30 et 40 règles ;
- une idée principale par règle ;
- ne pas écrire de recettes ;
- ne pas écrire dans `04_rules/final/` ;
- respecter le schéma `01_schema/rule.schema.json` ;
- utiliser des IDs de la forme `CUISSON_<SOUS_CATEGORIE>_NNN`.

## Périmètre V1

- saisir
- rissoler
- revenir
- suer
- mijoter
- braiser
- rotir
- griller
- pocher
- bouillir
- vapeur
- four
- basse_temperature
- friture
- rechauffer
- garder_au_chaud
- deglacer
- reduire
- confire

## Ligne éditoriale

- viser des principes robustes ;
- privilégier les erreurs fréquentes utiles ;
- expliciter les conditions réelles ;
- formuler des exceptions quand elles évitent une sur-généralisation ;
- rester prudent sur sécurité alimentaire, surtout pour `rechauffer`, `garder_au_chaud`, `friture`, `basse_temperature`.

## Interdits

- pas de conseil médical ;
- pas de détails arbitraires non recoupés ;
- pas de liste d'étapes de recette ;
- pas de règle qui mélange deux techniques.

## Résultat attendu

Un lot brut dense mais propre, servant de base à une review Gemini et à une normalisation ultérieure par Codex.
