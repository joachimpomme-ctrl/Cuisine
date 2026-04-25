# Plan de Couverture — Rattrapage V1

## Objectif

Construire un premier lot brut de règles sur le rattrapage des erreurs fréquentes en cuisine familiale.

## Périmètre couvert

- `trop_sale`
- `trop_acide`
- `trop_sucre`
- `trop_epice`
- `sauce_trop_liquide`
- `sauce_qui_tranche`
- `viande_seche`
- `legumes_trop_cuits`
- `pates_collees`
- `riz_rate`

## Cible de production

- 30 à 40 règles maximum ;
- lot brut unique ;
- règles atomiques uniquement ;
- aucune recette complète ;
- aucune écriture dans `final`.

## Répartition prévue

- `trop_sale` : 3
- `trop_acide` : 3
- `trop_sucre` : 3
- `trop_epice` : 3
- `sauce_trop_liquide` : 3
- `sauce_qui_tranche` : 3
- `viande_seche` : 3
- `legumes_trop_cuits` : 3
- `pates_collees` : 3
- `riz_rate` : 3

Total prévu : 30 règles.

## Axes de qualité

- une règle = une action de rattrapage ou un diagnostic clair ;
- pas de promesse irréaliste de réparation parfaite ;
- expliciter les limites de rattrapage ;
- garder un angle cuisine familiale ;
- distinguer correction immédiate, limitation des dégâts et prévention de répétition.

## Risques éditoriaux

- confondre rattrapage et transformation complète de recette ;
- formuler des astuces contextuelles comme des lois générales ;
- sous-documenter les limites de rattrapage ;
- dériver vers des conseils médicaux ou de sécurité non sourcés.

## Priorités pour la review

- robustesse réelle des actions proposées ;
- absence de faux miracles ;
- bonne séparation entre problèmes proches ;
- utilité concrète pour un agent domestique.
