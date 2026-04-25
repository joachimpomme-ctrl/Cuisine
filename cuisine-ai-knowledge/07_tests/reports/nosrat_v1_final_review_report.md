# Rapport de review finale Nosrat v1

- Date : 2026-04-25
- Décision finale : prêt pour final

## Sources contrôlées

- `cuisine-ai-knowledge/04_rules/raw/nosrat/nosrat_rules_v1.jsonl`
- `cuisine-ai-knowledge/04_rules/normalized/nosrat/nosrat_rules_v1_normalized.jsonl`
- `cuisine-ai-knowledge/04_rules/normalized/nosrat/nosrat_rules_v1_deferred.jsonl`
- `cuisine-ai-knowledge/01_schema/rule.schema.json`

Le fichier raw n’a pas été modifié.

## Volumétrie

- Règles raw : 50
- Règles normalisées : 47
- Règles déjà différées : 3
- Règles acceptées pour final : 44
- Règles à réviser avant final : 3
- Règles maintenues différées : 3

## Validation JSONL

Commande exécutée sur la normalisation :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py cuisine-ai-knowledge/04_rules/normalized/nosrat/nosrat_rules_v1_normalized.jsonl
```

Résultat :

```text
Validation effectuée sur 1 fichier(s) et 47 enregistrement(s) JSONL.
Validation réussie sans erreur.
```

Commande exécutée sur le final candidate :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py cuisine-ai-knowledge/04_rules/final/nosrat/nosrat_taste_rules_v1.jsonl
```

Résultat :

```text
Validation effectuée sur 1 fichier(s) et 44 enregistrement(s) JSONL.
Validation réussie sans erreur.
```

## Contrôle doublons

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py cuisine-ai-knowledge/04_rules/normalized/nosrat/nosrat_rules_v1_normalized.jsonl cuisine-ai-knowledge/04_rules/final --report cuisine-ai-knowledge/07_tests/reports/nosrat_v1_final_review_duplicates.md
```

L’option `--exclude-cross-stage` n’est pas disponible dans le script actuel ; elle n’a pas été utilisée.

Résultat :

```text
Analyse effectuée sur 6 fichier(s) et 261 enregistrement(s).
Groupes de doublons exacts : 0
Paires de quasi-doublons : 6
```

Les 6 quasi-doublons détectés concernent des paires déjà présentes dans le corpus final Escoffier.
Aucun doublon exact entre Nosrat normalisé et le corpus final existant n’a été détecté.

## Classement éditorial

### accepted_for_final

44 règles ont été acceptées et publiées dans :

```text
cuisine-ai-knowledge/04_rules/final/nosrat/nosrat_taste_rules_v1.jsonl
```

Critères validés :

- règle atomique ;
- actionnable ;
- conforme au schéma ;
- utile pour un agent cuisine domestique ;
- non spéculative dans son usage courant ;
- non redondante avec le corpus final existant au niveau doublon exact.

### revise_before_final

- `NOSRAT_FAT_002` : règle intéressante mais trop contextuelle sur le choix culturel du gras ; elle relève davantage d’un module inspiration/adaptation que d’une règle canonique immédiate.
- `NOSRAT_HEAT_005` : règle sur le tempérage de la viande utile mais à préciser avec des garde-fous de sécurité alimentaire avant publication canonique.
- `NOSRAT_HEAT_016` : règle sur le service très chaud des plats d’hiver trop générale et dépendante du contexte de service.

### keep_deferred

- `NOSRAT_020` : frites crues ou molles ; protocole trop spécifique et à revoir dans un module friture ou recette.
- `NOSRAT_030` : œufs brouillés secs ; correction à l’acide trop spécifique et à valider pratiquement.
- `NOSRAT_033` : saturation umami ; logique utile mais formulation et périmètre à arbitrer avant normalisation canonique.

## Règles exclues avec raison

- 3 règles normalisées exclues du final : `NOSRAT_FAT_002`, `NOSRAT_HEAT_005`, `NOSRAT_HEAT_016`.
- 3 règles différées conservées hors final : `NOSRAT_020`, `NOSRAT_030`, `NOSRAT_033`.

## Contraintes vérifiées

- Raw Nosrat non modifié.
- Export Gemini Nosrat non modifié.
- Prompt Gemini non modifié.
- Aucune règle inventée.
- Aucune règle non validée incluse en final.

## Décision finale

Prêt pour final.
