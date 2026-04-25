# Audit Codex `assaisonnement_v1_normalized`

## Périmètre

- Fichier audité : `cuisine-ai-knowledge/04_rules/normalized/assaisonnement/assaisonnement_v1_normalized.jsonl`
- Nombre de règles auditées : `36`
- Modifications des JSONL : `aucune`

## Méthode

L'audit contrôle :

- l'actionnabilité réelle ;
- l'absence de formulation floue ;
- la distinction entre `sel`, `acidite`, `sucre`, `gras`, `aromatique`, `umami` ;
- la cohérence avec `rattrapage` ;
- l'absence de pseudo-théorie culinaire ;
- l'utilité pour un agent IA ;
- les règles trop contextuelles ;
- les proximités conceptuelles trop fortes.

Décisions possibles :

- `keep`
- `revise`
- `move_later`
- `reject`

## Synthèse

- `keep` : `29`
- `revise` : `5`
- `move_later` : `2`
- `reject` : `0`

Lecture générale :

- le lot normalisé est solide et largement exploitable ;
- la majorité des règles sont suffisamment concrètes pour entrer dans un `final_candidate` ;
- les fragilités restantes concernent surtout des règles plus contextuelles ou plus conceptuelles que le noyau du lot ;
- le sous-ensemble `alcool` reste le moins prioritaire pour un premier lot `final`.

## Décision par règle

| ID | Décision | Motif |
| --- | --- | --- |
| `ASSAISONNEMENT_SEL_001` | `keep` | Très bonne règle de principe, claire et utile. |
| `ASSAISONNEMENT_SEL_002` | `keep` | Excellente règle de diagnostic, structurante pour tout le domaine. |
| `ASSAISONNEMENT_SEL_003` | `keep` | Procédure simple, actionnable, sans ambiguïté. |
| `ASSAISONNEMENT_SEL_004` | `keep` | Frontière métier bien posée entre sel pur et ingrédient salé. |
| `ASSAISONNEMENT_POIVRE_001` | `keep` | Distinction propre entre poivre et structure salée. |
| `ASSAISONNEMENT_POIVRE_002` | `revise` | Déjà mieux formulée, mais reste contextuelle et dépend encore du style du plat. |
| `ASSAISONNEMENT_ACIDITE_001` | `keep` | Bonne règle de levier gustatif, claire et domestique. |
| `ASSAISONNEMENT_ACIDITE_002` | `keep` | Diagnostic fin, sans glissement théorique. |
| `ASSAISONNEMENT_ACIDITE_003` | `keep` | Très bonne règle de méthode. |
| `ASSAISONNEMENT_SUCRE_001` | `keep` | La normalisation a bien resserré le champ. Règle désormais assez nette. |
| `ASSAISONNEMENT_SUCRE_002` | `keep` | Bonne frontière entre arrondir et masquer. |
| `ASSAISONNEMENT_GRAS_001` | `keep` | Règle claire, concrète, utile pour la cuisine familiale. |
| `ASSAISONNEMENT_GRAS_002` | `keep` | Très bon diagnostic différentiel contre le réflexe de resalage. |
| `ASSAISONNEMENT_UMAMI_001` | `keep` | Bonne règle, sans pseudo-théorie. |
| `ASSAISONNEMENT_UMAMI_002` | `keep` | Procédure prudente et exploitable. |
| `ASSAISONNEMENT_AMERTUME_001` | `keep` | Bonne règle de diagnostic, utile et non décorative. |
| `ASSAISONNEMENT_AMERTUME_002` | `revise` | Mieux qu'avant, mais la notion de `rondeur` reste encore un peu interprétative. |
| `ASSAISONNEMENT_HERBES_FRAICHES_001` | `keep` | Principe concret et robuste. |
| `ASSAISONNEMENT_HERBES_FRAICHES_002` | `keep` | Bonne règle de frontière entre aromatique et équilibre de base. |
| `ASSAISONNEMENT_HERBES_SECHES_001` | `keep` | Claire et directement applicable. |
| `ASSAISONNEMENT_HERBES_SECHES_002` | `keep` | La reformulation est désormais assez concrète. |
| `ASSAISONNEMENT_EPICES_001` | `revise` | Plus nette qu'avant, mais reste un peu générale autour du `rôle de l'épice`. |
| `ASSAISONNEMENT_EPICES_002` | `keep` | Bonne règle contre une fausse correction aromatique. |
| `ASSAISONNEMENT_AROMATES_001` | `keep` | Très bonne règle de construction de fond. |
| `ASSAISONNEMENT_AROMATES_002` | `keep` | Diagnostic utile et bien formulé. |
| `ASSAISONNEMENT_BOUILLON_001` | `keep` | Forte valeur pratique, distinction claire des effets. |
| `ASSAISONNEMENT_BOUILLON_002` | `keep` | Bonne règle de non-automatisme. |
| `ASSAISONNEMENT_ALCOOL_001` | `move_later` | Règle cohérente mais trop contextuelle et moins centrale pour un premier noyau domestique. |
| `ASSAISONNEMENT_ALCOOL_002` | `move_later` | Même constat. Bonne règle, mais redondante avec `ALCOOL_001` et moins prioritaire. |
| `ASSAISONNEMENT_EQUILIBRE_001` | `keep` | Excellente règle pivot pour l'agent. |
| `ASSAISONNEMENT_EQUILIBRE_002` | `keep` | Procédure simple, utile, très forte pour un `final_candidate`. |
| `ASSAISONNEMENT_EQUILIBRE_003` | `revise` | Déjà clarifiée, mais reste assez conceptuelle autour de la notion de `détourner l'attention`. |
| `ASSAISONNEMENT_PROGRESSIF_001` | `keep` | Très bonne règle stratégique, claire et concrète. |
| `ASSAISONNEMENT_PROGRESSIF_002` | `keep` | Procédure forte, robuste, immédiatement utilisable. |
| `ASSAISONNEMENT_DEGUSTATION_001` | `revise` | Mieux formulée, mais reste plus métacognitive qu'opérationnelle. |
| `ASSAISONNEMENT_DEGUSTATION_002` | `keep` | Excellente règle de lecture différentielle. |

## Contrôles métier

### Distinction des axes de goût

Le lot est maintenant propre sur la séparation entre :

- `sel`
- `acidite`
- `sucre`
- `gras`
- `aromatique`
- `umami`

Les règles les plus solides sur ce point sont :

- `ASSAISONNEMENT_SEL_002`
- `ASSAISONNEMENT_ACIDITE_002`
- `ASSAISONNEMENT_GRAS_002`
- `ASSAISONNEMENT_DEGUSTATION_002`

La distinction `aromatique` / `structure du goût` est également bien tenue sur :

- `POIVRE_001`
- `HERBES_FRAICHES_002`
- `EPICES_002`
- `AROMATES_001`

### Cohérence avec `rattrapage`

Le lot reste du côté :

- construction du goût ;
- ajustement progressif ;
- prévention de la surcorrection ;
- diagnostic précoce.

Les zones proches de `rattrapage` mais encore acceptables sont :

- `SUCRE_001`
- `AMERTUME_002`
- `EQUILIBRE_003`

Elles restent admissibles car elles parlent encore de correction légère ou de hiérarchie des leviers, et non de réparation d'un échec déjà installé.

### Absence de pseudo-théorie

Le lot évite bien les slogans culinaires vides et les causalités floues.

Ce qui reste un peu théorique :

- `AMERTUME_002`
- `EQUILIBRE_003`
- `DEGUSTATION_001`

Mais le niveau reste acceptable pour une prochaine passe.

## Règles trop contextuelles

Les plus contextuelles sont :

- `ASSAISONNEMENT_POIVRE_002`
- `ASSAISONNEMENT_ALCOOL_001`
- `ASSAISONNEMENT_ALCOOL_002`

Le problème n'est pas qu'elles soient fausses, mais qu'elles dépendent davantage du style de plat, du moment d'ajout et de l'intention culinaire que le reste du lot.

## Règles trop proches conceptuellement

Proximités à surveiller :

- `ALCOOL_001` / `ALCOOL_002`
- `EQUILIBRE_001` / `DEGUSTATION_001`
- `EQUILIBRE_002` / `PROGRESSIF_002`

Ces proximités restent gérables, mais la sélection d'un `final_candidate` devra éviter un noyau trop abstrait ou trop répétitif.

## Règles prioritaires à corriger

- `ASSAISONNEMENT_POIVRE_002`
- `ASSAISONNEMENT_AMERTUME_002`
- `ASSAISONNEMENT_EPICES_001`
- `ASSAISONNEMENT_EQUILIBRE_003`
- `ASSAISONNEMENT_DEGUSTATION_001`

## Règles à différer

- `ASSAISONNEMENT_ALCOOL_001`
- `ASSAISONNEMENT_ALCOOL_002`

## Recommandations avant création du `final_candidate`

- construire le `final_candidate` à partir du noyau très robuste : `sel`, `acidite`, `gras`, `umami`, `herbes`, `aromates`, `bouillon`, `equilibre`, `progressif`, `degustation_002`
- retravailler les `5` règles `revise` pour les rendre encore plus immédiatement actionnables
- laisser hors du premier `final_candidate` les `2` règles `alcool`
- surveiller le niveau d'abstraction de certaines règles de méthode afin que le futur lot `final` reste pratique et pas trop doctrinal

## Conclusion

Le lot normalisé est globalement solide et presque prêt pour un `final_candidate`. La stratégie recommandée est sélective :

- garder le noyau opérationnel déjà très bon ;
- réviser les quelques règles encore un peu conceptuelles ;
- différer le sous-ensemble `alcool`.
