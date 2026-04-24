# Audit Codex `rattrapage_v1_normalized`

## Périmètre

- Fichier audité : `cuisine-ai-knowledge/04_rules/normalized/rattrapage/rattrapage_v1_normalized.jsonl`
- Nombre de règles auditées : `30`
- Modification des JSONL : `aucune`

## Méthode

L'audit contrôle pour chaque règle :

- l'actionnabilité réelle ;
- l'absence de promesse irréaliste ;
- la distinction entre `rattrapage`, `atténuation` et `réorientation` ;
- l'utilité pour un agent IA ;
- la cohérence des exceptions ;
- la redondance conceptuelle ;
- le risque de formulation trop abstraite.

Décisions possibles :

- `keep`
- `revise`
- `move_later`
- `reject`

## Synthèse

- `keep` : `22`
- `revise` : `5`
- `move_later` : `3`
- `reject` : `0`

Lecture générale :

- le lot est globalement propre, prudent et cohérent avec le domaine `rattrapage` ;
- la faiblesse principale n'est pas la structure, mais la frontière entre correction immédiate et réorientation d'usage ;
- plusieurs règles sont utiles pour un agent, mais certaines restent trop abstraites ou trop dépendantes du contexte pour passer telles quelles vers un `final_candidate`.

## Décision par règle

| ID | Décision | Motif |
| --- | --- | --- |
| `RATTRAPAGE_TROP_SALE_001` | `keep` | Règle claire, actionnable, prudente, avec conditions et applications utiles. |
| `RATTRAPAGE_TROP_SALE_002` | `keep` | Bonne règle de diagnostic contre un faux bon réflexe. Très utile pour agent IA. |
| `RATTRAPAGE_TROP_SALE_003` | `keep` | C'est une atténuation au service, mais elle est explicitement présentée comme telle. |
| `RATTRAPAGE_TROP_ACIDE_001` | `keep` | Actionnable et bien bornée. Pas de promesse excessive. |
| `RATTRAPAGE_TROP_ACIDE_002` | `keep` | Prudente, progressive, avec exceptions pertinentes. |
| `RATTRAPAGE_TROP_ACIDE_003` | `keep` | Bonne règle de méthode. Utile pour éviter la surcorrection. |
| `RATTRAPAGE_TROP_SUCRE_001` | `revise` | Le mot `contraste` reste un peu abstrait. Le principe est bon, mais la formulation mérite un cadrage plus concret. |
| `RATTRAPAGE_TROP_SUCRE_002` | `keep` | Bonne articulation entre correction du goût et préservation de texture. |
| `RATTRAPAGE_TROP_SUCRE_003` | `move_later` | La règle glisse nettement vers la réorientation d'usage. Utile, mais pas idéale dans un premier noyau `rattrapage`. |
| `RATTRAPAGE_TROP_EPICE_001` | `keep` | Actionnable, prudent, pertinent pour usage familial. |
| `RATTRAPAGE_TROP_EPICE_002` | `keep` | Règle suffisamment utile et honnête malgré une part de variabilité contextuelle. |
| `RATTRAPAGE_TROP_EPICE_003` | `revise` | Le fond est bon, mais la formulation `geste spectaculaire` est trop éditoriale et pas assez technique. |
| `RATTRAPAGE_SAUCE_TROP_LIQUIDE_001` | `keep` | Rattrapage direct, net, très exploitable par agent. |
| `RATTRAPAGE_SAUCE_TROP_LIQUIDE_002` | `keep` | Bonne règle de diagnostic causal. Forte valeur pratique. |
| `RATTRAPAGE_SAUCE_TROP_LIQUIDE_003` | `revise` | Utile mais un peu floue. Le mécanisme d'absorption par volume solide demande une formulation plus précise. |
| `RATTRAPAGE_SAUCE_QUI_TRANCHE_001` | `keep` | Très bonne règle de premier geste. Prudente et non trompeuse. |
| `RATTRAPAGE_SAUCE_QUI_TRANCHE_002` | `revise` | Trop dépendante du type de sauce. Le principe est bon, mais l'action reste trop générique. |
| `RATTRAPAGE_SAUCE_QUI_TRANCHE_003` | `move_later` | Relève davantage de la réorientation ou du sauvetage d'usage que du rattrapage direct. |
| `RATTRAPAGE_VIANDE_SECHE_001` | `keep` | Honnête, utile, sans promesse irréaliste de retrouver une texture juteuse. |
| `RATTRAPAGE_VIANDE_SECHE_002` | `keep` | Bonne règle d'atténuation du défaut perçu, bien bornée par les conditions. |
| `RATTRAPAGE_VIANDE_SECHE_003` | `move_later` | Davantage une règle de revalorisation que de rattrapage. À isoler dans une phase ultérieure. |
| `RATTRAPAGE_LEGUMES_TROP_CUITS_001` | `keep` | Très bon cadrage de la promesse réaliste : on change l'objectif, on ne prétend pas restaurer la texture initiale. |
| `RATTRAPAGE_LEGUMES_TROP_CUITS_002` | `keep` | Cohérente avec le principe de réorientation de texture, tout en restant utile. |
| `RATTRAPAGE_LEGUMES_TROP_CUITS_003` | `keep` | Règle simple, atomique, directement exploitable. |
| `RATTRAPAGE_PATES_COLLEES_001` | `keep` | Bon principe de limitation de l'aggravation. Fortement actionnable. |
| `RATTRAPAGE_PATES_COLLEES_002` | `revise` | Le `relâchement doux` et `environnement compatible` restent trop vagues pour un passage direct en final. |
| `RATTRAPAGE_PATES_COLLEES_003` | `keep` | Réorientation explicite, mais encore assez proche du rattrapage pratique pour rester dans le lot. |
| `RATTRAPAGE_RIZ_RATE_001` | `keep` | Excellente règle de diagnostic initial. Très utile pour agent IA. |
| `RATTRAPAGE_RIZ_RATE_002` | `keep` | Actionnable et prudente. Bonne règle conditionnelle. |
| `RATTRAPAGE_RIZ_RATE_003` | `keep` | Réorientation d'usage, mais ici elle reste cohérente avec la logique du lot et bien signalée. |

## Points éditoriaux et métier

### 1. Actionnabilité réelle

Les règles les plus solides sont celles qui indiquent :

- un diagnostic clair avant action ;
- un geste prudent et progressif ;
- une limite explicite sur le résultat attendu.

Le lot est particulièrement bon sur :

- `trop salé`
- `trop acide`
- `trop épicé`
- `sauce trop liquide`
- `riz raté`

Les règles les moins robustes sur ce critère sont celles qui utilisent encore des formules comme :

- `contraste compatible`
- `reprise douce`
- `relâchement doux`
- `environnement compatible`

Ces formulations ne sont pas fausses, mais elles sont encore trop ouvertes pour une exploitation agentique fiable sans interprétation supplémentaire.

### 2. Promesse réaliste

Le lot est globalement prudent. Il évite bien la promesse de `réparer parfaitement` un échec culinaire. C'est un bon point.

Les meilleurs exemples :

- `RATTRAPAGE_VIANDE_SECHE_001`
- `RATTRAPAGE_LEGUMES_TROP_CUITS_001`
- `RATTRAPAGE_SAUCE_QUI_TRANCHE_001`

Les règles à surveiller sont celles où la correction possible dépend trop du contexte exact :

- `RATTRAPAGE_SAUCE_QUI_TRANCHE_002`
- `RATTRAPAGE_PATES_COLLEES_002`
- `RATTRAPAGE_SAUCE_TROP_LIQUIDE_003`

### 3. Distinction entre rattrapage, atténuation et réorientation

Le lot contient bien les trois logiques, mais elles ne sont pas toutes aussi bien séparées.

- `rattrapage direct` : très présent sur `trop salé`, `trop acide`, `sauce trop liquide`, `riz trop humide`
- `atténuation du défaut` : bien traitée sur `viande sèche`, `légumes trop cuits`, `plat trop salé au service`
- `réorientation d'usage` : présente sur `trop sucré_003`, `sauce qui tranche_003`, `viande sèche_003`, `pâtes collées_003`, `riz raté_003`

Pour un premier `final_candidate`, il vaut mieux garder surtout :

- le rattrapage direct ;
- l'atténuation explicite et honnête ;
- seulement les réorientations les plus nettes et les plus utiles.

### 4. Utilité agent IA

Le lot est globalement bon pour un agent conversationnel de cuisine familiale :

- bons diagnostics initiaux ;
- gestes progressifs ;
- exceptions présentes ;
- erreurs fréquentes utiles.

La qualité agent diminue dès qu'une règle demande à l'agent d'interpréter trop librement un terme flou. C'est la principale raison des décisions `revise`.

### 5. Cohérence des exceptions

Les exceptions sont dans l'ensemble non décoratives et utiles.

Points à surveiller :

- certaines exceptions sont encore génériques (`préparations très concentrées`, `plat compatible`, `usage alternatif possible`) ;
- ce n'est pas bloquant, mais cela réduit légèrement la netteté opérationnelle.

### 6. Redondance conceptuelle

Pas de redondance lourde ou de doublon conceptuel évident dans le lot.

En revanche, il existe une proximité forte entre certaines paires :

- `RATTRAPAGE_VIANDE_SECHE_001` et `RATTRAPAGE_VIANDE_SECHE_002`
- `RATTRAPAGE_LEGUMES_TROP_CUITS_001` et `RATTRAPAGE_LEGUMES_TROP_CUITS_002`
- `RATTRAPAGE_PATES_COLLEES_001` et `RATTRAPAGE_PATES_COLLEES_002`

Ces proximités restent acceptables car les angles de correction sont distincts.

## Règles prioritaires à corriger

- `RATTRAPAGE_TROP_SUCRE_001`
- `RATTRAPAGE_TROP_EPICE_003`
- `RATTRAPAGE_SAUCE_TROP_LIQUIDE_003`
- `RATTRAPAGE_SAUCE_QUI_TRANCHE_002`
- `RATTRAPAGE_PATES_COLLEES_002`

## Recommandations avant création d'un `final_candidate`

- construire le `final_candidate` à partir des `22` règles `keep` ;
- retravailler les `5` règles `revise` pour réduire les formulations trop ouvertes ;
- laisser hors du premier `final_candidate` les `3` règles `move_later` les plus clairement orientées vers la réorientation d'usage :
  - `RATTRAPAGE_TROP_SUCRE_003`
  - `RATTRAPAGE_SAUCE_QUI_TRANCHE_003`
  - `RATTRAPAGE_VIANDE_SECHE_003`
- conserver en revanche `RATTRAPAGE_PATES_COLLEES_003` et `RATTRAPAGE_RIZ_RATE_003` dans le périmètre candidat si l'orientation éditoriale accepte une part limitée de réorientation explicite
- faire un dernier passage de clarification lexicale avant promotion vers `final`, en ciblant les termes trop abstraits plutôt que le fond métier

## Conclusion

Le lot est suffisamment solide pour préparer un `final_candidate`, à condition de ne pas chercher à tout publier d'un bloc. La bonne stratégie est progressive :

- garder le noyau de règles directement actionnables ;
- réviser les règles encore trop vagues ;
- différer les cas qui relèvent davantage de la revalorisation ou de la réorientation que du rattrapage direct.
