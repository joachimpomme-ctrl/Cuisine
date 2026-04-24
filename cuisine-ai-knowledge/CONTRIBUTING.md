# CONTRIBUTING

## Périmètre

Ce dépôt sert à construire des bases de connaissance culinaires lisibles par humains et agents IA. La priorité actuelle est `04_rules/`.

## Règles obligatoires

- Ne jamais écrire directement dans `04_rules/final/` sans validation explicite.
- Toute production initiale doit être créée dans `04_rules/raw/`.
- `Claude` écrit uniquement dans `04_rules/raw/`.
- `Gemini` écrit lui aussi dans `04_rules/raw/` pour proposer enrichissements et compléments.
- Chaque lot brut doit toujours être accompagné d'un fichier `.meta.json`.
- Lancer `08_scripts/validate_jsonl.py` avant toute normalisation.
- Relire les doublons et quasi-doublons avec `08_scripts/detect_duplicates.py` avant finalisation.
- Toute règle finale doit être atomique, claire, actionnable et contextualisée.
- Ne pas créer de recettes complètes dans la base `rules`.
- Ne pas mélanger règles générales et préférences familiales.
- Ne pas intégrer d'information médicale ou nutritionnelle fragile sans prudence explicite.
- Signaler les règles liées à l'hygiène et à la sécurité alimentaire.

## Répartition des rôles

- `Codex` maintient la structure, valide, normalise, maintient les scripts et génère les exports.
- `Claude` produit du contenu brut uniquement dans `04_rules/raw/`.
- `Gemini` enrichit les lots bruts, signale les lacunes et aide à la couverture sans écrire directement dans `final`.
- `ChatGPT` arbitre la structure, la cohérence éditoriale et la qualité métier.

## Qualité attendue pour une règle

Une bonne règle est :

- atomique ;
- actionnable ;
- contextualisée ;
- prudente ;
- non redondante ;
- utile pour une cuisine familiale ;
- facilement exploitable par un agent IA.

Une mauvaise règle :

- est trop générale ;
- ressemble à une recette complète ;
- mélange plusieurs idées ;
- n'a pas de conditions ;
- n'a pas d'application concrète ;
- ignore les exceptions ;
- contredit une autre règle.

## Convention de lot brut

Exemple :

```text
04_rules/raw/cuisson/cuisson_fondamentale_claude_v1.jsonl
04_rules/raw/cuisson/cuisson_fondamentale_claude_v1.meta.json
```

Exemple de métadonnées :

```json
{
  "source_ai": "claude",
  "date": "YYYY-MM-DD",
  "domain": "cuisson",
  "scope": "cuissons fondamentales",
  "status": "raw",
  "reviewed_by": [],
  "notes": ""
}
```

## Commandes utiles

```bash
python3 08_scripts/validate_jsonl.py 04_rules/raw
python3 08_scripts/detect_duplicates.py 04_rules/raw 04_rules/normalized 04_rules/final
python3 08_scripts/build_exports.py
```
