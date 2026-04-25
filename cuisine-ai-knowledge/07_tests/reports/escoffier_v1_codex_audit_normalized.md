# Audit Codex `escoffier_v1` normalisé

## Synthèse

- nombre total de règles auditées : `163`
- `keep` : `122`
- `revise` : `28`
- `move_later` : `13`
- `reject` : `0`

## Lecture rapide

- le lot apporte une vraie couche de logique classique utile à l'agent IA ;
- `principes` est globalement solide mais plusieurs entrées `adaptation` restent trop génériques ;
- `systemes` est le sous-lot le plus fragile : utile, mais encore trop répétitif autour de `fonction / point critique / intérêt domestique` ;
- `associations` est bon sur les familles modernes, moins bon sur les diagnostics formulés presque toujours de la même façon ;
- `patterns` est exploitable, mais certains diagnostics sont trop génériques et deux entrées restent trop proches d'une logique de cours ;
- `vocabulaire` est très bon ; seuls quelques termes trop spécialisés peuvent être différés.

## Risques identifiés

- répétition de formulations génériques dans `systemes` et `associations`
- plusieurs entrées `adaptation` répondent plus à une règle de prudence éditoriale qu'à une vraie décision cuisine
- certains éléments restent trop proches d'une culture classique de restaurant plutôt que d'un usage domestique direct
- chevauchement conceptuel possible avec `cuisson` sur `réduction`, `liaison`, `finitions`, `fonds`
- chevauchement léger avec `techniques_cap` sur `vocabulaire` et quelques gestes, mais sans contradiction majeure

## Règles prioritaires à corriger

- `ESCOFFIER_SYSTEME_003` : utile mais trop abstrait ; il faut préciser le choix que l'agent doit aider à faire
- `ESCOFFIER_SYSTEME_006` : même problème sur le fonds blanc ; formulation trop méta
- `ESCOFFIER_SYSTEME_024` : demi-glace encore présentée comme prudence générale, pas comme décision concrète
- `ESCOFFIER_SYSTEME_033` : adaptation béchamel trop générique
- `ESCOFFIER_SYSTEME_050` : diagnostic beurre blanc utile mais encore trop court pour être vraiment opératoire
- `ESCOFFIER_ASSOCIATION_023` : `légumes racines` reste trop vague
- `ESCOFFIER_PATTERN_004` : diagnostic trop générique pour `viande braisée`
- `ESCOFFIER_PRINCIPE_009` : bon fond métier, mais encore formulé comme consigne de traduction

## Règles à différer en priorité

- `ESCOFFIER_SYSTEME_010`
- `ESCOFFIER_SYSTEME_012`
- `ESCOFFIER_SYSTEME_025`
- `ESCOFFIER_SYSTEME_027`
- `ESCOFFIER_SYSTEME_040`
- `ESCOFFIER_ASSOCIATION_031`
- `ESCOFFIER_ASSOCIATION_033`
- `ESCOFFIER_PATTERN_015`
- `ESCOFFIER_PATTERN_023`
- `ESCOFFIER_VOCABULAIRE_015`
- `ESCOFFIER_VOCABULAIRE_016`
- `ESCOFFIER_VOCABULAIRE_037`
- `ESCOFFIER_VOCABULAIRE_038`

## Décision par fichier

### `principes`

- `ESCOFFIER_PRINCIPE_001` — `keep` — principe central, directement exploitable
- `ESCOFFIER_PRINCIPE_002` — `revise` — bonne idée, mais formulation trop indirecte
- `ESCOFFIER_PRINCIPE_003` — `revise` — parle surtout de méthode de traduction, pas assez d'action
- `ESCOFFIER_PRINCIPE_004` — `keep` — utile pour hiérarchiser base et finition
- `ESCOFFIER_PRINCIPE_007` — `keep` — règle simple et structurante
- `ESCOFFIER_PRINCIPE_008` — `revise` — doublonne partiellement `007` avec une formulation plus faible
- `ESCOFFIER_PRINCIPE_009` — `revise` — intéressant pour l'agent, mais trop méta
- `ESCOFFIER_PRINCIPE_010` — `keep` — cohérent avec `cuisson` sans le contredire
- `ESCOFFIER_PRINCIPE_011` — `revise` — principe utile mais expression trop générique
- `ESCOFFIER_PRINCIPE_012` — `revise` — adaptation encore trop abstraite
- `ESCOFFIER_PRINCIPE_013` — `keep` — apporte une nuance utile sur la netteté
- `ESCOFFIER_PRINCIPE_015` — `revise` — bon ancrage domestique, mais trop elliptique
- `ESCOFFIER_PRINCIPE_016` — `keep` — très bon principe de liaison
- `ESCOFFIER_PRINCIPE_017` — `keep` — utile et directement actionnable
- `ESCOFFIER_PRINCIPE_018` — `keep` — clair, simple, opérationnel
- `ESCOFFIER_PRINCIPE_019` — `keep` — bonne règle de décision
- `ESCOFFIER_PRINCIPE_021` — `keep` — limite domestique utile
- `ESCOFFIER_PRINCIPE_022` — `keep` — bonne frontière entre base et aromatique
- `ESCOFFIER_PRINCIPE_024` — `keep` — traduit correctement l'usage domestique
- `ESCOFFIER_PRINCIPE_025` — `keep` — principe fort pour l'agent
- `ESCOFFIER_PRINCIPE_026` — `keep` — avertissement utile et lisible
- `ESCOFFIER_PRINCIPE_027` — `keep` — exploitable dans un conseil court
- `ESCOFFIER_PRINCIPE_028` — `keep` — utile pour éviter la sur-correction
- `ESCOFFIER_PRINCIPE_030` — `keep` — adaptation pertinente
- `ESCOFFIER_PRINCIPE_031` — `keep` — bon principe de différenciation
- `ESCOFFIER_PRINCIPE_032` — `keep` — anti-doublon logique avec `031`
- `ESCOFFIER_PRINCIPE_034` — `keep` — garde-fou systémique utile
- `ESCOFFIER_PRINCIPE_036` — `revise` — juste sur le fond, encore trop éditorial sur la forme

### `systemes`

- `ESCOFFIER_SYSTEME_001` — `keep` — utile pour comprendre la fonction d'un fonds brun
- `ESCOFFIER_SYSTEME_002` — `keep` — diagnostic concret et cohérent
- `ESCOFFIER_SYSTEME_003` — `revise` — adaptation trop générale, choix agent insuffisamment explicités
- `ESCOFFIER_SYSTEME_004` — `keep` — fonction claire, transférable en domestique
- `ESCOFFIER_SYSTEME_006` — `revise` — même faiblesse que `003`
- `ESCOFFIER_SYSTEME_007` — `keep` — très utile pour distinguer fumet et fond
- `ESCOFFIER_SYSTEME_008` — `revise` — utile mais encore trop court pour guider une décision
- `ESCOFFIER_SYSTEME_009` — `keep` — bonne adaptation domestique
- `ESCOFFIER_SYSTEME_010` — `move_later` — trop spécialisé pour une première base candidate
- `ESCOFFIER_SYSTEME_012` — `move_later` — même raison, intérêt domestique trop faible
- `ESCOFFIER_SYSTEME_013` — `keep` — utile pour comprendre le rôle d'une glace
- `ESCOFFIER_SYSTEME_015` — `keep` — encore exploitable comme garde-fou d'usage
- `ESCOFFIER_SYSTEME_016` — `keep` — roux bien positionné comme système
- `ESCOFFIER_SYSTEME_017` — `revise` — bon diagnostic, à rendre plus opératoire
- `ESCOFFIER_SYSTEME_018` — `keep` — bon filtre d'usage domestique
- `ESCOFFIER_SYSTEME_019` — `keep` — distinction `jus lié` utile
- `ESCOFFIER_SYSTEME_021` — `keep` — adaptation suffisamment utile
- `ESCOFFIER_SYSTEME_022` — `keep` — demi-glace encore utile comme logique de base préparée
- `ESCOFFIER_SYSTEME_024` — `revise` — trop générique, peu distincte des autres adaptations
- `ESCOFFIER_SYSTEME_025` — `move_later` — sauce mère trop restaurant pour un premier noyau
- `ESCOFFIER_SYSTEME_027` — `move_later` — adaptation d'un système déjà trop spécialisé
- `ESCOFFIER_SYSTEME_028` — `keep` — velouté très utile pour l'agent
- `ESCOFFIER_SYSTEME_029` — `revise` — diagnostic utile mais encore un peu faible
- `ESCOFFIER_SYSTEME_030` — `keep` — adaptation correcte
- `ESCOFFIER_SYSTEME_031` — `keep` — béchamel utile et domestique
- `ESCOFFIER_SYSTEME_033` — `revise` — adaptation trop générique
- `ESCOFFIER_SYSTEME_034` — `keep` — sauce tomate structurée utile
- `ESCOFFIER_SYSTEME_036` — `keep` — adaptation lisible
- `ESCOFFIER_SYSTEME_037` — `keep` — hollandaise utile et fréquente
- `ESCOFFIER_SYSTEME_038` — `keep` — diagnostic précis et domestique
- `ESCOFFIER_SYSTEME_039` — `keep` — adaptation suffisante
- `ESCOFFIER_SYSTEME_040` — `move_later` — béarnaise moins centrale pour un premier candidate
- `ESCOFFIER_SYSTEME_042` — `keep` — garde-fou d'usage acceptable même si le système est secondaire
- `ESCOFFIER_SYSTEME_043` — `keep` — mayonnaise incontournable
- `ESCOFFIER_SYSTEME_045` — `keep` — adaptation claire
- `ESCOFFIER_SYSTEME_046` — `keep` — vinaigrette utile et simple
- `ESCOFFIER_SYSTEME_048` — `keep` — adaptation exploitable
- `ESCOFFIER_SYSTEME_049` — `keep` — beurre blanc utile si bien cadré
- `ESCOFFIER_SYSTEME_050` — `revise` — diagnostic pertinent mais trop bref
- `ESCOFFIER_SYSTEME_051` — `revise` — adaptation trop passe-partout

### `associations`

- `ESCOFFIER_ASSOCIATION_001` — `keep` — famille de sauce claire et utile
- `ESCOFFIER_ASSOCIATION_002` — `revise` — diagnostic trop générique, réutilisé partout
- `ESCOFFIER_ASSOCIATION_003` — `keep` — bonne logique produit / sauce
- `ESCOFFIER_ASSOCIATION_004` — `revise` — même problème de diagnostic générique
- `ESCOFFIER_ASSOCIATION_005` — `keep` — utile et cohérent avec `cuisson`
- `ESCOFFIER_ASSOCIATION_006` — `revise` — diagnostic répétitif
- `ESCOFFIER_ASSOCIATION_007` — `keep` — bonne règle de priorité au jus
- `ESCOFFIER_ASSOCIATION_009` — `keep` — utile pour viande rouge grillée
- `ESCOFFIER_ASSOCIATION_010` — `revise` — diagnostic trop standardisé
- `ESCOFFIER_ASSOCIATION_011` — `keep` — famille cohérente et moderne
- `ESCOFFIER_ASSOCIATION_012` — `revise` — même faiblesse de formulation
- `ESCOFFIER_ASSOCIATION_013` — `keep` — association simple, actuelle
- `ESCOFFIER_ASSOCIATION_015` — `keep` — utile malgré une coloration classique plus marquée
- `ESCOFFIER_ASSOCIATION_016` — `keep` — diagnostic suffisamment lisible
- `ESCOFFIER_ASSOCIATION_017` — `keep` — bonne distinction selon température
- `ESCOFFIER_ASSOCIATION_018` — `revise` — diagnostic trop générique
- `ESCOFFIER_ASSOCIATION_019` — `keep` — utile pour service froid
- `ESCOFFIER_ASSOCIATION_021` — `keep` — cohérent et sobre
- `ESCOFFIER_ASSOCIATION_022` — `keep` — diagnostic acceptable
- `ESCOFFIER_ASSOCIATION_023` — `revise` — `liaison plus enveloppante` reste trop vague
- `ESCOFFIER_ASSOCIATION_025` — `keep` — bonne logique moderne
- `ESCOFFIER_ASSOCIATION_027` — `keep` — très bon rappel de priorité au jus
- `ESCOFFIER_ASSOCIATION_028` — `keep` — diagnostic encore utile
- `ESCOFFIER_ASSOCIATION_029` — `keep` — association claire et courte
- `ESCOFFIER_ASSOCIATION_031` — `move_later` — `veau blanc` trop spécifique pour le premier passage
- `ESCOFFIER_ASSOCIATION_033` — `move_later` — `abats` utile mais trop contextuel
- `ESCOFFIER_ASSOCIATION_035` — `keep` — intéressant et transférable
- `ESCOFFIER_ASSOCIATION_037` — `keep` — protège bien le croustillant
- `ESCOFFIER_ASSOCIATION_038` — `revise` — diagnostic encore trop générique

### `patterns`

- `ESCOFFIER_PATTERN_001` — `keep` — pattern très utile et simple
- `ESCOFFIER_PATTERN_002` — `keep` — diagnostic valable
- `ESCOFFIER_PATTERN_003` — `keep` — bonne structure de braisage
- `ESCOFFIER_PATTERN_004` — `revise` — diagnostic trop standardisé, peu spécifique au braisage
- `ESCOFFIER_PATTERN_005` — `keep` — utile pour poisson poché
- `ESCOFFIER_PATTERN_006` — `keep` — diagnostic encore lisible
- `ESCOFFIER_PATTERN_007` — `keep` — pattern clair
- `ESCOFFIER_PATTERN_008` — `keep` — cohérent, même s'il reste générique
- `ESCOFFIER_PATTERN_009` — `keep` — logique forte pour gibier
- `ESCOFFIER_PATTERN_010` — `revise` — diagnostic trop répétitif
- `ESCOFFIER_PATTERN_011` — `keep` — bon pattern végétal
- `ESCOFFIER_PATTERN_012` — `keep` — acceptable
- `ESCOFFIER_PATTERN_013` — `keep` — très utile pour guider le choix de sauce
- `ESCOFFIER_PATTERN_014` — `revise` — diagnostic trop générique
- `ESCOFFIER_PATTERN_015` — `move_later` — pattern froid encore trop proche d'une logique de service classique
- `ESCOFFIER_PATTERN_017` — `keep` — très utile pour rôti + jus
- `ESCOFFIER_PATTERN_018` — `keep` — diagnostic correct
- `ESCOFFIER_PATTERN_019` — `keep` — utile pour potages clairs
- `ESCOFFIER_PATTERN_021` — `keep` — utile pour potages liés
- `ESCOFFIER_PATTERN_023` — `move_later` — `entremets` sort du coeur d'usage domestique immédiat

### `vocabulaire`

- `ESCOFFIER_VOCABULAIRE_001` — `keep` — terme central
- `ESCOFFIER_VOCABULAIRE_002` — `keep` — très bonne traduction domestique
- `ESCOFFIER_VOCABULAIRE_003` — `keep` — utile et cohérent
- `ESCOFFIER_VOCABULAIRE_004` — `keep` — bien formulé
- `ESCOFFIER_VOCABULAIRE_005` — `keep` — définition nette
- `ESCOFFIER_VOCABULAIRE_006` — `keep` — traduction utile
- `ESCOFFIER_VOCABULAIRE_007` — `keep` — utile pour comprendre `glace`
- `ESCOFFIER_VOCABULAIRE_008` — `keep` — bonne traduction
- `ESCOFFIER_VOCABULAIRE_009` — `keep` — utile
- `ESCOFFIER_VOCABULAIRE_010` — `keep` — traduction directement exploitable
- `ESCOFFIER_VOCABULAIRE_011` — `keep` — mot moins fréquent mais encore utile
- `ESCOFFIER_VOCABULAIRE_012` — `keep` — traduction correcte
- `ESCOFFIER_VOCABULAIRE_013` — `keep` — mot essentiel
- `ESCOFFIER_VOCABULAIRE_014` — `keep` — bonne vulgarisation
- `ESCOFFIER_VOCABULAIRE_015` — `move_later` — terme trop spécialisé pour le noyau
- `ESCOFFIER_VOCABULAIRE_016` — `move_later` — même raison
- `ESCOFFIER_VOCABULAIRE_017` — `keep` — utile et fréquent
- `ESCOFFIER_VOCABULAIRE_018` — `keep` — traduction claire
- `ESCOFFIER_VOCABULAIRE_019` — `keep` — utile
- `ESCOFFIER_VOCABULAIRE_020` — `keep` — très utile pour agent domestique
- `ESCOFFIER_VOCABULAIRE_021` — `keep` — terme central
- `ESCOFFIER_VOCABULAIRE_022` — `keep` — traduction concrète
- `ESCOFFIER_VOCABULAIRE_023` — `keep` — utile pour filtres fins
- `ESCOFFIER_VOCABULAIRE_024` — `keep` — bon équivalent domestique
- `ESCOFFIER_VOCABULAIRE_025` — `keep` — cohérent avec `techniques_cap`
- `ESCOFFIER_VOCABULAIRE_026` — `keep` — bonne traduction
- `ESCOFFIER_VOCABULAIRE_027` — `keep` — déjà connu mais reste utile
- `ESCOFFIER_VOCABULAIRE_028` — `keep` — bonne vulgarisation
- `ESCOFFIER_VOCABULAIRE_029` — `keep` — terme utile
- `ESCOFFIER_VOCABULAIRE_030` — `keep` — traduction claire
- `ESCOFFIER_VOCABULAIRE_031` — `keep` — utile
- `ESCOFFIER_VOCABULAIRE_032` — `keep` — traduction cohérente
- `ESCOFFIER_VOCABULAIRE_033` — `keep` — mot moins courant mais encore explicatif
- `ESCOFFIER_VOCABULAIRE_034` — `keep` — traduction suffisante
- `ESCOFFIER_VOCABULAIRE_035` — `keep` — utile
- `ESCOFFIER_VOCABULAIRE_036` — `keep` — bonne traduction
- `ESCOFFIER_VOCABULAIRE_037` — `move_later` — terme trop classique et peu probable en usage courant
- `ESCOFFIER_VOCABULAIRE_038` — `move_later` — même raison
- `ESCOFFIER_VOCABULAIRE_039` — `keep` — rare, mais encore utile pour expliquer un nom classique
- `ESCOFFIER_VOCABULAIRE_040` — `keep` — traduction suffisante
- `ESCOFFIER_VOCABULAIRE_041` — `keep` — terme courant en cuisine
- `ESCOFFIER_VOCABULAIRE_042` — `keep` — bonne vulgarisation
- `ESCOFFIER_VOCABULAIRE_043` — `keep` — utile
- `ESCOFFIER_VOCABULAIRE_044` — `keep` — traduction claire
- `ESCOFFIER_VOCABULAIRE_045` — `keep` — utile
- `ESCOFFIER_VOCABULAIRE_046` — `keep` — bonne traduction

## Recommandations avant `final_candidate`

- faire une passe ciblée sur `systemes` pour transformer les `adaptation` encore génériques en règles plus décisionnelles
- resserrer les diagnostics répétitifs de `associations` et `patterns`
- sortir du premier `final_candidate` les systèmes et termes trop spécialisés plutôt que de les forcer dans le noyau
- conserver `vocabulaire` presque tel quel, car c'est le sous-lot le plus propre
- garder Escoffier comme couche de structure, pas comme surcouche qui remplace `cuisson`, `assaisonnement` ou `rattrapage`

## Décision

- décision : `pas encore prêt pour candidate en bloc`
- décision opérationnelle : `prêt pour un final_candidate progressif après une courte passe de révision ciblée`
