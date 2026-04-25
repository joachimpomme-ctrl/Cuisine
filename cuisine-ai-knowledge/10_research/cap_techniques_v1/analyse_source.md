# Analyse de source `0-livret_techniques.pdf`

## Identification

- Source : `0-livret_techniques.pdf`
- Nature : livret CAP cuisine
- Taille observée : `159` pages
- Type : support pédagogique technique avec sommaire détaillé, fiches gestes, protocoles d'hygiène, techniques de cuisson, fonds/sauces et fiches techniques de plats

## Intérêt pour la base `rules`

La source vaut le coup comme source technique secondaire parce qu'elle contient :

- des micro-techniques atomiques ;
- des définitions métier courtes ;
- des résultats escomptés explicites ;
- des ordres d'opérations utiles ;
- des erreurs et limites techniques implicites ;
- du vocabulaire de base exploitable par agent IA.

Elle est particulièrement utile pour enrichir les zones encore peu couvertes :

- gestes de préparation de base ;
- hygiène et mise en place ;
- tailles et vocabulaire métier ;
- liaisons, clarification, préparation de produits ;
- enchaînements techniques très courts.

## Limites de la source

- source scolaire, pas pensée pour une cuisine familiale ;
- présence de consignes locales de lycée ;
- nombreuses fiches recettes complètes ;
- matériel souvent détaillé à un niveau non utile pour notre base ;
- certains contenus sont très professionnels ou liés à l'exécution CAP ;
- plusieurs techniques de cuisson sont déjà mieux couvertes dans nos lots `cuisson`.

## Sections réellement exploitables

### Très exploitables

- protocoles d'hygiène et de poste :
  - lavage des mains
  - mise en place du plan de travail
  - stockage transitoire

- techniques de préparation de base :
  - laver
  - éplucher
  - préparer les herbes
  - peler à vif
  - émincer
  - tailler en brunoise, macédoine, mirepoix, julienne
  - ciseler
  - monder
  - paner
  - clarifier
  - préparer coquillages et poissons

- liaisons et vocabulaire :
  - lier à l'amidon
  - lier par réduction
  - lier par purée de légumes
  - émulsionner
  - chinoiser
  - sucs
  - déglacer

### Exploitables avec filtrage fort

- certaines cuissons :
  - blanchir
  - sauter-déglacer
  - vapeur
  - rôtir

Le filtrage doit être fort car ces zones recouvrent déjà largement `cuisson_fondamentale_v1`.

## Sections à exclure

- fiches techniques complètes de plats ;
- pâtisserie recette par recette ;
- quantités détaillées ;
- dressages ;
- listes de matériel exhaustives ;
- consignes locales propres au lycée ;
- temps et températures trop spécifiques quand ils ne servent qu'à une fiche scolaire.

## Position recommandée dans le système

Cette source ne doit pas devenir une base principale. Elle doit servir à :

- compléter les gestes de base ;
- enrichir le vocabulaire métier ;
- fournir des règles courtes et actionnables ;
- documenter des chaînes techniques simples ;
- renforcer certains points d'hygiène ou de logique opératoire.

Conclusion :

`source utile à intégrer de manière sélective`, pas comme document à absorber massivement.
