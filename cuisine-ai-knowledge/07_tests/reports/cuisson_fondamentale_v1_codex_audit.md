# Audit Codex — `cuisson_fondamentale_v1_normalized`

## Périmètre

Audit éditorial et métier du fichier :

- `cuisine-ai-knowledge/04_rules/normalized/cuisson/cuisson_fondamentale_v1_normalized.jsonl`

Contrainte respectée :

- aucune modification de `04_rules/final/`

## Diagnostic global

Le lot est globalement solide sur la structure :

- règles majoritairement atomiques ;
- champs bien remplis ;
- usage agentique généralement cohérent ;
- bonne couverture des techniques fondamentales ;
- pas de dérive vers la recette complète.

Les principaux points de vigilance sont éditoriaux et métier :

- quelques règles restent trop contextuelles pour un passage direct en `final` ;
- certaines règles de sécurité sont encore trop larges pour être promues sans audit métier renforcé ;
- le sous-ensemble `four` est plus dense que le reste et mélange principe, adaptation et vigilance de sécurité ;
- les frontières entre `revenir` et `suer`, puis entre `pocher` et `bouillir`, sont meilleures qu'avant mais doivent encore être surveillées à la relecture.

## 1. Qualité éditoriale

### Points forts

- les titres sont en majorité précis et lisibles ;
- la plupart des règles portent une seule idée principale ;
- les formulations sont actionnables ;
- les erreurs fréquentes sont souvent utiles et non décoratives.

### Points faibles

- certaines formulations restent trop prudentes ou trop générales pour être pleinement opératoires ;
- quelques règles d'adaptation sont proches du conseil contextuel plus que d'un principe stable ;
- certaines exceptions restent faibles ou très larges, notamment sur les règles les plus prudentes.

## 2. Qualité agent IA

### Points forts

- `conditions` et `application` sont le plus souvent exploitables ;
- `usage_agent` est cohérent sur l'essentiel ;
- les règles de diagnostic sont utiles pour un agent conversationnel ;
- les règles de sécurité utilisent une prudence compatible avec un usage domestique.

### Points faibles

- certaines règles gagneraient à distinguer plus clairement principe stable et astuce facultative ;
- quelques `usage_agent` sont corrects mais un peu optimistes au regard de la robustesse métier ;
- les règles très contextuelles devraient parfois être différées plutôt que simplement conservées telles quelles.

## 3. Cohérence métier

### Frontière `saisir` / `rissoler`

- ensemble cohérent ;
- `saisir` reste centré sur la chaleur vive et la surface ;
- `rissoler` reste centré sur la coloration progressive en corps gras.

### Frontière `revenir` / `suer`

- cohérence globalement correcte ;
- `revenir` joue bien le rôle de lancement aromatique ;
- `suer` reste bien dans l'attendrissement doux ;
- la règle `CUISSON_SUER_003` est toutefois plus contextuelle et moins fondamentale.

### Frontière `mijoter` / `bouillir` / `pocher` / `braiser`

- `mijoter` et `bouillir` sont correctement séparés ;
- `braiser` reste distinct grâce à la coloration initiale et au liquide limité ;
- `pocher` est bien orienté vers les aliments fragiles, mais `CUISSON_POCHER_003` est trop spécifique pour le noyau dur.

### Cohérence de `four`, `basse_temperature`, `friture`, `rechauffer`, `garder_au_chaud`

- `friture` est convaincant ;
- `rechauffer` est utile et prudemment formulé ;
- `garder_au_chaud` est pertinent mais encore trop large pour une promotion directe ;
- `basse_temperature` reste fragile sur le plan métier sans socle documentaire plus fort ;
- `four` contient de bonnes règles, mais le sous-ensemble est plus hétérogène que les autres techniques.

## 4. Sécurité alimentaire

### Règles satisfaisantes dans leur prudence

- `CUISSON_FRITURE_002`
- `CUISSON_RECHAUFFER_002`
- `CUISSON_RECHAUFFER_003`
- `CUISSON_FOUR_005`

### Règles trop vagues ou à surveiller avant `final`

- `CUISSON_BASSE_TEMPERATURE_002`
- `CUISSON_GARDER_AU_CHAUD_001`
- `CUISSON_POCHER_003` dans une moindre mesure, car elle implique une adaptation délicate.

### Candidats à déplacer plus tard vers un cluster plus explicite `hygiene` ou `conservation`

- `CUISSON_RECHAUFFER_002`
- `CUISSON_RECHAUFFER_003`
- `CUISSON_GARDER_AU_CHAUD_001`
- `CUISSON_BASSE_TEMPERATURE_002`

Remarque :

- ces règles peuvent rester dans le domaine `cuisson` à ce stade, mais elles gagneraient à être rattachées à une future logique éditoriale plus nette entre technique culinaire et sécurité / conservation.

## 5. Décision par règle

| ID | Décision | Motif |
|---|---|---|
| `CUISSON_SAISIR_002` | `keep` | Principe clair, atomique et utile. |
| `CUISSON_SAISIR_003` | `keep` | Diagnostic concret et très exploitable. |
| `CUISSON_RISSOLER_001` | `keep` | Bonne frontière avec la saisie, formulation stable. |
| `CUISSON_RISSOLER_002` | `keep` | Règle simple, actionnable et utile en diagnostic. |
| `CUISSON_REVENIR_001` | `keep` | Bonne règle de principe, frontière acceptable avec `suer`. |
| `CUISSON_SUER_002` | `keep` | Règle fondamentale claire et exploitable. |
| `CUISSON_SUER_003` | `revise` | Astuce utile mais plus contextuelle que fondamentale ; nécessite cadrage éditorial plus strict. |
| `CUISSON_MIJOTER_001` | `keep` | Très bon noyau de technique. |
| `CUISSON_MIJOTER_002` | `keep` | Diagnostic net, cohérent avec la technique. |
| `CUISSON_BRAISER_001` | `keep` | Distinction métier correcte avec `mijoter`. |
| `CUISSON_BRAISER_002` | `keep` | Procédure claire et concrète. |
| `CUISSON_ROTIR_001` | `keep` | Règle de principe claire et stable. |
| `CUISSON_ROTIR_002` | `keep` | Bon diagnostic, directement actionnable. |
| `CUISSON_GRILLER_001` | `keep` | Règle de principe solide. |
| `CUISSON_GRILLER_002` | `revise` | Bonne idée, mais formulation encore un peu scénarisée et dépendante du contexte. |
| `CUISSON_POCHER_001` | `revise` | Bonne base, mais formulation à clarifier pour éviter l'ambiguïté sur le niveau d'agitation du liquide. |
| `CUISSON_POCHER_002` | `keep` | Diagnostic pertinent et compatible avec la frontière `pocher` / `bouillir`. |
| `CUISSON_BOUILLIR_001` | `keep` | Principe net, distinction métier correcte. |
| `CUISSON_BOUILLIR_002` | `keep` | Adaptation utile, encore suffisamment générale. |
| `CUISSON_VAPEUR_001` | `keep` | Règle de base claire et fondamentale. |
| `CUISSON_VAPEUR_002` | `keep` | Très exploitable pour un agent domestique. |
| `CUISSON_FOUR_001` | `keep` | Règle stable, très bonne candidate au `final`. |
| `CUISSON_BASSE_TEMPERATURE_001` | `revise` | Idée recevable mais formulation trop générale pour un domaine sensible. |
| `CUISSON_FRITURE_001` | `keep` | Bonne règle de principe, utile et claire. |
| `CUISSON_FRITURE_002` | `keep` | Bonne règle de sécurité, suffisamment prudente. |
| `CUISSON_RECHAUFFER_002` | `keep` | Bonne règle de sécurité domestique, formulée sans sur-précision fragile. |
| `CUISSON_RECHAUFFER_003` | `keep` | Très utile pour agents IA orientés restes et sécurité. |
| `CUISSON_GARDER_AU_CHAUD_001` | `move_later` | Intuition juste, mais trop vague pour un passage immédiat en `final`. |
| `CUISSON_DEGLACER_001` | `keep` | Règle propre, atomique et bien cadrée. |
| `CUISSON_REDUIRE_001` | `keep` | Bonne règle de principe, stable et utile. |
| `CUISSON_CONFIRE_001` | `revise` | Bonne base mais trop générale ; distinction avec autres cuissons lentes à renforcer. |
| `CUISSON_REVENIR_002` | `keep` | Diagnostic utile, bon complément de `REVENIR_001`. |
| `CUISSON_FOUR_002` | `keep` | Adaptation utile et suffisamment concrète. |
| `CUISSON_BASSE_TEMPERATURE_002` | `move_later` | Sujet sensible, prudence correcte mais socle documentaire insuffisant pour `final`. |
| `CUISSON_GRILLER_003` | `keep` | Règle utile, non redondante, bonne valeur pratique. |
| `CUISSON_POCHER_003` | `move_later` | Trop spécifique et trop dépendante du cas d'usage pour le noyau fondamental. |
| `CUISSON_FOUR_003` | `keep` | Diagnostic simple et utile. |
| `CUISSON_FOUR_004` | `revise` | Utile, mais formulation trop générale et moins atomique que le reste du lot. |
| `CUISSON_FOUR_005` | `keep` | Bonne vigilance de sécurité, bien formulée sans précision fragile. |

## 6. Synthèse finale

- `keep` : 30
- `revise` : 6
- `move_later` : 3
- `merge` : 0
- `split` : 0
- `reject` : 0

## Règles prioritaires à corriger

- `CUISSON_SUER_003`
- `CUISSON_GRILLER_002`
- `CUISSON_POCHER_001`
- `CUISSON_BASSE_TEMPERATURE_001`
- `CUISSON_CONFIRE_001`
- `CUISSON_FOUR_004`

## Règles à différer

- `CUISSON_GARDER_AU_CHAUD_001`
- `CUISSON_BASSE_TEMPERATURE_002`
- `CUISSON_POCHER_003`

## Recommandations avant passage en `final`

- ne pas promouvoir le lot entier tel quel ;
- faire une passe de révision ciblée sur les 6 règles marquées `revise` ;
- différer les 3 règles marquées `move_later` tant que le cadrage documentaire n'est pas renforcé ;
- conserver la prudence actuelle sur la sécurité alimentaire et ne pas ajouter de températures ou durées non sourcées ;
- envisager à moyen terme un sous-ensemble éditorial distinct pour les règles de fin de cuisson et de sécurité (`rechauffer`, `garder_au_chaud`, `basse_temperature`) ;
- après révision, une sous-sélection d'environ 30 règles semble candidate crédible à une entrée progressive dans `final`.
