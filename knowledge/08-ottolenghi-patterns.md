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

---

## CUISINES DU MONDE — patterns essentiels (format compact)

> Ces patterns couvrent les registres asiatique, américain et britannique. Format délibérément allégé : formule + variantes + points critiques + déclencheurs Gemini. Même logique de base (formule réutilisable, points de vigilance, usage contextuel).

---

## Pattern 025 — Wok stir-fry : protéine + légumes + sauce soja-huître

**Registre** : cuisine asiatique (chinoise, thaï, coréenne)
**Intention** : cuisson ultra-rapide à feu maximal — la chaleur extrême crée le "wok hei" (goût de brûlé contrôlé), la sauce enrobe sans détremper.

### Pattern réutilisable

```text
protéine marinée (soja + fécule + huile) → wok fumant + huile neutre → saisir protéine → réserver → aromatics (ail + gingembre + oignon) → légumes durs puis tendres → sauce (soja + huître + sésame + sucre + fécule diluée) → remettre protéine → sortir du feu
```

### Variantes clés
- protéines : bœuf tranché fin, poulet, crevettes, tofu ferme, porc
- légumes : poivrons, brocoli, pak choï, champignons, courgettes, carottes en julienne
- sauce de base : soja + sauce huître + sésame + sucre + maïzena diluée dans eau froide
- variante thaï : soja + nuoc-mâm + sucre palm + piment + basilic thaï
- variante coréenne : gochujang + soja + sésame + ail + gingembre
- service : riz vapeur ou nouilles sautées

### Points critiques
- wok **vraiment fumant** avant d'ajouter l'huile — si la protéine colle, la T° est insuffisante
- **ne pas surcharger** le wok (cuire en deux fois si besoin) — sinon vapeur, pas de saisie
- la maïzena dans la marinade protège la protéine et lie la sauce
- la sauce se prépare **avant** de commencer (tout va vite ensuite)
- finir au sésame et ciboulette hors feu

### Usage Gemini
- proposer quand : "j'ai du bœuf/poulet et des légumes à passer", "wok", "cuisine asiatique rapide", "sauté de légumes"
- éviter quand : feu induction trop faible, légumes très fragiles (épinards → les ajouter en toute dernière seconde)

---

## Pattern 026 — Curry maison : base aromatique + lait de coco ou tomate + protéine

**Registre** : Inde du Sud, Thaïlande, Grande-Bretagne (curry britannique)
**Intention** : un plat qui sent les épices depuis l'entrée — la base aromatique frite dans l'huile est la clé ; tout le reste suit.

### Pattern réutilisable

```text
oignons longuement fondus + ail + gingembre → épices grillées dans l'huile (ne pas brûler) → tomates concassées OU pâte de curry → cuire 5-8 min jusqu'à pâte homogène → ajouter protéine → mouiller lait de coco ou bouillon → mijoter à couvert → finir coriandre + jus citron/lime
```

### Variantes clés
- curry du Nord (sauce tomate + yaourt) : poulet tikka masala, korma, butter chicken
- curry du Sud (lait de coco) : curry de crevettes, dal de lentilles corail coco
- curry thaï : pâte curry rouge/vert prête + lait de coco + nuoc-mâm + basilic thaï
- curry britannique "friday night" : sauce onctueuse + poulet + riz basmati + naan
- légumineuses : dal de lentilles + curcuma + cumin + coriandre + gingembre + lait de coco
- épices de base incontournables : curcuma, cumin, coriandre moulue, garam masala, piment

### Points critiques
- faire revenir les épices dans l'huile **avant** d'ajouter tout liquide — 30-60 secondes, ça chauffe vite
- cuire la pâte tomate/ail/gingembre jusqu'à ce qu'elle se détache des parois (la "tarka" est prête)
- ne pas sous-saler — un curry fade est souvent un curry mal salé
- finition acide obligatoire (citron ou lime) pour "lever" l'ensemble hors feu

### Usage Gemini
- proposer quand : "envie de curry", "j'ai du lait de coco", "plat indien/thaï", "recette réconfortante épicée"
- éviter quand : intolérance aux épices, besoin de rapide < 20 min (les oignons seuls prennent 15 min)

---

## Pattern 027 — Teriyaki et glazes asiatiques sucrés-salés

**Registre** : Japon, Asie de l'Est
**Intention** : laque brillante sur une protéine — le sucre caramélise en fin de cuisson et crée une croûte sirupeuse qui concentre les saveurs.

### Pattern réutilisable

```text
protéine sèche (saumon, poulet, bœuf, tofu) → saisir côté peau/présentation → sauce teriyaki (soja + mirin + saké + sucre) versée en fin → faire réduire en laquant la pièce → retourner une fois → servir avec riz vapeur + pickles rapides
```

### Variantes clés
- teriyaki classique : soja + mirin + saké + sucre (ratio 2:2:2:1)
- version sans saké : soja + miel + vinaigre de riz + ail + gingembre
- glaçage miso : miso blanc + mirin + sucre → idéal pour saumon ou aubergine
- glaçage gochujang : pâte coréenne + soja + miel + sésame → poulet ou côtes de porc
- accompagnements systématiques : riz vinaigré, concombre au sel, gingembre mariné, sésame

### Points critiques
- la sauce réduit très vite une fois dans la poêle — surveiller sans quitter
- protéine **très sèche** en surface avant cuisson (sinon pas de croûte)
- ajouter la sauce **en fin** de cuisson, pas au début (brûle sinon)
- le sucre dans la sauce crée la laque — ne pas réduire trop fort (amer)

### Usage Gemini
- proposer quand : "j'ai du saumon / du poulet et de la sauce soja", "envie de japonais", "glaçage sucré-salé"
- éviter quand : sans sucre, sans soja

---

## Pattern 028 — Bol de nouilles : bouillon ou sauce + nouilles + garnitures fraîches

**Registre** : Vietnam (pho, bún bò), Japon (ramen, soba), Thaïlande
**Intention** : le bol comme plat complet — la profondeur est dans le bouillon ou la sauce, la fraîcheur dans les garnitures ajoutées minute.

### Pattern réutilisable

```text
BOUILLON : base aromatique longuement mijotée (os + épices + gingembre + oignons brûlés) → filtrer → assaisonner nuoc-mâm/soja/sel
OU SAUCE FROIDE : soja + sésame + vinaigre + chili + ail + gingembre mixés
→ nouilles cuites séparément, égouttées → bol : bouillon ou sauce + nouilles + protéine tranchée fine + garnitures fraîches
```

### Variantes clés
- pho vietnamien : bouillon bœuf + anis étoilé + cannelle + gingembre brûlé + nuoc-mâm → bœuf cru tranché fin + herbes fraîches (menthe, basilic thaï, coriandre) + germes de soja + citron vert + piment
- ramen simplifié : bouillon poulet ou miso + œuf mollet mariné + porc effiloché + algues + maïs
- soba froid (été) : sauce tsuyu (soja + dashi + mirin) + soba froides + ciboulette + gingembre + sésame
- version express 30 min : bouillon cube + pâte de miso + nouilles + œuf mollet + légumes vapeur + gingembre

### Points critiques
- les garnitures fraîches se préparent et s'ajoutent **à la commande** — jamais dans le bouillon
- les nouilles se cuisent séparément pour ne pas troubler le bouillon
- finition acide (citron vert) obligatoire au service
- un pho express compense le temps court par plus d'épices grillées (anis, cannelle, badiane)

### Usage Gemini
- proposer quand : "envie de soupe asiatique", "bouillon de reste", "pho/ramen maison", "repas hivernal réconfortant"
- éviter quand : très peu de temps (sauf version express), intolérance gluten (adapter avec nouilles de riz)

---

## Pattern 029 — Riz sauté : riz de veille + œufs + aromatics + soja

**Registre** : Chine, Thaïlande, Japon, Corée
**Intention** : transformer des restes de riz en plat à part entière — le riz doit être sec et froid pour éviter la bouillie.

### Pattern réutilisable

```text
wok très chaud + huile → ail + gingembre (10 sec) → légumes durs → riz FROID égrené à la main → étaler et laisser croûter 30 sec sans toucher → œufs battus versés sur le riz → mélanger → soja + sésame → ciboulette ou oignon vert → servir immédiatement
```

### Variantes clés
- riz sauté cantonais : riz + œufs + crevettes + petits pois + soja + sésame + gingembre
- kimchi bokkeumbap : riz + kimchi + porc effiloché + œuf au plat dessus + gochujang + sésame
- chahan japonais : riz + œufs + jambon/bacon + ciboulette + soja + beurre
- version végé : riz + tofu ferme émietté + légumes variés + soja + nuoc-mâm

### Points critiques
- riz **impérativement** cuit la veille et réfrigéré — riz chaud = bouillie
- égrener le riz à la main avant d'aller au wok
- cuire sans toucher d'abord pour créer la croûte, mélanger ensuite
- saler uniquement avec soja ou nuoc-mâm, pas de sel seul

### Usage Gemini
- proposer quand : "reste de riz", "j'ai des œufs et du riz cuit", "riz sauté", "vide-frigo asiatique"
- éviter quand : riz fraîchement cuit (attendre 2h minimum au frigo)

---

## Pattern 030 — BBQ / pulled : cuisson longue + rub sec + sauce acide

**Registre** : Amérique du Nord (barbecue du Sud, Texas, Kansas City)
**Intention** : la viande fait tout le travail au temps — patience + feu doux = fibres qui se défont, croûte qui croustille, sauce qui contre-balance le gras.

### Pattern réutilisable

```text
rub sec appliqué 12-24h avant (sel + sucre brun + paprika fumé + cumin + ail poudre + poivre + piment) → cuisson four bas (130-150°C) 4-6h couvert → découvrir 30 min pour croûte → effilocher à la fourchette → sauce BBQ acide à côté → pain brioché ou polenta + coleslaw
```

### Variantes clés
- pulled pork : épaule de porc 6h → sauce BBQ (ketchup + vinaigre + miel + Worcestershire + piment fumé)
- ribs : rub + 3h four couvert + 30 min glaçage découvert
- poulet BBQ : cuisses + rub léger + 200°C + glaçage sauce en fin de cuisson
- coleslaw incontournable : chou + carottes + mayo + vinaigre de cidre + sucre + céleri sel
- version express cocotte : 2h à 160°C, moins de croûte mais même effilochage

### Points critiques
- **T° basse et longue** est le principe — ne pas chercher à aller vite
- rub appliqué la veille (pénètre mieux)
- effilocher uniquement quand la viande se défait sans résistance à la fourchette
- la sauce BBQ se sert **à part** — ne jamais noyer la viande avant service

### Usage Gemini
- proposer quand : "épaule de porc", "pulled pork", "BBQ maison", "plat festif pour beaucoup"
- éviter quand : moins de 3h disponibles, viande tendre de 1ère catégorie

---

## Pattern 031 — Roast Sunday : rôti + jus de cuisson + légumes rôtis + purée

**Registre** : cuisine britannique, irlandaise
**Intention** : architecture du repas dominical — chaque élément cuit séparément, le jus unifie l'assiette.

### Pattern réutilisable

```text
rôti assaisonné → four très chaud (saisie 15 min) → baisser T° → cuire jusqu'à T° à cœur → repos obligatoire 20-30 min → jus de plat (sucs déglaçés + bouillon réduit) → pommes de terre rôties dans graisse très chaude → légumes racines rôtis → purée beurrée → dresser
```

### Variantes clés
- agneau : gigot ou épaule + ail + romarin → mint sauce (menthe + vinaigre + sucre)
- bœuf : contre-filet + moutarde en croûte → jus + raifort râpé
- poulet : beurre sous la peau + citron + thym → jus du plat
- légumes systématiques : pommes de terre rôties (graisse de canard ou saindoux), panais, carottes, choux de Bruxelles
- sauce au pain (bread sauce) : accompagnement classique du poulet rôti britannique

### Points critiques
- les pommes de terre rôties veulent de la graisse **très chaude** pour croustiller (préchauffer la plaque avec la graisse)
- le jus de plat : bien dégraisser, bien réduire — c'est l'âme du roast
- **timing** : le rôti se repose 20-30 min → c'est ce temps-là qu'on utilise pour finir légumes et purée

### Usage Gemini
- proposer quand : "rôti du dimanche", "gigot/poulet/bœuf entier", "repas familial d'hiver", "cuisine britannique"
- éviter quand : peu de temps, repas léger, pas de four

---

## Pattern 032 — Pie à croûte de purée : shepherd's pie, cottage pie, hachis parmentier

**Registre** : cuisine britannique, irlandaise, française
**Intention** : deux couches — un ragoût fondant, une croûte de purée qui gratine. Se prépare à l'avance et passe au four au moment voulu.

### Pattern réutilisable

```text
oignon + ail + carotte fondus → viande hachée ou effilochée rissolée → tomate + bouillon + herbes + Worcestershire → mijoter 20-30 min → rectifier sel/poivre → verser en plat → couvrir purée épaisse beurrée (strié à la fourchette) → four 200°C 25-30 min jusqu'à croûte dorée
```

### Variantes clés
- shepherd's pie : agneau haché + romarin + petits pois + navet
- cottage pie : bœuf haché + thym + Worcestershire + champignons
- hachis parmentier : bœuf + tomate + vin rouge + gruyère sur la purée
- fish pie : poisson blanc + crevettes + œufs durs + béchamel + purée
- croûte sucrée-salée : patate douce + muscade à la place de pomme de terre classique

### Points critiques
- ragoût **bien réduit et assaisonné** avant d'assembler — la purée étouffe les défauts sans les corriger
- purée **épaisse** (sinon coule dans le ragoût) — beaucoup de beurre, pommes de terre bien égouttées
- strier la surface à la fourchette avant d'enfourner (crée plus de surface dorée)
- laisser reposer 5 min avant de servir

### Usage Gemini
- proposer quand : "shepherd's pie", "j'ai du haché", "plat hivernal réconfortant", "restes de viande à recycler"
- éviter quand : repas léger, peu de temps

---

## Pattern 033 — Burger : patty + sauce + empilage maîtrisé

**Registre** : Amérique du Nord, international
**Intention** : l'équilibre gras/acide/croquant/moelleux — chaque couche a un rôle précis dans la bouchée.

### Pattern réutilisable

```text
patty (viande 20% MG min, façonnée large et fine avec creux central) → poêle TRÈS chaude → saisie 2-3 min sans toucher → retourner → fromage fondu sous cloche → pain toasté côté intérieur → sauce sur pain → légumes croquants → patty → fermer
```

### Variantes clés
- sauce burger maison : mayo + ketchup + moutarde + cornichon haché + paprika fumé
- fromages : cheddar (fondant), mimolette, emmental, bleu (version premium)
- garnitures : laitue iceberg (croquant), tomate (acide), oignon caramélisé (sucré), pickles (acide), bacon
- smash burger : petite boule écrasée fort sur poêle très chaude → croûte Maillard maximale, bords croustillants
- version poisson : pavé de cabillaud pané + sauce tartare + chou rouge pickled

### Points critiques
- **20% matière grasse minimum** dans le haché — trop maigre = sec et sans goût
- ne jamais aplatir avec la spatule en cours de cuisson (sauf smash burger)
- **pain toasté** côté intérieur — empêche le détrempé
- la sauce va sur les deux moitiés de pain, pas directement sur la viande

### Usage Gemini
- proposer quand : "bœuf haché", "burger maison", "smash burger", "repas convivial décontracté"
- éviter quand : haché trop maigre, pas de poêle en fonte ou gril

---

## Pattern 034 — Mac & cheese et gratins de pâtes crémeux

**Registre** : cuisine américaine, européenne (gratin)
**Intention** : pâtes enrobées d'une béchamel fromagère avec croûte croustillante — le rapport sauce/pâtes est généreux, pas avare.

### Pattern réutilisable

```text
béchamel épaisse (beurre + farine + lait chaud) → fondre 2-3 fromages hors feu → assaisonner (moutarde, muscade, poivre de Cayenne) → mélanger pâtes cuites al dente égouttées → verser en plat → chapelure + parmesan + beurre en surface → four 200°C 20 min jusqu'à bulles et croûte dorée
```

### Variantes clés
- mac & cheese américain : cheddar fort + gruyère + macaroni + panko
- gratin dauphinois revisité : gruyère + comté + parmesan + pâtes ou macaroni
- add-ins : bacon croustillant, jalapeños, moutarde de Dijon dans la béchamel, paprika fumé
- version chic : gruyère + mozzarella + parmesan + pâtes fraîches + truffe râpée

### Points critiques
- ajouter le fromage **hors feu** — sinon la sauce graine
- béchamel bien cuite avant ajout du fromage (goût de farine crue sinon)
- pâtes cuites 2 min de moins qu'indiqué (finissent au four)
- ratio sauce/pâtes **généreux** — les pâtes absorbent au four

### Usage Gemini
- proposer quand : "gratin de macaroni", "mac and cheese", "fromage + pâtes", "repas réconfortant d'hiver"
- éviter quand : intolérance lactose, repas léger

---

## Pattern 035 — Poisson pané frit + sauce acide + frites

**Registre** : Grande-Bretagne (fish & chips), France (meunière/frite), international
**Intention** : panure qui bulle et croustille autour d'un poisson nacré — la sauce acide coupe le gras de la friture.

### Pattern réutilisable

```text
filet de poisson blanc séché + sel → farine → pâte à frire bière froide (farine + bière blonde + sel) OU panure anglaise (farine + œuf + chapelure) → friture 170-180°C jusqu'à dorure → égoutter sur papier → saler immédiatement → sauce tartare à côté
```

### Variantes clés
- pâte à bière (fish & chips) : farine + bière blonde très froide + sel → consistance pâte à crêpe épaisse
- panure anglaise : farine + œuf + chapelure (panko pour plus de croquant)
- sauce tartare : mayo + câpres + cornichons + ciboulette + citron
- mushy peas (accompagnement britannique) : petits pois + beurre + menthe + sel écrasés grossièrement
- poissons : cabillaud, aiglefin, merlan, lieu noir

### Points critiques
- **pâte à bière froide** (mettre la bière au congélateur 10 min) — le choc thermique crée les bulles
- poisson **très sec** avant panure — l'humidité fait décoller la panure
- frire par 2 filets max pour maintenir la T° de l'huile
- saler **immédiatement** à la sortie

### Usage Gemini
- proposer quand : "cabillaud/merlan", "fish and chips", "poisson frit maison", "bière froide + poisson"
- éviter quand : pas d'huile en quantité, poisson très fragile (sole → mieux à la meunière)

---

---

## Compléments issus des sources (enrichissement 2026-06)

_Patterns transposables, audités. Sources : Ottolenghi Simple, Plenty, Ducasse. Élagués : doublons absorbés par le corps (patterns 001-035)._

### data

**Accords fromage + fruit cru (no-cook, à dresser)**

Composer sans cuire, registre sucré juteux contre salé friable (complète le Pattern 018 burrata/grillé, ici tout cru) :
- Figues mûres + chèvre frais + roquette/basilic + vinaigrette mélasse de grenade.
- Poire ferme-acidulée (pas trop mûre) + chèvre affiné OU parmesan, sur crostini.
- Dattes Medjool + brebis salé (ou ricotta) + roquette + amandes grillées + grenade.
- Pastèque + féta + basilic + option oignon rouge fin + huile.
Repère figues : lourdes, un peu molles, parfum net, souvent fendues à la base.

### definition

**Citron/lime séchés de Perse**

Agrumes durcis iraniens, acidité vive + parfum unique :
- Mijotés/marinades : un entier perforé qui infuse, retiré avant service.
- Salades/assaisonnements : en poudre (durs comme pierre, moulin à épices puis tamiser).
- Poudre maison plus puissante que le commerce ; quelques cuillères suffisent.

### pattern

**Crème fouettée parfumée comme nappage salé (alternative au yaourt)**

Nappage frais pour poisson poêlé / entrée chic :
```text
crème 35% fouettée ferme + crème sure pliée dedans + jus aromatique (jus de gingembre pressé, zeste) + sel → souple → sous/à côté de la protéine + salsa croquante
```
Clés : presser le gingembre râpé pour extraire le JUS seul ; plier la crème sure délicatement (souple, pas ferme) ; contraste crème froide / poisson chaud peau croustillante ; se réfrigère jusqu'au service.

**Salade tiède protéine + légumes grillés poêle striée + vinaigrette vive**

Tout passé à la poêle striée brûlante (marques de grill, noirci), réuni tiède, lié par une vinaigrette acide-relevée. Contraste fumé/frais.
```text
légumes/fruits robustes (oignon en quartiers, maïs, tomates cerises) grillés SÉPARÉMENT à la poêle striée → protéine grillée en dernier (crevettes, calmar, bifteck) → réunir tiède → vinaigrette (gingembre + sriracha + huile + lime + pincée sucre) + herbe → mélanger délicatement
```
Clés : griller chaque ingrédient à part (cuissons différentes) ; chercher marques + noircissement ; assembler tiède (jamais brûlant ni froid frigo) ; vinaigrette préparable 2 j avant.
Variantes vinaigrette : soja-sésame-lime, citron-ail-piment.

**Mijoté fruit de mer (calmar/poulpe) + poivron + zeste orange** _(sous-cas du Pattern 015)_

Délta vs 015 = gestion texture céphalopode + zeste orange final :
```text
oignon + poivron rouge fondus → ail + épices chaudes (carvi, piment Jamaïque, laurier, thym) → calmar saisi court → pâte tomate + vin rouge → couvert, feu doux ~30 min jusqu'à tendreté → zeste d'orange à la toute fin
```
Clés : le calmar passe par une phase caoutchouteuse puis redevient tendre — ne pas s'arrêter trop tôt ; ajouter de l'eau si trop épais ; zeste hors feu ; meilleur 1-2 j après. Bases : calmar, poulpe, seiche.

**Barres au frigo chocolat (no-bake, vide-placard)**

```text
chocolats + beurre + sirop doré + pincée sel fondus au bain-marie → hors feu : biscuits cassés + noix concassées + fruits secs (option trempés alcool) → presser dans plat tapissé → frigo 2-3 h → couper, servir froid
```
Tout substituable : chocolats (noir 70%, aromatisés), biscuits (digestifs, spéculoos), noix, fruits secs.
Clés : bain-marie doux, fond du bol hors de l'eau ; garder un peu de noix en poudre pour le dessus ; bien presser (sinon friable) ; tient 1 semaine au frigo.

**Gâteau moelleux aux fruits déposés en surface (friand/clafoutis/crème sure)** _(complète le Pattern 024)_

Délta vs 024 = formats où les fruits sont posés dessus et le gâteau lève autour :
```text
fruits macérés court (sucre + vanille + épice/herbe : laurier, cannelle, thym) → pâte légère (friand : blancs montés + amandes moulues + peu de farine + beurre fondu ; OU clafoutis ; OU crème sure) → verser au plat → fruits + jus dessus → cuire jusqu'à doré et fruits bouillonnants
```
Clés : macérer 30 min MAX (sinon détrempe) ; alu si dore trop vite ; test "le dessus ne tremblote pas" (cure-dent ne ressort pas propre) ; gâteaux noix/amandes sèchent vite (1-2 j).
Fruits : prunes-mûres, figues, pêches-framboises, pommes, bleuets ; sucre demerara en surface pour croûte.

**Gazpacho vert / tarator (délta du Pattern 005 = corps pain + noix)**

Soupe froide verte plus dense qu'un gaspacho, onctuosité sans cuisson via pain + noix :
```text
verts crus (concombre + poivron vert + céleri) + épinard/basilic/persil + ail + piment vert + pain rassis + noix grillées + vinaigre Xérès + huile + yaourt + glaçons + sel → mixer lisse → ajuster eau
```
Clés : noix + pain = corps ; glaçons servent glacé et allègent ; croûtons huile-sel à part. Registre herbacé, texture nappante.

**Salade de tomates multi-textures (crues + rôties à degrés variés)**

Idée transférable : varier les cuissons d'un même légume crée de la profondeur sans ajouter d'ingrédients.
- certaines tomates CRUES (jus, fraîcheur)
- certaines rôties douces (~20 min/160°C, sucre brun + balsamique + huile)
- certaines rôties fort/court (~12 min/200°C)
→ réunir avec grain neutre (couscous, fregola, perles) + herbes multiples (origan, estragon, menthe) + ail + jus de rôtissage. Mélanger à la main, délicatement.

**Légume-coquille farci aux herbes (saler-égoutter d'abord)**

```text
légume évidé (tomate ferme, courgette) → SALER l'intérieur + retourner pour égoutter → farce : oignon + ail + olives fondus à l'huile, hors feu + panko + herbes (origan, persil, menthe) + câpres → remplir en dôme → four moyen jusqu'à tendre
```
Clés : saler/égoutter évite la farce détrempée ; panko HORS feu garde le croquant ; olives + câpres = sel/umami sans viande. Servir avec salade + chèvre.

**Mijoté légumineuse + acidité INTÉGRÉE dès le départ (tamarin)** _(nuance Patterns 007/015)_

Délta : l'acide est dans le plat dès le début, pas seulement en finition.
```text
légumineuse (pois chiches) + légume terreux/amer (blettes blanchies) + base oignon-graines (carvi, coriandre) + tomate + PÂTE DE TAMARIN diluée + sucre → mijoter ~30 min jusqu'à soupe épaisse
```
Servir sur riz, cratère central + yaourt + coriandre (+ option citron + piment à la fin).

**Beurre noisette aromatique versé sur légume rôti/grillé [outil de finition]**

```text
légume rôti/grillé → beurre fondu jusqu'à brun (noisette) avec amandes effilées OU câpres OU ail/épice → verser chaud → citron + herbe fraîche
```
Variantes : amandes + câpres frites + aneth (asperges) ; beurre noisette + ail/carvi + graines de courge + tahini (choux de Bruxelles) ; câpres frites seules.
Clés : de noisette à brûlé en quelques secondes ; câpres bien épongées (éclaboussent), cuites jusqu'à ouverture-croustillant ; servir aussitôt (le beurre fige). Sans lactose → huile d'olive chaude + aromates.

**Chorizo/charcuterie + légume-feuille braisé + citron confit + crème**

```text
chorizo/charcuterie + ail + paprika fumé saisis → retirer et réserver → vert braisé dans le gras parfumé (un peu d'eau, couvert puis découvert, tendre-croquant) → remettre charcuterie + citron confit haché + jus citron → hors feu, crème sure soulevée délicatement
```
Variantes : kale + chorizo + citron confit + crème sure ; bette/épinards + lardons + citron + crème. Service tapas ou avec grillé.
Clés : saisir la charcuterie d'abord puis braiser dans son gras ; feuilles tendres mais croquantes ; crème hors feu (ne tranche pas). Végé : le vert braisé + citron confit + crème tient seul.

**Glaçage aigre-doux épicé (harissa-miel) appliqué AVANT rôtissage [outil]**

Délta vs sauce ajoutée après : ici le glaçage cuit sur le légume et laque.
```text
bol : épice (cumin) + miel + harissa + beurre fondu + huile + sel → enrober → four très chaud jusqu'à doré mais croquant → finition fraîche après (grenade + coriandre + citron)
```
Variantes : carottes ; racines (panais, betterave) ; glaçage alt. paprika fumé + miel, ras-el-hanout + miel.
Clés : le miel caramélise ET peut brûler (surveiller, garder croquant) ; ne pas serrer sur la plaque ; finition fraîche obligatoire pour contraster.

**Sauce chraimeh : pâte d'épices frite + tomate + sucre + lime [outil condiment]**

Sauce piquante libyenne rouge, nappe poisson/légumes/tofu ; se conserve, se congèle.
```text
pâte : ail pressé + épices (paprika fort + carvi + cumin + cannelle) + huile → frire 1 min → pâte de tomate + sucre + jus de lime + sel → eau pour éclaircir → mijoter jusqu'à épaississement → y finir la protéine/le légume
```
Clés : frire la pâte d'épices+ail AVANT le liquide ; pincée de sucre obligatoire ; éclaircir à l'eau. Variantes : haricots verts + tofu doré ; poisson/poulet poché dedans ; trempette pain. Tient 1 sem. frigo / 1 mois congélo.

**Gratin de légume crémé épicé + croûte chapelure-fromage** _(distinct du Pattern 034, ici légume, sauce express sans béchamel)_

```text
légume à peine cuit vapeur (ferme) → sauce express : oignon fondu + épices (cumin/cari/moutarde/piment) + crème + fromage fondu jusqu'à léger épaississement → mêler le légume → couvrir chapelure + fromage + persil → four puis gril jusqu'à doré
```
Variantes : chou-fleur + cumin/cari/moutarde + cheddar vieilli. Préparable la veille jusqu'au four.
Clés : légume ferme (finit au four, pas de bouillie) ; sauce juste épaissie ; essuyer les parois (la crème brûle) ; surveiller sous le gril.

**Portobello farci fromage fondant**

```text
gros champignons pré-rôtis 15 min → farce sautée refroidie (oignon + céleri + tomates séchées + ail + parmesan + herbes) → garnir + tranches de fromage fondant → four jusqu'à fonte et champignon tendre
```
Clés : fromage jeune/gras qui fond lisse (taleggio, fontina, mozzarella, scamorza) — les très affinés (gruyère, vieux cheddar) grainent et deviennent huileux ; pré-rôtir pour évacuer l'eau ; saler la farce avec mesure si fromage salé. Farces alt. : duxelles ; épinards-ricotta ; chèvre-noix.

**Salade betterave + agrume + contraste salé**

Trio sucré-acide-salé net :
```text
betterave cuite en quartiers + segments d'agrume levés à vif (avec leur jus) + élément salé (olives noires OU chèvre/féta) + oignon rouge fin + herbe → vinaigrette légère (huile + vinaigre/fleur d'oranger) → mélanger peu
```
Variantes : agrumes (orange, sanguine, pamplemousse) ; salé (olives ridées, féta, chèvre, gorgonzola) ; feuille amère (trévise, endive, cresson) ; aromate (fleur d'oranger, carvi, aneth).
Clés : lever les segments à vif et garder le jus (= acide vinaigrette) ; cuire la betterave entière puis peler ; mélanger en dernier et peu (sinon tout vire au rose).

**Tempura de légumes (pâte à l'eau gazeuse) + trempette agrume**

```text
légumes en morceaux → roulés dans la fécule sèche (accroche) → pâte légère (fécule + farine levante + EAU GAZEUSE très froide + sel + huile) → friture à grésillement franc (pas brûlante) → égoutter, saler → trempette (agrume + herbe + piment + sucre + huile mixés)
```
Variantes légumes : topinambour, betterave, brocoli, chou-fleur, patate douce, carotte, poireau, panais. Trempette : lime-coriandre-cardamome-piment ; soja-gingembre-vinaigre de riz.
Clés : eau gazeuse très froide + pâte mélangée au dernier moment = légèreté ; pré-fécule sèche ; huile modérée (grésille sans brûler) ; petites quantités. (Pâte à bière → cf. Pattern 035.)

**Salade de riz tropicale (fruit + croquant)**

Inspiration SE-asiatique, double croquant :
```text
riz cuits froids (jasmin au basilic thaï + riz rouge) + fruit en dés (mangue) + poivron + herbes (basilic thaï, coriandre, menthe) + oignon vert + piment + lime + huile arachide → mélanger DÉLICATEMENT → cacahuètes + coco grillée + échalotes frites
```
Variantes : fruit (mangue, ananas, papaye verte) ; vinaigrette + trait de nuoc-mâm.
Clés : riz bien refroidi/étalé ; parfumer le jasmin à la cuisson (bouquet basilic thaï, retiré) ; mélanger délicat (fruit mûr se défait) ; croquant au dernier moment.

**Salade de grains tiède + huile d'herbes frites** _(délta vs 008/011 = huile d'herbes frites versée chaude)_

```text
quinoa + riz tièdes + légume rôti (patate douce) → huile chaude : ail doré 30 s + sauge/origan frits ~1 min, versée aussitôt sur les grains → menthe + oignon vert + jus citron + féta + acide poudré (citron séché de Perse / sumac)
```
Variantes : grains (quinoa+sauvage, boulgour, freekeh) ; légume (courge, betterave, chou-fleur) ; huile (ail + romarin / thym).
Clés : ail JUSTE doré (30 s) puis herbes ~1 min, verser tout de suite ; grains tièdes pour absorber ; mélanger délicat ; citron séché moulu = note unique (sinon sumac).

**Salade de pâtes + légume frit mariné à chaud + sauce d'herbes** _(délta vs 009/011 = légume frit puis mariné au vinaigre à chaud)_

```text
courgettes en tranches frites dorées → arrosées de vinaigre À CHAUD → pâtes courtes rincées froides → sauce mixée crue (basilic + persil + huile) + zeste citron + câpres + mozzarella déchirée + edamame → mélanger délicatement
```
Variantes : légume frit-mariné (courgette, aubergine, poivron) ; sauce (roquette-amande, menthe-pistache) ; ajouts (petits pois, burrata).
Clés : frire sans surcharger, retourner une fois, égoutter ; vinaigre à chaud (s'imprègne en refroidissant) ; rincer les pâtes froides ; mozzarella + basilic en tout dernier.

**Polenta de maïs frais + sauce**

« Polenta » soyeuse de MAÏS FRAIS mixé (pas de semoule) :
```text
maïs frais cuit ~12 min → mixé LONGUEMENT (casser les peaux) avec un peu de son eau → recuit en remuant jusqu'à purée → beurre + féta + sel, 2 min → lit, sauce chaude au centre (aubergine frite + concentré + tomate + origan)
```
Variantes : enrichissement (beurre + féta / parmesan / crème) ; sauce (aubergine-tomate, champignons, ragoût épicé). Strictement maïs frais en saison.
Clés : mixer longtemps (texture lisse) ; réserver l'eau de cuisson ; assumer plus mou qu'une polenta de semoule.

**Salade fruit poché + bleu doux + noix**

Fruit ferme poché en sirop épicé, posé sur feuilles amères ; le sirop sert aussi de vinaigrette.
```text
fruit ferme poché à couvert four doux (eau + sucre + vin + zeste orange + laurier + poivre + jus citron) jusqu'à tendre → feuilles amères + bleu doux en éclats + pistaches → vinaigrette : moutarde + vinaigre + huile + qq c. du sirop
```
Variantes : fruit (coing ~2 h, poire ferme, pomme, prune) ; bleu (gorgonzola doux, roquefort, stilton) ; feuilles (mizuna, pissenlit, cresson, trévise) ; noix. Sirop restant → nappe une glace vanille.
Clés : pocher à couvert jusqu'à tendreté complète (coing long) ; garder peaux + cœurs dans le sirop (couleur + pectine) ; cuillère de sirop dans la vinaigrette ; fromage en éclats à la main.

**Crostini fruit grillé + fromage** _(format chaud, distinct de l'accord cru et du Pattern 017)_

```text
pain épais badigeonné de pâte mixée (pignons + ail + huile + sel) → grillé → fruit FERME tranché, sucré-citronné, marqué au gril → chèvre/parmesan en lamelles → four bref 3-4 min (fondre à peine) → poivre + huile + cerfeuil
```
Variantes : fruit (poire mi-mûre, figue, pomme, raisin fermes) ; fromage (chèvre affiné, parmesan, gorgonzola) ; pâte du pain (pignons/noix/ail) ; pain (levain épais, ciabatta).
Clés : fruit FERME (mûr → bouillie au gril) ; marquer juste pour les rayures ; passage four bref (pain + fruit + fromage restent distincts).

**Garniture sautée croustillante « minute » sur grain/riz/nouilles [outil]**

Délta vs 022 (huile infusée) : garniture frite-minute versée brûlante, croquant + parfum.
```text
huile arachide chaude + aromates en julienne (gingembre + ail + piment) saisis 3-4 min jusqu'à dorer → herbes en tronçons + noix/arachides + sésame + sel → 1-2 min → verser brûlant sur le grain
```
Variantes : gingembre-ail-piment-coriandre-arachides-sésame (thaï) ; gingembre-oignon vert-piment-cacahuète (riz nature) ; cumin + amandes au beurre noisette (MO).
Clés : tout couper AVANT d'allumer (ça va vite) ; aromates dorés pas brûlés ; verser aussitôt sur grain chaud ; quartier de lime à table.

## Pattern — Pâtes sauce tomate mijotée longue + finition lactée + herbe

### Intention
Pâtes de placard mais profondes : une sauce tomate qui a vraiment cuit, relevée d'un levier salé-épicé, adoucie en finition par yaourt ou fromage. (Distinct du pattern pâtes-huile-infusée du corps : ici la profondeur vient du temps de réduction.)

### Pattern réutilisable
```text
ail/oignon dans l'huile + levier salé-épicé (harissa OU olives+câpres OU piment fumé) + tomates (cerises ou boîte) + pincée de sucre → mijoter jusqu'à épaississement RÉEL → pâtes al dente + eau de cuisson → finition : yaourt OU pecorino/parmesan + herbe déchirée (basilic, persil) + huile
```

### Variantes
- alla Norma : aubergines rôties + tomate-origan + ricotta salata
- tomates cerises mijotées ~1 h + piment ancho (fumé) + basilic + parmesan
- pappardelle : oignon caramélisé + harissa rose + tomate + olives kalamata + câpres → yaourt

### Points critiques
- la sauce doit VRAIMENT réduire (10 min à 1 h) : pas une tomate qui flotte
- réserver l'eau de cuisson pour lier ; pincée de sucre si tomates acides
- se garde ~5 j / se congèle : doubler vaut le coup

### Usage Gemini
- proposer quand : « pâtes tomate qui changent », « boîte de tomates », « sauce à faire d'avance »
- éviter quand : sauce express recherchée

---

## Pattern — Orzo cuit en une casserole façon risotto

### Intention
Plat unique réconfortant sans cuisson séparée des pâtes : l'orzo cuit DANS la sauce et libère son amidon comme un risotto.

### Pattern réutilisable
```text
orzo grillé à sec/huile jusqu'à doré → réserver → aromates (ail + zeste + épices) + tomates + bouillon + eau → remettre l'orzo, couvrir → mijoter ~15 min en remuant 1-2 fois → découvrir 1-2 min (crémeux, pas sec) → protéine rapide (crevettes) + herbe + fromage
```

### Points critiques
- griller l'orzo d'abord = goût de noisette + grains distincts
- protéine rapide en toute fin (2-3 min) ; cible crémeuse, pas sèche
- féta mariné (chili + fenouil grillé + huile) parsemé en fin pour le contraste

### Variantes
- orzo-tomate-bouillon + crevettes + féta mariné + basilic
- orzo + zeste d'orange + fenouil + tomate

### Usage Gemini
- proposer quand : « plat une casserole », « orzo », « pâtes sans égoutter »

---

## Pattern — Pain plat / tortilla farci à la viande hachée, poêlé (arayes)

### Intention
Repas rapide et nourrissant : viande hachée crue assaisonnée tartinée dans un pain plat plié, poêlé jusqu'à dorure du pain et cuisson de la viande.

### Pattern réutilisable
```text
viande hachée crue + oignon/tomate râpés + épices + tahini + ail + acide (mélasse de grenade) + herbe → étaler en couche FINE (1-1,5 cm) sur la moitié d'un pain plat/tortilla + fromage râpé → replier en demi-lune → poêler 2-3 min/face feu moyen-doux → badigeonner huile-sumac → servir avec yaourt
```

### Points critiques
- couche FINE sinon le pain brûle avant cuisson de la viande
- feu moyen-doux (le centre doit cuire) ; le tahini garde la viande moelleuse
- garniture préparable la veille

### Variantes
- agneau-piment Jamaïque-menthe-cheddar-grenade (classique) ; bœuf-cumin-persil ; pita au lieu de tortilla

### Usage Gemini
- proposer quand : « lunch avec du haché », « pita/tortilla à farcir », « goûter salé rapide »

---

## Pattern — Viande hachée sautée façon asiatique sur légume vapeur

### Intention
Quotidien express : un haché très assaisonné (sucré-salé-acide) servi sur un légume vapeur à part qui absorbe la sauce. (Distinct du wok stir-fry du corps : ici légume cuit séparément, haché qui rend du jus.)

### Pattern réutilisable
```text
aromates (oignon vert + gingembre + ail + piment) sautés feu vif → réserver → haché sauté jusqu'à coloration → sauce (mirin + soja + kecap manis + sésame + vinaigre de riz) 2 min → remettre aromates → hors feu : coriandre + arachides → servir sur légume vapeur (aubergine) + sésame
```

### Points critiques
- tout couper AVANT d'allumer le feu
- légume (aubergine) salé puis vapeur à part ~12 min : fondant, prêt à boire la sauce
- le plat rend du jus volontairement : c'est la sauce. Équilibre mirin(doux)+soja(salé)+vinaigre(acide)+sésame(parfum)

### Usage Gemini
- proposer quand : « express avec du haché », « j'ai aubergines + porc »
- éviter quand : pas de condiments asiatiques de base

---

## Pattern — Salade de nouilles FROIDE (riz/soba) + cru croquant + acide

### Intention
Lunch frais et croquant : nouilles refroidies, crus en julienne, acide vif, herbes en quantité. Assemblage minute. (Distinct du bol de nouilles chaud du corps.)

### Pattern réutilisable
```text
nouilles (riz/soba) cuites + rincées à l'eau FROIDE + huilées → oignon/gingembre macérés vinaigre+sucre → crus en julienne (concombre, pomme verte, piment) → herbes (menthe, estragon, coriandre, basilic) + graines + acide (lime) + sel → servir AUSSITÔT
```

### Points critiques
- rince eau froide = stoppe cuisson + retire l'amidon collant
- macérer oignon+gingembre 30 min dans vinaigre-sucre
- servir aussitôt assemblé (le concombre détrempe) ; protéine minute (crevettes, tofu, œuf mollet)

### Variantes
- nouilles de riz + concombre + pomme verte + menthe-estragon + pavot
- soba + avocat + lime + cardamome + pistaches + basilic-coriandre

### Usage Gemini
- proposer quand : « salade de nouilles fraîche », « lunch d'été », « concombre + herbes »

---

## Pattern — Épaule d'agneau confite lentement au four (marinade-incisions)

### Intention
Pièce de fête qui se défait à la fourchette : pâte d'épices massée dans des incisions, cuisson très longue basse température, racines confites dans le jus. (Distinct du mijoté cocotte et du BBQ pulled : grosse pièce entière au four sec.)

### Pattern réutilisable
```text
pâte d'épices (ail + zeste/jus citron + épices + herbes + huile + sel) au robot → piquer la viande ~30 fois + frotter en faisant pénétrer → mariner 1 nuit → four couvert (alu) 170°C 1 h, baisser 160°C + ajouter racines, 4 h en arrosant, puis découvrir 1 h 30 → viande effilochée + légumes caramélisés
```

### Points critiques
- piquer la chair partout (~30×) pour pénétration profonde ; mariner une nuit (min 4-5 h)
- alu d'abord (tendreté), découvert en fin (coloration)
- préparable la veille : cuire, réfrigérer, effilocher, réchauffer dans le jus ; servir avec féculent qui boit le jus

### Usage Gemini
- proposer quand : « grande tablée », « pièce d'agneau de fête », « plat qui cuit tout seul »
- éviter quand : pressé (~6 h 30 de four)

---

## Pattern — Poisson braisé dans une sauce maison + (option) 2e sauce contrastante

### Intention
Le poisson cuit doucement DANS une sauce déjà montée (tomate-épices ou pois chiches-harissa), cuisson courte, chair nacrée, une casserole. Possibilité de napper d'une 2e sauce froide.

### Pattern réutilisable
```text
base mijotée (oignon/ail + épices grillées + tomate OU pois chiches-harissa-citron confit + bouillon) jusqu'à épaississement → coucher le poisson → couvrir → 8-12 min jusqu'à chair en flocons → coriandre + (option) filet tahini-citron froid
```

### Variantes
- bases : tomate-piment-carvi-ancho (chraimeh) ; pois chiches-harissa-cardamome-citron confit ; poivron-orange
- poissons : flétan, morue, aiglefin, plie — tout poisson blanc ferme
- 2e sauce : tahini-citron, yaourt-citron, sauce verte

### Points critiques
- épaissir la sauce AVANT le poisson (sinon sauce claire / poisson surcuit)
- si sauce claire : retirer poisson, réduire, napper ; retourner délicatement à mi-cuisson ; saler le poisson ~15 min avant

### Usage Gemini
- proposer quand : « poisson blanc une casserole », « morue/cabillaud + pois chiches ou tomate »
- éviter quand : poisson très fragile (préférer pavé ferme)

---

## Pattern — Poisson rôti style asiatique + huile fumante versée à la fin

### Intention
Pièce maîtresse asiatique : poisson cuit sur lit de légumes avec sauce soja-gingembre, fini par de l'huile fumante versée qui croustille la peau et « cuit » les aromates crus.

### Pattern réutilisable
```text
sauce soja-sésame-vin de riz-sucre (réduite 1 min) → poisson incisé+salé sur lit de chou/oignons verts + gingembre julienne → verser la sauce → couvrir alu → four 220 °C, badigeonner 2× (~40 min) → aromates crus (oignon vert, piment, coriandre) → verser une huile fumante (arachide) → servir
```

### Variantes
- bar entier, dorade, ou pavés blanc/saumon ; lit chou/bok choy ; vin de riz shaoxing → xérès

### Points critiques
- inciser (5 entailles/face) pour cuisson homogène + pénétration du sel
- l'huile doit VRAIMENT fumer avant versement (croustille la peau, cuit les aromates)
- récupérer la sauce du plat pour arroser

### Usage Gemini
- proposer quand : « poisson entier au four », « repas asiatique festif », « sauce soja-gingembre »
- éviter quand : pas de four (sinon pavés)

---

## Pattern — Dessert en coupes : crème + fruit cuit + croquant (tout d'avance)

> Déclinaison du pattern dessert fruits+laitier du corps. DELTA propre : composants conservables assemblés minute, croquant cuit en « chapelure ».

### Pattern réutilisable
```text
base crémeuse (fromage frais ± féta + sucre + zeste + crème fouettée, OU yaourt grec égoutté + crème) + compote (fruit + sucre + épice/zeste) + croquant (noix + amandes moulues + sucre + sésame + beurre, doré au four en chapelure) → assembler en couches MINUTE
```

### Conservation (clé)
- crème 3 j / compote 5 j / croquant 1 semaine en boîte hermétique
- ne JAMAIS assembler d'avance (le croquant ramollit)

### Points critiques
- pincée de sel ou féta dans la crème pour casser le sucré ; compote 10-15 min (fondant, pas bouillie)

### Usage Gemini
- proposer quand : « verrines de fruits », « dessert la veille »

---

## Pattern — Cheesecake sans four : base biscuits + crème yaourt-fromage-chocolat blanc

### Intention
Le cheesecake le plus facile : pas de four, pas de crevasses, il prend au frigo. Le chocolat blanc fondu fait tenir la garniture.

### Pattern réutilisable
```text
yaourt grec égoutté (étamine) → base biscuits émiettés + beurre fondu (± thym) pressée, frigo → fouetter fromage à la crème + yaourt égoutté + sucre glace + zeste citron → incorporer chocolat blanc fondu → étaler → frigo 2 h min → napper sirop chaud (miel-thym) au service
```

### Variantes
- biscuits : Hobnobs, digestifs, spéculoos ; nappage miel-thym ou coulis ; aromate zeste/vanille/thym

### Points critiques
- bien égoutter le yaourt (sinon liquide) ; AUCUNE goutte d'eau dans le chocolat blanc (il graine)
- napper le sirop SEULEMENT au service (la base ramollit) ; se prépare 2 j à l'avance

### Usage Gemini
- proposer quand : « cheesecake facile sans four », « dessert la veille »
- éviter quand : envie d'un vrai cheesecake cuit dense

---

### condiments / sauces outils

**Dip aubergine fumée + tahini + mélasse de grenade**
Dip aigre-doux moyen-oriental à partir de chair d'aubergine brûlée.
Formule : chair d'aubergine fumée égouttée + tahini + eau + mélasse de grenade + jus citron + ail pressé + persil + sel → fouetter. Cible : franchement acide / légèrement sucré.
Usages : DIP lisse (crudités, agneau, poisson) ; SALADE d'été (+ concombre + tomates cerises + grenade + huile). Végan, 5 min une fois l'aubergine brûlée.

**Beurre composé aromatique (sauce minute sur plat chaud)**
Formule : beurre mou battu + zeste + jus agrume + ail fin + 1 herbe + piment + sel → boudin dans film → frigo ferme → trancher → poser sur le plat brûlant pour qu'il fonde.
Exemples : lime-coriandre-piment sur galettes d'épinard, patate douce, poisson grillé, maïs. Se prépare d'avance.

**Sauce tonnato : émulsion umami thon-anchois-câpres-citron**
Formule : au robot, jaunes d'œufs + jus citron + persil + thon (huile) + câpres + anchois + ail → purée → huile en filet continu jusqu'à mayonnaise souple.
Sert sur : pdt au four + œuf mollet, légumes vapeur, viande froide (vitello), œufs durs.
Points : huile TRÈS lentement (émulsion) ; triple levier salé (goûter avant de saler) ; se garde la veille.

---

### légumes verts / accompagnements

**Légume-feuille sauté feu vif + ail/piment croustillant + acide**
Intention : vert robuste (brocoli, kale, chou pointu, choy sum, minibrocoli) vif et croquant, jamais bouilli mou.
Formule :
```text
(blanchir 30-90 s si dense + éponger) → huile chaude infusée ail/piment/cumin → RETIRER l'aromate croustillant → sauter le vert feu vif jusqu'à bords croustillants → sel + acide (lime/citron) HORS feu → re-parsemer l'aromate + herbe
```
Points : bien éponger (sinon vapeur) ; retirer l'ail avant qu'il brûle, le remettre en finition ; acide hors feu.
Proposer quand : « brocoli/kale à passer », « vert rapide qui change ». Éviter : verts fragiles (épinard, à la dernière seconde).

**Vinaigrette aigre-douce asiatique sur légume à peine cuit**
Intention : enrober un vert juste blanchi/rôti d'une sauce vive sucrée-salée-acide + arachides.
Formule :
```text
huile chaude infusée (ail + gingembre + zeste + arachides) → réserver
légume à peine cuit → arroser de l'huile aromatique
réduction sucrée-salée (soja + miel, OU lime + piment + sirop + sésame) → napper MINUTE
```
Variantes : minibrocolis, choy sum, haricots verts, gombos (rôtis 7 min, fermes).
Points : mélanger juste avant service (la sauce tombe au fond) ; légume ferme et vert ; gombos entiers (sinon visqueux).

**Croustillant au four par enrobage polenta/semoule (frites sans friture)**
Formule :
```text
légume en bâtonnets (pdt pré-bouillies+séchées, OU patate douce crue) + huile généreuse + épices + poignée de polenta/semoule → enrober → étaler espacé → four chaud, retourner 1-2× jusqu'à croustillant → sel/sumac à la sortie
```
Variantes : pdt + gras d'oie + semoule + carvi + harissa ; patate douce + paprika fumé + Cayenne + ail + polenta + sumac.
Points : pré-bouillir et BIEN sécher (vapeur = mou), secouer pour bords floconneux ; plaque pas surchargée ; assaisonner à la sortie.

---

### purées & mezze

**Purée de légume relevée par huile aromatique OU salsa fraîche**
Intention : sortir une purée du fade — eau de cuisson aromatisée + finition à l'huile parfumée, ou couronne de salsa crue.
Formule :
```text
légume cuit (eau aromatisée thym/menthe/ail/zeste OU four) → écraser à l'huile (+ eau de cuisson) → creux en surface → huile aromatisée (ail+herbes+zeste+jus) OU salsa crue (herbes+ail+zeste+jus+huile)
```
Variantes : pdt (eau thym/menthe/ail/zeste) ; patate douce + salsa lime (basilic+coriandre+ail+lime). Pelures rôties 8 min = collation.
Points : réserver l'eau de cuisson ; purée à l'huile plus légère que beurre (pour plat principal riche) ; former des creux.

**Purée de légumineuse lisse + couronne contrastante [mezze]**
Formule :
```text
base lisse (légumineuse/avocat/gourganes mixés + huile + ail confit + citron + sel) étalée, creux central
+ topping : muhammara (poivrons rôtis+noix), OU oignons verts+zeste sautés, OU aromates croustillants + leur huile
```
Variantes : haricots blancs (huile+ail+thym) + muhammara ; avocat + gourganes (plus léger qu'un guacamole) ; toute légumineuse boîte mixée.
Points : base très lisse (eau/huile au besoin) ; ail caramélisé puis jeté parfume sans agressivité ; se garde 2-3 j (doubler).

---

### légumes — formats plats

**Légume rôti ET cru râpé dans la même salade (double texture)**
Intention : un seul légume, une part rôtie fondante + une part crue râpée croquante.
Formule :
```text
2/3 du légume en bouquets + oignon → rôti four chaud doré
1/3 du légume râpé cru
assembler TIÈDE : rôti + cru râpé + herbes multiples + grenade/noix + cumin + citron + huile
```
Variantes : chou-fleur (signature), brocoli, betterave, carotte, courgette ; ne pas jeter les feuilles (rôties ou crues).
Points : râper grossièrement ; assembler tiède (sinon herbes flétries) ; rôtir 4-6 h d'avance possible.

**Légume entier rôti longuement, badigeonné [pièce maîtresse végé]**
Intention : un légume entier comme centre partagé — pré-cuisson, puis four long avec badigeonnages jusqu'à cœur fondant / extérieur doré.
Formule :
```text
légume entier (pré-bouilli 6 min OU piqué) → four moyen → badigeonner beurre+huile (ou huile+épice) à intervalles → 1h30-3h jusqu'à très tendre à cœur et bruni → repos → quartiers → sel en flocons + citron OU sauce verte tahini
```
Variantes : chou-fleur (pré-bouilli 6 min, feuilles laissées croustillantes) ; céleri-rave (piqué, huile+coriandre) ; sauce verte tahini (tahini+persil+ail+citron+eau).
Points : badigeonnages réguliers (croûte, anti-dessèchement) ; patience ; pré-bouillage assure le cœur.

**Légumes farcis braisés (farce riz ou mie + herbes)**
Intention : légume creusé/en feuilles garni d'une farce, braisé dans un liquide aigre-doux. Plat végé tiède ou froid.
Formule :
```text
légume préparé (couches d'oignon / feuilles blanchies / boats de courgette) + farce (riz court OU mie + fromage + herbes + pignons + ail + épices douces) → rouler/garnir → braiser à couvert (vin/bouillon + sucre + citron + huile) jusqu'à absorption
```
Variantes : oignons, courgettes, feuilles chou/blette/vigne, poivrons, tomates ; farces riz-raisins-pignons-cannelle (turc), mie-féta-persil, riz-ricotta-menthe ; finition parmesan gratiné ou yaourt froid.
Points : blanchir les enveloppes (rouler sans casser) ; riz cuit aux 3/4 ; liquide à mi-hauteur, couvrir.

**Beignets de légumes liés par une pâte battue (fritters)**
> Distinct des croquettes panées du corps : ici la PÂTE est le liant, pas l'œuf-chapelure.
Formule :
```text
légume fondu et REFROIDI (poireau/oignon suées longuement) + épices + herbes → pâte (farine + levure + œuf + lait + beurre fondu) → blanc d'œuf monté plié en dernier → cuillerées poêlées 2 faces → sauce yaourt-herbes à côté
```
Variantes : poireau, oignon, courgette râpée pressée, épinards, maïs ; sauce verte yaourt+crème sure+ail+citron+persil+coriandre.
Points : suer et REFROIDIR le légume (chaud = cuit le blanc, retombe) ; monter/plier le blanc ; presser les légumes aqueux ; huile chaude pas brûlante.

---

### protéines végé asiatiques

**Sauté « beurre + chili + soja » (tofu, choux de Bruxelles)**
> Distinct du wok rapide du corps : beaucoup d'aromatics fondus, BEURRE au lieu d'huile.
Formule :
```text
tofu/légume fariné (fécule) frit doré → réserver → beurre fondu + masse échalotes/ail/gingembre/piment suée 15 min (fondance brillante) → sojas (clair+foncé+sucré) + sucre + poivre concassé → remettre base + oignon vert → enrober hors gros feu
```
Variantes : tofu ferme, choux de Bruxelles tranchés, shiitake ; registre poivre noir (black pepper tofu) ; registre sucré (chili doux+soja+sésame+érable). Service : riz, coriandre, sésame.
Points : fécule + huile chaude = croûte qui tient la sauce ; fondre les aromatics LONGUEMENT (15 min) ; sojas/sucre/poivre en fin hors gros feu.

---

### salades crues massées

**Légume-feuille / légume ferme cru MASSÉ à l'acide pour l'attendrir (slaw)**
> Fusion : kale massé + slaw chou/chou-rave (même geste de massage manuel).
Intention : rendre un cru ferme (kale, chou, chou-rave) tendre sans cuisson, par massage à la main dans une marinade acide ; équilibré par fruit sec et beaucoup d'herbe. Tient des heures, gagne en saveur.
Formule :
```text
feuilles déchirées (sans tiges) OU légume ferme tranché fin + huile + acide (citron/vinaigre) + moutarde + sirop/miel + sel → MASSER à la main 1 min jusqu'à ramollissement et changement de couleur → mariner 30 min (jusqu'à 4 h) → AU DERNIER MOMENT : croquant/frais (asperges sautées, édamames, fruit sec, graines, herbes)
```
Variantes : marinade moutarde ancienne + vinaigre vin blanc + érable, OU citron+ail+huile ; ajouts asperges, édamames, graines caramélisées, estragon/aneth.
Points : masser PHYSIQUEMENT avec les doigts (casse les fibres), pas remuer ; masser d'avance, assembler les ajouts à la dernière minute.
Proposer quand : « salade de kale/chou », « crus fermes à manger crus », « salade qui tient des heures ». Éviter : feuilles tendres (laitue, roquette).

### Pattern réutilisable
```text
légumes crus fermes tranchés très fin + sel + agrume généreux + ail + huile + fruit sec → masser 1 min → reposer 10-15 min → herbe abondante + croquant → rectifier (BEAUCOUP de sel pour contrer l'acide)
```

### Variantes
- légumes : chou blanc/rouge, chou-rave, carotte, fenouil, betterave crue
- fruits : cerises/raisins secs, grenade, mangue, papaye verte
- registre asiatique : lime + citronnelle + érable + sésame + piment
- herbes : aneth, menthe, coriandre, persil ; croquant : macadamias caramélisées, arachides, graines

### Points critiques
- trancher très fin (mandoline) ; MASSER physiquement ; saler généreusement (l'acide demande du sel) ; servir hors du jus
- erreurs : tranches épaisses → dur ; sous-salage → plat ; noyé → mou

### Usage Gemini
- proposer quand : salade d'hiver, chou/chou-rave à utiliser, slaw, accompagnement frais d'un plat riche

---

## Pattern — Légume rôti en croûte parmesan-chapelure-herbes

**Intention** : quartiers de légume huilés puis recouverts d'une croûte sèche (parmesan + chapelure + herbes + zeste + ail) qui gratine. Effet "farce croustillante" sur un légume entier.

### Pattern réutilisable
```text
légume en tranches/quartiers à plat + badigeon d'huile → croûte (parmesan + chapelure SÈCHE + herbes + zeste citron + ail + poivre, peu de sel car parmesan salé) tassée dessus → four moyen jusqu'à légume tendre + croûte dorée (alu si elle fonce trop vite) → crème sure-aneth à côté
```

### Variantes
- légumes : courge/potiron, courgette, tomate, fenouil, chou-fleur
- croûte : + noix concassées, zaatar ; herbes : persil-thym, origan, romarin ; sauce froide : crème sure-aneth, yaourt-citron

### Points critiques
- chapelure SÈCHE ; saler la croûte avec parcimonie (parmesan) ; tasser pour qu'elle adhère ; alu si elle brunit trop vite ; vérifier la cuisson du légume à la pointe
- éviter quand : sans four

### Usage Gemini
- proposer quand : courge/potiron, légume rôti plus consistant, plat végé de fête, reste de parmesan + chapelure

---

## Pattern — Curry de légumes épicé (vindaloo / dry curry)

**Pattern 045 — Légume tendre braisé dans un bouillon aromatique au four**

Cuire un légume délicat (courgette, fenouil, poireau) immergé dans un bouillon parfumé, à couvert au four, jusqu'à fondance — l'opposé du rôtissage sec (pattern 001). Texture soyeuse, registre mezze/entrée.

```text
légume serré dans un plat → bouillon chaud (ail + herbe) versé pour couvrir + sel → couvrir d'alu → four ~45 min jusqu'à fondant → égoutter → finition : huile + aromate frit (origan/ail) + sel en flocons
```

- variantes : courgettes-ail-origan ; fenouil-citron-thym ; poireaux entiers-bouillon-zeste
- critique : légume serré (tient et cuit régulier), bouillon chaud (gagne du temps), à couvert (on braise), finition frite fait tout le caractère
- proposer : "légume fondant sans friture", "mezze", "entrée délicate" — éviter si on veut coloration/croustillant (alors pattern 001)

**Pattern 047 — Légume évidé farci (farce liée par sa chair + œuf + fromage)**

Légume contenant (courgette/poivron/aubergine évidé), farci de sa propre chair liée œuf + fromage + mie, gratiné. Plat végé principal ou accompagnement généreux.

```text
légume en barquette, chair retirée + PRESSÉE → farce = chair + œuf + parmesan + mie + tomate écrasée + sel → garnir → four très chaud ~15 min jusqu'à doré → topping (pignons + zeste + herbes) au service
```

- variantes : courgette-parmesan-pignons-origan ; poivron-riz-féta ; aubergine-tomate-chapelure
- critique : garder ~1 cm de paroi, PRESSER la chair (sinon détrempée), trio liant œuf+fromage+mie, four très chaud (230-250°C), farce préparable la veille
- proposer : "légumes farcis", "grosses courgettes/poivrons" — éviter si peu de temps (évidage long)

**Pattern 043 — Taboulé inversé : herbes majoritaires, grain minoritaire**

Le taboulé Ottolenghi est une salade d'HERBES ; le grain n'est qu'un liant minoritaire. Variante sans gluten : chou-fleur cru râpé en "faux boulgour".

```text
herbes en MASSE (persil + menthe + aneth) + oignon vert → +grain cuit OU chou-fleur cru râpé grossier, macéré 20 min dans citron+sel → huile + épice (piment de la Jamaïque) → grenade/pistaches en finition
```

- critique : les herbes pèsent PLUS que le grain (c'est le principe) ; chou-fleur râpé grossier (pas en bouillie) ; macérer 20 min ; assembler et servir aussitôt
- proposer : "taboulé", "herbes à écouler", "salade légère sans gluten", "un chou-fleur" — éviter si peu d'herbes

### principe

**Recevoir sans stress : tout d'avance, servir à T° ambiante**

Philosophie d'organisation transversale pour les repas de réception.
- Privilégier les plats qui se préparent à l'avance et gagnent en saveur (mijotés de légumineuses, calmar, poisson piment-tahini : meilleurs le lendemain ; sauces/tartinades/vinaigrettes conservables).
- Prendre de l'avance par étapes : noix grillées, panure/farce prêtes, grains cuits refroidis, légumes blanchis/rôtis ramenés à T° ambiante.
- Servir à température ambiante (ou réchauffé) plutôt que froid frigo ; couvrir la table avant l'arrivée, chacun se sert. Seuls quelques plats s'assemblent minute.
- Choisir des plats faciles à doubler/tripler (congeler la moitié).
- Identifier ce qui s'assemble en dernier (herbes, vinaigrettes sur feuilles tendres, croquants, jus réservés) et le garder à part.
- Penser batch : oignons frits, dukkah, ail confit, sauces/huiles aromatiques en grande quantité, ça se conserve.
- activer quand : "je reçois", "menu pour X", "préparer à l'avance", "buffet/mezze", "quoi faire la veille"

**Substitution "vide-frigo" à poids net constant**

Dans une majorité de recettes (vinaigrettes d'herbes, beignets aux herbes, gâteaux frigo), les composants d'une même famille sont interchangeables tant que le poids net total reste identique.

```text
remplacer librement DANS une famille, à POIDS NET CONSTANT :
- herbes (persil ↔ coriandre ↔ aneth ↔ basilic ↔ estragon)
- fruits secs (raisin ↔ abricot ↔ datte ↔ cerise séchée)
- noix (amande ↔ pignon ↔ pistache ↔ noix)
- verts feuilles (épinard ↔ blette ↔ kale)
```

- critique : garder le poids total identique ; rester dans la même famille ; doser un peu en deçà les herbes très puissantes (estragon, menthe)
- réflexe par défaut quand : "je n'ai pas X, j'ai Y", "vide-frigo" → rassurer "même poids = ça marche"

**Assaisonner les herbes/feuilles délicates à la SECONDE du service**

Les herbes délicates (cresson, basilic, aneth, estragon, romaine) flétrissent instantanément au contact de la vinaigrette acide. Les garder à part au frais (boîte hermétique) et ne verser vinaigrette + noix qu'au moment exact de servir, puis mélanger doucement.
Corollaire : une salade d'herbes (cresson + basilic + coriandre + aneth + estragon + pistaches + vinaigrette citron-fleur d'oranger) est un excellent rafraîchisseur de palais entre deux plats riches.

### référence

**Substitutions et dosages — aide-mémoire**

- Cardamome : ½ c. à thé de graines broyées = ¼ c. à thé de moulue (la moulue est plus concentrée).
- Baies d'épine-vinette → raisins de Corinthe trempés 30 min dans jus de citron (30 ml pour 45 ml de raisins), égouttés.
- Harissa : goûter d'abord — si douce +50 %, si très piquante -50 % (gros écarts entre marques).
- Piment ancho séché → 1 c. à thé de paprika doux fumé.
- Noix de coco fraîche râpée → flocons séchés (griller 2-3 min au lieu de 6-7).
- Vin de riz shaoxing → xérès.
- consulter quand : un ingrédient signature manque, ou pour ajuster les doses d'épices fortes

**Les 10 ingrédients signature Ottolenghi [garde-manger]**

Dix "bombes de saveur" qui se conservent longtemps ; une pincée/un filet suffit. Provenance > marque (épicier moyen-oriental pour sumac, zaatar, tahini, épine-vinette).
- Sumac : épice rouge acidulée. Œufs, viandes, poissons, légumes grillés, vinaigrettes — même desserts.
- Zaatar : thym + sésame + sumac + sel. Sur viande/poisson/légumes, ou en huile.
- Piment d'Urfa : turc, fumé, chocolaté, peu piquant. Œufs brouillés, avocat sur tartine, tomates rôties chaudes.
- Cardamome : note douce, salé et sucré. Partir des gousses (écraser). Doser (½ c. graines = ¼ c. moulue).
- Mélasse de grenade : sirop aigre-doux. Trait sur légumes/viande, marinade, mijoté ; excellente sur agneau haché.
- Harissa à la rose : pâte de piment adoucie aux pétales. Marinades, pâtes, omelettes, oignons. Goûter avant de doser.
- Tahini : préférer le crémeux (libanais/israélien/palestinien). Sauces, vinaigrettes, croûte de hachis, arrosage de poisson.
- Baies d'épine-vinette : baies séchées acidulées. Beignets, frittatas, riz, salsa. Défaut : raisins de Corinthe trempés citron.
- Ail noir : fermenté, doux, balsamique/réglisse, umami. Pizza, risotto, équilibre l'amer des choux de Bruxelles.
- Citron confit (peau fine) : punch intense, souvent seulement l'écorce. Salades, vinaigrettes, betteraves rôties, œufs braisés.

**Tomates semi-séchées plutôt que séchées en salade**

Éviter les tomates séchées au soleil (dures, agressives). Préférer les SEMI-séchées (mi-confites, moelleuses, "sun-blushed") : concentration + umami sans le côté coriace qui déséquilibre une salade de feuilles. Maison conservées dans l'huile, ou commerciales moelleuses.

### pattern outil

**Pâte fraîche aromatisée dans la masse (zeste + curcuma + safran)**

Parfumer la PÂTE elle-même, pas que la sauce : la pâte devient un ingrédient de saveur.

```text
farine 00 + œufs + huile + AROMATE INTÉGRÉ (zeste citron / curcuma moulu / safran infusé 10 min dans eau chaude) → pétrir, reposer 30 min, abaisser
```

- variantes : zeste+curcuma → ravioli chèvre-citron (pignons roses, estragon) ; safran+curcuma → tagliatelles dorées (beurre épicé) ; sans pâte maison → pincée de safran dans l'eau de cuisson de pâtes sèches
- critique : infuser le safran avant ; curcuma colore fort (dosage modéré) ; pâte ni collante ni sèche ; ravioli au fromage : sceller sans bulle d'air

**Yaourt grec égoutté (labneh express)**

Geste de base récurrent, salé comme sucré.

```text
yaourt grec (+ sucre glace + pincée de sel si dessert) → passoire tapissée d'étamine/linge → baluchon + poids → frigo 30 min (express) à plusieurs heures → presser, jeter le petit-lait
```

- repères : 900 g → ~550 g (perte ~⅓) ; 30 min = crémeux épais ; plusieurs heures = labneh tartinable
- usages : cheesecake sans cuisson, crème pour fruits rôtis, labneh salé mezze, lit froid sous tomates rôties

**Bouillon de légumes à saveur profonde (sucs + pruneaux)**

Donner corps et umami à un bouillon végé fade.

```text
légumes aromatiques (carotte, céleri, oignon, ail, céleri-rave) revenus jusqu'à coloration + herbes + poivre + laurier + QUELQUES PRUNEAUX → eau froide → mijoter ~1h30 en écumant → filtrer
(variante umami : croûtes de parmesan pendant la cuisson, puis retirées)
```

- critique : COLORER les légumes = base de saveur ; pruneaux = rondeur sans sucrer ; croûtes de parmesan = umami gratuit (à congeler au fil du temps)
- proposer : base de soupe végé, risotto, braisé sans viande, "bouillon de légumes fade"

**Ail confit caramélisé**

Gousses entières → perles fondantes enrobées d'un sirop foncé. Condiment pour tartes, légumes rôtis, pâtes, tartines.

```text
gousses pelées blanchies 3 min (enlève l'âcreté) → égoutter → revenir 2 min à l'huile → balsamique + eau → mijoter 10 min → sucre + romarin/thym + sel → réduire jusqu'à caramel foncé enrobant
```

- critique : BLANCHIR d'abord (douceur) ; réduire jusqu'à sirop pas brûlé (amertume) ; balsamique + sucre = base sucrée-acide
- se garde plusieurs jours au frigo dans son sirop ; pour tarte/quiche, légumes rôtis, tartine, base de sauce

**Vinaigrette mélasse de grenade (échalote + moutarde)**

Vinaigrette signature sucrée-acide-fruitée, montée à l'échalote ; réveille salades fruit-fromage, légumes rôtis, grains, lentilles.

```text
échalote ciselée + moutarde Dijon + mélasse de grenade + sel/poivre → fouetter en versant l'huile en filet → émulsion homogène
```

- variantes : +citron, +sumac, grains de grenade en finition ; simplifiée : mélasse + huile + sel
- critique : monter en émulsion (nappe) ; mélasse très concentrée (peu suffit) ; l'échalote s'adoucit en macérant dans l'acide

### technique

**Pilaf de grain par absorption hors feu (boulgour, freekeh)**

Méthode "feu coupé", plus fiable que la cuisson continue (évite que le grain colle/brûle au fond).
- revenir oignons/légumes + griller épices et fruits secs dans la matière grasse
- ajouter le grain, mouiller (boulgour ~1 grain : 1,75 eau ; freekeh ~1 : 1,25 bouillon réduit)
- boulgour : ébullition, couvrir hermétiquement, RETIRER DU FEU, gonfler ≥20 min
- freekeh : ébullition puis 15 min feu minimal couvert + 5 min hors feu couvert ; tremper 5 min eau froide + rincer avant cuisson (enlève amertume/poussière de fumage)
- égrener à la fourchette ; si sec, filet d'huile

**Riz complet/rouge "comme des pâtes" + quinoa minute**

Pour les grains rustiques, abandonner l'absorption, cuire à grande eau.
- riz rouge de Camargue / complet : grand volume d'eau bouillante NON salée, ~20 min, égoutter
- quinoa : grande eau, frémir 9 min seulement, égoutter passoire fine ; laisser sécher tiède avant d'assaisonner (évite la bouillie)
- parfumer un riz nature : cuire avec des tiges de basilic (feuilles attachées), retirer après
- salades de grains : étaler sur plateau pour refroidir vite et garder séparé

**Polenta : point de cuisson et repère instant vs traditionnelle**

- verser EN PLUIE dans le liquide bouillant, remuer constamment, feu minimal
- temps : instantanée ~5 min ; traditionnelle jusqu'à 50 min
- prête quand elle se décolle des parois mais reste coulante ; si elle sèche, rallonger bouillon/eau ("porridge épais")
- finir hors feu : beurre + parmesan (ou féta)
- restes : étaler sur surface huilée, figer, couper, poêler à l'huile le lendemain

**Polenta de maïs frais (alternative douce à la semoule)**

Plus douce et légère, texture purée.
- égrener ~570 g de grains (~6 épis ; épi debout, couteau)
- cuire couverts d'eau, frémissement bas 12 min
- mixer longuement au robot (casser les enveloppes ; +eau de cuisson si sec)
- remettre purée + eau, cuire en remuant 10-15 min (consistance purée de pdt)
- finir beurre + féta ; servir avec une sauce relevée (base très douce)

**Réussir des champignons bien dorés (poêlée)**

- poêle large bien chaude, huile chaude, cuire en 2 fournées (ne pas surcharger)
- ne presque pas remuer (laisser des plaques dorées se former)
- ail, herbes, huile parfumée (truffe) ajoutés HORS FEU (l'ail ne brûle pas, herbes vives)
- même logique que saisir une viande : trop plein = vapeur, pas de coloration

**Fenouil poêlé caramélisé mais ferme**

Caramélisation = glaçage de surface, pas cuisson à cœur — le fenouil garde du croquant.
- trancher les bulbes en 1 cm (garder la base qui tient les couches)
- saisir par lots, beurre + huile chaude, ~2 min/face jusqu'à doré clair, retirer
- tout saisi : sucre + graines de fenouil + sel dans la poêle, 30 s
- remettre, enrober 1-2 min dans le sucre fondu (ferme dedans, juste glacé)
- finition T° ambiante : ail pressé + aneth + chèvre frais + zeste citron + pluches

**Légume amer caramélisé cut-side down + fromage fondu (endive, fenouil)**

Transformer un légume amer/anisé en gratin réconfortant.

```text
légume coupé (endive en 2, fenouil tranché) → poêle chaude beurre + huile + pincée de sucre → face coupée vers le bas, NE PAS BOUGER 3-5 min jusqu'à doré profond → plat → fromage fondu dessus → four jusqu'à bouillonnement → chapelure + poivre → gratiner
```

- critique : ne pas surcharger (sinon vapeur) ; ne pas remuer (croûte caramélisée contre l'amertume) ; sucre + beurre équilibrent l'amer
- variantes : endive + gruyère/taleggio/raclette ; fenouil + chèvre + zeste citron + aneth

**Courgettes frites puis marinées au vinaigre (salade de pâtes)**

- couper en tranches ~0,5 cm
- frire à l'huile chaude en plusieurs fournées sans surcharger, ~3 min, doré 2 faces, RETOURNER UNE SEULE FOIS
- égoutter, arroser de vinaigre de vin rouge encore tièdes (marinade express)
- pâtes en salade : al dente, rincer à l'eau froide, puis assaisonner
- sauce verte : mixer basilic + persil + huile + sel/poivre pour lier

**Blanchir en cascade : temps étagés, eau glacée**

Cuire plusieurs verts pour une salade croquante.
- blanchir chaque vert à son temps, refroidir IMMÉDIATEMENT à l'eau glacée (fixe la couleur, stoppe la cuisson)
- temps courts étagés : haricots verts ~4 min, pois mange-tout ~1 min, petits pois ~20 s
- réutiliser la même eau pour des verts à temps proches ; changer si trop colorée
- bien égoutter et SÉCHER avant d'assaisonner (sinon vinaigrette diluée)

**Graines entières grillées dans l'huile jusqu'à éclater, versées brûlantes**

Réveiller graines entières (moutarde, coriandre, cumin, nigelle) pour assaisonner une salade. Variante du pattern 022 (huile infusée), mais versée chaude sur du cru.
- graines + huile dans une petite casserole, chauffer jusqu'à ce qu'elles ÉCLATENT (popping)
- verser huile + graines BRÛLANTES directement sur les légumes (l'huile chaude libère les arômes ET sert de vinaigrette tiède)
- ajouter ensuite les aromates crus (oignon, piment, ail, zeste, herbes)

**Aubergine brûlée : chair fumée pour dip ou plat**

- TOUJOURS percer l'aubergine en plusieurs points (risque d'explosion sous le gril)
- sur gaz : directement sur la flamme, 12-15 min, tourner souvent, peau noircie partout + chair molle
- sur électrique : alu, sous gril chaud ~1h, tourner, l'aubergine se dégonfle complètement
- fendre, récupérer la chair en évitant la peau noire
- ÉGOUTTER la chair en passoire 15-30 min avant d'assaisonner (sinon trop d'eau)
- usages : dip tahini, croquettes, lentilles + aubergine, sauce

**Filet de poisson à peau croustillante (poêle)**

Poser peau dessous dans l'huile très chaude et PRESSER avec une spatule les premières secondes (empêche la peau de se rétracter). Cuire l'essentiel côté peau (saumon ~3 min, maquereau ~2 min) jusqu'à dorure, puis retourner brièvement pour finir la chair (1-4 min).
- ne pas bouger le filet tant que la peau n'est pas dorée ; réduire le feu après le retournement
- proposer : saumon, maquereau, bar, dorade à la poêle

**Panure noix de coco grillée pour poisson [complète Pattern 013]**

Variante de panure pour bâtonnets de poisson (plaît aux enfants).

```text
poisson blanc ferme mariné court (lime + crème de coco + sel, 1 h MAX) → essuyer → tremper dans beurre fondu → rouler dans noix de coco grillée à sec + panko + chili broyé + sel → gril, retourner à mi-cuisson, 5-6 min
```

- critique : griller la coco À SEC d'abord (sinon pas de goût) ; mariner 1 h max puis essuyer (sinon la panure n'adhère pas) ; chili doux ou omis pour enfants ; si dore trop vite, finir sur chaleur résiduelle

**Tempérer le yaourt pour une soupe chaude qui ne tranche pas**

Soupe chaude à base de yaourt sans qu'il graine.
- fouetter yaourt + ail + 1 œuf dans un grand bol résistant à la chaleur
- ajouter UNE louche de soupe chaude en fouettant, puis une autre, progressivement (≥ la moitié de la soupe)
- reverser ce mélange tempéré dans la casserole
- réchauffer feu moyen en remuant CONSTAMMENT, sans jamais bouillir (l'œuf stabilise + donne du corps)
- finir : herbes, zeste citron, filet d'huile

**Réduction sucrée-acide comme alternative au vinaigre (verjus, agrume)**

Vinaigrette à base d'un liquide acide RÉDUIT, plus rond et sirupeux qu'un vinaigre brut : réduire à frémissement jusqu'à sirop, refroidir, monter à l'huile.
- verjus réduit (~3 c. à s.) → vinaigrette douce-acide sur crudités fines (asperge crue, fenouil, betterave mandoline)
- jus d'orange sanguine + citron + sirop d'érable réduit 20-25 min → sirop pour salade amère (radicchio, trévise) + ricotta + grenade

**Pocher un coing (fruit qui "fait peur")**

Immangeable cru (dur, âpre), un pochage lent le transforme (chair rouge, parfumée, tendre).
- sirop : eau + sucre (~1,75 eau : 1,5 sucre) + poivre en grains, zestes d'orange, laurier, jus de citron, un peu de vin rouge ; chauffer pour dissoudre
- peler, épépiner, couper en quartiers ; GARDER peau et cœurs dans le sirop (pectine + couleur rouge)
- cuire couvert au four doux 135°C ~2 h jusqu'à tendreté complète
- sirop restant : chaud sur une glace vanille
- va avec : bleu/gorgonzola, viandes grasses (agneau, gibier, porc), salade amère + pistaches

**Beurre épicé façon marocain (pâtes/couscous)**

Condiment polyvalent (pâtes fraîches, couscous, légumes vapeur).
- fondre beurre + huile, y cuire doucement des échalotes ~10 min (elles fondent, le beurre brunit un peu)
- hors feu, incorporer : gingembre, paprika doux, coriandre, cannelle, cayenne, flocons de piment, curcuma + sel
- verser sur le grain, finir pignons grillés + menthe + persil
- raccourci : bonnes pâtes sèches + pincée de safran dans l'eau de cuisson

**Panko grillé à sec pour casser la lourdeur d'une pâte crémeuse**

- griller du panko à sec, poêle feu moyen, jusqu'à doré
- le mêler à une gremolata (zeste citron + ail + persil), éparpiller GÉNÉREUSEMENT au service
- sauce crème : la garder coulante, détendre avec de l'eau de cuisson réservée
- sauce vin-crème : réduire le vin des ⅔ AVANT d'ajouter la crème (concentre sans soupe)

**Carré de chocolat noir comme exhausteur umami dans un mijoté [complète Pattern 015]**

Un petit morceau de chocolat noir (70 %) en fin de mijotage d'un ragoût tomate-épices (poulet, agneau) apporte profondeur et umami sans goût sucré identifiable (logique du mole).
- ~15 g pour ~6 portions, ajouté en fin de cuisson à découvert, laisser fondre
- s'associe bien à harissa + paprika fumé + poivrons rôtis
- proposer : "mijoté qui manque de profondeur", touche secrète

**Extraire l'eau des légumes râpés crus avant de les lier [complète Pattern 013]**

Pour pain de viande, boulettes, galettes avec légumes crus râpés (courgette, carotte, oignon, tomate) : hacher au robot puis PRESSER fort dans une passoire avant de mélanger. Sinon l'eau relâchée détrempe et empêche la tenue.
- hacher à la taille du haché (consistance homogène)
- même principe que les galettes de légumes verts (presser petits pois, courgettes)

**Raffermir les croquettes/galettes au frigo avant cuisson [complète Pattern 013]**

Façonner puis réfrigérer 15 min minimum (ou jusqu'au lendemain) évite l'effondrement à la poêle et permet de tout préparer la veille.
- cuire à la poêle huile bien chaude (2-3 min/face) ou poêle + four ; on peut aussi cuire la veille et réchauffer
- mélange lié au robot par PULSATIONS courtes (pâte grossière, pas une purée)

---

## Récupérés après élagage (patterns distincts réinjectés)

**Pattern — Poulet mariné mijoté/rôti dans sa marinade aigre-douce (Marbella / miso-gingembre)**

Plat de réception zéro-stress : tout marine à l'avance, le four fait le reste, la marinade devient sauce.
```text
cuisses de poulet (peau, entaillées jusqu'à l'os) + marinade aigre-douce-salée → mariner 1-2 j frigo → étaler sur plaque + liquide (vin/bouillon) → four ~180-200°C 50-70 min, badigeonner 2-3× → servir avec tous les sucs
```
Familles de marinade : Marbella (ail-origan-vinaigre + olives vertes + câpres + dattes + laurier + vin blanc + mélasse de dattes) ; miso-gingembre-lime (miso blanc + mirin + érable + soja + gingembre + ail + lime) ; citron confit-thym-ail en beurre sous la peau.
Clés : entailler jusqu'à l'os (pénétration + cuisson homogène) ; sortir du frigo 30 min avant ; équilibre obligatoire d'un sucré (datte/sirop) + un acide (vinaigre/lime) + un salé (olive/câpre/miso). Proposer quand : « recevoir sans stress », « poulet à préparer la veille ».

**Pattern — Riz cuit au four sous papier scellé (méthode infaillible)**

Réussir le riz à tous les coups, sans surveillance, et pour grandes quantités.
```text
riz basmati + sel + beurre fondu + eau BOUILLANTE dans un plat à haut bord → couvrir HERMÉTIQUEMENT d'alu bien scellé → four 220-250°C 25 min → repos 10 min à couvert → aérer à la fourchette
```
Ratios : basmati ~1:2 (poids), sel ~¾ c. à thé, beurre ~50 g. Aromates posés DESSUS avant cuisson (menthe, cannelle, thym), retirés après.
Clés : eau déjà bouillante (jamais froide) ; sceller PARFAITEMENT (toute fuite de vapeur = riz raté) ; ne pas ouvrir avant la fin du repos.
Variante riz + légumes confits dessous : rôtir tomates cerises + ail + échalotes + herbes ~1 h à 180°C, parsemer le riz cru dessus sans mélanger, eau bouillante, sceller, 25 min.

**Pattern — Tarte/quiche salée aux légumes (appareil œuf-crème + fromage)**

Légumes pré-cuits dans une pâte croustillante et un appareil œuf-crème. Se mange tiède, voyage bien.
```text
pâte (brisée/feuilletée) cuite à blanc dorée + légumes pré-cuits (rôtis ou fondus) + fromage en morceaux + appareil (œufs + crème liquide + crème fraîche + sel, ~2 œufs/200 ml crème) versé pour combler les vides → four 160-180°C jusqu'à prise et dorure
```
Variantes : poivrons-aubergine-courgette rôtis ; poireau fondu ; ail confit ; épinards-féta. Fromages : 2 chèvres, gorgonzola, féta-ricotta, gruyère.
Clés : cuire la pâte à blanc lestée AVANT garniture (sinon fond détrempé) ; pré-cuire les légumes pour évacuer l'eau ; garder fromage apparent au-dessus pour gratiner ; four pas trop chaud (sinon appareil soufflé/granuleux).

**Pattern outil — Salsa froide d'aromates à l'huile chaude versée**

Condiment vif : verser une huile JUSTE chauffée sur des aromates crus — la chaleur les attendrit et libère les arômes sans les cuire. Topping universel (tomates, poulet rôti, tartine, riz).
```text
aromates frais crus (oignon vert + gingembre pilé avec le sel + piment) → verser dessus une huile neutre juste chauffée → +acide (vinaigre/lime) → repos → cuiller sur le plat
```
Variantes : oignon vert-gingembre-vinaigre de Xérès (Chinatown) ; +piment+coriandre (asiatique) ; échalote-piment-huile-citron.
Clés : huile JUSTE chaude, pas fumante (on attendrit, on ne frit pas) ; piler le gingembre avec le sel ; se garde 5 j au frigo, doubler. Distinct de l'huile infusée à feu doux : ici l'huile chaude va aux aromates crus.

**Pattern outil — Oignon caramélisé en lot (base aromatique à garder)**

Geste de prévoyance : caraméliser une grande quantité d'oignon une fois, garder, monter un plat en 5 min.
```text
oignons émincés + huile → feu moyen 9-15 min jusqu'à tendre et bien doré → (option +harissa/épice 1 min) → refroidir → bocal frigo 2-5 j
→ usage : œufs brouillés, omelette, frittata, salade de couscous, tofu brouillé, base de mijoté
```
Variantes : nature (universel) ; +harissa rose ; +cumin/ras-el-hanout (grains).
Clés : doubler/quadrupler systématiquement (effort marginal nul) ; l'épice en fin, 1 min, après caramélisation ; bien refroidir avant le bocal. Réflexe dès qu'une recette demande de caraméliser de l'oignon.

**Pattern outil — Topping de graines/noix grillées sucrées-épicées**

Transformer graines (courge, citrouille) ou noix en topping croustillant sucré-salé-piquant pour soupes, salades, légumes rôtis. Se fait en lot, garde une semaine.
```text
graines/noix + sirop d'érable (ou miel) + chili broyé + sel → étaler sur plaque → four ~15 min jusqu'à doré → REFROIDIR complètement (durcit en croustillant) → bocal hermétique 1 sem.
```
Variantes : graines de citrouille-érable-chili (soupe de courge) ; amandes effilées-paprika (poêle) ; noix-miel-sumac.
Clés : doubler/tripler ; refroidir complètement (mou à chaud) ; chili + sel équilibrent le sucre (sinon écœurant) ; amandes à la poêle brûlent vite. Réflexe dès qu'un plat manque de texture.

**Pattern outil — Beurre composé crémeux à tartiner (avocat + beurre)**

Enrichir une purée crémeuse (avocat surtout) au beurre ramolli pour une tartinade ultra-onctueuse. Sur pain grillé, fond sur viande chaude, se prépare la veille.
```text
avocat très mûr + beurre TRÈS MOU (jamais fondu) + zeste/jus agrume + sel → mixer lisse → incorporer herbes hachées → repos frigo 10 min → tartiner ou pocher
```
Variantes : avocat-beurre-lime-estragon-aneth ; beurre-herbes-ail (viande/poisson) ; beurre-miso-noisette (légumes rôtis).
Clés : beurre TRÈS mou, JAMAIS fondu (se séparerait) ; avocat vraiment mûr (sinon grumeleux) ; préparable 1 j à l'avance, séparé des garnitures. Distinct du beurre composé en boudin (maître d'hôtel).

**Pattern outil — Caviar (purée rustique) de légume rôti**

Légume rôti pressé et écrasé à la fourchette en tartinade rustique — entre baba ganoush et tapenade. Tartine, mezze, accompagnement de viande.
```text
légume (courgette, aubergine) rôti avec herbes sèches + huile → PRESSER pour extraire l'eau → ajouter ail rôti pressé → écraser à la FOURCHETTE (rustique, pas lisse) → herbes fraîches + citron au moment de servir
```
Variantes : courgette-thym-menthe-aneth ; aubergine-cumin (vers baba ganoush) ; +tahini ou yaourt.
Clés : extraire l'eau du légume (sinon liquide) ; écraser à la fourchette (pas mixé) ; ail rôti en chemise puis pressé ; herbes + citron seulement au service ; préparable 1 j à l'avance sans herbes/citron.

**Pattern — Tofu brouillé épicé (alternative végane aux œufs brouillés)**

Reproduire la texture d'œufs brouillés sans œuf — tofu soyeux écrasé dans une base aromatique épicée, sur pain grillé.
```text
oignons caramélisés + pâte aromatique épicée (harissa, curcuma, cumin) → tofu SOYEUX égoutté écrasé au PRESSE-PURÉE + sel → réchauffer 2 min → sur pain au levain grillé + salade fraîche acidulée à côté
```
Variantes : tofu-harissa-coriandre ; tofu-curcuma-cumin (style « œufs » indien) ; garniture échalotes frites, salade avocat-concombre-lime.
Clés : tofu SOYEUX (pas ferme) pour la texture ; écraser au presse-purée (pas au fouet) ; saler franchement (tofu neutre) ; ne pas trop cuire (rend de l'eau). Si seul tofu ferme dispo → basculer vers émietté sauté.

**Pattern — Œufs braisés en nids dans une base de légumes verts**

Variante « sèche » de la shakshuka — base de verts braisés où l'on creuse des nids pour pocher les œufs à couvert. Brunch/souper léger, 30 min.
```text
légume vert fondu (poireau/épinard/blette) + beurre-huile + aromate (cumin grillé, ail, citron confit) + bouillon réduit PRESQUE À SEC → creuser des nids à la cuillère → 1 œuf par nid + féta autour → couvrir 4-5 min (blanc pris, jaune coulant) → huile-zaatar
```
Clés : réduire le bouillon presque à sec avant les œufs (sinon ils flottent et ne cuisent pas) ; creuser de vrais nids au dos d'une cuillère ; cuire À COUVERT (la vapeur cuit le dessus du jaune). Délta vs shakshuka du corps = technique des nids + bouillon réduit à sec. Base verte préparable la veille.

**Pattern — Pain rapide salé sans levure ni pétrissage**

Pain-gâteau salé à la poudre à pâte/bicarbonate, sans levée ni pétrissage. Texture entre pain et cake, garni de légume râpé + fromage + graines. Se congèle, se grille.
```text
secs (farine + poudre à pâte + bicarbonate + sel + graines) // humides (œufs + huile + crème sure/yaourt + un peu de sucre/miel) → légume râpé (betterave, courgette, maïs) + fromage en morceaux → mélanger SANS EXCÈS → moule → four moyen 40-80 min → graines sur le dessus
```
Variantes : betterave-carvi-chèvre-graines de courge ; maïs-cheddar-féta-jalapeño (cornbread en poêle fonte).
Clés : ne pas trop mélanger (mie caoutchouteuse) ; fromage en morceaux délicatement ; cornbread = noircir le maïs à sec avant ; se grille bien rassis, congèle 1 mois.

**Pattern — Salade de fruits crus en registre salé (acide + herbe + épice)**

Traiter un fruit cru comme un légume de salade — bâtonnets nets, agrume vif, herbes, épice inattendue. Accompagnement d'été qui coupe le gras d'une viande grillée.
```text
fruit ferme en bâtonnets (melon d'eau, pomme verte, pêche) + agrume (lime/citron) + huile + aromate surprise (citronnelle, cinq-épices, échalote macérée) + herbes (menthe+coriandre) + graines grillées → assembler MINUTE, JETER le jus au fond du bol
```
Variantes : melon d'eau + pomme verte + lime + citronnelle + graines de moutarde ; pêche + framboise écrasée + cinq-épices + radicchio. Garniture : arachides/pistaches/cajou grillées salées.
Clés : fruits PAS trop mûrs (tiennent mieux, moins sucré) ; assembler juste avant de servir ; saler franchement (c'est une salade, pas un dessert).

**Pattern — Salade de rubans de légume cru massés à l'huile infusée**

Légume cru (courgette) en rubans fins, massé avec une huile parfumée pour l'assouplir sans cuisson. Garde du croquant.
```text
huile infusée à part (thym/ail/zeste, feu doux 8 min, filtrée) → légume en rubans fins (économe/mandoline) + noix + jus citron + sel → MASSER 1 min à la main (le légume se brise un peu) → herbes en finition
```
Variantes : courgette-thym-noix-basilic ; carotte/fenouil/asperge crue en rubans ; huiles ail-zeste, piment, cumin.
Clés : masser physiquement avec les doigts (assouplit, fait pénétrer l'huile) ; saler et citronner AU DERNIER MOMENT (sinon rend de l'eau) ; huile infusée préparable 3 j à l'avance. Distinct du slaw massé à l'acide : ici rubans + huile aromatique.

**Pattern — Grain monté à la pâte d'herbes (green couscous)**

Un grain devient vert et parfumé par une PÂTE d'herbes mixée à l'huile (pas des herbes ciselées en surface), incorporée au grain tiède. Saveur diffuse dans toute la bouchée.
```text
grain gonflé (couscous/boulgour) + pâte d'herbes mixée (3-4 herbes + huile) incorporée à la fourchette + oignon fondu au cumin + croquant (pistaches/amandes) + oignon vert + piment frais + roquette hachée → température ambiante
```
Variantes : pâte persil+coriandre (dominante)+estragon+aneth+menthe ; grains couscous/boulgour/quinoa/freekeh ; +féta (plus consistant).
Clés : mixer la pâte BIEN lisse à l'huile avant incorporation ; oignon-cumin tiède pas brûlant ; servir à T° ambiante (herbes restent vives). Repose sur la quantité d'herbes.

**Pattern — Polenta crémeuse en lit + garniture chaude**

La polenta molle sert de base apaisante (comme une purée) sous une garniture intense. Deux gestes : polenta enrichie + poêlée/sauce chaude au centre.
```text
bouillon bouillant + polenta en pluie → cuire en remuant jusqu'à porridge épais (se détache des parois mais reste coulant) → HORS feu : parmesan/féta + beurre + herbe → étaler en lit → garniture chaude au centre (champignons à l'ail-estragon-truffe, sauce aubergine-tomate)
```
Variantes : enrichissement parmesan+beurre (+Taleggio gratiné au gril) ou féta ; option gratin (couvrir de fromage, gril, puis garnir) ; restes étalés froids puis poêlés (croûtons).
Clés : fromage/beurre HORS feu ; garniture chaude et juteuse (ses jus = la sauce) ; rallonger au bouillon si ça sèche ; servir IMMÉDIATEMENT (fige). Distinct de la polenta de maïs frais.

**Pattern — Couscous d'hiver (racines rôties aux épices entières)**

Couscous chaud copieux où les racines sont rôties avec des épices ENTIÈRES (cannelle, badiane, laurier) pour un fond profond, relevé en finition par harissa + citron confit.
```text
racines + courge + grelots + épices entières (cannelle, badiane, laurier) + épices moulues + huile → four en deux temps → ajouter abricots secs + pois chiches AVEC leur jus → couscous safrané gonflé au beurre → FINITION : harissa + citron confit haché mélangés aux légumes + coriandre généreuse
```
Variantes : carotte, panais, navet, grelots, butternut ; fruits secs abricots/dattes/raisins.
Clés : rôtir en deux temps (dures d'abord, courge ensuite) ; garder le jus des pois chiches ; harissa + citron confit incorporés EN FIN (pas en cuisson) ; couscous gonflé à part au bouillon safrané, aéré à la fourchette.

**Pattern — Légumes char-grillés (poêle striée/plancha) + huile d'herbes vive**

Griller les légumes sur poêle striée/plancha brûlante leur donne un goût presque carné (fumée + parties brûlées) ; une huile d'herbes crue versée sur les légumes chauds les imprègne.
```text
légumes tranchés huilés + salés → poêle striée/gril TRÈS chaud (5 min de chauffe), marques nettes des 2 côtés sans cuire à cœur → huile d'herbes mixée crue (herbes + huile + ail + citron + sel) versée sur les légumes CHAUDS → tiédir et infuser
```
Variantes : courgette, aubergine, chou-rave, fenouil, asperge, poivron, carotte ; fromage grillé à part (halloumi, manouri) ; huiles persil-ail-citron, basilic, coriandre-lime ; finitions pignons, parmesan, sumac.
Clés : gril vraiment brûlant (sinon les légumes suent, pas de marques) ; huiler les légumes pas la poêle, ne pas surcharger ; l'aubergine peut finir au four ; verser l'huile d'herbes à chaud (meilleure absorption).

**Pattern outil — Panure croustillante aux graines + épices (schnitzel revisité)**

Panure qui croustille mieux et parfume : panko enrichi de graines variées et d'épices. Polyvalente viande/poisson/légume.
```text
farine salée-poivrée → œuf battu → panko + graines (sésame blanc+noir, tournesol concassé, coriandre broyée) + épices (curcuma, cayenne) + sel → frire dans ~½ cm d'huile chaude, retourner à mi-cuisson, 5-6 min jusqu'à doré
```
Clés : aplatir la viande (~1 cm) entre deux films pour cuisson rapide ; huile BIEN chaude (sinon la panure boit l'huile) ; frire par petites quantités (ne pas faire chuter la T°) ; le mélange panko+graines se prépare en grande quantité (garde ~1 mois en bocal) ; marche aussi sur lanières de poisson blanc, bâtonnets de butternut.

