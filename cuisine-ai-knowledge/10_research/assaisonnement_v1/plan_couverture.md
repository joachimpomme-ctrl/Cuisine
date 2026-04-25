# Plan de couverture `assaisonnement_v1`

## Objectif

Produire un premier lot de règles d'assaisonnement centré sur les principes actionnables, la dégustation progressive et le diagnostic des déséquilibres. Ce lot doit rester distinct du domaine `rattrapage` :

- `assaisonner` : construire ou ajuster le goût pendant la préparation ;
- `corriger` : traiter un défaut déjà installé ;
- `masquer` : détourner une perception dominante sans régler la cause ;
- `équilibrer` : améliorer la cohérence globale des saveurs.

## Axes couverts

### 1. Sel

- rôle structurant dans la lisibilité du goût
- effet d'amplification des saveurs déjà présentes
- risque de confusion entre plat fade et plat sous-salé

### 2. Poivre

- rôle aromatique et piquant
- intérêt souvent plus tardif que le sel
- risque de l'utiliser à la place d'un vrai assaisonnement

### 3. Acidité

- rôle de tension, fraîcheur, relief
- utilité pour réveiller un plat plat ou lourd
- risque de surcorrection qui durcit le profil

### 4. Sucre

- rôle d'arrondi ponctuel
- utilité limitée pour équilibrer acidité ou amertume
- risque de déporter un plat salé vers une lecture sucrée

### 5. Gras

- rôle de liant gustatif et de rondeur
- lien avec la perception des arômes et de la satiété
- risque de confondre manque de gras et manque de sel

### 6. Umami

- rôle de profondeur et de persistance
- utilité dans les plats jugés fades malgré une bonne salinité
- risque de surcharge si plusieurs sources se cumulent

### 7. Amertume

- rôle utile en petite dose mais vite dominante
- nécessité de distinguer amertume structurante et amertume parasite
- lien fort avec acidité, gras et sucre dans l'équilibrage

### 8. Herbes fraîches

- rôle de fraîcheur et de relief aromatique
- intérêt fréquent en finition
- risque de perte aromatique si ajout trop précoce

### 9. Herbes sèches

- rôle de fond aromatique plus diffus
- intérêt souvent plus en amont que les herbes fraîches
- risque de saveur poussiéreuse ou dominante

### 10. Épices

- rôle aromatique, chaleureux, piquant ou terreux selon le profil
- importance du moment d'ajout
- risque de masquer le plat au lieu de le soutenir

### 11. Aromates

- rôle de base de goût
- importance de leur cohérence avec le profil du plat
- risque de les accumuler sans diagnostic

### 12. Bouillon

- rôle de support double : salinité et profondeur
- utilité pour renforcer un fond gustatif
- risque de surcharger en sel sans s'en rendre compte

### 13. Alcool en cuisine

- rôle aromatique et de relief
- usage lié au profil recherché, pas à une logique de correction automatique
- risque de s'en servir pour masquer un plat mal construit

### 14. Équilibre global des saveurs

- lecture d'ensemble du plat
- hiérarchie des déséquilibres dominants
- articulation entre sel, acidité, gras, aromatique et umami

### 15. Assaisonnement progressif

- corrections par étapes
- une variable à la fois
- re-dégustation systématique

### 16. Dégustation et ajustement

- diagnostic avant action
- distinction entre défaut principal et défaut secondaire
- adaptation selon contexte de service

## Découpage prévu du lot RAW

- `sel` : 4 règles
- `poivre` : 2 règles
- `acidite` : 3 règles
- `sucre` : 2 règles
- `gras` : 2 règles
- `umami` : 2 règles
- `amertume` : 2 règles
- `herbes_fraiches` : 2 règles
- `herbes_seches` : 2 règles
- `epices` : 2 règles
- `aromates` : 2 règles
- `bouillon` : 2 règles
- `alcool` : 2 règles
- `equilibre_global` : 3 règles
- `assaisonnement_progressif` : 2 règles
- `degustation_ajustement` : 2 règles

Total visé : `34` règles.

## Frontière avec `rattrapage`

Le lot `assaisonnement_v1` doit prioriser :

- les gestes de construction du goût ;
- le diagnostic précoce ;
- les ajustements progressifs encore réversibles.

Le lot ne doit pas glisser vers :

- `plat trop salé`
- `plat trop acide`
- `plat trop sucré`
- `plat trop épicé`

Ces cas relèvent d'abord du domaine `rattrapage`.
