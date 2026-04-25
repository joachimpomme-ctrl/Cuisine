# Ottolenghi SIMPLE — patterns culinaires V2

> Source : *SIMPLE* — Yotam Ottolenghi (2018, ed. fr. 2018)
> Statut : patterns extraits, **aucune recette copiée**
> Version : V2 consolidée (Claude V1 colonne vertébrale + angles morts Codex)
> Usage : base d'inspiration pour agent IA cuisine, pas livre de recettes

---

## Principes d'utilisation

Ce fichier ne contient pas de recettes. Il contient **24 architectures de plats** : la grammaire culinaire d'Ottolenghi distillée en formules réutilisables.

Il sert à :
- inspirer une idée de plat à partir d'ingrédients disponibles
- adapter une recette existante à ce qu'on a sous la main
- enrichir un plat simple avec une signature aromatique cohérente
- guider un agent IA qui veut "penser comme Ottolenghi" sans recopier

Il **ne remplace pas** :
- les règles techniques de cuisson (temps, températures, points de cuisson) — voir Nosrat ou autre source de règles atomiques
- les principes scientifiques de la cuisine — voir McGee ou équivalent
- les techniques génériques (comment trancher, comment émulsionner) — connaissance de base

Chaque pattern a quatre niveaux d'usage :
1. **formule réutilisable** : l'équation générique
2. **variantes** : ce qu'on peut substituer sans perdre l'esprit
3. **points critiques + erreurs** : ce qui sépare un plat réussi d'un plat raté
4. **usage Gemini** : quand activer ce pattern, quand l'éviter

Les patterns sont organisés en familles : plats légumes/grains (1-9), plats protéines (10-16), formats légers (17-18), patterns outils (19-22), desserts (23-24).

---

## Pattern 001 — Légume rôti + sauce yaourt aromatisée + croquant + herbes

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : aubergines rôties yaourt cari ; chou-fleur rôti et œufs cari ; courges rôties ; panais rôtis ; variations sur ce schéma
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Transformer un légume brut en pièce maîtresse : intensité par le four, fraîcheur par la sauce froide, contraste par le topping.

### Structure
- base : légume dense (aubergine, chou-fleur, courge, panais, carotte, betterave)
- transformation : rôti à four chaud, monocouche, jusqu'à coloration profonde
- sauce / liant : yaourt grec ou labneh aromatisé (zeste agrume + épice douce + ail pressé)
- contraste : oignon caramélisé OU élément acide (grenade, citron confit, zeste)
- finition : herbes fraîches en quantité (coriandre, persil, menthe, aneth)
- texture : noix ou graines grillées (amandes, pignons, pistaches, cumin, coriandre)

### Logique de goût
- salé : sel sur le légume avant rôtissage
- gras : huile d'olive + corps gras du yaourt
- acide : zeste agrume + jus dans la sauce ; grenade en option
- sucré : caramélisation naturelle du légume rôti
- amer : —
- umami : profondeur de la croûte rôtie ; renforcée si parmesan ou féta
- aromatique : épice douce dominante (cari, sumac, cumin, zaatar)

### Pattern réutilisable

```text
légume dense rôti + yaourt grec aromatisé (épice + zeste) + oignon caramélisé OU grenade + herbes fraîches + noix/graines grillées
```

### Variantes
- bases : aubergine, chou-fleur, courge butternut, patate douce, panais, carotte, betterave
- sauces : yaourt + sumac, yaourt + cari, yaourt + zaatar, yaourt + harissa, labneh nature
- toppings : amandes effilées, pignons, pistaches, graines de courge grillées, sésame, dukkah
- herbes / épices : coriandre, menthe, persil, aneth, origan ; cumin, cardamome, ras-el-hanout
- protéines compatibles : agneau grillé, poulet rôti, féta, pois chiches grillés, halloumi
- version simple : un seul légume + sauce yaourt-zeste-sel + huile + persil
- version festive : assortiment 2-3 légumes + 2 toppings (caramélisé + croquant) + grenade + herbes triples

### Points critiques
- bien sécher le légume avant huile + sel
- monocouche stricte sur la plaque
- four vraiment chaud (220°C+)
- ne pas saler le yaourt trop tôt
- ajouter les herbes au tout dernier moment

### Erreurs fréquentes
- plaque surchargée → vapeur, pas de coloration
- légume pas séché → ne dore pas
- sel direct sur yaourt qui attend → rend de l'eau
- herbes ajoutées trop tôt → ramollissent

### Repères sensoriels
- bords du légume franchement bruns
- tendreté à la pointe du couteau
- yaourt qui forme un creux où le légume se dépose
- contraste chaud/froid au service

### Usage Gemini
- proposer quand : "j'ai un légume dense + du yaourt", "comment rendre des légumes rôtis intéressants", "idée style Ottolenghi"
- éviter quand : légume très aqueux, repas express < 25 min, intolérance lactose sans alternative
- adaptation rapide : remplacer yaourt par tahini éclairci si végan ; tout cuit ensemble version monoplaque

---

## Pattern 002 — Tomates rôties chaudes sur base laitière froide

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : tomates cerises grillées sur yogourt froid ; et variations sur ce geste
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Choc thermique + acide vivant + base apaisante : la tomate bouillonnante rencontre le yaourt froid, qui fond partiellement à son contact.

### Structure
- base : yaourt grec très épais ou labneh, étalé froid en lit
- transformation : tomates cerises (ou autre fruit/légume juteux) rôties à four chaud avec ail, herbes, zeste
- sauce / liant : huile aromatique de la plaque (jus rendus + huile + ail confit)
- contraste : chaud/froid franc
- finition : herbes fraîches + flocons de piment doux (Urfa, Alep)
- texture : option — graines de cumin grillées, pain croustillant en accompagnement

### Logique de goût
- salé : sel sur tomates avant rôtissage + pincée dans le yaourt
- gras : huile d'olive + corps du yaourt
- acide : jus naturel des tomates rôties + zeste de citron
- sucré : pincée de cassonade si tomates pas assez mûres ; sinon caramélisation naturelle
- amer : —
- umami : tomate concentrée par le four + ail confit
- aromatique : thym, origan, piment doux fumé en finition

### Pattern réutilisable

```text
yaourt épais froid en lit + fruit/légume juteux rôti chaud + huile aromatique de plaque + herbes + piment doux
```

### Variantes
- bases : yaourt grec, labneh, ricotta battue, fromage frais, mascarpone détendu
- éléments rôtis chauds : tomates cerises, prunes, raisins, figues, poivrons, oignons, abricots
- aromates dans la plaque : ail tranché, thym, origan, lanières de zeste citron, graines de cumin
- herbes / épices : origan, thym, piment Urfa, piment d'Alep, sumac
- protéines compatibles : poulet rôti à part, pois chiches grillés, agneau
- version simple : tomates cerises + ail + huile + yaourt + sel + origan
- version festive : 3 fruits rôtis différents + labneh maison + double huile aromatique + pain plat chaud

### Points critiques
- yaourt vraiment froid au moment du service
- tomates posées **directement** depuis le four, brûlantes
- récupérer **toute** l'huile et le jus de la plaque, c'est la sauce
- creux dans le yaourt avec le dos d'une cuillère pour recevoir les tomates
- ne pas mélanger : laisser le contraste visuel et thermique

### Erreurs fréquentes
- mélanger tomates et yaourt → perd l'effet
- yaourt à température ambiante → pas de contraste
- plaque trop grande, jus évaporé → pas de sauce
- tomates pas assez rôties → pas de concentration

### Repères sensoriels
- yaourt qui commence à fondre au contact des tomates
- tomates qui ont éclaté et noirci par endroits
- huile colorée par les tomates et les épices

### Usage Gemini
- proposer quand : "j'ai des tomates cerises et du yaourt", "entrée d'été simple mais qui en jette", "végé impressionnant"
- éviter quand : pas de four, tomates hors saison fades, repas froid en intégralité
- adaptation rapide : sous le gril si pas le temps, 6-8 min, surveiller

---

## Pattern 003 — Légume rôti + sauce tahini éclaircie + herbes + grenade/zaatar

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : variations chou-fleur tahini, aubergine tahini, légumes au tahini
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Version végan ou plus profonde du pattern 001 : la sauce tahini apporte le crémeux du yaourt + une note grillée et amère qui fait écho à la croûte rôtie.

### Structure
- base : légume rôti (chou-fleur, aubergine, brocoli, courge, betterave)
- transformation : rôti à four chaud jusqu'à brunissement franc
- sauce / liant : tahini + jus citron + ail pressé + eau (consistance crème épaisse)
- contraste : grenade fraîche OU oignon caramélisé OU citron confit haché
- finition : herbes fraîches abondantes
- texture : pignons, amandes, ou graines (sésame, courge)

### Logique de goût
- salé : sel sur légume + sel dans la sauce
- gras : huile d'olive + tahini lui-même très gras
- acide : citron dans la sauce ; éventuellement grenade ou sumac
- sucré : caramélisation du légume + grenade en option
- amer : note amère naturelle du tahini, équilibrée par citron et sel
- umami : profondeur de la croûte
- aromatique : zaatar, sumac, cumin, persil

### Pattern réutilisable

```text
légume dense rôti + tahini-citron-ail-eau + grenade ou citron confit + herbes + graines/noix grillées
```

### Variantes
- bases : chou-fleur entier, aubergine en quartiers, brocoli rôti, betterave, patate douce
- sauces : tahini classique, tahini-yaourt 50/50, tahini + harissa, tahini + miel pour sucré-salé
- toppings : grenade, oignons frits, pignons, amandes effilées, sumac, zaatar
- herbes / épices : persil, coriandre, menthe ; sumac, zaatar, piment d'Alep
- protéines compatibles : agneau grillé, poulet rôti, pois chiches frits, œuf mollet
- version simple : chou-fleur en bouquets + sauce tahini base + persil + sumac
- version festive : chou-fleur entier rôti + tahini + grenade + herbes triples + pignons frits + citron confit haché

### Points critiques
- la sauce tahini se solidifie au contact du citron : ajouter l'eau **après**, en filet, en fouettant
- consistance cible : nappe une cuillère mais coule lentement
- goûter et ajuster : presque toujours +sel +acide
- tahini de qualité (texture coulante, goût propre)
- ne pas chauffer la sauce tahini

### Erreurs fréquentes
- ajouter l'eau avant le citron → mauvaise émulsion
- tahini rance → ruine tout
- sauce trop épaisse → masque le légume
- sauce sous-salée → reste plate

### Repères sensoriels
- sauce qui dessine un ruban quand on la verse depuis la cuillère
- légume qui craque légèrement sous la fourchette mais cède au cœur
- éclats de grenade qui apportent jus + croquant simultanément

### Usage Gemini
- proposer quand : "j'ai du tahini, quoi en faire", "version végan d'un plat de légume rôti", "plat partageable type mezze"
- éviter quand : aversion au sésame, repas express, allergie sésame
- adaptation rapide : sauce tahini en 2 min, légume rôti en 25 min sur une plaque

---

## Pattern 004 — Soupe légume crémée + topping aromatique chaud final

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : soupe lentilles cari coco ; potage courgettes pois basilic ; potage citrouille safran orange
- origine consolidation : Claude V1, enrichi par Codex (geste "herbes ajoutées hors feu" explicité)
- statut : pattern extrait, pas recette copiée

### Intention
Une soupe qui n'est pas qu'une soupe : le bol contient deux gestes (la base mixée + le topping qui craque ou aromatise au moment du service).

### Structure
- base : un légume principal (courge, courgette, lentille, chou-fleur, betterave) + bouillon
- transformation : oignon revenu, épices grillées, légume mijoté, mixage final ; pour les soupes vertes, herbes/feuilles ajoutées **hors feu** juste avant le mixage
- sauce / liant : crème fraîche, lait de coco, ou yaourt incorporés en fin de cuisson
- contraste : topping aromatique distinct ajouté **à l'assiette** (pas dans la casserole)
- finition : zeste, filet d'huile parfumée, herbes fraîches
- texture : graines grillées sucrées-salées, croûtons, oignons frits, éclats de noix

### Logique de goût
- salé : sel par paliers en cuisson
- gras : huile + crème fraîche/coco selon variante
- acide : zeste + jus en finition (citron, lime, orange)
- sucré : douceur naturelle du légume + caramélisation oignon
- amer : option (zeste pamplemousse, harissa)
- umami : bouillon + caramélisation
- aromatique : safran, cari, harissa, cumin, gingembre selon variante

### Pattern réutilisable

```text
légume mijoté avec oignon-épices + (verts ajoutés hors feu si soupe verte) + mixage + crème (vache ou coco) + topping chaud aromatique distinct + zeste agrume + herbes fraîches
```

### Variantes
- bases : courge butternut, citrouille, courgette, chou-fleur, lentille corail, lentille verte, panais, betterave, petits pois
- liquide crémeux : crème fraîche, lait de coco, yaourt grec, crème de cajou
- toppings : graines de courge grillées sucrées-épicées, croûtons huile-ail, oignons frits, dukkah, herbes frites, pancetta croustillante, œuf poché
- herbes / épices : safran, harissa, cari, cumin, gingembre frais, cardamome ; coriandre, menthe, persil, basilic
- protéines compatibles : œuf poché, dés de jambon, pois chiches frits, féta émietté
- version simple : 1 légume + bouillon + crème + filet d'huile + zeste + herbe
- version festive : double légume + 2 toppings (croquant + aromatique) + harissa maison + 3 herbes

### Points critiques
- griller les épices avant le liquide pour libérer les arômes
- mixer chaud puis vérifier l'assaisonnement (saler après mixage)
- ajouter la crème **hors du feu** ou à frémissement, jamais à ébullition
- pour la couleur verte vive (courgette/petits pois/basilic) : retirer du feu **dès** l'ajout des verts, mixer immédiatement
- le topping doit être préparé pendant la cuisson, prêt au service

### Erreurs fréquentes
- crème ajoutée à ébullition → tranche
- mixé sans regoûter → sous-salé
- topping intégré au mix → perd l'effet de surprise
- légume vert trop cuit → couleur terne, perte d'arôme
- herbes ajoutées trop tôt dans la cuisson → grises

### Repères sensoriels
- texture veloutée mais pas collante
- couleur vive, pas terne
- topping qui croustille distinctement à la cuillère
- zeste qui se sent au nez avant la première gorgée

### Usage Gemini
- proposer quand : "soupe qui change de l'ordinaire", "j'ai un légume qui tourne", "entrée chaude avant un repas léger"
- éviter quand : pas de mixeur, repas "ça tient" recherché (sauf coco-lentille)
- adaptation rapide : oignon + légume surgelé + bouillon + lait de coco + cari = 25 min

---

## Pattern 005 — Soupe froide légume aqueux + yaourt + herbes

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : gaspachos et potages froids estivaux du chapitre Brunchs et Légumes crus
- origine consolidation : Codex (angle mort de la V1 Claude qui ne couvrait que les soupes chaudes)
- statut : pattern extrait, pas recette copiée

### Intention
Soupe d'été qu'on boit autant qu'on mange : fraîcheur, acide net, base laitière qui apaise, garniture qui ajoute du relief.

### Structure
- base : légume aqueux cru ou peu cuit (concombre, tomate très mûre, melon d'eau, courgette blanchie, poivrons crus)
- transformation : mixage à froid avec base laitière acide, repos au frigo
- sauce / liant : la soupe **est** la sauce ; consistance veloutée mais pas trop épaisse
- contraste : garniture solide en assiette (légumes en brunoise, fromage, croûtons, huile aromatique)
- finition : herbes fraîches abondantes au moment du service + zeste
- texture : croûtons croustillants, dés très fins de légume cru, graines, ou éclats de noix

### Logique de goût
- salé : sel + parfois fromage ou anchois
- gras : huile d'olive + yaourt
- acide : vinaigre, jus citron, ou base de tomate ; dominant
- sucré : douceur naturelle du légume mûr
- amer : option (zeste d'agrume amer)
- umami : option (parmesan, anchois, tomate concentrée)
- aromatique : ail cru, gingembre, basilic, menthe, aneth, coriandre

### Pattern réutilisable

```text
légume aqueux + yaourt/labneh + acide (vinaigre ou citron) + huile + sel → mixé à froid → repos frigo → garniture solide en assiette + herbes + zeste
```

### Variantes
- bases : concombre, tomate, melon d'eau + tomate, courgette blanchie, avocat, poivron rôti et pelé, betterave crue
- liquides crémeux : yaourt grec, labneh dilué, ayran, kéfir, lait ribot, crème de cajou pour version végane
- garnitures solides : brunoise du même légume, croûtons huile-ail, féta émietté, œuf dur, jambon en dés, crevettes, raisins coupés
- herbes / épices : aneth, menthe, basilic, coriandre, ciboulette ; sumac, cumin, piment d'Alep
- protéines compatibles : crevettes, jambon serrano, œuf dur, féta, halloumi
- version simple : concombre + yaourt + ail + citron + menthe ; mixé ; brunoise concombre en garniture
- version festive : 3 légumes mêlés + labneh + huile aromatique + 3 garnitures solides + 4 herbes

### Points critiques
- soupe **vraiment** froide : 1 h minimum au frigo après mixage
- légume très mûr ou très qualitatif (impossible de masquer un mauvais ingrédient en cru)
- équilibre acide-sel goûté **après** le repos froid (le froid masque le sel — re-ajuster à la sortie du frigo)
- garniture solide servie à part dans un petit bol, ajoutée minute par convive
- huile fruitée en filet final, jamais mixée

### Erreurs fréquentes
- soupe servie tiède → perd tout son intérêt
- assaisonnée chaude puis refroidie → fade
- garniture mélangée trop tôt → légumes qui ramollissent dans le bol
- mauvaise tomate → soupe acide et plate, sans rondeur
- herbes mixées avec → couleur terne, goût d'herbe écrasée

### Repères sensoriels
- couleur vive, jamais grise
- nappe la cuillère sans figer
- crunch distinct de la garniture solide à chaque cuillerée
- zeste qui se sent au nez avant la première gorgée

### Usage Gemini
- proposer quand : "soupe froide d'été", "j'ai des concombres et du yaourt", "entrée fraîche pour temps chaud", "végé léger avant un plat consistant"
- éviter quand : hors saison, légumes pas assez mûrs, dîner d'hiver
- adaptation rapide : mixeur + 5 min ; le repos au frigo se fait pendant qu'on prépare la suite

---

## Pattern 006 — Salade composée crue + herbes en abondance + acide vif + croquant

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : salade tomate-concombre tahini-zaatar ; salade pêches framboises cinq-épices ; salade melon-pomme verte à la lime ; cœurs de romaine vinaigrette herbes vide-frigo
- origine consolidation : Claude V1, enrichi par Codex (variantes salade crudités-tahini absorbées)
- statut : pattern extrait, pas recette copiée

### Intention
Salade qui tient debout comme plat. Elle ne sert pas de garniture : elle est l'événement. Herbes traitées comme un légume, pas comme un décor.

### Structure
- base : 2-3 ingrédients crus complémentaires (légume + fruit, ou légume + légume + fruit)
- transformation : aucune cuisson ; macération de l'échalote dans l'acide ; coupes nettes
- sauce / liant : vinaigrette légère avec tahini ou yaourt OU acide pur + huile
- contraste : élément sucré (fruit) ou salé (féta, olive, anchois)
- finition : herbes fraîches en quantité de salade, pas en pincée
- texture : graines, noix grillées, ou granité (zaatar, dukkah)

### Logique de goût
- salé : sel en flocons en finition + élément salé éventuel
- gras : huile d'olive + éventuel tahini ou avocat
- acide : citron / lime / vinaigre + fruit acide
- sucré : fruit cru OU légume sucré (tomate mûre, betterave crue)
- amer : option (radicchio, roquette, endive)
- umami : option (féta, parmesan, anchois)
- aromatique : herbes multiples (jamais une seule), zaatar, sumac

### Pattern réutilisable

```text
2-3 crus en dés réguliers + macération échalote acide + vinaigrette tahini/yaourt OU citron-huile + herbes multiples en quantité + finition croquante
```

### Variantes
- bases : tomate-concombre-poivron, melon-pomme verte, pêche-radicchio, fenouil-orange, betterave-pomme, carotte râpée-orange
- vinaigrettes : citron-huile, tahini-citron-eau, yaourt-gingembre-citron, vinaigre Xérès-huile, lime-citronnelle
- toppings : pignons, amandes, sésame, dukkah, zaatar, pita rôti en croûtons, graines de nigelle
- herbes / épices : 3-4 herbes obligatoires (menthe, coriandre, persil, aneth, basilic, estragon)
- protéines compatibles : féta, halloumi grillé, poulet effiloché, crevettes grillées, œuf mollet
- version simple : tomate + concombre + 3 herbes + citron + huile + sel
- version festive : 3 crus + 4 herbes + tahini-zaatar + féta + pignons + grenade

### Points critiques
- macérer l'échalote dans l'acide AVANT d'assembler
- ne pas saler avant le tout dernier moment (les légumes rendent de l'eau)
- couper les crus en dés réguliers pour la même bouchée
- les herbes doivent peser presque autant qu'un autre légume
- assaisonner les feuilles tendres en dernier

### Erreurs fréquentes
- 1 seule herbe → manque le caractère
- sel trop tôt → légumes inondés
- oignon cru pas macéré → agressif
- sauce versée tôt → ramollit

### Repères sensoriels
- salade humide mais pas inondée
- herbes encore fermes et vertes, jamais flétries
- sons distincts en bouche : eau du crus + croquant des graines
- zeste qui parfume avant la première bouchée

### Usage Gemini
- proposer quand : "salade fraîche mais pas plate", "j'ai des herbes qui traînent", "entrée d'été qui en impose"
- éviter quand : herbes manquantes (le pattern s'effondre), repas très consistant en suite
- adaptation rapide : 1 crus + 1 acide + 1 herbe + 1 graines = 5 min ; le pattern est "accumulez"

---

## Pattern 007 — Mijoté légumineuse + tomate + épices Moyen-Orient + yaourt en finition

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : haricots d'Espagne en sauce tomate ; pois chiches bette à carde yaourt ; lentilles du Puy aubergine yaourt ; ragoût de lentilles aubergine
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Plat principal végétarien réconfortant, peu cher, qui s'améliore avec le temps. Architecture : base mijotée + cuillerée de yaourt qui apaise et rafraîchit.

### Structure
- base : légumineuse (pois chiches, haricots blancs, lentilles du Puy, haricots cocos)
- transformation : mijoté avec oignons caramélisés, ail, tomates, épices, jusqu'à fondance
- sauce / liant : la propre sauce du mijoté, partiellement réduite
- contraste : cuillerée généreuse de yaourt grec froid au service
- finition : herbes fraîches abondantes (coriandre dominante) + filet d'huile + jus citron
- texture : option — graines (cumin, sésame), noix concassées

### Logique de goût
- salé : sel par paliers + ajustement final
- gras : huile d'olive + yaourt
- acide : tomate + jus citron en finition + acidité du yaourt
- sucré : oignons caramélisés
- amer : —
- umami : tomate longuement cuite + pâte de tomate
- aromatique : cumin, coriandre, paprika, carvi, harissa, baharat selon variante

### Pattern réutilisable

```text
légumineuse fondante + base oignon-ail-épices + tomate longuement mijotée + cuillerée de yaourt froid + coriandre + huile + citron
```

### Variantes
- bases : pois chiches, haricots blancs, lentilles vertes/du Puy/corail, haricots cocos, haricots d'Espagne
- aromates dominants : cumin + coriandre, paprika fort + carvi, ras-el-hanout, baharat, harissa rose
- légumes ajoutés : aubergine rôtie, bette à carde, épinards, courgettes, carottes
- herbes : coriandre (majeure), persil, menthe, aneth
- protéines compatibles : tofu doré, agneau haché, merguez en option
- version simple : pois chiches en boîte + tomate + cumin + ail + yaourt + coriandre
- version festive : double légumineuse + aubergine rôtie + harissa maison + herbes triples + pignons grillés

### Points critiques
- caraméliser vraiment les oignons (8-12 min minimum)
- griller les épices entières dans l'huile avant les tomates
- pour les lentilles : ne pas saler trop tôt
- yaourt **ajouté en finition**, jamais cuit
- citron en toute fin pour relever

### Erreurs fréquentes
- yaourt cuit dans la sauce → tranche
- oignons pas assez cuits → goût cru
- épices ajoutées avec liquide → pas réveillées
- plat servi tout de suite → le plat est meilleur le lendemain

### Repères sensoriels
- sauce qui nappe les légumineuses, ne flotte pas
- légumineuses tendres mais pas écrasées
- couleur orangée/rouge profond
- yaourt qui fait un tourbillon visible dans la sauce

### Usage Gemini
- proposer quand : "plat végé qui tient au corps", "dîner de semaine à préparer la veille", "j'ai des pois chiches en boîte"
- éviter quand : besoin de léger, aversion cumin/coriandre fraîche
- adaptation rapide : tout en boîte (légumineuse + tomate concassée), 25 min, sans rôtissage

---

## Pattern 008 — Grain pilaf + caramélisation + fruit sec + noix + zeste agrume

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : couscous au ras-el-hanout ; boulgour aux champignons ; riz brun aux oignons caramélisés et ail noir ; riz à la menthe et grenade
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Faire d'un grain neutre un plat principal aromatique : caramélisation comme socle de saveur, fruit sec comme pont sucré-salé, noix comme texture.

### Structure
- base : grain (couscous, boulgour, riz basmati, riz brun, freekeh, orzo)
- transformation : grain cuit séparément, gonflé/égoutté ; oignons caramélisés en parallèle, longuement
- sauce / liant : huile d'olive + jus de cuisson de l'oignon + zeste d'agrume
- contraste : fruit sec macéré (raisin sec, abricot sec, datte, grenade fraîche)
- finition : herbes fraîches en grande quantité (menthe + persil + coriandre)
- texture : noix grillées (amandes, pignons, pistaches, noix de pécan)

### Logique de goût
- salé : sel dans l'eau du grain + sel sur l'oignon
- gras : huile d'olive abondante + huile de l'oignon confit
- acide : zeste + jus d'agrume (citron, lime), grenade éventuelle
- sucré : oignons caramélisés + fruit sec
- amer : —
- umami : caramélisation profonde
- aromatique : ras-el-hanout, cumin, cinq-épices, baharat, ou herbes seules

### Pattern réutilisable

```text
grain gonflé + oignon longuement caramélisé + fruit sec + noix grillées + zeste agrume + herbes fraîches abondantes
```

### Variantes
- bases : couscous, boulgour fin/moyen, riz basmati, riz brun, freekeh, perles de couscous, orzo
- caramélisation : oignon jaune, oignon rouge, échalote, poireau confit
- fruits secs : raisin de Smyrne, raisin doré, abricot sec, datte, cerise séchée, grenade fraîche
- noix : amandes effilées, pignons, pistaches, noix, noix de pécan, noisettes
- herbes / épices : ras-el-hanout, baharat, cinq-épices, cumin, coriandre moulue ; menthe, coriandre, persil, aneth
- protéines compatibles : agneau, poulet, halloumi, féta, pois chiches frits
- version simple : couscous + oignon caramélisé + raisins secs + amandes + persil + zeste citron
- version festive : freekeh + oignon + abricot sec + pistaches + grenade + 3 herbes + ras-el-hanout

### Points critiques
- vraiment caraméliser l'oignon : doré franc, pas blond
- griller les noix à sec ou avec un soupçon d'huile, jusqu'au parfum
- ajouter le zeste **au dernier moment**
- grain bien aéré à la fourchette, jamais en bloc compact
- assaisonner le grain *avant* d'ajouter herbes/zeste

### Erreurs fréquentes
- oignon pas assez cuit → goût cru
- noix non grillées → texture mais pas de parfum
- zeste cuit → perd ses huiles essentielles
- grain compact → mauvaise texture

### Repères sensoriels
- oignon translucide à brun-acajou, jamais brûlé
- noix dorées et parfumées sans amertume
- grain qui se sépare grain à grain
- équilibre visible : 3 couleurs (grain pâle, oignon foncé, herbes vertes)

### Usage Gemini
- proposer quand : "accompagnement qui ne ressemble pas à un accompagnement", "plat unique végé", "j'ai des restes de viande à étirer"
- éviter quand : régime très bas en glucides, aversion aux fruits secs dans le salé
- adaptation rapide : couscous (5 min) + oignons préparés à l'avance ; grain prêt en 15 min

---

## Pattern 009 — Pâtes + huile aromatique infusée + agrume + croquant + herbes

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : trofies basilic-anchois-pistaches ; spaghettis anchois-salicorne ; et variations
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Pâtes minimalistes mais intenses : l'huile a fait tout le travail aromatique avant. La pâte rencontre une émulsion concentrée, pas une sauce volumineuse.

### Structure
- base : pâtes longues ou courtes (spaghetti, trofie, fusilli, linguine)
- transformation : huile infusée à part avec ingrédient salé puissant (anchois, ail, piment)
- sauce / liant : huile aromatique + un peu d'eau de cuisson des pâtes (émulsion légère)
- contraste : élément végétal vert (pois mange-tout, salicorne, roquette, basilic en purée)
- finition : zeste de citron + herbes fraîches + parmesan ou pecorino râpé
- texture : noix concassées (pistaches, pignons) ou chapelure dorée

### Logique de goût
- salé : anchois ou câpres + eau de cuisson + parmesan
- gras : huile d'olive abondante
- acide : zeste de citron + un trait de jus
- sucré : douceur naturelle de l'ail confit
- amer : option (zeste, roquette)
- umami : anchois + parmesan = double levier umami
- aromatique : basilic ou persil dominant, piment broyé, ail

### Pattern réutilisable

```text
pâtes al dente + huile infusée (anchois/ail/piment) + élément vert + eau de cuisson pour émulsion + zeste citron + noix concassées + herbes
```

### Variantes
- bases : spaghetti, linguine, trofie, fusilli, orecchiette, tagliatelle
- huiles infusées : anchois-ail-piment, ail-piment seul, sauge-beurre noisette, câpres-citron-ail, basilic-pistache (purée crue)
- éléments verts : pois mange-tout, salicorne, fanes, roquette, brocoli haché, basilic en purée
- noix : pistaches, pignons, noix, noisettes, amandes
- herbes / épices : basilic, persil, origan, piment d'Alep, piment d'Urfa
- protéines compatibles : ricotta, burrata, œuf cru sur pâtes chaudes, sardines, thon mi-cuit
- version simple : spaghetti + ail-anchois-piment + persil + parmesan
- version festive : trofie + purée basilic-anchois-pistache + pois mange-tout + zeste + pecorino + pignons

### Points critiques
- ne pas brûler l'ail/anchois dans l'huile (feu doux, fondre)
- conserver une grosse louche d'eau de cuisson **avant d'égoutter**
- finir la cuisson des pâtes 1-2 min dans la sauce avec un peu d'eau
- zeste **après** le feu, jamais cuit
- les pâtes ne doivent jamais être nues sur le bord du bol

### Erreurs fréquentes
- ail brûlé → amer
- égoutter sans réserver d'eau → sauce sèche
- zeste cuit → fade
- pâtes trop cuites avant la sauce → bouillies

### Repères sensoriels
- huile colorée par les aromates, plus aussi blonde
- sauce qui adhère aux pâtes en ruban
- éclats verts et notes d'agrume distincts

### Usage Gemini
- proposer quand : "pâtes vite mais pas fades", "j'ai des anchois et du citron", "pasta qui change de la tomate"
- éviter quand : aversion anchois (mais le pattern reste valide en remplaçant par câpres ou olives)
- adaptation rapide : 15-20 min ; l'huile s'infuse pendant que les pâtes cuisent

---

## Pattern 010 — Protéine simple saisie + salsa fraîche acidulée

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : tartare de truite beurre noir pistaches ; filets d'agneau amandes fleur d'oranger ; filets de maquereau salsa pistache cardamome ; salade de bifteck au basilic
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
La protéine est neutre, propre, parfaitement cuite. La salsa transforme tout : c'est elle qui définit le plat, change la culture culinaire.

### Structure
- base : protéine animale tendre (filet d'agneau, bifteck, maquereau, truite, crevettes)
- transformation : marinade courte ou aucune + saisie franche OU cru salé/citronné
- sauce / liant : la salsa servie à côté, pas dessus
- contraste : la salsa est le contraste — herbes hachées + acide + huile + élément texturé
- finition : sel en flocons + zeste
- texture : noix concassées dans la salsa (pistaches, amandes, pignons)

### Logique de goût
- salé : sel sur la viande + sel dans la salsa
- gras : huile dans la salsa + matière grasse de la cuisson
- acide : citron, lime ou vinaigre dans la salsa, dominant
- sucré : option (mélasse de grenade, miel, fruit dans la salsa)
- amer : option (zeste)
- umami : viande saisie
- aromatique : herbes en quantité dans la salsa (menthe, coriandre, persil, estragon), épices grillées

### Pattern réutilisable

```text
protéine tendre saisie nature + salsa fraîche : herbes hachées + noix concassées + acide + huile + zeste + parfois fruit/épice
```

### Variantes
- bases : agneau (filet, côtelettes), bœuf (bifteck, onglet), poulet (cuisse, blanc), poisson blanc, saumon, truite, crevettes, calmars
- salsas : pistache-cardamome, amandes-fleur d'oranger, pignons-mélasse de grenade, basilic-anchois, olives-grenade, menthe-noisettes
- herbes : 1-2 dominantes par salsa, abondantes
- épices : cardamome, cumin, sumac, piment fumé, fleur d'oranger
- protéines compatibles : interchangeables — la salsa est la signature, pas la protéine
- version simple : poulet saisi + salsa persil-citron-pignons-huile
- version festive : agneau filet mariné + salsa amandes-fleur d'oranger-menthe + grenade

### Points critiques
- protéine sèche en surface avant saisie, sel juste avant
- salsa préparée avant de cuire la protéine, repose 10-15 min
- ne pas verser la salsa **sur** la viande chaude, la déposer **à côté**
- noix grillées au moment du jour, pas la veille
- repos de la viande après cuisson (3-5 min minimum)

### Erreurs fréquentes
- salsa versée chaude → ramollit
- viande pas séchée → ne saisit pas
- noix non grillées → manque le parfum
- salsa pré-faite la veille → herbes flétries

### Repères sensoriels
- viande qui résiste légèrement puis cède
- salsa qui sent à 50 cm
- contraste de température : viande chaude, salsa fraîche

### Usage Gemini
- proposer quand : "j'ai une belle protéine", "je veux faire simple mais impressionnant", "recevoir sans stress", "protéine simple mais impressionnante"
- éviter quand : pas d'herbes fraîches, pas de noix
- adaptation rapide : la même salsa fonctionne sur 4-5 protéines — préparer une fois, varier la base

---

## Pattern 011 — Salade-repas grain ou pâtes + protéine + acide + croquant

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : salade de couscous ; salade chou-fleur rôti et œufs cari ; salade de bifteck basilic ; salade crevettes maïs tomates
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Salade qui constitue le plat entier : féculent + protéine + crus + sauce. Architecture du "bowl" avant que le mot existe.

### Structure
- base : grain ou pâtes courtes refroidi(e)s, OU mélange légume rôti tiède + grain
- transformation : grain cuit, refroidi ; un autre élément cuit (œuf dur, protéine saisie, légume rôti)
- sauce / liant : vinaigrette dense (yaourt-mayonnaise-épice, ou tahini, ou citron-huile généreuse)
- contraste : herbes en quantité + élément acide (zeste, échalote macérée, pickle)
- finition : sel en flocons + filet d'huile + dernière herbe
- texture : noix grillées + parfois croûtons (pita rôti)

### Logique de goût
- salé : sel + parfois fromage (féta, parmesan)
- gras : huile + sauce crémeuse + protéine
- acide : citron-vinaigre + cornichon ou pickle éventuel
- sucré : option (raisin sec, fruit, oignon caramélisé)
- amer : roquette, endive, radicchio en option
- umami : protéine + parfois fromage affiné + tomate concentrée
- aromatique : herbes multiples + épice porteuse (cumin, cari, baharat)

### Pattern réutilisable

```text
grain/pâte refroidi(e) + protéine + crus + sauce dense crémeuse ou acide + herbes multiples + croquant + sel en flocons
```

### Variantes
- bases : couscous, boulgour, freekeh, riz refroidi, lentilles cuites, pâtes courtes (orzo, ditali)
- protéines : œuf dur, poulet poché ou saisi, bifteck saignant, crevettes, féta, halloumi, pois chiches grillés
- crus : tomates cerises, concombre, oignon rouge, radis, fenouil, herbes
- sauces : yaourt-mayo-cari, tahini-citron, vinaigrette aux anchois, vinaigrette aux fines herbes, mayo-citron-câpres
- noix/croquants : amandes, pistaches, pignons, croûtons de pita, dukkah
- protéines compatibles : œuf, viande, poisson, fromage — interchangeables
- version simple : couscous + thon en boîte + tomate + concombre + citron-huile + persil
- version festive : freekeh + agneau saignant + roquette + tahini-citron + pignons + grenade + 3 herbes

### Points critiques
- assaisonner le grain **chaud** (il absorbe mieux), puis laisser tiédir
- ne pas trop sauter — la salade-repas n'est pas un mélange unique, elle a 4-5 composants visibles
- sauce assemblée à part, montée à la dernière minute
- le grain doit être tiède ou à température ambiante, pas froid frigo
- équilibrer les volumes : 1/3 grain, 1/3 protéine, 1/3 crus + herbes + sauce

### Erreurs fréquentes
- grain assaisonné froid → fade
- tout mélangé → bouillie sans relief
- sauce trop liquide → noie le grain
- manque de croquant → texture monocorde

### Repères sensoriels
- bol coloré en couches visibles
- sauce qui fait des taches distinctes, pas un brassage uniforme
- herbes vertes en abondance qui dépassent
- texture variée à chaque bouchée

### Usage Gemini
- proposer quand : "déjeuner du lendemain", "lunch box qui tient", "dîner d'été léger mais qui rassasie"
- éviter quand : besoin de chaud réconfortant, repas formel
- adaptation rapide : grain pré-cuit + protéine cuite la veille + crus + vinaigrette = 10 min d'assemblage

---

## Pattern 012 — Boulettes de viande aux épices + sauce yaourt/tahini + topping

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : boulettes d'agneau au féta ; siniyah à l'agneau (architecture proche)
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Boulettes qui sortent de l'ordinaire : herbes et fromage **dans** la viande, glaçage final acide, sauce crémeuse en accompagnement.

### Structure
- base : viande hachée (agneau, bœuf, mélange) + liant (mie de pain, œuf)
- transformation : épices et herbes intégrées au mélange ; saisie à la poêle puis finition au four
- sauce / liant : yaourt ou tahini, à part, en cuillerée
- contraste : glaçage final acide (mélasse de grenade, jus de citron concentré, sirop de tamarin)
- finition : herbes fraîches + sumac ou zaatar
- texture : pignons grillés, oignons croustillants, dukkah

### Logique de goût
- salé : sel dans la viande + féta éventuel
- gras : viande grasse (agneau idéal) + huile de cuisson
- acide : glaçage final + acide dans la sauce yaourt/tahini
- sucré : mélasse de grenade ou miel dans le glaçage
- amer : —
- umami : viande saisie + féta éventuel
- aromatique : cumin, cannelle, baharat, ras-el-hanout, piment d'Alep, menthe, persil

### Pattern réutilisable

```text
viande hachée + herbes + épices + fromage frais en option + saisie + finition four + glaçage acide-sucré + sauce yaourt/tahini à côté + topping croquant + herbes
```

### Variantes
- bases : agneau, bœuf, agneau-bœuf, agneau-veau, dinde-poulet pour version légère
- liants : mie de pain trempée, semoule, œuf
- fromages intégrés : féta, halloumi en dés, ricotta
- glaçages : mélasse de grenade, miel-cumin, sirop de tamarin, harissa-miel, balsamique réduit
- sauces : yaourt-citron-ail, tahini classique, tzatziki, sauce harissa-yaourt
- toppings : pignons grillés, oignons frits, dukkah, sumac, menthe ciselée
- protéines compatibles : version végé avec haché de pois chiches/champignons
- version simple : boulettes agneau-féta-cumin + yaourt-citron + persil
- version festive : boulettes agneau-féta-thym + glaçage mélasse de grenade + tahini + pignons + sumac + 3 herbes

### Points critiques
- ne pas trop pétrir le mélange (boulettes durcissent)
- saisir à feu vif puis terminer au four
- glaçage **en fin de cuisson**, pas avant
- la sauce yaourt/tahini ne se cuit pas
- repos de 3 min avant service

### Erreurs fréquentes
- mélange trop pétri → boulettes dures
- tout cuit poêle → brûlé dehors / cru dedans
- glaçage trop tôt → brûle
- sauce versée chaude sur boulettes → ramollit

### Repères sensoriels
- boulettes brunes-acajou, pas noires
- glaçage qui brille
- sauce blanche qui contraste visuellement
- arôme cumin/cannelle qui domine

### Usage Gemini
- proposer quand : "j'ai du haché et envie d'autre chose qu'une bolognaise", "recevoir avec viande facile", "pita-meal du soir"
- éviter quand : végétarien strict (sauf adaptation pois chiches), aversion cumin
- adaptation rapide : pré-mélanger la veille, cuire en 15 min ; sauces préparables à l'avance

---

## Pattern 013 — Croquettes / galettes (protéine ou légume vert) + base liée + sauce crémeuse acidulée

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : croquettes poisson fumé panais ; schnitzel poulet graines sésame-tournesol ; croquettes poisson coco ; tacos croquettes poisson mangue ; beignets de petits pois au féta et zaatar
- origine consolidation : Claude V1, enrichi par Codex (variante "galettes/beignets de légumes verts" intégrée)
- statut : pattern extrait, pas recette copiée

### Intention
Confort food revisitée : croustillant à l'extérieur, fondant à l'intérieur, et une sauce qui tire vers la fraîcheur acide pour empêcher la lourdeur. Pattern élargi pour absorber les beignets/galettes de légumes verts (petits pois, courgettes, herbes), qui suivent la même architecture.

### Structure
- base : protéine hachée (poisson, poulet, crevettes) OU légume vert haché/râpé (petits pois, courgettes, épinards) + fromage frais éventuel
- transformation : façonné, lié par œuf et chapelure ou par purée de légume ; cuisson mi-poêle mi-four
- sauce / liant : sauce yaourt ou tahini ou mayo acidulée, à part
- contraste : élément frais (oignon mariné, mangue, herbes, salade)
- finition : quartier de citron, herbes fraîches, sel en flocons
- texture : panure aux graines (sésame, panko, noix de coco grillée) OU surface dorée non panée

### Logique de goût
- salé : sel dans la pâte + sel dans la panure + féta éventuel
- gras : matière grasse de friture + sauce crémeuse + fromage
- acide : citron au service + sauce
- sucré : option (mangue, miel dans la sauce, petit pois sucré naturel)
- amer : —
- umami : poisson fumé, parmesan, féta éventuel
- aromatique : cumin, coriandre, aneth, ciboulette ; sésame, noix de coco, zaatar selon variante

### Pattern réutilisable

```text
base hachée (protéine OU légume vert) + liant (purée de légume, œuf + chapelure, ou féta) + panure aux graines en option + cuisson mi-poêle mi-four + sauce yaourt/mayo acide + élément frais + herbes
```

### Variantes
- bases : poisson blanc fumé + panais, poisson blanc + œuf, poulet en lanières, crevettes hachées, petits pois écrasés + féta, courgettes râpées + féta, pois chiches (végé), épinards-ricotta
- liants : purée de panais, purée de pomme de terre, mie de pain trempée, œuf battu, féta émietté qui agglutine
- panures : panko + sésame + tournesol, chapelure de noix de coco grillée + chili, semoule de maïs, parmesan + chapelure ; ou aucune panure (galettes simples passées dans la farine)
- sauces : yaourt-cumin-zeste de lime, mayo-citron-aneth, tahini-citron-ail, harissa-yaourt, yaourt-menthe
- éléments frais : oignon mariné, mangue julienne, salade de chou, herbes, salade verte simple
- herbes / épices : aneth, ciboulette, coriandre, persil, menthe ; cumin, curcuma, piment de Cayenne, zaatar
- protéines compatibles : interchangeables (poisson, poulet, crevettes, pois chiches, légumes verts)
- version simple : croquettes poisson + chapelure simple + mayo-citron + persil ; OU beignets petits pois + féta + yaourt-menthe
- version festive : croquettes poisson fumé + purée panais + panure mixed graines + tahini-citron + oignons croustillants + 3 herbes

### Points critiques
- mélange ni trop sec ni trop humide
- réfrigérer 15-30 min avant cuisson pour qu'elles tiennent
- huile bien chaude, pas tiède
- finition au four pour éviter brûlure extérieure / centre cru
- pour les versions légumes verts : extraire l'eau des légumes (presser, égoutter) sinon la galette s'effondre
- sauce préparée à l'avance, plus acide que ce qu'on pense

### Erreurs fréquentes
- pâte trop molle → s'effondre à la poêle
- huile pas assez chaude → croquette boirait
- tout poêle → centre cru
- sauce manque acide → plat plat
- légumes verts pas égouttés → galettes molles

### Repères sensoriels
- panure ou surface dorée uniforme, pas brûlée
- intérieur tendre qui se défait à la fourchette
- sauce qui contraste en couleur (blanche/verte sur doré)

### Usage Gemini
- proposer quand : "réutiliser un reste de poisson", "j'ai des petits pois ou courgettes en trop", "brunch ou souper familial", "végé qui plaise aux enfants"
- éviter quand : pas de four, peu de matériel
- adaptation rapide : croquettes formées la veille, cuisson minute le jour J

---

## Pattern 014 — Œufs + base aromatique + verdure (œufs braisés, frittata, shakshuka)

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : frittatas et omelettes ; œufs sur champignons-rôties ; shakshuka et variations vertes
- origine consolidation : Claude V1, enrichi par Codex (shakshuka verte et frittata enrichie absorbées comme variantes)
- statut : pattern extrait, pas recette copiée

### Intention
Œuf comme support de saveur : ce sont les aromates et la base qui font le plat, l'œuf liant et apaisant. Pattern qui couvre œufs braisés (shakshuka rouge ou verte), frittata enrichie de fromage et légumes, omelette plate, œufs au plat sur poêlée.

### Structure
- base : œufs entiers (au plat, brouillés, en frittata, pochés/braisés)
- transformation : cuisson douce ; pochage dans une sauce ou poêlée à part
- sauce / liant : œuf coulant lui-même OU sauce dans laquelle l'œuf cuit (tomate, verts braisés)
- contraste : verdure (épinard, bette à carde, herbes), pickle, ou yaourt
- finition : sel en flocons, zeste, piment doux, fines herbes
- texture : pain croustillant grillé pour saucer, féta émietté, fromage râpé fondu

### Logique de goût
- salé : sel + féta + parfois anchois
- gras : huile + beurre + parfois crème + fromage
- acide : tomate, citron, ou yaourt
- sucré : oignon longuement cuit
- amer : —
- umami : tomate, féta, parmesan, champignons
- aromatique : cumin, paprika, harissa, sumac selon variante ; herbes vertes pour shakshuka verte

### Pattern réutilisable

```text
œufs cuits doucement + base aromatique (sauce tomate épicée, verts braisés, champignons, frittata-légumes-fromage) + verdure ou yaourt + pain croustillant + sel en flocons + piment doux
```

### Variantes
- types de cuisson : pochés dans sauce (shakshuka rouge ou verte), brouillés crémeux, frittata, sur le plat, omelette plate
- bases aromatiques rouges : sauce tomate épicée, oignons-poivrons confits, harissa-tomate
- bases aromatiques vertes : épinards-bette à carde + ail, courgettes-petits pois-herbes, fanes braisées
- frittata enrichies : épinards-féta, courgettes-menthe-féta, herbes multiples-parmesan
- éléments laitiers : féta, ricotta, halloumi, yaourt, mascarpone, parmesan
- pains : pain au levain grillé, pita, focaccia, pain plat
- herbes / épices : harissa, paprika fumé, cumin, sumac ; coriandre, persil, ciboulette, aneth, menthe
- protéines compatibles : merguez, chorizo, jambon, saumon fumé en option
- version simple : œufs au plat + champignons à l'ail + persil + pain grillé
- version festive : œufs pochés en shakshuka verte (épinards-courgettes-herbes-féta-zaatar) + pain plat fait maison

### Points critiques
- œufs à température ambiante, pas frigo (cuisent inégalement)
- la base doit être prête et chaude **avant** de casser les œufs dedans
- pour shakshuka verte : les verts doivent être tombés et un peu tiédis, pas crus, pour que les œufs cuisent dans une vraie sauce
- jaune coulant = surveillance constante les 2 dernières minutes
- pour frittata : cuisson douce sur le feu puis fin au four ou sous le gril
- sel en flocons en finition, jamais en cuisson directe sur le jaune

### Erreurs fréquentes
- œufs frigo → cuisent inégalement
- base pas chaude → œufs cuisent trop lentement
- sel sur jaune cru → tâches blanches
- jaune trop ferme → plat raté
- pour shakshuka verte : verts pas assez réduits → soupe verte avec œufs flottants

### Repères sensoriels
- jaune brillant qui coule à la cuillère
- blanc opaque mais tendre, pas caoutchouteux
- sauce qui mijote doucement autour
- vapeur parfumée

### Usage Gemini
- proposer quand : "brunch avec œufs et légumes verts", "frigo presque vide mais une boîte de tomates", "œufs + pas grand chose", "souper rapide"
- éviter quand : œufs pas frais, repas froid recherché
- adaptation rapide : 15 min top, un œuf transforme tout reste de légume cuit en plat

---

## Pattern 015 — Mijoté de viande à la cocotte + base tomate-épices + finition acide-herbes

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : siniyah à l'agneau ; mijoté de poulet en croûte de maïs ; calmars au poivron rouge ; ragoûts long-cooking
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Plat de réception qui se prépare à l'avance, gagne en saveur le lendemain, et libère le cuisinier au moment du service.

### Structure
- base : viande peu noble (épaule, jarret, cuisse, calmar) en morceaux
- transformation : oignons longuement caramélisés + ail + épices grillées → tomate concentrée → viande → liquide → mijotage long couvert puis découvert
- sauce / liant : la sauce du mijotage, réduite en fin
- contraste : finition acide (zeste, jus citron, mélasse de grenade) + herbes fraîches
- finition : option croûte ou topping (croûte de tahini, croûte de maïs, polenta crémeuse)
- texture : noix grillées (pignons, amandes), ou pain pour saucer

### Logique de goût
- salé : sel par paliers
- gras : huile + gras de la viande
- acide : tomate + finition citronnée
- sucré : oignons longuement caramélisés
- amer : option (cacao dans la sauce, zeste)
- umami : viande + tomate concentrée + bouillon
- aromatique : baharat, ras-el-hanout, harissa, paprika fumé, cumin selon variante

### Pattern réutilisable

```text
viande peu noble + oignons caramélisés + épices grillées + tomate concentrée + liquide + mijotage long → finition acide + herbes + topping optionnel
```

### Variantes
- bases : agneau (épaule, gigot, collier), bœuf (paleron, joue), poulet (cuisse, haut), calmar, joue de porc
- épices : baharat, ras-el-hanout, harissa, paprika fumé + cumin, garam masala, berbéré
- liquides : vin rouge, vin blanc, bière, bouillon, eau + tomate
- finitions acides : citron pressé, mélasse de grenade, vinaigre de Xérès, jus de lime
- toppings : croûte de tahini gratinée, croûte de maïs (cornbread), polenta, semoule de boulgour, riz
- herbes : coriandre, persil, menthe, origan
- version simple : poulet (cuisses) + oignons + tomate + paprika fumé + bouillon + 90 min ; finition citron-coriandre
- version festive : agneau (épaule) + oignons + ail + ras-el-hanout + tomate + vin rouge + 3h ; croûte tahini + pignons + grenade + 3 herbes

### Points critiques
- **vraiment** caraméliser les oignons : 15-20 min à feu doux
- saisir la viande avant le mijotage si on cherche profondeur
- saler la viande la veille si possible
- le mijotage long se fait à frémissement, pas ébullition
- le plat est meilleur le lendemain — prévoir
- finition acide TOUJOURS hors du feu

### Erreurs fréquentes
- oignons pas assez caramélisés → goût plat
- ébullition forte → viande sèche
- sel insuffisant → plat fade
- acide cuit → perd son lift

### Repères sensoriels
- viande qui se défait à la fourchette
- sauce qui nappe le dos de la cuillère
- fond de cocotte qui a bruni
- arôme dégagé à 2 mètres

### Usage Gemini
- proposer quand : "plat à préparer la veille", "recevoir 6+ personnes sans stress", "dimanche d'hiver"
- éviter quand : peu de temps, pas de cocotte, repas léger recherché
- adaptation rapide : version "fond" sur cuisinière en 90 min ; version slow-cooker 6h

---

## Pattern 016 — Plat unique au four (one-tray bake)

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : nombreuses recettes à plaque unique du livre — légumes + protéine cuits ensemble
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Le plat moindre-effort par excellence : tout sur une plaque, le four fait le travail, vaisselle minimale. Ottolenghi prend ce format basique et le sublime par les aromates.

### Structure
- base : protéine + légumes denses sur une seule plaque
- transformation : tout assaisonné ensemble, étalé en monocouche, four chaud
- sauce / liant : jus rendus de la plaque
- contraste : finition fraîche au sortir du four (yaourt, herbes, salsa, oignons macérés)
- finition : zeste + sel en flocons + huile fruitée
- texture : noix ou graines grillées sur la plaque pour les 5 dernières min

### Logique de goût
- salé : sel sur tout
- gras : huile généreuse + gras de la protéine
- acide : zeste + finition citron/grenade
- sucré : caramélisation des légumes
- amer : —
- umami : protéine saisie + caramélisation
- aromatique : épices entières (cumin, coriandre, fenouil) + herbes fraîches finales

### Pattern réutilisable

```text
légumes denses coupés + protéine assaisonnée + huile + épices + sel + monocouche sur plaque + four chaud → finition acide-herbes-yaourt
```

### Variantes
- protéines : cuisses de poulet, saucisses, pavés de saumon, blocs de halloumi, pois chiches en boîte
- légumes : pommes de terre nouvelles, poivrons, oignons, fenouil, courgettes, choux de Bruxelles, panais, patates douces
- épices : ras-el-hanout, harissa, paprika fumé, sumac, cari, mélange "shawarma"
- finitions : yaourt-citron, salsa verte, oignons macérés, grenade, herbes
- topping : pignons grillés ajoutés en fin, féta émietté à la sortie
- version simple : cuisses de poulet + pommes de terre + harissa + citron + persil
- version festive : agneau (épaule en morceaux) + 4 légumes + ras-el-hanout + grenade + tahini + 3 herbes

### Points critiques
- couper les légumes de taille **homogène** sinon cuisson inégale
- monocouche stricte
- protéine sur le dessus si elle rend du gras (poulet, saucisse) pour graisser les légumes
- plaque assez grande sinon vapeur, pas de coloration
- assaisonner avec une marge — la saveur "se diluera"
- la finition fraîche est OBLIGATOIRE pour que le plat ne soit pas plat

### Erreurs fréquentes
- légumes mal calibrés → cuisson inégale
- plaque trop chargée → vapeur, pas de coloration
- oubli de la finition fraîche → plat plat
- sous-assaisonnement → fade par dilution

### Repères sensoriels
- bords des légumes brun-noir, pas pâles
- jus dans la plaque qui chante
- protéine bien dorée, peau croustillante si applicable
- contraste de couleur cuit/frais à la sortie

### Usage Gemini
- proposer quand : "dîner de semaine sans vaisselle", "j'ai une protéine + des légumes"
- éviter quand : besoin d'une cuisson très précise par composant
- adaptation rapide : 10 min de prep, 40 min au four, finition 2 min

---

## Pattern 017 — Tartine crémeuse + salsa vive

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : tartines au labneh / avocat / ricotta + garnitures variées du chapitre Brunchs
- origine consolidation : Codex (angle mort de la V1 Claude)
- statut : pattern extrait, pas recette copiée

### Intention
Format brunch ou apéro qui combine simplicité maximum et impact visuel : une base crémeuse étalée sur du pain bien grillé, une salsa qui apporte fraîcheur et acide, des herbes qui réveillent.

### Structure
- base : pain rustique grillé (levain, focaccia, pain plat) ou cracker épais
- transformation : pain frotté à l'ail cru + filet d'huile, grillé jusqu'à doré franc
- sauce / liant : élément crémeux étalé (avocat écrasé, labneh, ricotta, fromage frais, hummus)
- contraste : salsa vive (tomates, herbes, oignon mariné, agrume, fruit)
- finition : sel en flocons + filet d'huile fruitée + poivre frais + zeste
- texture : graines, noix concassées, ou flocons croustillants (sumac, dukkah, zaatar)

### Logique de goût
- salé : sel en flocons + parfois fromage affiné, anchois, capres
- gras : élément crémeux + huile fruitée
- acide : agrume ou vinaigre dans la salsa + fromage frais
- sucré : option (fruit cru ou rôti, miel)
- amer : option (zeste, roquette)
- umami : option (anchois, parmesan, tomate concentrée, miso)
- aromatique : herbes multiples + zaatar, sumac, piment broyé

### Pattern réutilisable

```text
pain rustique grillé (frotté ail) + élément crémeux étalé + salsa vive (cru-acide-herbes) + sel en flocons + filet d'huile + zeste
```

### Variantes
- bases : pain au levain, focaccia, pain plat moyen-oriental, sourdough épais, bagel toasté
- éléments crémeux : avocat écrasé citronné, labneh, ricotta + herbes, fromage frais ail-herbes, hummus, mascarpone, fromage de chèvre frais, beurre noisette + miso
- salsas : tomates cerises-basilic-balsamique, oignon mariné-grenade, fenouil-orange-herbes, pêche-radicchio-menthe, champignons rôtis-thym, pois chiches écrasés-citron
- herbes / épices : aneth, ciboulette, basilic, menthe, coriandre, persil ; sumac, zaatar, piment d'Alep
- protéines compatibles : œuf poché ou mollet, saumon fumé, anchois, jambon serrano, sardines
- version simple : pain grillé ail-huile + avocat écrasé + tomates cerises + sel + basilic
- version festive : focaccia maison + labneh aux herbes + salsa pêche-fenouil-grenade + sumac + 3 herbes + huile fruitée

### Points critiques
- pain **vraiment** grillé : doré franc, surface qui craque (pas blond mou)
- frottage à l'ail cru sur pain encore chaud
- élément crémeux assaisonné lui-même (sel + acide), pas seulement la salsa
- salsa préparée à l'avance, repose 10 min ; éléments coupés finement, taille uniforme
- assemblage minute, sinon le pain ramollit
- huile fruitée de finition obligatoire — c'est la signature

### Erreurs fréquentes
- pain pas assez grillé → ramollit instantanément sous la crème
- crémeux non assaisonné → tartine plate malgré une belle salsa
- salsa trop liquide → détrempe tout
- assemblage trop tôt → pain mou avant service
- mauvais pain (pain de mie, baguette industrielle) → support sans caractère

### Repères sensoriels
- premier "crac" sonore en bouche
- contraste de couleur fort : pain doré + crémeux blanc + salsa colorée + herbes vertes
- huile qui brille en surface
- arôme dégagé en passant l'assiette

### Usage Gemini
- proposer quand : "j'ai du pain, de l'avocat et des tomates", "brunch facile", "apéro qui ne ressemble pas à un apéro", "lunch simple mais beau"
- éviter quand : pas de bon pain, élément crémeux mauvais, repas du soir consistant attendu
- adaptation rapide : 8-10 min total ; modulaire selon le frigo du jour

---

## Pattern 018 — Burrata/féta + élément grillé sucré-acide + herbes

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : burrata raisins grillés au basilic ; et adaptations féta + fruits/légumes grillés
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Entrée minimaliste mais à fort impact visuel et gustatif : un fromage frais lacté, un élément grillé qui caramélise, des herbes qui réveillent.

### Structure
- base : fromage frais lacté, à température ambiante (burrata, mozzarella, féta, ricotta)
- transformation : un élément (fruit ou légume) grillé/rôti rapidement avec marinade aigre-douce
- sauce / liant : jus rendus de l'élément grillé + huile d'olive de finition
- contraste : herbes fraîches + parfois épice grillée (fenouil, cumin)
- finition : sel en flocons, poivre frais, filet d'huile fruitée
- texture : noix grillées en option (pignons, amandes, pistaches)

### Logique de goût
- salé : sel en flocons
- gras : fromage + huile
- acide : vinaigre dans la marinade + jus naturel du fruit
- sucré : sucre brun ou miel dans la marinade + caramélisation
- amer : option (zeste, roquette autour)
- umami : fromage affiné en option
- aromatique : basilic, menthe, origan ; graines de fenouil, cardamome

### Pattern réutilisable

```text
fromage frais lacté + fruit/légume grillé brièvement avec vinaigre+sucre+épice + jus rendus + huile d'olive + herbes + sel en flocons
```

### Variantes
- bases : burrata, mozzarella di bufala, féta, ricotta fraîche, stracciatella, labneh
- éléments grillés : raisins en brochettes, figues coupées, prunes, abricots, tomates cerises, poivrons rôtis, asperges, pêches
- aromates dans la marinade : balsamique, vinaigre de Xérès, miel, sucre roux, graines de fenouil, cardamome, romarin
- herbes : basilic (vert ou rouge), menthe, origan, thym, estragon
- noix optionnelles : pignons, pistaches, amandes effilées
- protéines compatibles : prosciutto, jambon serrano, anchois en option
- version simple : burrata + tomates cerises grillées + basilic + huile + sel
- version festive : burrata triple + raisins grillés + figues grillées + basilic rouge + pignons + balsamique vieux

### Points critiques
- fromage **à température ambiante** 30 min avant service
- élément grillé chaud à tiède, **jamais froid**
- ne pas mélanger : composer le plat
- huile fruitée de qualité — c'est elle qui parfume tout
- sel en flocons sur le fromage juste avant service

### Erreurs fréquentes
- fromage froid frigo → texture caoutchouteuse
- élément grillé refroidi → plat plat
- huile bas de gamme → tout retombe
- mélanger → perd l'effet de composition

### Repères sensoriels
- contraste blanc lacté / coloration grillée
- fromage qui se "casse" tendrement à la cuillère
- huile parfumée distincte au nez

### Usage Gemini
- proposer quand : "entrée pour recevoir, simple mais wow", "fromage de qualité à valoriser", "fruits de saison à mettre en avant"
- éviter quand : pas de fromage frais de qualité, allergie lactose
- adaptation rapide : 10 min, totalement modulaire selon ce qu'on a

---

## Pattern 019 — Sauce yaourt aromatisée [pattern outil]

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : sauce yaourt sumac ; yaourt cari ; yaourt citron confit ; yaourt lime cumin ; nombreuses autres
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Pattern outil : sauce universelle qui transforme un plat en plat Ottolenghi. À combiner avec n'importe quelle base rôtie, grillée, frite, ou crue.

### Structure
- base : yaourt grec **épais** (ou labneh)
- transformation : aucune, juste mélange à froid
- sauce / liant : c'est la sauce elle-même
- contraste : —
- finition : un filet d'huile + une herbe en surface
- texture : —

### Logique de goût
- salé : sel obligatoire
- gras : yaourt entier (pas allégé)
- acide : citron + acidité naturelle yaourt
- sucré : —
- amer : option (zeste râpé fin)
- umami : option (anchois broyé pour version "ranch revisité")
- aromatique : 1 épice dominante + 1 herbe + 1 zeste

### Pattern réutilisable

```text
yaourt grec + sel + jus citron/lime + 1 épice (sumac, cumin grillé, cari, harissa) + 1 zeste + 1 herbe ciselée + filet d'huile en service
```

### Variantes
- yaourt-sumac-zeste citron-menthe
- yaourt-cumin grillé-jus citron-coriandre
- yaourt-cari-curcuma-jus lime-menthe
- yaourt-citron confit haché-zeste-aneth
- yaourt-harissa-jus citron-coriandre
- yaourt-ail-zaatar-huile
- yaourt-mayo-cari (version chou-fleur rôti)
- yaourt-tahini-citron-ail (version mêlée)

### Points critiques
- ne pas saler trop tôt si on attend longtemps (yaourt rendrait de l'eau)
- presser l'ail finement, ne pas hacher (texture désagréable)
- griller les épices à sec puis les broyer pour libérer les arômes
- consistance cible : nappe la cuillère, ne coule pas trop vite
- le repos 10-30 min améliore la sauce (les saveurs fusionnent)

### Erreurs fréquentes
- sel trop tôt → yaourt rend l'eau
- ail haché grossier → texture désagréable
- épices non grillées → arômes en surface
- pas assez d'acide → sauce plate

### Repères sensoriels
- couleur unie tirant légèrement vers la couleur de l'épice dominante
- texture lisse, pas grumeleuse
- équilibre acide-sel ressenti à la première cuillère

### Usage Gemini
- proposer quand : "j'ai du yaourt, comment l'utiliser autrement que nature", "sauce rapide pour légume rôti"
- éviter quand : intolérance lactose (basculer vers tahini équivalent)
- adaptation rapide : 3 min de préparation, un mois d'inspiration

---

## Pattern 020 — Sauce tahini éclaircie [pattern outil]

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : sauce tahini classique ; sauce tahini à l'ail ; sauce tahini aux herbes ; sauce tahini sur siniyah
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Pattern outil : la sauce signature Ottolenghi. Une fois maîtrisée, elle se décline en mille variantes et porte presque n'importe quel plat de légume.

### Structure
- base : tahini de qualité (coulant, pas sec)
- transformation : émulsion à froid avec citron + ail + eau, dans cet ordre
- sauce / liant : sauce indépendante, à servir froide ou tiède, jamais chaude
- contraste : —
- finition : huile, herbes, sumac, ou graines de sésame en surface
- texture : —

### Logique de goût
- salé : obligatoire
- gras : tahini lui-même
- acide : citron généreux
- sucré : —
- amer : naturel du tahini, équilibré par le citron
- umami : —
- aromatique : ail dominant ; option : cumin grillé, herbes hachées

### Pattern réutilisable

```text
tahini + jus citron généreux + ail pressé + sel → mélanger (la sauce se solidifie, c'est normal) → ajouter de l'eau froide en filet en fouettant jusqu'à consistance crème
```

### Variantes
- tahini-citron-ail (base universelle)
- tahini-citron-ail-cumin grillé
- tahini-citron-ail-harissa
- tahini + yaourt mêlés (50/50, plus léger)
- tahini-citron-ail-herbes mixées (persil, coriandre, menthe au robot) → "sauce verte tahini"
- tahini-miso (version umami)
- tahini-mélasse de grenade (version sucré-salé)

### Points critiques
- **toujours dans cet ordre** : tahini + citron + ail + sel → mélanger → eau ensuite
- la sauce se "casse" et se solidifie quand on ajoute le citron — c'est normal
- consistance cible : ruban qui tombe lentement de la cuillère
- goûter et ajuster : presque toujours +sel +acide
- ne pas chauffer (devient amère)

### Erreurs fréquentes
- eau ajoutée avant citron → mauvaise émulsion
- tahini rance → ruine tout
- sauce pas assez salée/acide → plate
- sauce chauffée → amère

### Repères sensoriels
- couleur crème homogène
- texture qui nappe sans figer
- goût équilibré : ni trop pâteux, ni trop liquide

### Usage Gemini
- proposer quand : "j'ai du tahini, quoi en faire", besoin d'une alternative végan au yaourt, plat moyen-oriental
- éviter quand : tahini de mauvaise qualité (rance, sec)
- adaptation rapide : 2 minutes ; une fois faite, se garde 3-4 jours au frigo

---

## Pattern 021 — Macération aigre-douce d'oignon ou échalote [pattern outil]

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : échalote-sumac-vinaigre ; oignon rouge mariné ; technique présente dans une majorité des salades du livre
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Pattern outil omniprésent : enlève l'agressivité de l'oignon cru, le rend tendre, légèrement sucré, et apporte une note acide dans le plat final.

### Structure
- base : oignon rouge ou échalote, tranché très finement
- transformation : massé avec sel + acide + parfois sucre + parfois épice
- sauce / liant : —
- contraste : —
- finition : —
- texture : —

### Logique de goût
- salé : sel
- gras : —
- acide : vinaigre ou jus d'agrume
- sucré : option (pincée de sucre, surtout avec vinaigre)
- amer : —
- umami : —
- aromatique : sumac, graines de moutarde, piment broyé

### Pattern réutilisable

```text
oignon/échalote tranché très fin + sel + acide (vinaigre ou jus citron) + (sucre + épice optionnels) → masser → laisser 15-30 min minimum
```

### Variantes
- échalote + sumac + vinaigre de vin blanc + sel
- oignon rouge + jus de citron + sel
- échalote + jus de citron + sucre + sel (pour tartare)
- oignon rouge + vinaigre de cidre + sucre + graines de moutarde
- oignon + jus de lime + piment broyé (style mexicain)

### Points critiques
- **trancher très finement**
- masser physiquement avec les doigts, pas seulement remuer
- 15 min minimum, 30 min idéalement, quelques heures sans problème
- si le liquide est très coloré : option de jeter ou d'utiliser

### Erreurs fréquentes
- tranches trop épaisses → reste cru
- pas assez longtemps → encore agressif
- pas massé → infusion irrégulière

### Repères sensoriels
- oignon translucide et un peu mou
- couleur passée vers rose pâle ou rouge éclatant
- saveur arrondie, ne fait plus pleurer

### Usage Gemini
- proposer quand : "salade qui contient de l'oignon cru", "tartare", "tacos", "garniture vive"
- éviter quand : —
- adaptation rapide : geste de 30 secondes, fait à l'avance pendant le reste de la cuisine

---

## Pattern 022 — Huile aromatique infusée [pattern outil]

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : huile ail-piment-gingembre des tomates grillées ; huile aux anchois ; huile aromatique de plaque
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Pattern outil : transformer une huile en condiment puissant. S'utilise comme finition de plat, base de vinaigrette, ou élément à part entière.

### Structure
- base : huile d'olive (ou neutre selon registre culinaire)
- transformation : aromates infusés à feu doux
- sauce / liant : c'est l'huile elle-même qui est la sauce
- contraste : —
- finition : —
- texture : optionnel — les aromates restés croquants servent de garniture

### Logique de goût
- salé : option (anchois, sel)
- gras : huile en quantité
- acide : —
- sucré : —
- amer : —
- umami : option (anchois, ail confit)
- aromatique : ail, piment, gingembre, herbes, zestes, épices entières

### Pattern réutilisable

```text
huile + aromates choisis + chaleur douce contrôlée → ail et aromates pas brûlés mais juste dorés → réserver l'huile + les aromates séparément pour usage final
```

### Variantes
- huile-ail-piment-gingembre-tiges de coriandre (asiatique-MO)
- huile-anchois-ail-piment broyé (méditerranéenne)
- huile-thym-ail-zeste citron (italienne)
- huile-cumin-graines (épicée)
- huile-curry-curcuma-feuilles de cari (indienne)
- huile-romarin-ail-piment (arrosage de pizza)

### Points critiques
- feu **doux**, jamais vif : l'ail brûle et devient amer en quelques secondes
- retirer les aromates à l'écumoire dès la coloration
- l'huile s'utilise tiède ou refroidie
- conserver 3-4 jours au frigo, ramener à température avant usage
- ne pas utiliser une huile rance

### Erreurs fréquentes
- feu trop vif → ail brûle, huile amère
- aromates oubliés dans l'huile chaude → continuent à cuire et noircissent
- huile rance → défaut amplifié

### Repères sensoriels
- aromates juste dorés, pas bruns
- huile colorée mais pas fumante
- arôme dégagé sans piquant chimique

### Usage Gemini
- proposer quand : "comment finir un plat", "rendre une tomate ou un avocat exceptionnels", "vinaigrette qui a du caractère"
- éviter quand : —
- adaptation rapide : 5 min de préparation, garde 3 jours, transforme tout

---

## Pattern 023 — Fruits rôtis + base laitière épaisse + herbe inattendue [dessert]

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : fraises rôties au sumac et yogourt épaissi ; friand prunes-mûres-laurier ; clafoutis figues-thym
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Dessert qui ne tombe pas dans le sucre : un fruit rôti qui révèle son acide, une base laitière qui apaise, et une herbe ou épice salée qui surprend.

### Structure
- base : fruit de saison (fraise, prune, figue, mûre, raisin, abricot, pêche)
- transformation : rôti court à four chaud avec sucre + acide + herbe inattendue
- sauce / liant : jus de cuisson sirupeux récupéré
- contraste : base laitière froide ou tiède (yaourt épaissi, mascarpone, crème fraîche, glace vanille)
- finition : herbes fraîches en surface (menthe, basilic, thym frais)
- texture : option : crumble, biscuit émietté, granola, amandes effilées

### Logique de goût
- salé : pincée de sel équilibre
- gras : base laitière
- acide : sumac, citron, vinaigre balsamique, vin rouge
- sucré : modéré (cassonade, miel, sucre muscovado)
- amer : zeste éventuel
- umami : —
- aromatique : laurier, thym, romarin, basilic, menthe, gousse de vanille, cardamome

### Pattern réutilisable

```text
fruit de saison + sucre brun + acide (citron/vinaigre) + herbe ou épice surprise → rôti court → jus récupéré → servi sur base laitière épaisse + herbes fraîches
```

### Variantes
- bases laitières : yaourt grec égoutté, mascarpone, crème fraîche, ricotta sucrée, glace vanille
- fruits : fraises (sumac), prunes (laurier), figues (thym), pêches (cardamome), raisins (romarin), abricots (lavande), cerises (balsamique)
- liquides de rôtissage : eau, vin rouge, vin doux, jus d'agrume
- épices/herbes : laurier, thym, romarin, vanille, cardamome, sumac, poivre noir, gingembre
- toppings : crumble d'amandes, granola, sablés émiettés, brisures de meringue
- version simple : fraises + sucre + jus citron + thym + yaourt grec + miel
- version festive : 3 fruits rôtis + mascarpone + sablés + 3 herbes + filet de jus réservé

### Points critiques
- ne pas trop cuire le fruit (il doit garder forme, pas devenir purée)
- récupérer le jus, le filtrer, le réserver — c'est le sirop final
- l'herbe ou épice "surprise" doit être discrète, jamais dominer
- base laitière vraiment froide si fruit chaud (contraste)
- sucrer modérément — le but n'est pas une confiture

### Erreurs fréquentes
- fruit trop cuit → purée sans tenue
- jus jeté → on perd le sirop
- herbe trop forte → masque le fruit
- trop sucré → confiture

### Repères sensoriels
- fruit qui a libéré son jus mais garde sa forme
- jus sirupeux qui colore l'assiette
- herbe verte en éclat sur fond rouge/violet

### Usage Gemini
- proposer quand : "dessert simple mais qui sort du lot", "fruits de saison à utiliser", "dessert sans pâtisserie compliquée"
- éviter quand : pas de four, fruits hors saison
- adaptation rapide : 15 min au four, base laitière en 30 secondes, dressage minute

---

## Pattern 024 — Gâteau moelleux amande-citron + fruit en garniture

### Source
- auteur : Yotam Ottolenghi
- livre : SIMPLE
- recettes sources : pain-gâteau bleuets-amandes-citron ; friand prunes-mûres
- origine consolidation : Claude V1
- statut : pattern extrait, pas recette copiée

### Intention
Gâteau accessible mais sophistiqué : moelleux dû à la poudre d'amandes, parfum dû au zeste, fruit qui éclate en bouche, glaçage citronné.

### Structure
- base : pâte à base de poudre d'amandes + farine en complément + beurre + sucre + œufs
- transformation : cuisson moule à cake ou plat carré, four moyen
- sauce / liant : glaçage simple sucre glace + jus de citron
- contraste : fruit acidulé en cours de cuisson (bleuets, framboises, prunes)
- finition : zeste râpé en surface
- texture : moelleux dense de l'amande, croquant léger du glaçage figé

### Logique de goût
- salé : pincée de sel dans la pâte
- gras : beurre + amande
- acide : citron (zeste + jus dans le glaçage) + fruit
- sucré : modéré, sucre glace dominant
- amer : zeste
- umami : —
- aromatique : zeste citron, vanille, parfois fleur d'oranger ou cardamome

### Pattern réutilisable

```text
pâte amandes-farine-beurre-sucre-œufs + zeste agrume + fruit acidulé en cours de cuisson + glaçage sucre glace + jus citron
```

### Variantes
- bases : amande pure (style friand), amande + farine, amande + farine de riz pour version sans gluten
- agrumes : citron, lime, orange sanguine, bergamote
- fruits ajoutés : bleuets, framboises, prunes, mûres, cerises, pommes, abricots
- aromates : vanille, fleur d'oranger, cardamome, laurier infusé, thym
- toppings : amandes effilées sur le dessus, sucre demerara, glaçage citron
- version simple : pâte amande-citron + bleuets + glaçage citron
- version festive : pâte amande-fleur d'oranger + 3 fruits + amandes effilées + 2 glaçages

### Points critiques
- amandes finement moulues, pas grossières (texture sableuse autrement)
- ne pas trop battre la pâte une fois la farine ajoutée
- ajouter une partie des fruits **après** un premier temps de cuisson pour qu'ils ne coulent pas
- glaçage **après** refroidissement complet, sinon il fond
- conservation : 3 jours en boîte hermétique, le 2e jour est meilleur

### Erreurs fréquentes
- amandes grossières → texture sableuse
- fruit lourd dès le départ → coule au fond
- glaçage sur gâteau chaud → fond
- pâte trop battue → caoutchouteuse

### Repères sensoriels
- doré franc, pas pâle
- cure-dent qui ressort propre mais le gâteau légèrement humide
- arôme citron qui domine
- glaçage figé brillant

### Usage Gemini
- proposer quand : "gâteau de week-end facile", "fruits de saison à valoriser", "dessert qui voyage bien"
- éviter quand : allergie aux noix, version sans matière grasse
- adaptation rapide : pâte en 10 min, cuisson 40-45 min, glaçage minute

---
