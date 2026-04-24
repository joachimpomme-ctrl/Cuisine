# Protocole Source vers Règle

## Objectif

Définir une méthode stricte pour transformer une source culinaire en règle JSONL fiable. Ce protocole sert à éviter trois dérives :

- recopier la source sans structuration ;
- produire une règle trop vague ;
- inventer une précision non soutenue par la documentation.

## Principe général

Une source n'est jamais transformée directement en lot massif. On extrait d'abord une information brute, on la découpe, on la simplifie, puis on ne conserve que ce qui peut devenir une règle atomique, actionnable et prudente.

## Étapes obligatoires

### 1. Extraire l'information brute

Recueillir dans des notes intermédiaires :

- le passage ou l'idée principale ;
- le contexte ;
- le type de source ;
- le niveau de fiabilité estimé ;
- les éléments explicitement formulés ;
- les zones d'incertitude.

À cette étape, il ne faut pas encore écrire directement une règle finale.

### 2. Identifier les composantes de la future règle

À partir de la note brute, isoler :

- le `principe` ;
- les `conditions` ;
- l'`application` ;
- les `erreurs fréquentes` ;
- les `exceptions`.

Si plusieurs principes indépendants apparaissent, il faut créer plusieurs règles potentielles et non une seule règle trop large.

### 3. Vérifier la cohérence

Contrôler :

- que la formulation n'entre pas en contradiction avec d'autres sources solides ;
- que le principe est stable et non anecdotique ;
- que les conditions sont compatibles avec l'application proposée ;
- que les exceptions ne détruisent pas le coeur de la règle.

Si la cohérence est douteuse, la règle est bloquée ou descend en fiabilité.

### 4. Simplifier

Réduire l'information à ce qui reste utile pour agir :

- supprimer les anecdotes ;
- retirer les variantes décoratives ;
- éliminer les formulations trop littéraires ;
- conserver seulement le noyau transmissible.

La simplification ne doit jamais supprimer une limite de sécurité ou une exception importante.

### 5. Transformer en règle atomique

Vérifier que la sortie candidate :

- exprime une seule idée principale ;
- peut être appliquée en cuisine familiale ;
- ne ressemble pas à une recette ;
- ne suppose pas un matériel professionnel rare ;
- contient une valeur opérationnelle claire.

Si la phrase contient plusieurs idées, la découper.

### 6. Mapper sur le schéma JSON

Renseigner explicitement :

- `id`
- `domaine`
- `categorie`
- `sous_categorie`
- `type_regle`
- `titre`
- `regle`
- `conditions`
- `application`
- `erreurs_frequentes`
- `exceptions`
- `niveau`
- `fiabilite`
- `usage_agent`

Le mapping doit rester fidèle à la source. Un champ inconnu ne doit pas être inventé de manière arbitraire.

### 7. Valider la qualité finale

Contrôler avant sauvegarde :

- validité JSON ;
- conformité au schéma ;
- absence de doublon évident ;
- clarté de la formulation ;
- actionnabilité ;
- prudence ;
- exploitabilité par agent IA.

## Questions de contrôle

- la règle porte-t-elle une seule idée principale ;
- permet-elle une décision ou une action ;
- les conditions d'application sont-elles explicites ;
- les erreurs fréquentes sont-elles utiles ;
- les exceptions empêchent-elles une généralisation abusive ;
- le niveau de fiabilité est-il honnête ;
- la règle est-elle plus proche d'un principe que d'une mini-recette.

## Cas de refus

Il faut refuser de produire une règle finale si :

- la source est trop faible ;
- plusieurs sources se contredisent sans arbitrage clair ;
- le contenu est trop contextuel ;
- la sécurité alimentaire exigerait une précision non disponible ;
- la formulation ne peut pas devenir atomique sans perdre le sens.

## Exemple 1 — Technique de cuisson

### Avant : texte brut

```text
Pour bien saisir une viande, il faut une poêle déjà bien chaude. Si la viande rend trop d'eau ou si la poêle est trop remplie, elle ne colore pas correctement et elle a tendance à bouillir dans son jus.
```

### Analyse intermédiaire

- principe : la saisie exige une chaleur de surface élevée ;
- conditions : poêle préchauffée, pièce peu humide, quantité modérée ;
- application : chauffer avant, sécher si besoin, éviter la surcharge ;
- erreurs fréquentes : poêle tiède, trop de morceaux à la fois ;
- exceptions : cas où la coloration n'est pas recherchée.

### Après : règle JSONL

```json
{"id":"CUISSON_SAISIR_900","domaine":"cuisson","categorie":"technique_fondamentale","sous_categorie":"saisir","type_regle":"principe","titre":"La saisie demande une surface très chaude et peu chargée","regle":"Une bonne saisie exige une surface de cuisson déjà très chaude et une quantité d'aliments limitée pour éviter que l'humidité accumulée n'empêche la coloration.","conditions":["poêle préchauffée","aliment peu humide","petite quantité par fournée"],"application":["faire chauffer le récipient avant d'ajouter l'aliment","sécher la surface si nécessaire","cuire en plusieurs fournées si besoin"],"erreurs_frequentes":["commencer sur une poêle tiède","surcharger la poêle"],"exceptions":["cuissons où l'on ne recherche pas de coloration"],"niveau":"fondamental","fiabilite":"haute","usage_agent":["conseil_cuisson","diagnostic_erreur","adaptation_recette"]}
```

## Exemple 2 — Cuisson humide

### Avant : texte brut

```text
Un mijotage efficace ne doit pas faire bouillir fortement le plat. Si ça bout trop, les morceaux se bousculent, la texture se dégrade et la sauce réduit plus vite que prévu.
```

### Analyse intermédiaire

- principe : le mijotage repose sur un frémissement doux ;
- conditions : cuisson longue, milieu humide, faible agitation ;
- application : régler le feu pour maintenir un léger mouvement ;
- erreurs fréquentes : ébullition trop forte, réduction excessive ;
- exceptions : réductions volontaires en fin de cuisson.

### Après : règle JSONL

```json
{"id":"CUISSON_MIJOTER_900","domaine":"cuisson","categorie":"technique_fondamentale","sous_categorie":"mijoter","type_regle":"procedure","titre":"Mijoter demande un frémissement doux, pas une forte ébullition","regle":"Mijoter consiste à maintenir une cuisson douce avec un léger frémissement afin d'attendrir et d'homogénéiser sans agitation brutale.","conditions":["milieu humide","cuisson longue","feu modéré"],"application":["régler le feu pour garder un léger frémissement","surveiller la réduction du liquide","ajuster le couvercle selon la concentration souhaitée"],"erreurs_frequentes":["laisser bouillir fortement","réduire trop vite le liquide"],"exceptions":["phase finale volontairement plus vive pour concentrer une sauce"],"niveau":"fondamental","fiabilite":"haute","usage_agent":["conseil_cuisson","adaptation_recette","diagnostic_erreur"]}
```

## Sortie attendue

La sortie normale du protocole est soit :

- une règle JSONL conforme et justifiable ;
- une note de blocage expliquant pourquoi la source n'est pas assez solide.
