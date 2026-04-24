# Plan d'extraction `cap_techniques_v1`

## Objectif

Extraire du livret CAP uniquement des règles utiles à un agent IA domestique :

- diagnostic
- décision
- geste
- ordre logique
- limite technique

## Périmètre retenu

### 1. Hygiène et poste

- lavage des mains
- lavage / désinfection de légumes
- lavage / désinfection d'herbes
- organisation du poste de travail
- réserve au froid quand elle est directement utile

### 2. Tailles et préparations de base

- peler à vif
- émincer
- ciseler
- tailler en cubes
- tailler en mirepoix
- tailler en julienne
- monder
- paner à l'anglaise
- clarifier œuf
- clarifier beurre
- batter / aplatir

### 3. Produits de la mer et produits bruts

- gratter / ôter le byssus / laver
- ébarber
- habiller un poisson

### 4. Cuissons ou chaînes techniques seulement si l'apport est nouveau

- blanchir une viande ou une volaille
- sauter-déglacer
- jus de rôti
- liaisons

### 5. Vocabulaire métier

- suprême
- mirepoix
- julienne
- matignon
- sucs
- déglacer
- chinoiser

## Logique d'exclusion

À exclure même si présent dans le document :

- recettes CAP complètes ;
- sauces détaillées comme recettes ;
- fiches pâtisserie ;
- températures, poids et ratios qui n'apportent pas une règle stable ;
- indications de dressage ;
- matériel non décisif ;
- décor et présentation.

## Découpage prévu du lot RAW

- hygiène / poste : `6` règles
- tailles / gestes de base : `14` règles
- produits bruts / poisson / coquillages : `5` règles
- liaisons / chaînes techniques : `7` règles
- vocabulaire métier : `4` règles

Total visé : `36` règles maximum.

## Règle de filtrage principale

Si une idée est déjà correctement couverte par :

- `cuisson_fondamentale_v1`
- `rattrapage_v1`
- `assaisonnement_v1`

elle ne doit pas être recréée ici.
