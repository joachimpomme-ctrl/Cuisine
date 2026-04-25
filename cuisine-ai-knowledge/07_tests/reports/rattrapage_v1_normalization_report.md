# Rapport de normalisation `rattrapage_v1`

## Périmètre

- Source : `04_rules/raw/rattrapage/rattrapage_v1_raw.jsonl`
- Sortie normalisée : `04_rules/normalized/rattrapage/rattrapage_v1_normalized.jsonl`
- Domaine : `rattrapage`
- Objectif : préparer un lot relisible et validable avant audit éditorial et métier

## Résumé

- Nombre de règles dans le lot normalisé : `30`
- Règles supprimées : `0`
- Règles ajoutées : `0`
- Identifiants modifiés : `0`
- Validation JSONL : `OK`
- Erreurs bloquantes : `0`

La normalisation est volontairement légère. Le contenu métier n'a pas été enrichi. Les ajustements portent uniquement sur certaines formulations trop abstraites ou trop générales.

## Contrôles effectués

### 1. Validation JSONL et schéma

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py cuisine-ai-knowledge/04_rules/normalized/rattrapage/rattrapage_v1_normalized.jsonl
```

Résultat :

- `30` enregistrements validés
- aucune erreur de structure
- aucun champ obligatoire manquant
- types et valeurs contrôlées conformes

### 2. Détection de doublons

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py \
  cuisine-ai-knowledge/04_rules/normalized/rattrapage/rattrapage_v1_normalized.jsonl \
  cuisine-ai-knowledge/04_rules/raw/rattrapage/rattrapage_v1_raw.jsonl \
  cuisine-ai-knowledge/04_rules/final \
  cuisine-ai-knowledge/04_rules/normalized/cuisson \
  --report cuisine-ai-knowledge/07_tests/reports/rattrapage_v1_normalized_duplicate_report.md
```

Résultat brut :

- Groupes de doublons exacts : `67`
- Paires de quasi-doublons : `2`

Interprétation utile :

- les doublons exacts concernant `rattrapage` proviennent presque entièrement de la coexistence normale entre le fichier `raw` et le fichier `normalized` ;
- une partie du bruit vient aussi des doublons historiques déjà présents dans le corpus `cuisson` ;
- aucune collision conceptuelle ou textuelle claire n'a été détectée entre le lot `rattrapage` normalisé et les lots `cuisson` existants ;
- les `2` quasi-doublons concernent uniquement des règles `rattrapage` légèrement reformulées entre `raw` et `normalized`, ce qui est attendu.

## Harmonisations réalisées

La normalisation a conservé les `30` règles et tous les IDs d'origine.

Ajustements légers effectués :

- `RATTRAPAGE_TROP_SUCRE_003` : formulation rendue plus explicite sur la réorientation d'usage quand la correction directe n'est plus réaliste
- `RATTRAPAGE_SAUCE_QUI_TRANCHE_002` : formulation adoucie pour éviter une promesse trop forte de récupération
- `RATTRAPAGE_VIANDE_SECHE_001` : recentrage sur le principe de service et non sur une restauration illusoire de texture
- `RATTRAPAGE_PATES_COLLEES_002` : titre clarifié pour mieux signaler le caractère limité du rattrapage

Ces ajustements n'introduisent ni nouvelle règle ni nouvelle précision technique fragile.

## Règles faibles ou à surveiller

Les règles ci-dessous ne sont pas invalides, mais elles demandent un audit éditorial plus serré avant promotion éventuelle vers `final`.

- `RATTRAPAGE_SAUCE_QUI_TRANCHE_002`
  La formulation reste contextuelle. Le type de sauce et l'état de rupture conditionnent fortement l'utilité réelle de la règle.

- `RATTRAPAGE_TROP_SUCRE_003`
  La règle bascule vers la réorientation d'usage. Elle est utile, mais moins directement corrective que d'autres règles du lot.

- `RATTRAPAGE_VIANDE_SECHE_003`
  Même risque : valeur pratique réelle, mais orientation davantage centrée sur la revalorisation que sur le rattrapage immédiat.

- `RATTRAPAGE_PATES_COLLEES_002`
  La marge de récupération est étroite. La règle doit être relue pour vérifier qu'elle reste assez actionnable sans promettre trop.

- `RATTRAPAGE_RIZ_RATE_002`
  Le principe est pertinent, mais il faut vérifier que la formulation reste suffisamment prudente et ne laisse pas croire à un résultat systématique.

## Zones de flou

- frontière entre `rattrapage immédiat` et `réorientation d'usage`
- frontière entre `correction technique` et `limitation des dégâts`
- variabilité forte selon la préparation pour `sauce qui tranche`, `pâtes collées` et `riz raté`
- risque d'avoir des règles exactes en structure mais inégales en valeur pratique selon le contexte culinaire

## Recommandations pour l'audit

- vérifier quelles règles relèvent vraiment du `rattrapage` et lesquelles devraient peut-être être traitées plus tard comme `revalorisation` ou `anti_gaspillage`
- contrôler que chaque règle reste atomique et orientée action, même quand le vrai rattrapage est limité
- relire en priorité les règles les plus contextuelles : `sauce_qui_tranche`, `viande_seche`, `pates_collees`, `riz_rate`
- vérifier que les exceptions sont suffisantes là où le rattrapage n'est pas reproductible
- confirmer que le lot ne promet jamais une restauration complète quand il s'agit seulement d'atténuer un défaut

## Conclusion

Le lot `rattrapage_v1_normalized.jsonl` est propre sur le plan structurel et prêt pour un audit éditorial et métier. La principale vigilance ne porte pas sur le schéma ou les IDs, mais sur la frontière entre correction réelle, atténuation du défaut et réorientation d'usage.
