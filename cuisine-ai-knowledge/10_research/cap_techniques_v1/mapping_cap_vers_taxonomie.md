# Mapping CAP vers taxonomie

## Principe

Le livret CAP ne correspond pas directement à la taxonomie actuelle du projet. Ce mapping sert à repérer :

- ce qui peut entrer dans des lots futurs ;
- ce qui est déjà couvert ;
- ce qui doit rester hors base.

## Mapping par blocs

### Protocoles du lycée

- taxonomie cible probable :
  - `hygiene`
  - `organisation`
- statut :
  - partiellement exploitable
- remarques :
  - garder seulement les gestes universels, exclure les consignes locales

### Techniques de préparations de base

- taxonomie cible probable :
  - nouveau lot `techniques_cap`
  - éventuellement futur domaine `ingredient`
  - parfois `organisation`
- statut :
  - très exploitable
- remarques :
  - c'est le coeur de la valeur du document

### Cuissons

- taxonomie cible probable :
  - `cuisson`
- statut :
  - déjà largement couvert
- remarques :
  - n'extraire que ce qui apporte un geste ou un ordre logique absent des lots existants

### Fonds, sauces, jus, marinades, liaisons

- taxonomie cible probable :
  - `sauce`
  - `assaisonnement`
  - nouveau lot `techniques_cap`
- statut :
  - exploitable avec filtrage fort
- remarques :
  - garder surtout les principes de liaison, réduction, émulsion, dégraissage, chinois

### Pâtisserie

- taxonomie cible probable :
  - `patisserie`
- statut :
  - hors périmètre de ce lot
- remarques :
  - trop proche de recettes et d'appareils détaillés

### Autres techniques

- taxonomie cible probable :
  - variable selon la technique
- statut :
  - à trier au cas par cas

## Vocabulaire métier à réutiliser

- `suprême`
- `mirepoix`
- `matignon`
- `julienne`
- `chinoiser`
- `sucs`
- `déglacer`

## Écart de schéma actuel

Le lot demandé utilise `domaine: technique`, mais ce domaine n'existe pas encore dans :

- `01_schema/rule.schema.json`
- `08_scripts/validate_jsonl.py`

Conséquence :

- le lot peut être créé en `raw` pour recherche et arbitrage ;
- il n'est pas encore validable par le pipeline actuel sans évolution du schéma ou remapping vers un domaine existant.
