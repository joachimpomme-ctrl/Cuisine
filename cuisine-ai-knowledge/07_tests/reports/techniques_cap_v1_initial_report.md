# Rapport initial `techniques_cap_v1`

## Résumé

- Nombre de règles extraites : `38`
- Statut : `raw`
- Source principale : `0-livret_techniques.pdf`
- Décision : `prêt pour normalisation`, avec réserve de schéma

## Pages / sections couvertes

### Sections réellement exploitées

- protocoles d'hygiène et de poste :
  - pages `6`, `10`, `15`, `17`
- préparations de base :
  - pages `20`, `21`, `22`, `23`, `24`, `26`, `27`, `32`, `34`, `35`
- produits bruts / coquillages / poisson :
  - pages `42`, `43`
- opérations techniques et liaisons :
  - pages `60`, `62`, `80`, `99`
- définitions et chaînes techniques dérivées :
  - pages `59`, `61`, `80`, `99`

### Sections couvertes indirectement

- sommaire global pages `2` à `4` pour cartographier les techniques disponibles

## Règles exclues

Exclusions principales :

- fiches recettes complètes ;
- fiches techniques CAP de plats ;
- pâtisserie détaillée ;
- quantités de recettes ;
- matériels exhaustifs ;
- dressage et décoration ;
- températures et temps trop liés à une fiche précise ;
- cuissons déjà largement couvertes dans `cuisson_fondamentale_v1`.

## Risques de doublon

### Risque faible

- tailles, vocabulaire métier, clarification, panure, hygiène de poste

### Risque moyen

- `blanchir`
- `déglacer`
- `réduction comme liaison`
- quelques chaînes techniques autour du jus de rôti

Gestion choisie :

- ne pas recréer les règles générales de cuisson déjà publiées ;
- ne garder ici que les versions centrées sur :
  - ordre opératoire
  - vocabulaire métier
  - geste précis

## Apports nouveaux par rapport aux lots existants

Apports les plus nets :

- gestes de base :
  - peler à vif
  - émincer
  - brunoise
  - mirepoix
  - julienne
  - ciseler
  - monder
  - paner
  - clarifier

- produits bruts :
  - moules
  - poisson entier

- hygiène et poste :
  - lavage des mains
  - désinfection des végétaux
  - gestion du poste

- vocabulaire métier :
  - suprême
  - sucs
  - déglacer
  - chinoiser
  - matignon

## Réserve importante sur le schéma

Le lot demandé utilise :

- `domaine: technique`

Mais ce domaine n'est pas reconnu par :

- `01_schema/rule.schema.json`
- `08_scripts/validate_jsonl.py`

Conséquence :

- le lot est cohérent comme matière RAW de recherche ;
- il n'est pas encore validable dans le pipeline actuel sans évolution du schéma ou remapping vers un domaine existant.

## Recommandations avant normalisation

- décider d'abord si le projet accepte un nouveau domaine `technique`
- sinon remapper proprement les sous-ensembles vers :
  - `hygiene`
  - `organisation`
  - `ingredient`
  - `sauce`
  - `materiel` pour une très petite partie si utile
- vérifier à la normalisation les recouvrements avec `cuisson`
- garder le lot centré sur :
  - gestes
  - ordre logique
  - vocabulaire métier
  - limites techniques courtes

## Conclusion

Le PDF apporte une vraie valeur comme source technique secondaire, surtout pour les micro-techniques et le vocabulaire métier. Le lot extrait est exploitable, mais il faut arbitrer le problème de schéma avant de l'intégrer proprement au pipeline.
