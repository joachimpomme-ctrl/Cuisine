# Rapport de normalisation Nosrat v1

- Date : 2026-04-25
- Décision : prêt pour review avant final

## Source utilisée

- Source unique : `cuisine-ai-knowledge/04_rules/raw/nosrat/nosrat_rules_v1.jsonl`
- Source éditoriale déclarée : `Salt, Fat, Acid, Heat` — Samin Nosrat
- Le fichier raw n’a pas été modifié.

## Volumétrie

- Règles raw analysées : 50
- Règles normalisées : 47
- Règles différées : 3

## Fichiers produits

- `cuisine-ai-knowledge/04_rules/raw/nosrat/nosrat_rules_v1.meta.json`
- `cuisine-ai-knowledge/04_rules/normalized/nosrat/nosrat_rules_v1_normalized.jsonl`
- `cuisine-ai-knowledge/04_rules/normalized/nosrat/nosrat_rules_v1_deferred.jsonl`
- `cuisine-ai-knowledge/07_tests/reports/nosrat_v1_normalization_duplicates.md`
- `cuisine-ai-knowledge/07_tests/reports/nosrat_v1_normalization_report.md`

## Mapping appliqué

- `salt` -> domaine `assaisonnement`, catégorie `sel`
- `fat` -> domaine `assaisonnement`, `cuisson` ou `sauce` selon l’usage
- `acid` -> domaine `assaisonnement`, `cuisson`, `sauce`, `rattrapage` ou `conservation` selon l’usage
- `heat` -> domaine `cuisson` ou `sauce` selon l’usage
- `priority: 1` -> niveau `fondamental`
- `priority: 2` -> niveau `intermediaire`
- `priority: 3` -> niveau `avance`
- Les IDs ont été rendus explicites par famille : `NOSRAT_SALT_*`, `NOSRAT_FAT_*`, `NOSRAT_ACID_*`, `NOSRAT_HEAT_*`.
- Les champs `trigger`, `diagnostic`, `action` et `effect` ont été reformulés en règles françaises atomiques avec `conditions`, `application`, `erreurs_frequentes` et `exceptions`.

## Sources

Le schéma canonique actuel `01_schema/rule.schema.json` ne contient pas le champ `sources`.
Les règles normalisées n’intègrent donc pas de champ `sources`, afin de rester strictement conformes au schéma.
La traçabilité de lot est portée par `nosrat_rules_v1.meta.json`.

## Règles différées

- `NOSRAT_020` : règle trop spécifique aux frites et formulation source à revoir avec un protocole friture complet.
- `NOSRAT_030` : règle sur les œufs brouillés jugée trop spécifique et potentiellement contestable sans validation pratique.
- `NOSRAT_033` : règle sur la saturation umami utile mais trop dépendante du contexte et formulée de façon trop informelle pour passage direct.

## Règles fusionnées ou reformulées

- Aucune fusion de règles source.
- Les 47 règles retenues ont été reformulées pour respecter le schéma canonique et produire des règles actionnables en français.
- Les contenus ont été conservés dans le périmètre du raw : aucune règle nouvelle n’a été ajoutée.

## Problèmes détectés

- Le raw Nosrat est structuré, mais non conforme au schéma canonique.
- Certaines entrées relèvent davantage d’un protocole technique ou d’un arbitrage éditorial que d’une règle canonique immédiate.
- Le champ `sources` demandé ne peut pas être ajouté aux règles tant qu’il n’existe pas dans le schéma.

## Validation JSONL

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py cuisine-ai-knowledge/04_rules/normalized/nosrat/nosrat_rules_v1_normalized.jsonl
```

Résultat :

```text
Validation effectuée sur 1 fichier(s) et 47 enregistrement(s) JSONL.
Validation réussie sans erreur.
```

## Doublons exacts / quasi-doublons

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py cuisine-ai-knowledge/04_rules/normalized/nosrat/nosrat_rules_v1_normalized.jsonl cuisine-ai-knowledge/04_rules/final --report cuisine-ai-knowledge/07_tests/reports/nosrat_v1_normalization_duplicates.md
```

L’option `--exclude-cross-stage` n’est pas disponible dans le script actuel ; elle n’a donc pas été utilisée.

Résultat :

```text
Analyse effectuée sur 6 fichier(s) et 261 enregistrement(s).
Groupes de doublons exacts : 0
Paires de quasi-doublons : 6
```

Les 6 quasi-doublons signalés concernent des paires déjà présentes dans le corpus final Escoffier.
Aucun doublon exact Nosrat/final n’a été détecté.

## Décision

Prêt pour review avant final.
