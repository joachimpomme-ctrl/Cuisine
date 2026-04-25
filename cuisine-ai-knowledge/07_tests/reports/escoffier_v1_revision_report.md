# Rapport de révision `escoffier_v1`

## Résultat

- règles révisées : `28`
- règles déplacées vers `escoffier_v1_deferred.jsonl` : `13`
- total normalisé après révision : `150`
- total différé après révision : `46`

Répartition par fichier après révision :

- `escoffier_principes_v1_normalized.jsonl` : `28`
- `escoffier_systemes_v1_normalized.jsonl` : `35`
- `escoffier_associations_v1_normalized.jsonl` : `27`
- `escoffier_patterns_v1_normalized.jsonl` : `18`
- `escoffier_vocabulaire_v1_normalized.jsonl` : `42`

## Règles corrigées

- `ESCOFFIER_PRINCIPE_002`
- `ESCOFFIER_PRINCIPE_003`
- `ESCOFFIER_PRINCIPE_008`
- `ESCOFFIER_PRINCIPE_009`
- `ESCOFFIER_PRINCIPE_011`
- `ESCOFFIER_PRINCIPE_012`
- `ESCOFFIER_PRINCIPE_015`
- `ESCOFFIER_PRINCIPE_036`
- `ESCOFFIER_SYSTEME_003`
- `ESCOFFIER_SYSTEME_006`
- `ESCOFFIER_SYSTEME_008`
- `ESCOFFIER_SYSTEME_017`
- `ESCOFFIER_SYSTEME_024`
- `ESCOFFIER_SYSTEME_029`
- `ESCOFFIER_SYSTEME_033`
- `ESCOFFIER_SYSTEME_050`
- `ESCOFFIER_SYSTEME_051`
- `ESCOFFIER_ASSOCIATION_002`
- `ESCOFFIER_ASSOCIATION_004`
- `ESCOFFIER_ASSOCIATION_006`
- `ESCOFFIER_ASSOCIATION_010`
- `ESCOFFIER_ASSOCIATION_012`
- `ESCOFFIER_ASSOCIATION_018`
- `ESCOFFIER_ASSOCIATION_023`
- `ESCOFFIER_ASSOCIATION_038`
- `ESCOFFIER_PATTERN_004`
- `ESCOFFIER_PATTERN_010`
- `ESCOFFIER_PATTERN_014`

## Règles déplacées

- `ESCOFFIER_SYSTEME_010`
- `ESCOFFIER_SYSTEME_012`
- `ESCOFFIER_SYSTEME_025`
- `ESCOFFIER_SYSTEME_027`
- `ESCOFFIER_SYSTEME_040`
- `ESCOFFIER_ASSOCIATION_031`
- `ESCOFFIER_ASSOCIATION_033`
- `ESCOFFIER_PATTERN_015`
- `ESCOFFIER_PATTERN_023`
- `ESCOFFIER_VOCABULAIRE_015`
- `ESCOFFIER_VOCABULAIRE_016`
- `ESCOFFIER_VOCABULAIRE_037`
- `ESCOFFIER_VOCABULAIRE_038`

## Exemples avant / après

### `ESCOFFIER_PRINCIPE_011`

- avant :
  - `Quand la réduction sont négligés, la sauce devient plus confuse, plus lourde ou moins cohérente avec le produit servi.`
- après :
  - `Si une réduction devient trop sombre, trop salée ou amère, il faut arrêter la réduction et détendre avec un liquide cohérent plutôt que continuer à concentrer.`

### `ESCOFFIER_SYSTEME_003`

- avant :
  - `Pour un agent domestique, fonds brun doit être proposé seulement si son mécanisme apporte une vraie décision et non une complication historique.`
- après :
  - `Proposer un fonds brun seulement si l'utilisateur a besoin d'une base brune profonde pour un jus ou un braisage ; sinon, un jus court ou un fond plus simple suffit.`

### `ESCOFFIER_ASSOCIATION_023`

- avant :
  - `Pour légumes racines, la famille liaison plus enveloppante reste souvent plus cohérente car une sauce un peu plus enveloppante peut rester cohérente.`
- après :
  - `Pour des légumes racines, choisir une sauce courte beurrée, une crème légère ou le jus de cuisson ; si la sauce devient trop lourde, elle efface le goût du légume.`

### `ESCOFFIER_PATTERN_004`

- avant :
  - `Le pattern viande braisee échoue souvent quand la sauce ou la garniture prennent le dessus sur la logique centrale du plat.`
- après :
  - `Une viande braisée se dérègle si la garniture ou une sauce ajoutée prend la place du fond de braisage réduit ; il faut revenir au jus du plat.`

## Validation JSONL

- `principes` : `OK`
- `systemes` : `OK`
- `associations` : `OK`
- `patterns` : `OK`
- `vocabulaire` : `OK`
- `deferred` : `OK`

## Doublons après révision

Contrôle relancé contre `04_rules/final`.

- doublons exacts :
  - `principes` : `0`
  - `systemes` : `0`
  - `associations` : `0`
  - `patterns` : `0`
  - `vocabulaire` : `0`

- quasi-doublons :
  - `principes` : `0`
  - `systemes` : `45`
  - `associations` : `3`
  - `patterns` : `3`
  - `vocabulaire` : `0`

## Effet de la révision

- `systemes` reste le sous-lot le plus dense, mais la réduction de bruit est nette
- `associations` est désormais beaucoup plus décisionnel
- `patterns` est plus proche d'une logique d'agent que d'une logique de cours
- `vocabulaire` a été allégé des termes les moins utiles au premier passage

## Problèmes restants

- certains `systemes` restent proches entre `fonds`, `glaces`, `demi-glace` et `jus liés`
- la frontière entre savoir utile et culture classique reste plus délicate sur les sauces mères
- un futur `final_candidate` devra probablement rester progressif plutôt qu'intégrer tout le lot en une fois

## Décision

- décision : `prêt pour candidate`
- recommandation : commencer par un `final_candidate` centré sur `principes`, `associations`, `patterns`, `vocabulaire`, puis intégrer `systemes` de façon plus sélective si besoin
