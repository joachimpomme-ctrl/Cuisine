# Audit Codex `assaisonnement_v1_raw`

## Périmètre

- Fichier audité : `cuisine-ai-knowledge/04_rules/raw/assaisonnement/assaisonnement_v1_raw.jsonl`
- Nombre de règles auditées : `36`
- Modifications des JSONL : `aucune`

## Méthode

L'audit contrôle :

- la qualité éditoriale ;
- l'exploitabilité directe par un agent IA ;
- la cohérence métier propre au domaine `assaisonnement` ;
- les risques spécifiques du domaine : abstraction, redondance, glissement vers `rattrapage`, formulations trop conceptuelles.

Décisions utilisées :

- `keep`
- `revise`
- `move_later`
- `reject`

## Synthèse

- `keep` : `27`
- `revise` : `7`
- `move_later` : `2`
- `reject` : `0`

Lecture générale :

- le lot est globalement cohérent, utile et mieux cadré que beaucoup de lots RAW classiques ;
- la structure est bonne, les règles sont majoritairement atomiques et prudentes ;
- le principal risque n'est pas le faux contenu, mais le flou conceptuel sur certaines règles plus abstraites ;
- la frontière `assaisonnement` / `rattrapage` est globalement respectée, mais quelques formulations s'en approchent.

## Décision par règle

| ID | Décision | Motif |
| --- | --- | --- |
| `ASSAISONNEMENT_SEL_001` | `keep` | Principe clair, utile et directement exploitable. |
| `ASSAISONNEMENT_SEL_002` | `keep` | Très bonne règle de diagnostic, structurante pour tout le lot. |
| `ASSAISONNEMENT_SEL_003` | `keep` | Procédure simple, concrète, immédiatement actionnable. |
| `ASSAISONNEMENT_SEL_004` | `keep` | Bonne distinction entre saler et ajouter un ingrédient salé. |
| `ASSAISONNEMENT_POIVRE_001` | `keep` | Frontière claire entre relief aromatique et correction de structure. |
| `ASSAISONNEMENT_POIVRE_002` | `revise` | Utile mais encore un peu contextuelle. Le `souvent` et le moment tardif devront être resserrés éditorialement. |
| `ASSAISONNEMENT_ACIDITE_001` | `keep` | Bonne règle de levier gustatif, claire et domestiquement applicable. |
| `ASSAISONNEMENT_ACIDITE_002` | `keep` | Diagnostic fin et utile, sans glisser vers une pseudo-théorie vague. |
| `ASSAISONNEMENT_ACIDITE_003` | `keep` | Excellente règle de méthode, directement exploitable. |
| `ASSAISONNEMENT_SUCRE_001` | `revise` | Fond juste, mais le couplage `acidité ou amertume` rend la règle légèrement trop large. |
| `ASSAISONNEMENT_SUCRE_002` | `keep` | Bonne règle de non-masquage, utile pour agent IA. |
| `ASSAISONNEMENT_GRAS_001` | `keep` | Règle concrète, bien distinguée du sel et de l'acidité. |
| `ASSAISONNEMENT_GRAS_002` | `keep` | Bonne qualité de diagnostic, utile pour la cuisine familiale. |
| `ASSAISONNEMENT_UMAMI_001` | `keep` | Bien formulée, utile, sans mysticisme culinaire. |
| `ASSAISONNEMENT_UMAMI_002` | `keep` | Bonne règle procédurale, claire et prudente. |
| `ASSAISONNEMENT_AMERTUME_001` | `keep` | Bonne base de diagnostic, cohérente et non excessive. |
| `ASSAISONNEMENT_AMERTUME_002` | `revise` | La notion de `rééquilibrage` reste un peu abstraite et multi-leviers. |
| `ASSAISONNEMENT_HERBES_FRAICHES_001` | `keep` | Règle claire, exploitable, non fragile. |
| `ASSAISONNEMENT_HERBES_FRAICHES_002` | `keep` | Bonne frontière entre aromatique et base gustative. |
| `ASSAISONNEMENT_HERBES_SECHES_001` | `keep` | Principe simple, domestiquement robuste. |
| `ASSAISONNEMENT_HERBES_SECHES_002` | `revise` | Bonne idée mais formulation un peu floue sur `alourdir` et `peu fondue`. |
| `ASSAISONNEMENT_EPICES_001` | `revise` | Le coeur est bon, mais la notion d'`effet recherché` reste encore large. |
| `ASSAISONNEMENT_EPICES_002` | `keep` | Bonne mise en garde contre un faux correctif aromatique. |
| `ASSAISONNEMENT_AROMATES_001` | `keep` | Bonne règle de structure, utile et cohérente. |
| `ASSAISONNEMENT_AROMATES_002` | `keep` | Très bon point de diagnostic, sans abstraction excessive. |
| `ASSAISONNEMENT_BOUILLON_001` | `keep` | Règle claire, à forte valeur pratique. |
| `ASSAISONNEMENT_BOUILLON_002` | `keep` | Bonne règle de frontière entre enrichir et corriger par réflexe. |
| `ASSAISONNEMENT_ALCOOL_001` | `move_later` | Intéressant, mais plus contextuel et moins central pour un premier noyau domestique d'assaisonnement. |
| `ASSAISONNEMENT_ALCOOL_002` | `move_later` | Solide conceptuellement, mais proche du précédent et moins prioritaire pour le coeur du domaine. |
| `ASSAISONNEMENT_EQUILIBRE_001` | `keep` | Très bonne règle pivot pour tout le lot. |
| `ASSAISONNEMENT_EQUILIBRE_002` | `keep` | Règle simple, atomique, très utile pour agent IA. |
| `ASSAISONNEMENT_EQUILIBRE_003` | `revise` | Bonne frontière conceptuelle, mais le mot `masquer` peut rester un peu abstrait sans reformulation plus opérationnelle. |
| `ASSAISONNEMENT_PROGRESSIF_001` | `keep` | Très bonne règle stratégique, claire et directement actionnable. |
| `ASSAISONNEMENT_PROGRESSIF_002` | `keep` | Bonne règle de procédure, simple et robuste. |
| `ASSAISONNEMENT_DEGUSTATION_001` | `revise` | Le fond est excellent, mais la formulation `fade ou bizarre` gagnerait à être plus nette. |
| `ASSAISONNEMENT_DEGUSTATION_002` | `keep` | Très bonne règle structurante, au coeur du domaine. |

## Qualité éditoriale

Points forts :

- la majorité des titres sont précis ;
- les règles portent généralement une seule idée principale ;
- le ton reste pragmatique et non démonstratif ;
- peu de pseudo-théorie culinaire gratuite.

Faiblesses principales :

- certaines règles s'appuient sur un vocabulaire encore un peu conceptuel :
  - `rééquilibrage`
  - `effet recherché`
  - `masquer`
  - `alourdir`
  - `bizarre`
- quelques règles sont plus des principes de lecture que des gestes directement formulés.

## Qualité agent IA

Le lot est globalement bon pour un agent IA :

- les conditions sont le plus souvent utiles ;
- les applications sont généralement concrètes ;
- les erreurs fréquentes sont pertinentes ;
- les exceptions servent réellement à limiter la généralisation abusive.

Les règles les moins nettes sur ce critère sont :

- `ASSAISONNEMENT_AMERTUME_002`
- `ASSAISONNEMENT_EPICES_001`
- `ASSAISONNEMENT_EQUILIBRE_003`
- `ASSAISONNEMENT_DEGUSTATION_001`

Ce ne sont pas de mauvaises règles, mais elles demandent plus d'interprétation que le noyau du lot.

## Cohérence métier

### Distinction entre axes de goût

La séparation est globalement bonne entre :

- `sel`
- `acidite`
- `sucre`
- `gras`
- `aromatique`

Points particulièrement réussis :

- `SEL_002` vs `GRAS_002`
- `ACIDITE_002` vs `SEL_002`
- `DEGUSTATION_002`, qui synthétise bien les différences sans les confondre

### Assaisonnement vs rattrapage

Le lot reste majoritairement dans l'assaisonnement :

- construction du goût ;
- ajustement progressif ;
- diagnostic précoce ;
- prévention de la surcorrection.

Le glissement vers `rattrapage` existe surtout quand la règle parle trop de correction d'un défaut déjà dominant. C'est le cas à surveiller pour :

- `SUCRE_001`
- `AMERTUME_002`
- `EQUILIBRE_003`

### Règles trop vagues

Le lot évite globalement les formulations du type `ajouter ce qui manque`. C'est un bon point.

Les règles qui restent un peu trop générales sont surtout :

- `EPICES_001`
- `AMERTUME_002`
- `EQUILIBRE_003`

## Risques spécifiques au domaine assaisonnement

### Règles trop abstraites

- `ASSAISONNEMENT_AMERTUME_002`
- `ASSAISONNEMENT_EQUILIBRE_003`
- `ASSAISONNEMENT_DEGUSTATION_001`

### Règles trop contextuelles

- `ASSAISONNEMENT_POIVRE_002`
- `ASSAISONNEMENT_ALCOOL_001`
- `ASSAISONNEMENT_ALCOOL_002`

### Règles potentiellement redondantes

Proximités acceptables mais à surveiller :

- `ALCOOL_001` / `ALCOOL_002`
- `EQUILIBRE_001` / `DEGUSTATION_001`
- `PROGRESSIF_002` / `EQUILIBRE_002`

La redondance n'est pas encore problématique, mais une normalisation soignée devra mieux distinguer :

- diagnostic du défaut ;
- méthode de correction ;
- rappel de prudence.

### Règles trop “chef” ou peu domestiques

Le lot évite assez bien ce piège.

Le seul sous-ensemble un peu plus sophistiqué est :

- `alcool`
- `umami`
- `amertume`

Mais même là, le niveau reste globalement accessible.

## Règles les plus faibles

- `ASSAISONNEMENT_AMERTUME_002`
- `ASSAISONNEMENT_EPICES_001`
- `ASSAISONNEMENT_EQUILIBRE_003`
- `ASSAISONNEMENT_DEGUSTATION_001`
- `ASSAISONNEMENT_POIVRE_002`

## Risques majeurs

- trop de règles de “méthode générale” proches les unes des autres
- quelques formulations encore plus conceptuelles qu'opérationnelles
- risque de glisser de l'assaisonnement vers la correction tardive de type `rattrapage`
- sous-ensemble `alcool` utile mais non prioritaire pour un premier noyau stable

## Recommandations avant normalisation

- conserver le noyau fort du lot : `sel`, `acidite`, `gras`, `equilibre`, `progressif`, `degustation`
- resserrer les règles encore trop conceptuelles avec des verbes d'action plus nets
- décider si le sous-ensemble `alcool` doit vraiment rester dans le premier lot ou être traité plus tard
- mieux distinguer dans la normalisation :
  - diagnostic
  - procédure
  - erreur à éviter
- surveiller les redondances entre :
  - `equilibre_global`
  - `assaisonnement_progressif`
  - `degustation_ajustement`

## Conclusion

Le lot `assaisonnement_v1_raw.jsonl` est suffisamment solide pour entrer en normalisation, mais pas encore assez net pour être promu rapidement sans passe éditoriale.

Décision globale :

`prêt pour normalisation`, avec vigilance ciblée sur les règles les plus abstraites et sur le sous-ensemble `alcool`.
