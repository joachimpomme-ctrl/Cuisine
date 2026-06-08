# Patterns de plats & planification

_Bundle Gem consolidé regroupant : 08-ottolenghi-patterns.md, 20-planification-menus.md_



<!-- ===== 08-ottolenghi-patterns.md ===== -->

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

_110 entrées ajoutées, auditées (verdict ≠ rejected). Sources : Ottolenghi Simple, Plenty, Ducasse (patterns transposables)._

### data

**Accords fromage + fruit (Plenty) prets a dresser**

Accords simples fromage/fruit, format "composer sans cuire" :
- Figues fraiches mures + chevre frais cremeux + roquette/basilic + vinaigrette a la melasse de grenade.
- Poire (mi-mure, ferme et un peu acidulee, PAS trop mure sinon elle se defait) + chevre affine OU parmesan/pecorino, sur crostini.
- Dattes Medjool + fromage de brebis sale (ou ricotta/mozzarella de bufflonne) + roquette + amandes grillees + melasse de grenade.
- Pasteque + feta + basilic + (option oignon rouge tres fin) + filet d'huile : le sucre juteux contre le sale friable.
Repere figues : lourdes, legerement molles, parfum sucre net, souvent fendues a la base.

### definition

**Citron/lime seches de Perse : usage et preparation**

Citrons (ou limes) seches iraniens : petits agrumes durcis qui apportent une acidite et un parfum unique.
- Plats mijotes/marinades : en jeter un entier, legerement perfore, qui infuse tout le plat (le retirer avant de servir).
- Salades/assaisonnements : utiliser en poudre. Ils sont durs comme la pierre, un moulin a epices marche bien ; au robot, tamiser ensuite.
- La poudre maison est plus puissante que celle du commerce.
Profil : aigreur vive + arome parfume ; quelques cuilleres suffisent.

### pattern

**Pattern outil — Panure aux graines (schnitzel revisité)**

## Pattern outil — Panure croustillante aux graines + épices

### Intention
Une panure qui sort de l'ordinaire : panko enrichi de graines variées et d'épices, qui croustille mieux et parfume. Polyvalente sur viande, poisson, légume.

### Pattern réutilisable
```text
farine salée-poivrée → œuf battu → panko + graines (sésame blanc+noir, tournesol concassé, coriandre broyée) + épices (curcuma, cayenne) + sel → frire dans ~1/2 cm d'huile chaude, retourner à mi-cuisson, 5-6 min jusqu'à doré
```

### Points critiques
- aplatir la viande (~1 cm) entre deux films pour cuisson rapide et homogène
- huile **bien chaude** (pas tiède) sinon la panure boit l'huile
- frire par petites quantités pour ne pas faire chuter la température
- le mélange panko+graines se prépare en grande quantité et se garde ~1 mois en bocal
- s'utilise aussi sur lanières de poisson blanc, bâtonnets de courge butternut

### Usage Gemini
- proposer quand : « escalope/schnitzel », « panure qui change », « plat que les enfants aiment »
- déclencheurs : schnitzel, panure graines, poulet pané maison

**Pattern — Crème montée légère parfumée (finition poisson/entrée)**

## Pattern outil — Crème fouettée légère parfumée comme nappage d'entrée

### Intention
Alternative fraîche au yaourt pour napper un poisson poêlé ou une entrée : crème montée souple, allégée de crème sure, parfumée d'un jus aromatique.

### Pattern réutilisable
```text
crème 35 % fouettée ferme + crème sure pliée dedans + jus aromatique (jus de gingembre pressé, zeste) + sel → texture souple → déposer sous/à côté de la protéine + salsa croquante
```

### Points critiques
- presser le gingembre râpé dans une passoire pour extraire le JUS seul (pas la pulpe)
- plier la crème sure délicatement : on veut souple, pas ferme
- contraste : crème froide / poisson chaud à peau croustillante / salsa croquante
- se réfrigère jusqu'au service

### Usage Gemini
- proposer quand : « napper un poisson finement », « entrée chic », alternative au yaourt
- déclencheurs : crème au gingembre, nappage poisson

**Pattern — Salade tiède de protéine + légumes grillés poêle striée + vinaigrette vive**

## Pattern — Salade de protéine + légumes grillés à la poêle striée + vinaigrette vive

### Intention
Tout est passé à la poêle striée brûlante (marques de grill, noirci par endroits), réuni tiède, puis lié par une vinaigrette acide et relevée. Le contraste fumé/frais fait le plat.

### Pattern réutilisable
```text
légumes/fruits robustes (oignon en quartiers, maïs, tomates cerises) grillés successivement à la poêle striée brûlante jusqu'à marques + noircissement → protéine grillée en dernier (crevettes, calmar, bifteck) → réunir tiède dans un saladier → vinaigrette (gingembre + sriracha + huile + zeste/jus lime + pincée sucre) + herbe (marjolaine, basilic) → mélanger délicatement
```

### Variantes
- protéines : crevettes, calmar, bifteck saignant émincé, poulet
- légumes grillés : maïs, oignon rouge, tomates cerises, poivrons, courgettes
- vinaigrette : gingembre-sriracha-lime, soja-sésame-lime, citron-ail-piment

### Points critiques
- griller chaque ingrédient SÉPARÉMENT (temps de cuisson différents) ; bien ventiler la cuisine
- chercher les marques de grill et le noircissement : c'est la saveur
- assembler tiède, jamais brûlant (herbes flétries) ni froid frigo
- vinaigrette préparable jusqu'à 2 jours à l'avance

### Usage Gemini
- proposer quand : "salade-repas d'été", "crevettes ou calmar à passer", "j'ai une poêle à griller"
- éviter quand : pas de poêle striée ni grill, repas réconfortant chaud recherché

**Pattern — Mijoté de fruits de mer (calmar/poulpe) + poivron + zeste d'orange**

## Pattern — Fruit de mer mijoté doucement + poivron-tomate + zeste d'agrume final

> Note : la recette source ("calmars au poivron rouge") est déjà citée comme source du Pattern 015 (mijoté à la cocotte). Ce pattern en isole la spécificité fruit de mer (gestion de la texture du calmar, zeste d'orange final), non détaillée dans le 015. À traiter comme sous-cas/renvoi du 015.

### Intention
Une casserole, mijotage tranquille pendant qu'on fait le reste. Le calmar (ou poulpe), souvent jugé difficile, devient tendre par une cuisson lente à couvert. Meilleur le lendemain.

### Pattern réutilisable
```text
oignon + poivron rouge fondus → ail + épices chaudes (carvi, piment de la Jamaïque, laurier, thym) → calmar en lanières, saisir court → pâte de tomate + vin rouge → couvrir, feu doux, mijoter ~30 min jusqu'à tendreté → zeste d'orange râpé à la toute fin
```

### Variantes
- bases : calmar, poulpe, seiche
- épices : carvi, piment de la Jamaïque, laurier, thym, paprika fumé
- liquide : vin rouge, ou bouillon
- finition : zeste d'orange (signature), persil

### Points critiques
- le calmar passe par une phase caoutchouteuse puis redevient tendre : ne pas s'arrêter trop tôt
- ajouter un peu d'eau si la sauce épaissit trop en fin de cuisson
- zeste d'agrume APRÈS le feu (arômes volatils)
- encore meilleur préparé 1-2 jours avant et réchauffé

### Usage Gemini
- proposer quand : "calmar/poulpe à cuisiner", "plat de la mer à préparer la veille", "tapas"
- éviter quand : envie de calmar croustillant minute (autre technique)

**Pattern — Barres frigo chocolat-garde-manger (no-bake, vide-placard)**

## Pattern — Barres au frigo : chocolat fondu + biscuits + noix + fruits secs (vide-placard)

### Intention
Dessert "libère le garde-manger" : on lie au chocolat fondu tout ce qu'on a sous la main. Pas de cuisson, prend au frigo.

### Pattern réutilisable
```text
chocolats + beurre + sirop doré (ou de maïs) + pincée de sel fondus au bain-marie → hors feu, incorporer biscuits cassés + noix concassées + fruits secs (trempés dans alcool, option) → presser dans un plat tapissé → frigo 2-3 h → couper en barres, servir bien froid
```

### Variantes (tout est substituable)
- chocolats : noir 70 %, aromatisés (menthe, gingembre, chili)
- biscuits : digestifs, sablés, spéculoos
- noix : pistaches, noisettes, amandes
- fruits secs : raisins (trempés rhum), cerises séchées, abricots

### Points critiques
- fondre au bain-marie doucement, eau frémissante, fond du bol hors de l'eau
- garder un peu de noix en fine poudre pour parsemer le dessus
- bien presser/égaliser avant le frigo (sinon barres friables)
- conservation : 1 semaine en boîte hermétique au frigo

### Usage Gemini
- proposer quand : "dessert sans cuisson", "vider le placard", "chocolat + biscuits + noix"
- éviter quand : dessert chaud recherché

**Pattern — Gâteau moelleux aux fruits déposés en surface (friand/clafoutis/gâteau)**

## Pattern — Gâteau moelleux aux fruits déposés en surface (friand, clafoutis, gâteau aux pommes)

> Complète le Pattern 024 (gâteau amande-citron + fruit) en couvrant les formats friand / clafoutis / gâteau crème sure, où les fruits sont déposés en surface et le gâteau lève autour.

### Intention
Gâteau "maison réconfortant" : pâte simple versée au plat, fruits de saison disposés dessus, le gâteau lève autour d'eux.

### Pattern réutilisable
```text
fruits macérés court (sucre + vanille + épice/herbe : laurier, cannelle, thym) → pâte légère (friand : blancs montés + amandes moulues + peu de farine + beurre fondu ; OU clafoutis : jaunes-farine-crème + blancs en neige pliés ; OU gâteau crème sure) → verser au plat → disposer les fruits + leur jus dessus → cuire jusqu'à doré et fruits bouillonnants
```

### Variantes
- fruits : prunes-mûres, figues, pêches-framboises, pommes (Cortland + Granny), bleuets ; substituer selon la saison
- aromate : laurier, thym, cannelle, mélange épices à tarte, vanille
- garniture sucre : demerara/cassonade en surface pour croûte croustillante

### Points critiques
- macérer les fruits 30 min MAX (au-delà ils rendent trop de jus et détrempent)
- couvrir d'alu en fin de cuisson si ça dore trop vite
- gâteau aux pommes : le cure-dent ne ressort PAS propre (humidité des fruits) ; tester par "le dessus ne tremblote pas"
- gâteaux aux noix/amandes : sèchent vite, manger dans les 1-2 jours

### Usage Gemini
- proposer quand : "gâteau aux fruits de saison", "clafoutis", "dessert maison réconfortant"
- éviter quand : besoin d'un gâteau qui se conserve longtemps

**Gazpacho vert : crudités + noix + pain + glace mixés (tarator)**

Soupe froide verte, plus dense qu'un gaspacho classique (inspirée du tarator balkanique).

Formule :
légumes verts crus (concombre + poivron vert + céleri) + épinard/basilic/persil cru + ail + piment vert + pain rassis (corps) + noix grillées (corps + gras) + vinaigre de Xérès + huile + yaourt + glaçons + sel → mixer lisse → ajuster eau.

Clés :
- noix et pain donnent l'onctuosité sans cuisson
- glaçons : sert glacé immédiatement et allège
- finition : croûtons huile-sel maison à part

Différent du gaspacho rouge : registre vert/herbacé, texture plus nappante. (Recoupe le Pattern 005 'soupe froide' mais ajoute le levier corps = pain + noix.)

**Salade de tomates multi-textures (crues + rôties à degrés variés)**

Mettre en valeur plusieurs variétés/couleurs de tomates en jouant les textures.

Principe : maximiser l'effet 'tomate' en cuisant différemment selon le morceau.
- certaines laissées CRUES (jus, fraîcheur)
- certaines rôties douces (~20 min à 160°C, sucre brun + balsamique + huile)
- certaines rôties plus fort/court (~12 min à 200°C)
→ réunir avec un grain neutre (couscous, fregola, perles), herbes multiples (origan + estragon + menthe), ail, et les jus de rôtissage. Mélanger à la main, délicatement.

Idée transférable : varier les cuissons d'un même légume crée de la profondeur sans ajouter d'ingrédients.

**Légume-coquille farci aux herbes (saler-égoutter d'abord)**

Entrée provençale rapide : légume évidé, farci d'une farce herbacée.

Formule :
légume évidé (tomate ferme, courgette) → SALER l'intérieur + retourner pour égoutter l'eau → farce : oignon + ail + olives fondus à l'huile, hors feu + panko + herbes multiples (origan, persil, menthe) + câpres → remplir en dôme → four moyen jusqu'à tendreté.

Clés :
- saler/égoutter le légume évite une farce détrempée
- panko ajouté HORS feu garde du croquant
- olives + câpres = sel/umami sans viande

Servir avec petite salade + chèvre.

**Mijoté légumineuse + acidité INTÉGRÉE dès le départ (tamarin)**

Mijoté qui tient son acidité de l'intérieur, pas seulement en finition.

Formule :
légumineuse (pois chiches) + légume terreux/amer (blettes blanchies) + base oignon-graines (carvi, coriandre) + tomate + PÂTE DE TAMARIN diluée + sucre → mijoter ~30 min jusqu'à consistance de soupe épaisse.

Idée clé : sur les mijotés 'sérieux', Ottolenghi veut toujours une acidité vive pour casser la lourdeur. Ici elle est dans le plat dès le début (tamarin + blettes), pas seulement un filet de citron à la fin (qu'on peut quand même ajouter, + piment).

Servir sur riz avec cratère central + yaourt + coriandre. (Nuance les Patterns 007/015 SIMPLE où l'acide est surtout une finition.)

**Beurre noisette + amandes/aromates versé sur légume rôti**

## Pattern — Beurre noisette aromatique versé sur légume rôti/grillé [outil de finition]

**Intention** : finition rapide qui donne profondeur et richesse à un légume cuit — beurre bruni avec amandes, câpres frites ou ail, versé chaud au service.

### Pattern réutilisable
```text
légume rôti/grillé → beurre fondu jusqu'à brun foncé (noisette) avec amandes effilées OU câpres OU ail/épice broyée → verser chaud sur le légume → acide (citron) + herbe fraîche en finition
```

### Variantes
- amandes effilées dorées + câpres frites + aneth (asperges)
- beurre noisette + ail/carvi + graines de courge + tahini en filet (choux de Bruxelles, ail noir)
- câpres frites croustillantes seules (sur tout vert)

### Points critiques
- surveiller le beurre : de noisette à brûlé en quelques secondes
- câpres bien épongées avant friture (éclaboussent) ; cuire jusqu'à ce qu'elles s'ouvrent et croustillent
- servir immédiatement, le beurre fige en refroidissant

### Usage Gemini
- proposer quand : "finir des asperges/brocolis/choux de manière gourmande", "beurre + légume du week-end"
- éviter quand : version sans lactose (basculer huile d'olive chaude + aromates)

**Charcuterie épicée + légume-feuille braisé + acide + crème**

## Pattern — Chorizo/charcuterie + légume-feuille braisé + citron confit + crème

**Intention** : un vert robuste rendu gourmand et complet — le gras épicé du chorizo le parfume, le citron confit apporte le punch acide-salé, une cuillerée de crème lie le tout.

### Pattern réutilisable
```text
chorizo/charcuterie + ail + paprika fumé saisis → retirer et réserver
vert braisé dans le gras parfumé (un peu d'eau, couvert puis découvert jusqu'à tendre-croquant)
remettre la charcuterie + citron confit haché + jus citron → hors feu, crème sure soulevée délicatement
```

### Variantes
- chou palmier/kale + chorizo + citron confit + crème sure
- bette/épinards + lardons/pancetta + citron + crème
- service : en tapas, ou avec viande/légumes grillés

### Points critiques
- saisir la charcuterie d'abord, la retirer, braiser le vert dans son gras coloré
- garder les feuilles tendres mais encore un peu croquantes, pas en bouillie
- crème ajoutée hors feu pour ne pas trancher

### Usage Gemini
- proposer quand : "chou frisé/bette + du chorizo", "tapas", "accompagnement réconfortant rapide"
- éviter quand : végétarien (mais le vert braisé + citron confit + crème tient seul)

**Glaçage aigre-doux harissa-miel appliqué AVANT rôtissage**

## Pattern — Glaçage aigre-doux épicé (harissa-miel) appliqué AVANT rôtissage

**Intention** : carottes/racines enrobées d'une marinade épicée-sucrée avant le four, qui caramélise et laque le légume. Différent d'une sauce ajoutée après : ici le glaçage cuit sur le légume.

### Pattern réutilisable
```text
bol : épice (cumin) + sucre (miel) + pâte piquante (harissa) + beurre fondu + huile + sel → enrober le légume → rôtir four très chaud jusqu'à doré mais encore croquant → finition fraîche après (grenade + coriandre + jus citron)
```

### Variantes
- carottes + cumin + miel + harissa rose + beurre, finition grenade+coriandre
- racines (panais, betterave) + même glaçage
- glaçage alternatif : paprika fumé + miel ; ras-el-hanout + miel

### Points critiques
- le miel dans la marinade fait caraméliser ET peut brûler : surveiller, garder le légume croquant
- ne pas trop serrer sur la plaque (sinon vapeur, pas de laque)
- finition fraîche (grenade, herbes, citron) obligatoire pour contraster le sucré-épicé

### Usage Gemini
- proposer quand : "carottes qui en jettent", "légume rôti coloré et épicé", "à-côté pour agneau/poulet"
- éviter quand : aversion au piquant (réduire la harissa)

**Sauce chraimeh (épices-ail-tomate-sucre-lime) pour poisson/légumes [outil]**

## Pattern — Sauce chraimeh : pâte d'épices frite + tomate + sucre + lime [outil condiment]

**Intention** : sauce piquante libyenne rouge, intense, qui nappe poisson, légumes ou tofu. Se conserve longtemps, se congèle. Alternative chaleureuse à la sauce tomate banale.

### Pattern réutilisable
```text
pâte : ail pressé + épices (paprika fort + carvi + cumin + cannelle) + huile → frire la pâte 1 min (réveiller les arômes) → pâte de tomate + sucre + jus de lime + sel → eau pour éclaircir → mijoter jusqu'à épaississement → y finir la protéine/le légume
```

### Variantes
- haricots verts + tofu doré (plat végé)
- poisson blanc ou poulet poché dans la sauce
- trempette avec du pain
- se garde 1 semaine au frigo / 1 mois au congélateur : doubler/tripler

### Points critiques
- frire la pâte d'épices+ail dans l'huile AVANT le liquide (sinon arômes plats)
- pincée de sucre obligatoire pour équilibrer le piquant et l'acide
- éclaircir à l'eau, ajuster la consistance

### Usage Gemini
- proposer quand : "sauce épicée pour poisson/tofu/poulet", "changer de la sauce tomate", "batch de condiment à congeler"
- éviter quand : aversion au piquant fort

**Gratin de légume : crème-fromage-épices + croûte chapelure**

## Pattern — Gratin de légume crémé épicé + croûte chapelure-fromage

**Intention** : un légume (chou-fleur, etc.) en gratin réconfortant mais relevé d'épices, avec une sauce crème-fromage rapide (pas de béchamel) et une croûte croustillante finie sous le gril.

### Pattern réutilisable
```text
légume à peine cuit vapeur (ferme) → sauce express : oignon fondu + épices (cumin/cari/moutarde/piment) + crème + fromage fondu jusqu'à léger épaississement → mêler le légume → couvrir d'un mélange chapelure+fromage+persil → four puis gril jusqu'à doré-croustillant
```

### Variantes
- chou-fleur + cumin/cari/moutarde sèche+graines+piments verts + cheddar vieilli
- croûte : mie de pain + cheddar + persil
- préparable la veille jusqu'à l'étape four

### Points critiques
- légume cuit ferme à la vapeur (il finira au four) — pas de bouillie
- sauce crème-fromage juste épaissie, pas réduite à mort
- essuyer les parois du plat (la crème brûle) ; surveiller sous le gril pour ne pas carboniser la croûte

### Usage Gemini
- proposer quand : "gratin de chou-fleur qui change", "plat réconfortant à préparer la veille", "à-côté de poulet rôti/saucisses"
- éviter quand : intolérance lactose, repas léger

**Gros champignon farci fromage fondant + duxelles-tomate séchée**

## Pattern — Portobello farci fromage fondant

### Intention
Gros chapeau de champignon comme coupelle : pré-rôti pour ramollir et évacuer l'eau, garni d'une farce umami, couronné d'un fromage qui fond bien, repassé au four.

### Pattern réutilisable
```text
gros champignons (portobello) pré-rôtis 15 min → farce sautée refroidie (oignon + céleri + tomates séchées + ail + parmesan + herbes) → garnir + tranches de fromage fondant dessus → four jusqu'à fonte et champignon tendre
```

### Variantes
- fromage fondant (clé) : taleggio, fontina, mozzarella, scamorza fumée
- farce : duxelles ; épinards-ricotta ; chèvre-noix
- herbes : estragon, basilic, thym

### Points critiques
- choisir un fromage jeune/gras qui fond lisse ; les fromages très affinés (gruyère, vieux cheddar) se séparent et deviennent granuleux
- pré-rôtir le champignon pour évacuer l'eau avant de garnir
- saler la farce avec mesure si le fromage est salé (taleggio)

### Erreurs fréquentes
- fromage trop affiné → graine et devient huileux ; champignon non pré-rôti → rend de l'eau dans l'assiette

### Usage Gemini
- proposer quand : gros champignons, entrée végé chaude, plat sans viande qui rassasie
- éviter quand : petits champignons (pas de cavité)

**Salade betterave + agrume + élément salé (olive/chèvre)**

## Pattern — Salade betterave + agrume + contraste salé

### Intention
La douceur terreuse de la betterave sert de fond à l'acidité vive de l'agrume et au salé d'une olive ou d'un fromage : trio sucré-acide-salé simple et net.

### Pattern réutilisable
```text
betterave cuite en quartiers + segments d'agrume levés à vif (avec leur jus) + élément salé (olives noires séchées OU chèvre/féta) + oignon rouge fin + herbe → vinaigrette légère (huile + vinaigre/fleur d'oranger) → mélanger délicatement
```

### Variantes
- agrumes : orange, sanguine, pamplemousse
- salé : olives noires ridées (plus salées), féta, chèvre, gorgonzola
- amer/feuille : trévise, endive, cresson
- aromate : eau de fleur d'oranger, carvi, aneth

### Points critiques
- lever les segments d'agrume à vif et récupérer le jus (= acide de la vinaigrette)
- cuire la betterave entière puis peler (garde couleur et saveur)
- mélanger en dernier et peu, pour éviter que tout vire au rose

### Erreurs fréquentes
- agrume avec membranes → amer et filandreux ; trop mélangé → couleur terne

### Usage Gemini
- proposer quand : betteraves, salade d'hiver colorée, entrée fraîche acidulée

**Tempura/friture légère de légumes de saison + sauce trempette agrume**

## Pattern — Tempura de légumes (pâte légère à l'eau gazeuse) + trempette

### Intention
Légumes de saison enrobés d'une pâte ultra-légère à l'eau gazeuse, frits croustillants, trempés dans une sauce vive et acide. Le contraste croquant-chaud / sauce-fraîche-acide fait tout.

### Pattern réutilisable
```text
légumes en morceaux → roulés dans la fécule sèche (accroche) → trempés dans pâte légère (fécule + farine levante + EAU GAZEUSE très froide + sel + huile) → friture à grésillement franc (pas brûlante) → égoutter, saler → trempette (agrume + herbe + piment + sucre + huile mixés)
```

### Variantes
- légumes : topinambour, betterave, brocoli, chou-fleur, patate douce, carotte, poireau, panais
- pâte : fécule de maïs + farine levante + eau gazeuse (clé du croustillant)
- trempette : lime-coriandre-cardamome-piment ; soja-gingembre-vinaigre de riz

### Points critiques
- eau gazeuse très froide + pâte mélangée au dernier moment = légèreté
- pré-enrober de fécule sèche pour que la pâte accroche
- huile à température modérée : grésille franchement sans brûler
- frire en petites quantités, retirer les morceaux brûlés flottants

### Erreurs fréquentes
- pâte tiède/reposée → lourde ; huile trop chaude → brûlé dehors cru dedans, trop froide → gras ; friteuse surchargée → chute de température

### Usage Gemini
- proposer quand : tempura, légumes variés à frire, apéro/entrée croustillante, vide-frigo de légumes
- éviter quand : pas d'huile en quantité ; cf. pattern poisson pané frit (SIMPLE) pour la pâte à bière

**Pattern — Salade de riz tropicale (fruit + croquant)**

## Pattern — Salade de riz tropicale (fruit + croquant)

**Intention** : salade de riz fraîche d'inspiration sud-est asiatique : riz colorés froids, fruit mûr en dés, herbes thaï, vinaigrette agrume-piment, et double croquant (cacahuètes + oignons/échalotes frits).

### Formule
```text
riz cuits froids (jasmin parfumé au basilic + riz rouge) + fruit en dés (mangue) + poivron émincé + herbes (basilic thaï, coriandre, menthe) + oignon vert + piment frais + zeste/jus citron + huile arachide → mélanger DÉLICATEMENT → garnir cacahuètes + coco grillée + échalotes frites
```

### Variantes
- riz : jasmin/basmati + riz rouge de Camargue (contraste couleur/texture)
- fruit : mangue (Alphonso idéal), ananas, papaye verte
- croquant : cacahuètes grillées salées, copeaux de coco, échalotes frites
- vinaigrette : citron/lime + piment + huile arachide (+ trait de nuoc-mâm)

### Points critiques
- riz BIEN refroidi et étalé pour qu'il ne colle pas
- parfumer le riz jasmin à la cuisson (bouquet de basilic thaï dans l'eau, retiré ensuite)
- mélanger DÉLICATEMENT : le fruit mûr se défait sinon
- éléments croquants au tout dernier moment

### Usage Gemini
- proposer : « salade de riz qui change », « mangue mûre à utiliser », « accompagnement exotique frais »
- éviter : fruit pas assez mûr (plat fade)

**Pattern — Salade de grains tiède + huile d'herbes frites**

## Pattern — Salade de grains tiède + huile d'herbes frites

**Intention** : mélange quinoa + riz tiède où la saveur vient d'une HUILE D'HERBES FRITES (ail doré + sauge/origan frits) versée chaude sur les grains, plus un légume rôti et un acide poudré (citron séché de Perse / sumac).

### Formule
```text
quinoa + riz cuits tièdes + légume rôti (patate douce) → huile chaude : ail doré 30 s + sauge/origan frits ~1 min, versée aussitôt sur les grains → menthe + oignon vert + jus citron + féta + acide poudré → tiède ou ambiant
```

### Variantes
- grains : quinoa + basmati/sauvage, boulgour, freekeh
- légume rôti : patate douce, courge, betterave, chou-fleur
- huile d'herbes : ail + sauge + origan ; ail + romarin ; ail + thym
- acide poudré : citron séché (lime de Perse) moulu, sumac, zeste séché
- ajout salé : féta émietté

### Points critiques
- frire l'ail JUSTE doré (30 s) puis les herbes ~1 min sans brûler, verser tout de suite
- grains encore tièdes pour absorber l'huile aromatique
- mélanger DÉLICATEMENT (ne pas écraser légume rôti + féta)
- citron séché moulu = note acide-parfumée unique (sinon sumac)

### Usage Gemini
- proposer : « salade de grains nourrissante », « patate douce + féta », « plat unique tiède »
- éviter : besoin de chaud réconfortant

**Pattern — Salade de pâtes + légume frit mariné + sauce d'herbes**

## Pattern — Salade de pâtes + légume frit mariné + sauce d'herbes

**Intention** : salade de pâtes de pique-nique où le légume est FRIT puis aussitôt arrosé de vinaigre (mariné chaud), lié par une sauce d'herbes mixée crue, avec mozzarella déchirée. Riche mais vive.

### Formule
```text
courgettes en tranches frites dorées → arrosées de vinaigre à chaud → pâtes courtes cuites, rincées froides → sauce mixée (basilic + persil + huile) + zeste citron + câpres + mozzarella déchirée + edamame → mélanger délicatement
```

### Variantes
- légume frit-mariné : courgette, aubergine, poivron
- pâtes : strozzapreti, penne, fusilli, orecchiette
- sauce mixée : basilic-persil-huile ; roquette-amande ; menthe-pistache
- ajouts : edamame ou petits pois, câpres, mozzarella ou burrata

### Points critiques
- frire les tranches sans surcharger, retourner UNE fois, égoutter
- vinaigre versé À CHAUD sur le légume frit (s'imprègne en refroidissant)
- rincer les pâtes à l'eau froide (stopper la cuisson)
- mozzarella + reste de basilic ajoutés en TOUT dernier

### Usage Gemini
- proposer : « salade de pâtes pour pique-nique », « courgettes à valoriser », « plat froid d'été »
- éviter : on veut chaud / léger en gras (friture)

**Pattern — Polenta de maïs frais + sauce**

## Pattern — Polenta de maïs frais + sauce

**Intention** : une « polenta » douce et soyeuse faite de MAÏS FRAIS mixé (pas de semoule de maïs), enrichie de beurre et féta, servie sous une sauce tomate-aubergine. Texture purée sucrée, réconfortante.

### Formule
```text
grains de maïs frais cuits ~12 min → mixés LONGUEMENT (casser les peaux) avec un peu de leur eau → recuits en remuant jusqu'à consistance purée → beurre + féta + sel/poivre, 2 min de plus → lit, avec sauce chaude au centre (aubergine frite + concentré + tomate + origan)
```

### Variantes
- enrichissement : beurre + féta ; beurre + parmesan ; crème
- sauce : aubergine-tomate-origan, champignons, ragoût épicé
- saison : strictement maïs frais en épi (rien à voir avec la polenta de semoule)

### Points critiques
- mixer LONGUEMENT pour briser un maximum de peaux (texture lisse)
- réserver l'eau de cuisson du maïs pour ajuster la consistance
- beurre + féta en fin
- plus mou et moins consistant qu'une polenta classique : assumer

### Usage Gemini
- proposer : « maïs frais en saison », « plat doux et réconfortant », « alternative originale à la purée »
- éviter : hors saison maïs (surgelé/conserve donne moins bien)

**Pattern — Salade fruit poché + bleu doux + noix**

## Pattern — Salade fruit poché + bleu doux + noix

**Intention** : un fruit ferme poché longuement dans un sirop épicé (eau-sucre-vin, zeste agrume, laurier, poivre) devient fondant et parfumé, posé sur feuilles amères avec un bleu doux et des pistaches. Le sirop de pochage sert aussi de base de vinaigrette.

### Formule
```text
fruit ferme poché à couvert au four doux en sirop (eau + sucre + vin + zeste orange + laurier + poivre + jus citron) jusqu'à tendre → feuilles amères + bleu doux en éclats + pistaches → vinaigrette : moutarde + vinaigre + huile + qq c. du sirop de pochage
```

### Variantes
- fruit : coing (~2 h), poire ferme, pomme, prune
- fromage : gorgonzola doux, roquefort, stilton, bleu d'Auvergne
- feuilles amères : mizuna, pissenlit, cresson, trévise/radicchio
- noix : pistaches, noix, noisettes
- bonus : le sirop restant, réchauffé, nappe une glace vanille

### Points critiques
- pocher À COUVERT à four doux jusqu'à tendreté complète (le coing est dur, prévoir du temps)
- garder peaux + cœurs dans le sirop (couleur + pectine)
- la vinaigrette intègre une cuillère du sirop (lien sucré-acide)
- monter la salade en hauteur, fromage en éclats à la main

### Usage Gemini
- proposer : « entrée chic d'automne/hiver », « coing ou poire ferme », « accord bleu + fruit »
- éviter : peu de temps (pochage long), fruit déjà très mûr (se déferait)

**Pattern — Crostini fruit + fromage**

## Pattern — Crostini fruit + fromage

**Intention** : tartine chaude où le pain est badigeonné d'une pâte de noix-ail-huile puis grillé, surmonté de fruit ferme marqué au gril et de fromage qui fond à peine. Accord pain-fromage-fruit italien, en bouchée tiède.

### Formule
```text
pain épais badigeonné de pâte mixée (pignons + ail + huile + sel) → grillé au four → fruit FERME tranché, sucré-citronné, marqué au gril (rayures) → chèvre/parmesan en lamelles dessus → court passage four (3-4 min) pour fondre à peine → poivre + huile + cerfeuil
```

### Variantes
- fruit : poire mi-mûre, figue, pomme, raisin (fermes, pas blets)
- fromage : chèvre affiné, parmesan, pecorino, gorgonzola
- pâte du pain : pignons-ail-huile ; noix ; huile-ail simple
- pain : levain épais, ciabatta

### Points critiques
- fruit FERME (un fruit trop mûr devient bouillie au gril)
- marquer le fruit juste pour les rayures, ne pas le ramollir
- passage four FINAL bref : fromage fond PARTIELLEMENT, on voit pain + fruit + fromage distincts
- huile fruitée + poivre frais en finition

### Usage Gemini
- proposer : « apéro ou entrée chaude rapide », « poire + fromage », « crostini original »
- éviter : fruit trop mûr, pas de bon pain

**Pattern — Garniture frite croustillante minute (gingembre-piment-noix)**

## Pattern outil — Garniture sautée croustillante « minute » sur grain/riz/nouilles

### Intention
Transformer un riz ou des nouilles neutres en plat asiatique : une garniture frite-minute versée brûlante par-dessus apporte croquant, piment et parfum.

### Pattern réutilisable
```text
huile (arachide) chaude + aromates en julienne (gingembre + ail + piment) saisis 3-4 min jusqu'à dorer → ajouter herbes en tronçons + noix/arachides + graines de sésame + sel → 1-2 min jusqu'à doré → verser brûlant sur le grain
```

### Points critiques
- **tout couper avant** d'allumer le feu : une fois la poêle chaude, ça va trop vite
- aromates dorés mais pas brûlés (l'ail et le gingembre brûlent vite)
- verser immédiatement, garniture chaude sur grain chaud
- finir d'un quartier de lime à presser à table

### Variantes
- gingembre-ail-piment rouge-coriandre-arachides-sésame (thaï)
- gingembre-oignon vert-piment-cacahuète (sur riz blanc nature)
- graines de cumin + amandes dans beurre noisette (registre moyen-oriental)

### Usage Gemini
- proposer quand : « riz blanc trop fade », « finir des nouilles », « petit festin asiatique express »
- déclencheurs : riz collant, garniture croustillante, gingembre frit

**Pattern — Pâtes sauce tomate longue + finition yaourt/fromage/herbe**

## Pattern — Pâtes sauce tomate mijotée + finition lactée + herbe

### Intention
Pâtes de fond de placard mais profondes : une sauce tomate qui a vraiment cuit, relevée d'un levier salé-épicé, adoucie en finition par yaourt ou fromage râpé.

### Pattern réutilisable
```text
ail/oignon dans l'huile + levier salé-épicé (harissa OU olives+câpres OU piment fumé) + tomates (cerises ou en boîte) + pincée de sucre → mijoter jusqu'à épaississement réel → pâtes al dente + un peu d'eau de cuisson → finition : yaourt OU pecorino/parmesan + herbe déchirée (basilic, persil) + filet d'huile
```

### Variantes
- alla Norma : aubergines rôties + tomate-origan + pecorino (ou ricotta salata)
- tomates cerises mijotées ~1 h + piment ancho (note fumée) + basilic + parmesan
- pappardelle : oignon caramélisé + harissa rose + tomates + olives kalamata + câpres → finition yaourt
- pincée de sucre pour corriger l'acidité des tomates pas assez mûres

### Points critiques
- la sauce doit **vraiment réduire** (10 min à 1 h selon variante) : pas une tomate qui flotte
- réserver de l'eau de cuisson avant d'égoutter pour lier
- la sauce se conserve ~5 j au frigo et se congèle : doubler/tripler vaut le coup
- aubergines (Norma) : pelées en lanières (rayures), rôties à part, ajoutées en fin

### Usage Gemini
- proposer quand : « pâtes tomate qui changent », « j'ai une boîte de tomates », « sauce à faire en avance »
- éviter quand : sauce express recherchée (la profondeur vient du temps)

**Pattern — Pâtes/orzo façon risotto une casserole**

## Pattern — Petites pâtes (orzo) cuites en une casserole façon risotto

### Intention
Plat unique réconfortant sans cuisson séparée des pâtes : l'orzo cuit DANS la sauce et absorbe le liquide, comme un risotto, en libérant son amidon.

### Pattern réutilisable
```text
orzo grillé à sec/huile jusqu'à doré → réserver → aromates (ail + zeste + épices) + tomates + bouillon + eau → remettre l'orzo, couvrir → mijoter ~15 min en remuant 1-2 fois → découvrir 1-2 min jusqu'à consistance risotto → ajouter protéine rapide (crevettes) + herbe → finition fromage
```

### Points critiques
- griller l'orzo d'abord = goût de noisette + grains qui restent distincts
- ajouter la protéine rapide (crevettes) en toute fin, 2-3 min
- la cible n'est pas sèche : crémeux comme un risotto
- féta mariné (chili + graines de fenouil grillées + huile) parsemé à la fin pour le contraste

### Variantes
- orzo-tomate-bouillon + crevettes + féta mariné + basilic
- orzo + zeste d'orange + fenouil + tomates

### Usage Gemini
- proposer quand : « plat unique en une casserole », « orzo », « repas simple sans égoutter de pâtes »
- déclencheurs : one-pot pasta, orzo crevettes

**Pattern — Pain plat farci à la viande poêlé (arayes)**

## Pattern — Pain plat / tortilla farci à la viande hachée, poêlé (arayes)

### Intention
Repas rapide et nourrissant pour le lunch ou le goûter : viande hachée crue assaisonnée tartinée dans un pain plat plié, poêlé jusqu'à ce que le pain dore et la viande cuise.

### Pattern réutilisable
```text
viande hachée crue + oignon/tomate râpés + épices + tahini + ail + acide (mélasse de grenade) + herbe → étaler en couche fine (1-1,5 cm) sur la moitié d'un pain plat/tortilla + fromage râpé → replier en demi-lune → poêler 2-3 min par face à feu moyen-doux → badigeonner d'huile-sumac → servir avec yaourt
```

### Points critiques
- couche de viande **fine** (1-1,5 cm) sinon le pain brûle avant que la viande cuise
- feu moyen-doux, pas vif : il faut le temps que le centre cuise
- le tahini DANS la farce garde la viande moelleuse
- garniture préparable la veille
- servir avec salade de légumes hachés + yaourt au sumac

### Variantes
- agneau-piment de la Jamaïque-menthe-cheddar-grenade (classique)
- bœuf-cumin-persil ; version pita au lieu de tortilla

### Usage Gemini
- proposer quand : « lunch avec du haché », « goûter salé rapide », « pita/tortilla à farcir »
- déclencheurs : arayes, pain farci viande, tortilla à la viande

**Pattern — Sauté de haché asiatique + légume vapeur à part**

## Pattern — Viande hachée sautée façon asiatique servie sur légume cuit vapeur

### Intention
Repas vite fait du quotidien : un haché sauté très assaisonné (sucré-salé-acide), une garniture croquante, servi sur un légume cuit vapeur à part qui absorbe la sauce.

### Pattern réutilisable
```text
aromates (oignon vert + gingembre + ail + piment) sautés à feu vif → réserver → haché sauté jusqu'à coloration → sauce (mirin + soja + kecap manis + huile de sésame + vinaigre de riz) 2 min → remettre aromates → hors feu : coriandre + arachides → servir sur légume vapeur (aubergine…) + sésame
```

### Points critiques
- **tout couper avant** d'allumer le feu (sauté = rapide)
- légume (aubergine) salé puis cuit vapeur à part ~12 min : reste fondant, prêt à recevoir la sauce
- le plat rend beaucoup de jus volontairement : c'est la sauce
- équilibre type : mirin (doux) + soja (salé) + vinaigre de riz (acide) + sésame (parfum)

### Usage Gemini
- proposer quand : « repas express avec du haché », « sauté asiatique », « j'ai des aubergines + du porc »
- éviter quand : pas de condiments asiatiques de base (soja, mirin, sésame)

**Pattern — Salade de nouilles froide asiatique + cru croquant + acide**

## Pattern — Salade de nouilles froide (riz/soba) + cru croquant + vinaigrette acide

### Intention
Plat-lunch frais et croquant : des nouilles refroidies, des crus en julienne, une note acide vive, des herbes en quantité. Assemblage minute pour garder le croquant.

### Pattern réutilisable
```text
nouilles (riz plates ou soba) cuites + rincées à l'eau FROIDE + huilées → oignon/gingembre macérés dans vinaigre+sucre → crus en julienne (concombre, pomme verte, piment) → herbes (menthe, estragon, coriandre, basilic) + graines + acide (lime/vinaigre) + sel → mélanger et servir AUSSITÔT
```

### Points critiques
- rincer les nouilles à l'eau froide stoppe la cuisson + retire l'amidon collant
- macérer oignon+gingembre dans vinaigre-sucre 30 min : adoucit et parfume
- **servir aussitôt assemblé** : le concombre rend de l'eau et détrempe si on attend
- composants préparables à l'avance séparément, assemblage au dernier moment
- protéine en option ajoutée minute : crevettes, tofu, œuf mollet

### Variantes
- nouilles de riz + concombre + pomme verte + menthe-estragon + graines de pavot
- soba + avocat + lime + cardamome broyée + pistaches + basilic-coriandre

### Usage Gemini
- proposer quand : « salade de nouilles fraîche », « lunch d'été », « j'ai un concombre et des herbes »
- éviter quand : besoin de chaud réconfortant

**Pattern — Épaule d'agneau confite basse température (marinade-incisions)**

## Pattern — Grosse pièce (épaule d'agneau) confite lentement au four

### Intention
Pièce de fête qui se défait à la fourchette : marinade-pâte massée dans des incisions, cuisson très longue à basse température, légumes-racines confits dans le jus.

### Pattern réutilisable
```text
pâte d'épices (ail + zeste/jus citron + épices + herbes + huile + sel) au robot → piquer la viande ~30 fois + frotter en faisant pénétrer → mariner 1 nuit → four couvert (alu) 170°C 1 h, baisser à 160°C + ajouter racines, 4 h en arrosant, puis découvrir 1 h 30 → viande qui s'effiloche + légumes caramélisés
```

### Points critiques
- **piquer la chair** partout (~30 fois) pour que la marinade pénètre en profondeur
- mariner idéalement une nuit (min 4-5 h)
- couvert d'alu d'abord (vapeur, tendreté), découvert en fin (coloration)
- préparable la veille : cuire, réfrigérer, effilocher et réchauffer dans le jus
- accompagner d'un féculent qui boit le jus (haricots écrasés, riz, semoule)

### Usage Gemini
- proposer quand : « grande tablée », « pièce d'agneau pour fête », « plat qui cuit tout seul des heures »
- éviter quand : peu de temps (prévoir ~6 h 30 de four)

**Pattern — Poisson poché/braisé dans une sauce épicée + double sauce**

## Pattern — Poisson braisé dans une sauce maison + (option) seconde sauce contrastante

### Intention
Le poisson cuit doucement DANS une sauce déjà montée (tomate-épices ou pois chiches-harissa), au lieu d'être saisi à part. Cuisson courte, chair nacrée, une seule casserole. On peut napper d'une 2e sauce froide pour le contraste.

### Pattern réutilisable
```text
base aromatique mijotée (oignon/ail + épices grillées + tomate OU pois chiches-harissa-citron confit + bouillon) jusqu'à épaississement → coucher le poisson dans la sauce → couvrir → cuisson douce 8-12 min jusqu'à ce que la chair se défasse en flocons → finir coriandre + (option) filet de sauce tahini-citron froide
```

### Variantes
- bases : tomate-piment-carvi-ancho (chraimeh) ; pois chiches-harissa-cardamome-citron confit ; poivron-orange
- poissons : flétan, morue, aiglefin, plie, tout poisson blanc ferme
- 2e sauce option : tahini-citron-eau, yaourt-citron, sauce verte
- finition : coriandre dominante, zeste, piment doux

### Points critiques
- monter et épaissir la sauce AVANT d'ajouter le poisson (sinon sauce claire et poisson trop cuit)
- si le poisson a rendu de l'eau et que la sauce est claire : retirer le poisson, faire réduire la sauce, puis napper
- ne pas remuer brutalement : retourner délicatement à mi-cuisson
- saler le poisson ~15 min avant

### Usage Gemini
- proposer quand : "poisson blanc rapide une casserole", "poisson sans le faire sécher", "morue/cabillaud + pois chiches ou tomate"
- éviter quand : poisson très fragile qui se défait (préférer pavé ferme)
- adaptation rapide : pois chiches + tomate en boîte + harissa = sauce en 8 min, poisson 4 min

**Pattern — Poisson entier/pavé rôti style asiatique + huile fumante versée**

## Pattern — Poisson rôti style asiatique + huile fumante versée à la fin

### Intention
Pièce maîtresse d'un repas asiatique : poisson cuit sur un lit de légumes avec sauce soja-gingembre, puis fini par de l'huile chaude versée dessus qui rend peau et légumes croustillants et libère les arômes des aromates crus.

### Pattern réutilisable
```text
sauce soja-sésame-vin de riz-sucre (réduite 1 min) → poisson incisé et salé sur lit de chou/oignons verts + gingembre julienne → verser la sauce → couvrir alu → four chaud 220 °C, badigeonner 2x (~40 min) → parsemer aromates crus (oignon vert, piment, coriandre) → verser dessus une huile fumante (arachide) → servir
```

### Variantes
- poissons : bar entier, dorade, ou pavés de poisson blanc/saumon
- lit : chou, oignons verts, bok choy
- aromates crus finaux : gingembre, piment rouge, oignon vert, coriandre
- huile : arachide ou neutre, chauffée jusqu'à fumée légère
- vin de riz shaoxing → xérès

### Points critiques
- inciser le poisson (5 entailles/face) pour cuisson homogène et pénétration du sel
- l'huile doit VRAIMENT fumer avant de la verser : c'est elle qui "cuit" les aromates crus et croustille la peau
- récupérer la sauce du plat pour arroser au service
- prépa possible jusqu'au début de l'étape four quelques heures avant

### Usage Gemini
- proposer quand : "poisson entier au four", "repas asiatique festif", "sauce soja-gingembre"
- éviter quand : pas de four, peur de manipuler un poisson entier (utiliser des pavés)

**Pattern — Dessert assemblé en coupes : crème + compote + crumble (tout d'avance)**

## Pattern — Dessert en coupes : crème onctueuse + fruit cuit + croquant (tout fait à l'avance)

> Parent : Pattern 023 (fruits + base laitière + herbe). Ce pattern en est la déclinaison "verrine assemblée à composants conservables", avec un croquant cuit en chapelure.

### Intention
Le dessert sans stress de réception : trois composants préparés à l'avance, assemblés minute dans des coupes. Aucune cuisson de dernière minute.

### Pattern réutilisable
```text
base crémeuse (fromage frais ± féta + sucre + zeste + crème fouettée incorporée, OU yaourt grec égoutté + crème) → compote de fruit mijotée (fruit + sucre + épice/zeste : anis étoilé, vanille, sumac) → garniture croquante (noix + amandes moulues + sucre + sésame + beurre, dorée au four en "chapelure") → assembler en couches dans des coupes au moment de servir
```

### Variantes
- crème : féta-fromage à la crème (sucré-salé), yaourt égoutté-crème, mascarpone
- compotes : cerises-anis étoilé-orange, fraises-sumac, rhubarbe-fraise, prunes
- croquant : noisettes-amandes-sésame doré, granola, sablés émiettés

### Conservation (clé du pattern)
- crème : jusqu'à 3 jours au frigo ; compote : 5 jours ; croquant : 1 semaine en boîte hermétique à T° ambiante
- ne JAMAIS assembler à l'avance (le croquant ramollit) : montage minute

### Points critiques
- une pincée de sel ou du féta dans la crème pour casser le sucré
- compote mijotée court (10-15 min) : fruit fondant mais pas en bouillie
- croquant travaillé du bout des doigts en texture chapelure avant cuisson

### Usage Gemini
- proposer quand : "dessert à préparer la veille", "recevoir sans stress", "verrines de fruits"
- éviter quand : dessert chaud à la sortie du four recherché

**Pattern — Cheesecake sans cuisson au yaourt égoutté + chocolat blanc**

## Pattern — Cheesecake sans four : base biscuits + crème yaourt-fromage-chocolat blanc

### Intention
Le cheesecake le plus facile à réussir : pas de bain-marie, pas de four, pas de crevasses. Il prend au frigo. Le chocolat blanc fondu remplace une partie du sucre et fait tenir la garniture.

### Pattern réutilisable
```text
yaourt grec égoutté (étamine, presser le petit-lait) → base biscuits émiettés + beurre fondu (+ herbe option : thym) pressée au fond, au frigo → fouetter fromage à la crème + yaourt égoutté + sucre glace + zeste citron → incorporer chocolat blanc fondu → étaler sur la base → frigo 2 h min → napper d'un sirop chaud au service (miel-thym)
```

### Variantes
- biscuits : flocons d'avoine (Hobnobs), digestifs, spéculoos
- chocolat : blanc classique ; nappage : miel-thym tiédi, coulis de fruit
- aromate : zeste citron, vanille, thym dans la base

### Points critiques
- bien égoutter le yaourt (étamine, poids dessus) : sinon garniture liquide
- AUCUNE goutte d'eau dans le chocolat blanc fondu (il fige/graine) ; bol loin de l'eau frémissante
- napper le sirop chaud SEULEMENT au service (la base de biscuits ramollit au fil des jours)
- se prépare jusqu'à 2 jours à l'avance

### Usage Gemini
- proposer quand : "cheesecake facile sans four", "dessert à préparer la veille", "pas envie d'allumer le four"
- éviter quand : envie d'un vrai cheesecake cuit dense

**Dip aubergine fumée + tahini + mélasse de grenade**

Dip/condiment moyen-oriental aigre-doux à partir de chair d'aubergine brûlée.

Formule :
chair d'aubergine fumée égouttée + tahini + eau + mélasse de grenade + jus citron + ail pressé + persil + sel/poivre → fouetter

Cible de goût : franchement acide / légèrement sucré (ajuster ail, citron, mélasse jusqu'à équilibre robuste).

Deux usages :
- DIP/condiment : version lisse, avec crudités, agneau ou poisson
- SALADE d'été : ajouter dés de concombre + tomates cerises + grains de grenade + filet d'huile

Végan, prêt en 5 min une fois l'aubergine brûlée.

**Beurre composé aromatique posé sur galettes/légumes chauds**

Beurre parfumé (maître d'hôtel revisité) qui fond sur un plat chaud comme sauce minute.

Formule :
beurre mou battu crémeux + zeste + jus d'agrume + ail finement haché + 1 herbe + piment + sel → rouler en boudin dans film → frigo jusqu'à ferme → trancher → poser une rondelle sur le plat brûlant pour qu'elle fonde.

Exemples : beurre lime-coriandre-piment sur galettes d'épinard ; idem sur patate douce au four, poisson grillé, maïs.

Avantage : se prépare à l'avance, se garde au frigo, transforme un reste chaud en plat fini.

**Légume-feuille sauté feu vif ail-piment croustillant + acide**

## Pattern — Légume-feuille sauté feu vif + ail/piment croustillant + acide

**Intention** : transformer un vert robuste (brocoli, kale, chou pointu, choy sum, minibrocoli) en accompagnement vif et croquant — feu vif, matière grasse aromatisée, jamais l'ébullition molle.

### Pattern réutilisable
```text
(blanchir 30-90 sec si vert dense + bien éponger) → huile chaude infusée ail/piment/cumin → retirer l'aromate croustillant et réserver → sauter le vert feu vif jusqu'à bords croustillants → sel + acide (lime/citron) hors feu → re-parsemer de l'aromate croustillant + herbe fraîche
```

### Variantes
- verts : brocoli, kale, chou pointu, chou palmier, choy sum, minibrocolis
- huile infusée : ail+cumin, ail+piment, ail+gingembre+zeste orange
- finition : menthe+lime+piment broyé, coriandre+arachides, estragon

### Points critiques
- bien éponger après blanchiment, sinon ça vapore au lieu de saisir
- retirer l'ail/aromate AVANT qu'il brûle, le remettre seulement en finition (croustillant, pas amer)
- acide toujours hors feu

### Usage Gemini
- proposer quand : "un brocoli/kale à passer", "accompagnement vert rapide qui change", "vide-frigo de légumes verts"
- éviter quand : verts très fragiles (épinard) — les ajouter à la dernière seconde

**Vinaigrette aigre-douce asiatique : huile aromatique + sucre + agrume + arachides**

## Pattern — Vinaigrette aigre-douce asiatique sur légume à peine cuit

**Intention** : enrober un vert juste blanchi/rôti d'une sauce vive sucrée-salée-acide, avec arachides grillées pour le croquant. Registre asiatique léger d'Ottolenghi.

### Pattern réutilisable
```text
huile chaude infusée (ail + gingembre + zeste agrume + arachides jusqu'à doré) → réserver l'huile parfumée + les aromates
légume à peine cuit (vapeur/blanchi/rôti court) → arroser de l'huile aromatique
réduction sucrée-salée à part (soja + miel, OU lime + piment + sirop + sésame) → napper minute
```

### Variantes
- légumes : minibrocolis, choy sum, haricots verts, gombos (rôtis 7 min, encore fermes)
- base sucre : miel, sirop d'érable
- base salée/acide : soja + sésame, OU jus de lime + huile de sésame + piment
- croquant : arachides salées, sésame

### Points critiques
- la vinaigrette tombe au fond du bol : mélanger juste avant de servir
- légume gardé ferme et vert vif, jamais surcuit
- gombos : ne pas exposer les graines (sinon visqueux), les garder entiers et à peine cuits

### Usage Gemini
- proposer quand : "accompagnement asiatique pour volaille ou bol de riz", "haricots/brocolis autrement"
- éviter quand : sans sucre, sans soja/sésame

**Kale/chou frisé cru massé et mariné (salade tendre)**

## Pattern — Légume-feuille cru massé pour l'attendrir + salade

**Intention** : rendre un kale cru tendre et savoureux sans cuisson, par massage manuel dans une marinade acide-grasse.

### Pattern réutilisable
```text
feuilles déchirées (sans tiges) + huile + acide (vinaigre/citron) + moutarde + sirop/miel + sel → masser à la main 1 min jusqu'à ramollissement et changement de couleur → mariner 30 min min (jusqu'à 4 h) → ajouter au dernier moment éléments croquants/frais (asperges sautées, édamames, graines, herbes)
```

### Variantes
- marinade : moutarde à l'ancienne + vinaigre vin blanc + sirop d'érable ; OU citron + ail + huile
- ajouts : asperges sautées, édamames, graines tournesol/courge caramélisées, herbes (estragon, aneth)

### Points critiques
- masser PHYSIQUEMENT avec les doigts, pas remuer — c'est ça qui casse les fibres
- masser à l'avance, assembler le reste à la dernière minute (sinon les ajouts ramollissent)

### Usage Gemini
- proposer quand : "salade de kale", "feuilles robustes à manger crues", "salade qui tient des heures"
- éviter quand : feuilles tendres (laitue, roquette) sans besoin de massage

**Salade légume deux textures : rôti + cru râpé**

## Pattern — Légume rôti ET cru râpé dans la même salade (double texture)

**Intention** : contraste de textures à partir d'un seul légume — une part rôtie/caramélisée fondante, une part crue râpée croquante et fraîche. Révélation d'Ottolenghi sur le chou-fleur.

### Pattern réutilisable
```text
2/3 du légume en bouquets + oignon → rôti four chaud jusqu'à doré
1/3 du légume râpé cru, réservé
assembler tiède : rôti + cru râpé + herbes multiples + grenade/noix + cumin + citron + huile
```

### Variantes
- base : chou-fleur (signature), brocoli, betterave, carotte, courgette
- garniture : grenade + pistaches + persil/menthe/estragon + cumin
- ne pas jeter les feuilles du chou-fleur : rôties croustillantes ou râpées crues

### Points critiques
- râper grossièrement la part crue (pas en purée)
- assembler tiède, jamais brûlant (les herbes flétriraient)
- préparable à l'avance : rôtir jusqu'à 4-6 h avant, assembler au service

### Usage Gemini
- proposer quand : "salade de chou-fleur qui sort de l'ordinaire", "un seul légume mais texture intéressante"
- éviter quand : légume qui ne se mange pas cru agréablement

**Légume rôti ENTIER longuement, badigeonné (pièce maîtresse)**

## Pattern — Légume entier rôti longuement, badigeonné [pièce maîtresse]

**Intention** : un légume rôti entier comme pièce centrale partagée — pré-cuisson à l'eau ou piqûres, puis four long avec badigeonnages répétés jusqu'à cœur fondant et extérieur doré-croustillant.

### Pattern réutilisable
```text
légume entier (pré-bouilli 6 min OU piqué) → four moyen → badigeonner beurre+huile (ou huile+épice) à intervalles réguliers → 1h30 à 3h jusqu'à très tendre à cœur et bruni dehors → repos → trancher en quartiers → sel en flocons + citron OU sauce verte au tahini
```

### Variantes
- chou-fleur entier : pré-bouilli 6 min, four 1h30-2h, beurre+huile, feuilles laissées (croustillantes)
- céleri-rave entier : piqué, frotté huile+coriandre+sel, four long
- accompagnement : sauce verte au tahini (tahini+persil+ail+citron+eau au robot), OU crème fraîche, OU juste citron

### Points critiques
- les badigeonnages réguliers évitent le dessèchement et construisent la croûte
- patience : c'est la durée qui rend le cœur fondant
- le pré-bouillage du chou-fleur raccourcit le four et assure la cuisson à cœur

### Usage Gemini
- proposer quand : "plat végé central à partager", "recevoir avec un légume spectaculaire", "chou-fleur entier"
- éviter quand : pressé (c'est long), pas de four

**Purée de légume + huile aromatique ou salsa en finition**

## Pattern — Purée de légume relevée par huile aromatique OU salsa fraîche

**Intention** : sortir une purée du fade — soit en infusant l'eau de cuisson d'aromates et en finissant à l'huile parfumée, soit en couronnant d'une salsa crue vive. La purée devient un plat.

### Pattern réutilisable
```text
légume cuit (eau aromatisée thym/menthe/ail/zeste OU four) → écraser avec huile d'olive (+ un peu d'eau de cuisson) → creux à la surface → soit huile aromatisée (ail+herbes+zeste+jus) soit salsa crue (herbes+ail+zeste+jus+huile)
```

### Variantes
- pomme de terre : eau infusée thym/menthe/ail/zeste citron + huile aromatisée même base
- patate douce : salsa lime (basilic+coriandre+ail+zeste+jus de lime+huile)
- garder les pelures, les rôtir 8 min en collation croustillante

### Points critiques
- réserver l'eau de cuisson pour ajuster la texture
- purée à l'huile d'olive plus légère que beurre/crème — adaptée quand le plat principal est riche
- former des creux pour que l'huile/salsa s'y dépose visiblement

### Usage Gemini
- proposer quand : "purée qui change", "accompagnement végétal pour plat riche", "patate douce autrement qu'en frites"
- éviter quand : besoin de la purée crème classique réconfortante

**Purée/trempette de légumineuse + topping contrastant (mezze)**

## Pattern — Purée de légumineuse lisse + couronne contrastante [mezze]

**Intention** : une base crémeuse de légumineuse/légume, lissée à l'huile, surmontée d'un topping coloré qui apporte texture et punch. Format mezze à préparer à l'avance.

### Pattern réutilisable
```text
base lisse (légumineuse/avocat/gourganes mixés + huile + ail confit + citron + sel) étalée, creux au centre
+ topping contrastant : trempette poivrons rôtis-noix (muhammara), OU oignons verts+zeste sautés, OU aromates croustillants + leur huile
```

### Variantes
- haricots blancs (huile+ail+thym) + muhammara (poivrons rôtis+ail+noix+paprika fumé+balsamique)
- avocat + gourganes blanchies (plus léger qu'un guacamole) + oignons verts+zeste citron
- toute légumineuse en boîte mixée + huile + acide

### Points critiques
- mixer la base très lisse, ajouter eau/huile au besoin
- l'ail caramélisé dans l'huile puis jeté parfume la base sans agressivité
- se garde 2-3 jours au frigo : doubler les quantités

### Usage Gemini
- proposer quand : "apéro/mezze à préparer à l'avance", "trempette qui change du houmous", "boîte de haricots à valoriser"
- éviter quand : besoin d'un plat chaud consistant

**Sauce tonnato (mayonnaise thon-câpres-anchois au robot) [outil]**

## Pattern — Sauce tonnato : émulsion umami thon-anchois-câpres-citron [outil]

**Intention** : sauce-condiment crémeuse à fort umami qui transforme un aliment neutre (pomme de terre, œuf, légume, viande froide). Une mayonnaise montée au robot avec thon, anchois et câpres.

### Pattern réutilisable
```text
au robot : jaunes d'œufs + jus citron + persil + thon (huile) + câpres + anchois + ail → mixer en purée → ajouter l'huile en filet continu jusqu'à consistance mayonnaise souple
```

### Variantes
- plus de thon = sauce plus consistante
- sert sur : pomme de terre au four + œuf mollet, légumes vapeur, viande froide (vitello), œufs durs
- garnir : reste de câpres + persil + filet d'huile

### Points critiques
- huile ajoutée TRÈS lentement en filet pour que l'émulsion prenne (comme une mayo)
- triple levier salé/umami (thon + anchois + câpres) : goûter avant d'ajouter du sel
- se prépare la veille, se garde au frigo

### Usage Gemini
- proposer quand : "sauce qui sublime des pommes de terre/œufs", "thon en boîte à valoriser", "viande froide à accompagner"
- éviter quand : aversion poisson/anchois

**Frites/légumes au four enrobés de polenta ou semoule (croustillant sans friture)**

## Pattern — Croustillant au four par enrobage polenta/semoule

**Intention** : obtenir des frites/légumes vraiment croustillants au four (sans friteuse) en enrobant d'une fine couche de polenta ou semoule qui croûte à la chaleur.

### Pattern réutilisable
```text
légume en bâtonnets (pdt pré-bouillies puis séchées, OU patate douce crue) + huile généreuse + épices + une poignée de polenta/semoule → bien enrober → étaler espacé sur plaque → four chaud, retourner 1-2 fois jusqu'à doré et croustillant → sel en flocons + sumac/herbe à la sortie
```

### Variantes
- pomme de terre : pré-bouillie 10 min, séchée et secouée (bords floconneux), gras d'oie/huile + semoule + carvi + harissa
- patate douce : crue + paprika fumé + Cayenne + ail + polenta + huile + sumac
- finition signature : sumac, origan+féta, sel en flocons immédiat

### Points critiques
- pré-bouillir et BIEN sécher les pommes de terre (vapeur résiduelle = mou) ; les secouer pour des bords floconneux qui croustillent
- étaler espacé, plaque pas surchargée (sinon vapeur)
- saler/épicer la finition immédiatement à la sortie

### Usage Gemini
- proposer quand : "frites maison au four croustillantes", "frites de patate douce", "accompagnement croquant sans friteuse"
- éviter quand : pas de four, plaque trop petite

**Beignets de légumes liés à la pâte (fritters) + sauce yaourt-herbes**

## Pattern — Beignets de légumes (fritters) liés par une pâte battue

### Intention
Légume fondant noyé dans une pâte légère levée, poêlé en galettes dorées. La pâte EST le liant (distinct des croquettes panées du pattern croquettes/galettes).

### Pattern réutilisable
```text
légume fondu et refroidi (poireau/oignon longuement sués) + épices + herbes → pâte (farine + levure + œuf + lait + beurre fondu) → blanc d'œuf monté plié en dernier → cuillerées poêlées des 2 côtés → sauce yaourt-herbes à côté
```

### Variantes
- légumes : poireau, oignon, courgette râpée pressée, épinards, maïs
- épices : cumin, coriandre moulue, curcuma, piment
- sauce verte : yaourt + crème sure + ail + citron + persil + coriandre mixés

### Points critiques
- faire suer et REFROIDIR le légume avant de l'ajouter à la pâte (chaud → cuit le blanc, retombe)
- monter et plier le blanc d'œuf séparément pour la légèreté
- huile chaude pas brûlante ; 2-3 min par face
- presser les légumes aqueux (courgette) sinon pâte trop liquide

### Erreurs fréquentes
- légumes chauds dans la pâte → retombe ; pâte trop liquide → s'étale ; huile tiède → gras

### Usage Gemini
- proposer quand : j'ai des poireaux/courgettes, apéro/brunch végé, galettes croustillantes
- note : une giclée de citron suffit si pas le temps de la sauce ; cf. pattern croquettes/galettes pour la version panée à l'œuf-chapelure

**Légumes farcis braisés (oignons, courgettes, chou) — farce riz/mie-herbes**

## Pattern — Légumes farcis braisés (farce riz ou mie + herbes)

### Intention
Légume creusé ou en feuilles, garni d'une farce parfumée, braisé doucement dans un liquide aigre-doux jusqu'à fondance. Plat principal végé, souvent servi tiède ou froid.

### Pattern réutilisable
```text
légume préparé (couches d'oignon ou feuilles blanchies / boats de courgette) + farce (riz court OU mie + fromage + herbes + pignons + ail + épices douces) → rouler/garnir → braiser à couvert dans liquide (vin/bouillon + sucre + citron + huile) jusqu'à absorption
```

### Variantes
- légumes : oignons (couches), courgettes, feuilles de chou/blettes/vigne, poivrons, tomates
- farces : riz court + raisins + pignons + cannelle (style turc) ; mie + féta + persil + tomate râpée ; riz + ricotta + menthe
- liquide : vin blanc + bouillon + sucre + citron ; bouillon + tomate
- finition : parmesan gratiné, ou yaourt froid au service

### Points critiques
- blanchir les enveloppes (feuilles, couches d'oignon) pour rouler sans casser
- riz cuit aux 3/4 si la farce mijote ensuite
- liquide à mi-hauteur, pas jusqu'à la farce ; couvrir et laisser absorber

### Erreurs fréquentes
- enveloppe non blanchie → casse ; trop de liquide → farce détrempée ; riz cru + temps court → grains durs

### Usage Gemini
- proposer quand : plat végé qui en jette, cuisine turque/moyen-orientale, oignons/chou/courgettes à valoriser, plat tiède à l'avance
- éviter quand : repas express

**Sauté beurre + chili + soja (tofu / légume robuste)**

## Pattern — Sauté "beurre + chili + soja" (tofu, choux de Bruxelles)

### Intention
Protéine ou légume robuste saisi puis enrobé d'une sauce où le BEURRE (signature Ottolenghi) lie une base aromatique longuement fondue (échalote-ail-gingembre-piment) et des sojas sucrés-salés. Distinct du wok classique : beaucoup d'aromatics fondus, beurre au lieu d'huile.

### Pattern réutilisable
```text
tofu/légume fariné (fécule) frit doré ou saisi fort → réserver → beurre fondu + masse échalotes/ail/gingembre/piment suée 15 min jusqu'à fondance brillante → sojas (clair + foncé + sucré) + sucre + poivre noir concassé → remettre la base + oignon vert → enrober hors gros feu
```

### Variantes
- bases : tofu ferme, choux de Bruxelles tranchés, shiitake
- registre poivre noir : beaucoup de poivre concassé (black pepper tofu)
- registre sucré : chili doux + soja + sésame + érable
- service : riz vapeur, coriandre, sésame

### Points critiques
- fécule sur le tofu + huile chaude = croûte fine qui tient la sauce
- fondre les aromatics LONGUEMENT (15 min) : c'est la base de saveur
- sojas/sucre puis poivre en fin, hors gros feu

### Erreurs fréquentes
- aromatics pas assez fondus → sauce crue agressive ; tofu non fariné → pas de croûte ; sucre brûlé → amer

### Usage Gemini
- proposer quand : tofu, choux de Bruxelles autrement, plat asiatique végé qui impressionne
- éviter quand : aversion soja/piment ; cf. pattern wok stir-fry pour le sauté rapide classique (huile, feu max)

**Salade crue massée à l'acide (chou, chou-rave) + fruit sec + herbe**

## Pattern — Salade crue massée à l'acide (slaw moyen-oriental)

### Intention
Légumes crus fermes tranchés fins puis MASSÉS à la main avec citron/sel pour les attendrir, équilibrés par un fruit et beaucoup d'herbe. Tient plusieurs heures, gagne en saveur.

### Pattern réutilisable
```text
légumes crus fermes tranchés très fin + sel + agrume généreux + ail + huile + fruit sec → masser 1 min à la main → reposer 10-15 min → ajouter herbe abondante + croquant → rectifier (BEAUCOUP de sel pour contrer l'acide)
```

### Variantes
- légumes : chou blanc/rouge, chou-rave, carotte, fenouil, betterave crue
- fruits : cerises séchées, raisins secs, grenade, mangue, papaye verte
- registre asiatique : lime + citronnelle + érable + sésame + piment
- herbes : aneth, menthe, coriandre, persil
- croquant : macadamias caramélisées, arachides, graines

### Points critiques
- trancher très fin (mandoline) sinon reste dur
- MASSER physiquement, pas juste remuer
- saler généreusement : l'acide demande du sel pour s'équilibrer
- soulever la salade hors de son jus pour servir

### Erreurs fréquentes
- tranches épaisses → cru et agressif ; sous-salage → goût acide plat ; servi noyé → mou

### Usage Gemini
- proposer quand : salade d'hiver, chou/chou-rave à utiliser, slaw qui change, accompagnement frais d'un plat riche

**Légume en quartiers croûté gratin (parmesan-chapelure-herbes-zeste)**

## Pattern — Légume rôti en croûte parmesan-chapelure-herbes

### Intention
Quartiers de courge/légume badigeonnés d'huile puis recouverts d'une croûte sèche (parmesan + chapelure + herbes + zeste + ail) qui gratine et croustille au four. Effet "farce croustillante" sur un légume entier.

### Pattern réutilisable
```text
légume en tranches/quartiers à plat + badigeon d'huile → croûte (parmesan + chapelure sèche + herbes + zeste citron + ail + poivre, sel léger car parmesan salé) tassée dessus → four moyen jusqu'à légume tendre + croûte dorée (alu si elle fonce trop vite) → crème sure-aneth à côté
```

### Variantes
- légumes : courge/potiron, courgette, tomate, fenouil, chou-fleur
- croûte : parmesan + panko ; ajout noix concassées, zaatar
- herbes : persil + thym ; origan ; romarin
- sauce froide : crème sure-aneth, yaourt-citron

### Points critiques
- chapelure SÈCHE pour le croustillant
- saler la croûte avec parcimonie (le parmesan apporte le sel)
- tasser la croûte pour qu'elle adhère ; couvrir d'alu si elle brunit avant cuisson du légume
- vérifier la cuisson du légume à la pointe du couteau

### Erreurs fréquentes
- croûte trop salée (parmesan oublié dans le calcul) ; croûte brûlée avant cuisson → alu ; chapelure humide → pas croustillante

### Usage Gemini
- proposer quand : courge/potiron, légume rôti plus consistant, plat végé de fête, reste de parmesan + chapelure
- éviter quand : sans four

**Curry de légumes épicé type vindaloo (épices grillées-moulues + acide)**

## Pattern — Curry de légumes épicé (vindaloo/dry curry)

### Intention
Légumes mijotés dans une base d'épices entières grillées puis moulues, montée avec aromatics (échalote, gingembre, piment, feuilles de cari) et un acide marqué (vinaigre de cidre). Meilleur le lendemain, yaourt frais en condiment.

### Pattern réutilisable
```text
épices entières grillées à sec puis moulues (cardamome + cumin + coriandre + clou) + curcuma/paprika/cannelle → échalotes + graines moutarde/fenugrec suées → mix d'épices + cari + gingembre + piment 3 min → tomate + vinaigre + eau + sucre + sel → mijoter couvert → légumes par ordre de fermeté → réduire à découvert
```

### Variantes
- légumes : pomme de terre + patate douce + poivron ; chou-fleur ; aubergine
- registre coco : remplacer une partie de l'eau par lait de coco
- acide : vinaigre de cidre (vindaloo), jus de lime
- service : riz nature, yaourt épais, menthe/coriandre

### Points critiques
- griller les épices entières à SEC jusqu'à ce qu'elles sautent, puis moudre (arôme max)
- revenir le mix d'épices dans l'huile AVANT tout liquide
- ajouter les légumes par fermeté décroissante
- le plat gagne à reposer : préparer la veille

### Erreurs fréquentes
- épices ajoutées avec le liquide → arômes en surface ; tous les légumes ensemble → cuisson inégale ; manque d'acide/sel → terne

### Usage Gemini
- proposer quand : curry de légumes, plat épicé à préparer la veille, pommes de terre + patate douce
- éviter quand : aversion épices, repas express ; cf. pattern curry maison (SIMPLE) pour la version coco/tomate générique

**Ratatouille fondante : cuire chaque légume à part puis confire ensemble**

## Pattern — Ratatouille/poêlée "bien fondue" (cuisson en étapes)

### Intention
À rebours du "légume croquant" : cuire les légumes par groupes selon leur fermeté, les réunir, puis les confire ensemble (mijoté + four) jusqu'à fondance complète. Chaque légume garde son identité tout en se mariant.

### Pattern réutilisable
```text
colorer les légumes par lots selon fermeté (durs d'abord : oignon, courge, panais ; tendres ensuite : aubergine, courgette, haricots) dans la même huile → tout réunir + tomate + concentré + sucre + sel + un peu d'eau → mijoter couvert → finir au four à découvert jusqu'à fondance et évaporation
```

### Variantes
- légumes : aubergine, courgette, poivrons, courge, panais, haricots verts, pomme de terre
- registre : tomate + sucre (méditerranéen) ; cumin-coriandre + coriandre fraîche en finition

### Points critiques
- TOUT le découpage fait avant de commencer (ça enchaîne vite)
- cuire par lots selon la fermeté, pas tout ensemble
- le but est la surcuisson maîtrisée : légumes fondants, pas al dente
- le passage au four à découvert concentre et lie

### Erreurs fréquentes
- tout cuit ensemble → certains crus, d'autres en purée ; pas assez cuit → manque la fondance ; trop de liquide non évaporé → soupe

### Usage Gemini
- proposer quand : ratatouille, légumes d'été en abondance, plat qui se bonifie, accompagnement fondant
- éviter quand : on cherche des légumes croquants

**Pattern — Grain monté à la pâte d'herbes (green couscous)**

## Pattern — Grain monté à la pâte d'herbes

**Intention** : un grain devient vert et parfumé non par des herbes ciselées en surface mais par une PÂTE d'herbes mixée à l'huile, incorporée au grain encore tiède. Saveur d'herbe diffuse dans toute la bouchée.

### Formule
```text
grain gonflé (couscous/boulgour) + pâte d'herbes mixée (3-4 herbes + huile d'olive) incorporée à la fourchette + oignon fondu au cumin + croquant (pistaches/amandes) + oignon vert + piment frais + roquette hachée → température ambiante
```

### Variantes
- pâte : persil + coriandre (dominante) + estragon + aneth + menthe
- grains : couscous, boulgour, semoule, quinoa, freekeh
- croquant : pistaches, amandes, pignons grillés
- ajouts : roquette, oignon vert, piment frais, féta émietté (version plus consistante)

### Points critiques
- mixer la pâte BIEN lisse à l'huile avant incorporation
- gonfler le couscous sous film 10 min à l'eau/bouillon bouillant, puis aérer à la fourchette
- oignon-cumin mélangé tiède, pas brûlant
- servir à température ambiante (herbes restent vives)

### Usage Gemini
- proposer : « accompagnement vert et frais », « j'ai plein d'herbes », « side pour poisson ou légumes pochés »
- éviter : herbes fanées ou en faible quantité (le pattern repose dessus)

**Pattern — Beurre composé épicé en sauce de pâtes**

## Pattern — Beurre composé épicé en sauce de pâtes

**Intention** : remplacer une sauce par un BEURRE fondu chargé d'échalotes confites et d'épices chaudes (gingembre, paprika, coriandre, cannelle, cayenne, curcuma). Sauce instantanée, parfumée, sans réduction.

### Formule
```text
beurre + huile → échalotes fondues ~10 min jusqu'à beurre légèrement noisette → toutes les épices moulues + sel HORS feu, garder au chaud → verser sur pâtes chaudes → pignons grillés + menthe + persil
```

### Variantes
- épices (registre marocain) : gingembre + paprika doux + coriandre + cannelle + cayenne + piment + curcuma
- autres : beurre-cumin-citron, beurre-sauge-noisette, beurre-harissa
- support : tagliatelles, fettuccine, gnocchis, semoule, légumes vapeur, poisson poché
- finition : pignons + menthe + persil ; ou amandes + coriandre

### Points critiques
- laisser le beurre virer LÉGÈREMENT noisette avec les échalotes
- épices ajoutées HORS feu (ne pas brûler), puis maintenir au chaud
- express : pâtes sèches + ce beurre + pincée de safran dans l'eau de cuisson

### Usage Gemini
- proposer : « pâtes sans sauce classique », « beurre + épices », « accompagnement parfumé pour légumes/poisson »
- éviter : sans beurre / faible en gras

**Pattern — Polenta crémeuse en lit + garniture chaude**

## Pattern — Polenta crémeuse en lit + garniture chaude

**Intention** : la polenta molle sert de base apaisante (comme une purée) sous une garniture intense. Deux gestes : polenta enrichie beurre+fromage, et une poêlée/sauce chaude versée au centre.

### Formule
```text
bouillon bouillant + polenta en pluie → cuire en remuant jusqu'à porridge épais (se détache des parois mais reste coulant) → HORS feu : parmesan/féta + beurre + herbe → étaler en lit → garniture chaude au centre (champignons à l'ail, sauce aubergine-tomate)
```

### Variantes
- enrichissement : parmesan + beurre (+ Taleggio gratiné au gril), ou féta
- garnitures : champignons saisis + ail + estragon + huile de truffe ; sauce aubergine-tomate-origan ; ragoût de légumineuse
- option gratin : étaler, couvrir de fromage, passer au gril, puis garnir
- restes : étaler la polenta froide, découper, poêler le lendemain (croûtons de polenta)

### Points critiques
- fromage/beurre incorporés HORS feu
- garniture chaude et juteuse (ses jus = la sauce)
- ajouter du bouillon si la polenta sèche
- servir IMMÉDIATEMENT (fige en refroidissant)

### Usage Gemini
- proposer : « alternative à la purée », « champignons à valoriser », « végé réconfortant sans gluten »
- éviter : plat froid ou qui attend

**Pattern — Couscous d'hiver (racines rôties aux épices entières)**

## Pattern — Couscous d'hiver (racines rôties aux épices entières)

**Intention** : couscous chaud et copieux où les légumes-racines sont rôtis avec des épices ENTIÈRES (cannelle, badiane, laurier) pour un fond profond, relevé en finition par harissa + citron confit.

### Formule
```text
racines + courge + grelots + épices entières (bâtons cannelle, badiane, laurier) + épices moulues + huile → four en deux temps → ajouter abricots secs + pois chiches AVEC leur jus → couscous safrané gonflé au beurre → FINITION : harissa + citron confit haché mélangés aux légumes + coriandre généreuse
```

### Variantes
- racines : carotte, panais, navet, échalotes/grelots, butternut
- épices entières : cannelle, badiane, laurier (+ moulues : gingembre, curcuma, paprika fort, piment)
- fruits secs : abricots, dattes, raisins
- finition signature : harissa + citron confit + coriandre

### Points critiques
- rôtir en deux temps (dures d'abord 15 min, courge ensuite ~35 min)
- garder le jus des pois chiches (humidifie le plat)
- harissa + citron confit incorporés EN FIN, pas en cuisson
- couscous gonflé à part au bouillon safrané + beurre, aéré à la fourchette

### Usage Gemini
- proposer : « plat végé d'hiver généreux », « grand plat unique pour recevoir », « légumes-racines à écouler »
- éviter : repas express (cuisson four ~1h)

**Pattern — Assiette fromage frais + fruit + noix (architecture)**

## Pattern — Assiette fromage frais + fruit + noix (architecture)

**Intention** : entrée/plateau sans cuisson où un fromage frais lacté rencontre un fruit mûr, des herbes, des noix grillées et une vinaigrette à la mélasse de grenade. La CONSTRUCTION (éléments empilés, tous visibles) est le geste.

### Formule
```text
fromage frais lacté + fruit mûr + lit de roquette + herbes (basilic, aneth) + noix grillées + huile d'olive + mélasse de grenade + sel/poivre → construire en hauteur, chaque élément visible
```

### Variantes
- fromage : chèvre crémeux, ricotta/mozzarella de bufflonne, brebis turc en saumure, féta, gorgonzola doux
- fruit : figues fraîches, dattes Medjool, raisins, poire, pastèque
- liant acide-sucré : mélasse de grenade (signature) ou grains de grenade
- noix : amandes, pistaches, noix, noisettes

### Points critiques
- fromage à TEMPÉRATURE AMBIANTE (texture, parfum)
- construire en hauteur, chaque élément visible (ne pas mélanger)
- noix grillées le jour même
- vinaigrette mélasse-huile montée à part, arrosée en finition
- pastèque-féta : assembler MINUTE, servir aussitôt (rend de l'eau)

### Usage Gemini
- proposer : « entrée sans cuisson qui en jette », « fromage de qualité + fruit de saison », « plateau apéro chic »
- éviter : fromage froid frigo, fruit pas mûr

**Pattern — Riz au four scellé (méthode infaillible)**

## Pattern — Riz cuit au four sous papier scellé (méthode infaillible)

### Intention
Réussir le riz à tous les coups, sans surveillance. Pour ceux qui ratent le riz à la casserole, et pour cuire de grandes quantités.

### Pattern réutilisable
```text
riz basmati + sel + beurre fondu (ou huile) + eau BOUILLANTE dans un plat à haut bord → couvrir HERMÉTIQUEMENT de papier alu bien scellé → four chaud (220-250°C) 25 min → repos 10 min à couvert → aérer à la fourchette
```

### Ratios repères
- basmati : ~2 volumes d'eau pour 1 volume de riz (env. 1:2 en poids : 400 g riz / 800 ml eau, ou 300 g / 600 ml)
- sel : ~3/4 c. à thé ; beurre : ~50 g
- aromates posés DESSUS avant cuisson : tiges de menthe, bâtons de cannelle, thym (retirés après)

### Points critiques
- eau **déjà bouillante** versée sur le riz, jamais froide
- sceller le papier alu PARFAITEMENT : toute fuite de vapeur = riz raté
- ne pas ouvrir avant la fin du repos de 10 min
- aérer à la fourchette, jamais touiller en bloc

### Variante riz + légumes confits dessous
Rôtir d'abord tomates cerises + ail + échalotes + herbes + huile ~1 h à 180°C, puis parsemer le riz cru directement dessus (sans mélanger), ajouter eau bouillante, sceller et cuire 25 min. Le riz boit les sucs.

### Usage Gemini
- proposer quand : « je rate toujours le riz », « riz pour beaucoup de monde », « accompagnement sans surveillance »
- déclencheurs : riz au four, basmati infaillible, riz pour invités

**Pattern — Poulet mariné mijoté au four (Marbella / miso-gingembre)**

## Pattern — Cuisses de poulet marinées puis rôties dans leur marinade aigre-douce

### Intention
Plat de réception zéro-stress : tout marine à l'avance (jusqu'à 2 jours), on étale sur une plaque et le four fait le reste. La marinade devient sauce.

### Pattern réutilisable
```text
cuisses de poulet (peau, entaillées jusqu'à l'os) + marinade aigre-douce-salée-aromatique → mariner 1-2 jours au frigo → étaler sur plaque + liquide (vin/bouillon) → four ~180-200°C 50-70 min, badigeonner 2-3 fois → servir avec tous les sucs
```

### Familles de marinade
- Marbella : ail-origan-vinaigre de vin + olives vertes + câpres + dattes + laurier + vin blanc + mélasse de dattes (salé-sucré-acide)
- miso-gingembre-lime : miso blanc + mirin + sirop d'érable + soja + gingembre + ail + zeste/jus lime (registre japonais)
- citron confit-thym-ail (en beurre sous la peau)

### Points critiques
- entailler peau/chair jusqu'à l'os = la marinade pénètre + cuisson homogène
- saisir la peau à la poêle d'abord (option) pour le croustillant, puis finir au four
- mariner long = meilleur ; si pressé, saler la peau à part puis enrober
- sortir du frigo 30 min avant cuisson
- équilibre obligatoire : un sucré (datte/sirop/mélasse) + un acide (vinaigre/lime) + un salé (olive/câpre/miso/soja)

### Usage Gemini
- proposer quand : « recevoir sans stress », « poulet à préparer la veille », « plat qui marine tout seul »
- déclencheurs : poulet Marbella, poulet miso, cuisses au four marinées

**Tarte/quiche salée aux légumes — appareil œuf-crème + fromage sur pâte cuite à blanc**

## Pattern — Tarte salée aux légumes (appareil œuf-crème + fromage)

### Intention
Légumes pré-cuits enfermés dans une pâte croustillante et un appareil œuf-crème. Plat complet réconfortant, se mange tiède ou à température ambiante, voyage bien.

### Pattern réutilisable
```text
pâte (brisée/feuilletée) cuite à blanc dorée + légumes pré-cuits (rôtis ou fondus) + fromage en morceaux + appareil (œufs + crème + crème fraîche + sel) versé pour combler les vides → four moyen jusqu'à prise et dorure
```

### Variantes
- garnitures : poivrons-aubergine-courgette rôtis ; poireau fondu ; ail confit caramélisé ; épinards-féta
- fromages : 2 chèvres (frais + affiné), gorgonzola, féta-ricotta, gruyère
- appareil : œufs + crème liquide + crème fraîche ; ~2 œufs pour 200 ml de crème
- aromates : thym, romarin, estragon, ciboulette

### Points critiques
- cuire la pâte à blanc (lestée) puis dorée AVANT garniture, sinon fond détrempé
- pré-cuire les légumes pour évacuer l'eau
- garder fromage/garniture apparents au-dessus de l'appareil pour gratiner
- four 160-180°C : l'appareil prend sans gonfler ni trancher

### Erreurs fréquentes
- pâte non cuite à blanc → fond mou ; légumes humides → tarte qui rend de l'eau ; four trop chaud → appareil soufflé puis granuleux

### Usage Gemini
- proposer quand : reste de légumes rôtis, tarte salée, plat tiède pique-nique/lunch, recevoir sans stress
- éviter quand : pas de four, repas express

**Légumes grillés au gril/plancha + huile d'herbes vive**

## Pattern — Légumes char-grillés + huile d'herbes

### Intention
Griller les légumes sur poêle striée/plancha très chaude leur donne un goût presque carné (fumée + parties brûlées). Une huile d'herbes crue versée sur les légumes encore chauds les imprègne.

### Pattern réutilisable
```text
légumes tranchés huilés + salés → poêle striée/gril TRÈS chaud, marques nettes des 2 côtés sans cuire à cœur → huile d'herbes mixée crue (herbes + huile + ail + citron + sel) versée sur les légumes chauds → tiédir et infuser
```

### Variantes
- légumes : courgette, aubergine, chou-rave, fenouil, asperge, poivron, carotte
- fromage grillé à part : halloumi, manouri, anari
- huiles : persil-ail-citron ; basilic-persil-ail ; coriandre-lime
- finitions : pignons, copeaux de parmesan, sumac

### Points critiques
- gril/poêle vraiment brûlant (5 min de chauffe) pour les marques sans bouillir
- l'aubergine boit l'huile et peut finir au four pour cuire à cœur
- huiler les légumes pas la poêle ; ne pas surcharger
- verser l'huile d'herbes sur les légumes CHAUDS

### Erreurs fréquentes
- gril tiède → légumes qui suent, pas de marques ; huile versée à froid → moins d'absorption ; tranches trop épaisses → brûlées dehors crues dedans

### Usage Gemini
- proposer quand : barbecue/plancha, légumes d'été, accompagnement qui a du caractère, halloumi grillé
- éviter quand : pas de gril/poêle striée

**Pattern — Pâtes crémeuses finies au croquant de chapelure**

## Pattern — Pâtes crémeuses finies au croquant de chapelure

**Intention** : casser la monotonie d'une sauce crème par une chapelure (panko) grillée à sec, mêlée zeste-ail-persil, parsemée GÉNÉREUSEMENT au dernier moment. Contraste mou/croustillant.

### Formule
```text
champignons saisis + vin réduit + thym/laurier + crème → sauce nappante + eau de cuisson pour détendre + légume vert blanchi (brocolini) + pâtes al dente → FINITION panko grillé mêlé zeste citron-ail-persil, à l'assiette
```

### Variantes
- crunch : panko (idéal), chapelure rustique, pignons, noisettes concassées
- gremolata : zeste citron + ail + persil (ou estragon, basilic)
- base crémeuse : champignons-crème, courgette-crème, poireau-crème, ail-crème-parmesan
- vert : brocolini, brocoli, petits pois, asperges

### Points critiques
- panko grillé À SEC à la poêle jusqu'à doré, puis mêlé au zeste-ail-persil HORS feu
- garder de l'eau de cuisson : la sauce crème sèche vite, la viser plutôt liquide
- saler généreusement la sauce crème
- chapelure ajoutée à l'assiette, jamais dans la casserole (ramollirait)

### Usage Gemini
- proposer : « pâtes à la crème pas plates », « champignons + crème + pâtes »
- éviter : on veut léger / sans lactose

### pattern_outil

**Pattern 039 — Beurre composé crémeux à tartiner [outil]**

## Pattern 039 — Beurre composé crémeux à tartiner [pattern outil]

**Intention** : enrichir une purée crémeuse (avocat surtout) avec du beurre ramolli pour une tartinade ultra-onctueuse. S'étale sur pain grillé, fond sur une viande chaude, se prépare la veille.

### Pattern réutilisable

```text
avocat très mûr + beurre très mou (jamais fondu) + zeste/jus agrume + sel → mixer lisse → incorporer herbes hachées → repos frigo 10 min → tartiner ou pocher
```

### Variantes clés
- avocat-beurre-lime-estragon-aneth (base SIMPLE)
- beurre-herbes-ail (viande/poisson chauds)
- beurre-miso-noisette (umami, légumes rôtis)

### Points critiques
- **beurre très mou à température ambiante**, JAMAIS fondu (il se séparerait)
- avocat vraiment mûr sinon grumeleux
- préparable 1 jour à l'avance, séparé des garnitures

### Usage Gemini
- proposer quand : "rendre un avocat plus riche", "tartine de luxe", "beurre maison pour viande"
- éviter quand : on cherche du léger (c'est gras assumé)

**Pattern 046 — Caviar (purée rustique) de légume rôti [outil]**

## Pattern 046 — Caviar (purée rustique) de légume rôti [pattern outil]

**Intention** : transformer un légume rôti pressé et écrasé à la fourchette en tartinade rustique — entre baba ganoush et tapenade de légume. Topping de tartine, mezze, ou accompagnement de viande.

### Pattern réutilisable

```text
légume (courgette, aubergine) rôti avec herbes sèches + huile → PRESSER pour extraire l'eau → ajouter ail rôti pressé → écraser à la fourchette (rustique, pas lisse) → herbes fraîches + citron en finition
```

### Variantes clés
- courgette-thym-menthe-aneth (caviar de courgettes)
- aubergine-cumin (vers le baba ganoush)
- ajout possible : tahini, yaourt

### Points critiques
- **extraire l'eau** du légume rôti (passoire, presser) sinon tartinade liquide
- écraser à la **fourchette** : rustique, pas une purée mixée
- ail rôti en chemise puis pressé = douceur sans agressivité
- herbes + citron **au moment de servir** seulement
- préparable 1 jour à l'avance (sans herbes/citron)

### Usage Gemini
- proposer quand : "tartinade maison", "courgettes/aubergines à écouler", "mezze", "reste de légumes rôtis"

**Pattern 041 — Salsa froide d'aromates à l'huile chaude versée [outil]**

## Pattern 041 — Salsa froide d'aromates à l'huile chaude versée [pattern outil]

**Intention** : condiment vif obtenu en versant une huile juste chauffée sur des aromates crus (oignon vert, gingembre, piment) — la chaleur les attendrit et libère les arômes sans les cuire. Topping universel sur tomates, poulet rôti, tartine, riz.

### Pattern réutilisable

```text
aromates frais crus (oignon vert + gingembre pilé + sel) → verser dessus huile neutre juste chauffée → +acide (vinaigre/lime) → repos → cuiller sur n'importe quel plat
```

### Variantes clés
- oignon vert-gingembre-huile-vinaigre de Xérès (style Chinatown)
- oignon vert-gingembre-piment-coriandre (asiatique)
- échalote-piment-huile-citron

### Points critiques
- huile **juste chaude**, pas fumante (on attendrit, on ne frit pas)
- piler le gingembre avec le sel pour une purée parfumée
- se garde 5 jours au frigo, doubler la quantité

### Usage Gemini
- proposer quand : "condiment pour relever un plat fade", "tomates crues ou poulet rôti à booster", "gingembre + oignon vert"

> Distinct du pattern 022 (huile infusée à feu doux) : ici c'est l'huile chaude qui va aux aromates crus, pas l'inverse.

**Pattern 048 — Topping de graines/noix grillées sucrées-épicées [outil]**

## Pattern 048 — Topping de graines/noix grillées sucrées-épicées [pattern outil]

**Intention** : transformer graines (courge, citrouille) ou noix en topping croustillant sucré-salé-piquant qui réveille soupes, salades et légumes rôtis. Se fait en lot, se garde une semaine.

### Pattern réutilisable

```text
graines/noix + sirop d'érable (ou miel) + chili broyé + sel → étaler sur plaque → four ~15 min jusqu'à doré → refroidir (durcit en croustillant) → bocal hermétique, 1 semaine
```

### Variantes clés
- graines de citrouille-érable-chili (topping soupe de courge)
- amandes effilées-paprika (à la poêle, poêlées de légumes)
- noix-miel-sumac

### Points critiques
- **doubler/tripler** : garde une semaine, sert sur tout
- refroidir complètement pour le croustillant (mou à chaud)
- chili + sel équilibrent le sucre — sinon écœurant
- amandes à la poêle : surveiller, elles brûlent vite

### Usage Gemini
- proposer quand : "topping pour soupe/salade", "rendre un plat plus intéressant", "croquant à préparer d'avance"
- réflexe à suggérer dès qu'un plat manque de texture

**Pattern 037 — Oignon caramélisé en lot, base aromatique à garder [outil]**

## Pattern 037 — Oignon caramélisé en lot, base aromatique à garder [pattern outil]

**Intention** : geste de prévoyance signature SIMPLE — caraméliser une grande quantité d'oignon (souvent avec harissa ou épice) une fois, garder 2-5 jours au frigo, puis monter un plat en 5 min. Convertit une corvée de 15 min en raccourci permanent.

### Pattern réutilisable

```text
oignons émincés + huile → feu moyen 9-15 min jusqu'à tendre et bien doré → (option : +harissa/épice 1 min) → refroidir → bocal au frigo 2-5 jours
→ usage : œufs brouillés, omelette, frittata, salade de couscous, tofu brouillé, base de mijoté
```

### Variantes clés
- oignon nature caramélisé (base universelle)
- oignon + harissa à la rose (tofu/œufs brouillés)
- oignon + cumin/ras-el-hanout (grains)

### Points critiques
- **doubler ou quadrupler** systématiquement — l'effort marginal est nul
- l'épice (harissa) s'ajoute en fin, 1 min, après caramélisation
- bien refroidir avant le bocal
- ramener à température ou réchauffer avant usage

### Usage Gemini
- proposer quand : "gagner du temps en semaine", "batch cooking", "beaucoup d'oignons"
- réflexe à suggérer dès qu'une recette demande de caraméliser de l'oignon

### pattern_plat

**Pattern 036 — Œufs braisés en nids dans une base de légumes verts (technique des nids)**

## Pattern 036 — Œufs braisés en nids dans une base de légumes verts

**Intention** : variante "sèche" de la shakshuka — base de légumes verts braisés (poireaux, épinards, blette) où l'on creuse des nids pour pocher les œufs à couvert. Brunch ou souper léger, 30 min. Sous-cas technique du pattern 014 ; à retenir surtout pour le geste "réduire à sec + creuser des nids".

### Pattern réutilisable

```text
légume vert fondu (poireau/épinard/blette) + beurre-huile + aromate (cumin grillé, ail, citron confit) + bouillon réduit PRESQUE À SEC → creuser des nids à la cuillère → 1 œuf par nid + féta autour → couvrir 4-5 min (blanc pris, jaune coulant) → finir huile-zaatar
```

### Variantes clés
- bases : poireaux-épinards, blettes, courgettes râpées-petits pois, fanes braisées
- aromates : cumin grillé-citron confit, ail-piment, coriandre-curcuma
- fromage : féta, halloumi en dés, chèvre frais
- finition : huile-zaatar, huile-sumac, piment d'Urfa

### Points critiques
- réduire le bouillon **presque à sec** avant les œufs (sinon ils flottent et ne cuisent pas)
- creuser de vrais nids au dos d'une cuillère pour contenir le blanc
- cuire **à couvert** : la vapeur cuit le dessus du jaune
- huile + épice sèche badigeonnée au service, jamais en cuisson

### Usage Gemini
- proposer quand : "brunch œufs sans tomate", "poireaux/épinards + œufs", "souper léger réconfortant"
- éviter quand : pas de poêle à couvercle
- base verte préparable la veille, œufs cassés minute

> Recoupe le pattern 014 (œufs sur base verte braisée). Le complément utile ici = technique des nids + bouillon réduit à sec.

**Pattern 038 — Tofu brouillé épicé (alternative végane aux œufs brouillés)**

## Pattern 038 — Tofu brouillé épicé (alternative végane aux œufs brouillés)

**Intention** : reproduire la texture d'œufs brouillés sans œuf — tofu soyeux écrasé dans une base aromatique épicée, servi sur pain grillé. Brunch végan qui plaît aux non-végans.

### Pattern réutilisable

```text
oignons caramélisés + pâte aromatique épicée (harissa, curcuma, cumin) → tofu soyeux égoutté écrasé au presse-purée (texture brouillée) + sel → réchauffer 2 min → sur pain au levain grillé + salade fraîche acidulée à côté
```

### Variantes clés
- tofu-harissa-coriandre (base SIMPLE)
- tofu-curcuma-cumin (style "œufs" indien)
- garniture : échalotes frites croustillantes, herbes, salade avocat-concombre-lime

### Points critiques
- **tofu soyeux** (pas ferme) pour la texture crémeuse type œuf
- écraser au presse-purée, pas au fouet
- saler franchement (le tofu est neutre)
- ne pas trop cuire : juste chaud, sinon il rend de l'eau

### Usage Gemini
- proposer quand : "brunch végan", "alternative aux œufs", "tofu soyeux"
- éviter quand : seul tofu ferme dispo (basculer vers émietté sauté)

**Pattern 040 — Pain rapide salé sans levure ni pétrissage**

## Pattern 040 — Pain rapide salé sans levure ni pétrissage

**Intention** : pain-gâteau salé monté à la poudre à pâte/bicarbonate, sans levée ni pétrissage. Texture entre pain et cake, garni de légume râpé + fromage + graines. Se congèle, se grille.

### Pattern réutilisable

```text
secs (farine + poudre à pâte + bicarbonate + sel + graines) // humides (œufs + huile + crème sure/yaourt + un peu de sucre/miel) → légume râpé (betterave, courgette, maïs) + fromage en morceaux → mélanger sans excès → moule → four moyen 40-80 min → graines sur le dessus
```

### Variantes clés
- betterave-carvi-chèvre-graines de courge (style cake)
- maïs-cheddar-féta-jalapeño (cornbread en poêle fonte)
- ajouter une herbe sèche (thym) dans la pâte

### Points critiques
- **ne pas trop mélanger** (mie caoutchouteuse sinon)
- ajouter le fromage en morceaux délicatement
- cornbread : noircir le maïs à sec avant de l'incorporer (saveur grillée)
- se grille bien une fois rassis ; congèle 1 mois

### Usage Gemini
- proposer quand : "pain maison sans attente", "betterave/courgette à écouler", "accompagnement brunch"
- éviter quand : on veut une vraie mie de pain levé

**Pattern 042 — Salade de rubans de légume cru massés à l'huile infusée**

## Pattern 042 — Salade de rubans de légume cru massés à l'huile infusée

**Intention** : légume cru (courgette) taillé en rubans fins, massé avec une huile parfumée pour l'assouplir sans cuisson. Rend un légume aqueux savoureux et tendre tout en gardant du croquant.

### Pattern réutilisable

```text
huile infusée à part (thym/ail/zeste, feu doux 8 min, filtrée) → légume en rubans fins (économe/mandoline) + noix + jus citron + sel → MASSER 1 min à la main (le légume se brise un peu) → herbes en finition
```

### Variantes clés
- courgette-thym-noix-basilic
- carotte/fenouil/asperge crue en rubans
- huiles : ail-zeste citron, piment, graines de cumin

### Points critiques
- **masser physiquement** avec les doigts (assouplit, fait pénétrer l'huile)
- saler et citronner **au dernier moment** (le légume rend de l'eau sinon)
- huile infusée préparable 3 jours à l'avance
- rubans fins et réguliers

### Usage Gemini
- proposer quand : "courgettes crues", "salade qui change", "légume cru à valoriser sans cuisson"
- éviter quand : légume pas assez frais

**Pattern 044 — Salade de fruits crus en registre salé (acide + herbe + épice)**

## Pattern 044 — Salade de fruits crus en registre salé (acide + herbe + épice)

**Intention** : traiter un fruit cru comme un légume de salade — bâtonnets nets, agrume vif, herbes fraîches, épice/aromate inattendu (citronnelle, cinq-épices, graines de moutarde). Accompagnement d'été qui coupe le gras d'une viande grillée.

### Pattern réutilisable

```text
fruit ferme en bâtonnets/quartiers (melon d'eau, pomme verte, pêche) + agrume (lime/citron) + huile + aromate surprise (citronnelle, cinq-épices, échalote macérée) + herbes (menthe+coriandre) + graines grillées → assembler MINUTE, égoutter le jus
```

### Variantes clés
- melon d'eau + pomme verte + lime + citronnelle + graines de moutarde
- pêche + framboise écrasée + cinq-épices + radicchio + cresson
- garniture : arachides/pistaches/cajou grillées salées

### Points critiques
- fruits **pas trop mûrs** (sinon trop sucré, et tiennent mieux en bâtonnets)
- assembler **juste avant de servir** et **jeter le jus** au fond du bol
- saler franchement (c'est une salade, pas un dessert)

### Usage Gemini
- proposer quand : "salade d'été originale", "accompagnement de BBQ/porc", "melon ou pêche à utiliser"
- éviter quand : fruits hors saison ou fades

**Pattern 045 — Légume tendre braisé dans un bouillon aromatique au four**

## Pattern 045 — Légume tendre braisé dans un bouillon aromatique au four

**Intention** : cuire un légume délicat (courgettes, fenouil) immergé dans un bouillon parfumé, à couvert au four, jusqu'à fondance complète — technique douce opposée au rôtissage sec. Texture soyeuse, plat de mezze ou entrée.

### Pattern réutilisable

```text
légume rangé serré dans un plat → bouillon chaud aromatisé (ail + herbe) versé pour couvrir + sel → couvrir d'alu → four ~45 min jusqu'à fondant → égoutter → finition : huile + aromate frit (origan/ail) + sel en flocons
```

### Variantes clés
- courgettes-ail-origan (origan frit en finition)
- fenouil-citron-thym
- poireaux entiers-bouillon-zeste

### Points critiques
- légume **serré** dans le plat (tient et cuit régulièrement)
- bouillon **chaud** versé (gagne du temps)
- cuire **à couvert** (on braise, on ne rôtit pas)
- la finition (huile + aromate frit + sel en flocons) fait tout le caractère

### Usage Gemini
- proposer quand : "courgettes tendres", "mezze", "entrée délicate", "légume fondant sans friture"
- éviter quand : on cherche coloration/croustillant (alors rôtir, pattern 001)

**Pattern 047 — Légume évidé farci (farce liée par sa chair + fromage)**

## Pattern 047 — Légume évidé farci (farce liée par sa chair + fromage)

**Intention** : transformer un légume en contenant — courgette/poivron évidé, farci d'une farce qui réutilise sa propre chair liée à l'œuf et au fromage, gratiné au four. Plat principal végétarien ou accompagnement généreux.

### Pattern réutilisable

```text
légume coupé en barquette, chair retirée + PRESSÉE pour extraire l'eau → farce = chair + œuf + parmesan + mie de pain + tomate écrasée + sel → garnir → four très chaud ~15 min jusqu'à doré → topping (pignons + zeste + herbes) au service
```

### Variantes clés
- courgette-parmesan-pignons-origan (base SIMPLE)
- poivron-riz-féta
- aubergine-tomate-chapelure

### Points critiques
- garder ~1 cm de paroi (la barquette doit tenir)
- **presser la chair** retirée (sinon farce détrempée)
- œuf + fromage + mie = le trio liant
- farce préparable la veille
- four très chaud (230-250°C) pour gratiner la farce sans dessécher le légume

### Usage Gemini
- proposer quand : "légumes farcis", "grosses courgettes/poivrons", "plat végé soigné"
- éviter quand : peu de temps (l'évidage est long)

**Pattern 043 — Taboulé inversé : herbes majoritaires, grain minoritaire**

## Pattern 043 — Taboulé inversé : herbes majoritaires, grain minoritaire

**Intention** : le taboulé Ottolenghi est une salade d'HERBES, le grain n'est qu'un liant minoritaire. Variante : remplacer le grain par du chou-fleur cru râpé ("faux boulgour") pour une version légère sans gluten.

### Pattern réutilisable

```text
base = herbes en MASSE (persil + menthe + aneth) + oignon vert → +grain cuit OU chou-fleur cru râpé grossièrement macéré 20 min dans citron+sel → huile + épice (piment de la Jamaïque) → grenade ou pistaches en finition
```

### Variantes clés
- chou-fleur cru râpé (sans gluten, plus léger)
- boulgour fin classique (minoritaire)
- finition : grenade, pistaches grillées, ou les deux

### Points critiques
- les herbes pèsent **plus** que le grain — c'est le principe
- chou-fleur râpé grossièrement (râpe ou robot par à-coups) — ne pas réduire en bouillie
- macérer chou-fleur/grain dans citron+sel 20 min avant d'assembler
- assembler et servir aussitôt

### Usage Gemini
- proposer quand : "taboulé maison", "beaucoup d'herbes à écouler", "salade légère sans gluten", "un chou-fleur"
- éviter quand : peu d'herbes (le plat s'effondre)

### principe

**Principe — Cuisiner pour recevoir : tout d'avance, servir à T° ambiante**

## Principe — La logique "prendre de l'avance" Ottolenghi (recevoir sans stress)

Philosophie d'organisation pour les repas de réception, à appliquer transversalement.

- **Privilégier les plats qui se préparent à l'avance** et gagnent en saveur (mijotés de légumineuses, calmar, poisson au piment-tahini : meilleurs le lendemain ; sauces/tartinades/vinaigrettes conservables au frigo ou congélateur).
- **Prendre de l'avance par étapes**, pas seulement par stockage : noix grillées, panure/farce préparées, grains cuits et refroidis, légumes blanchis/rôtis et ramenés à T° ambiante — des heures avant ou la veille.
- **Servir à température ambiante** (ou réchauffé) plutôt que froid du frigo ; couvrir la table avant l'arrivée, chacun se sert. Seuls quelques plats sortent du four ou s'assemblent minute (signalé dans les recettes).
- **Choisir des plats faciles à doubler/tripler** : une sauce ou un ragoût se double aussi facilement, on congèle la moitié.
- **Identifier ce qui s'assemble en dernier** (herbes, vinaigrettes sur feuilles tendres, croquants, jus réservés) et le garder à part jusqu'au service.
- Penser **batch** : oignons frits, dukkah, ail confit, sauces et huiles aromatiques en grande quantité, ça se conserve.

### Usage Gemini
- activer quand : "je reçois", "menu pour X personnes", "préparer à l'avance", "buffet/mezze", "qu'est-ce que je peux faire la veille"

**Principe transverse — Substitution "vide-frigo" à poids net constant**

## Principe transverse — Substitution "vide-frigo" à poids net constant

**Idée** : dans une majorité de recettes SIMPLE (vinaigrettes d'herbes, beignets aux herbes, gâteaux frigo), les composants d'une même famille sont **librement interchangeables tant que le poids net total reste identique**. La clé pour cuisiner avec ce qu'on a au lieu de courir après une liste.

### Règle pratique

```text
remplacer librement à l'intérieur d'une famille, à POIDS NET CONSTANT :
- herbes fraîches (persil ↔ coriandre ↔ aneth ↔ basilic ↔ estragon)
- fruits secs (raisin ↔ abricot ↔ datte ↔ cerise séchée)
- noix (amande ↔ pignon ↔ pistache ↔ noix)
- légumes verts feuilles (épinard ↔ blette ↔ kale)
```

### Points critiques
- garder le **poids total** identique (sinon l'équilibre change)
- rester dans la **même famille** (pas d'herbe contre une noix)
- herbes très puissantes (estragon, menthe) : doser un peu en deçà

### Usage Gemini
- réflexe par défaut quand l'utilisateur dit "je n'ai pas X, j'ai Y à la place"
- proposer quand : "vide-frigo", "j'ai des herbes qui traînent", "je n'ai pas l'ingrédient exact"
- rassurer : "tant que le poids reste le même, ça marchera"

### principle

**Assaisonner les herbes/feuilles délicates à la SECONDE du service**

Règle pour salades d'herbes et feuilles tendres (cresson, basilic, aneth, estragon, romaine).

Principe : les herbes délicates flétrissent instantanément au contact de la vinaigrette acide. Garder feuilles et herbes à part (au frais, en boîte hermétique, jusqu'à quelques heures), et ne verser la vinaigrette + noix qu'au moment EXACT de servir, puis mélanger doucement.

Corollaire : une salade d'herbes (cresson + basilic + coriandre + aneth + estragon + pistaches grillées + vinaigrette citron-fleur d'oranger) est un excellent rafraîchisseur de palais entre deux plats riches.

### reference

**Substitutions et équivalences utiles (cardamome, épine-vinette, harissa…)**

## Substitutions et dosages — aide-mémoire

- **Cardamome** : ½ c. à thé de graines (à broyer) = ¼ c. à thé de cardamome moulue. La moulue est plus concentrée, diviser de moitié.
- **Baies d'épine-vinette** → raisins de Corinthe trempés 30 min dans du jus de citron (30 ml de jus pour 45 ml de raisins) puis égouttés.
- **Harissa** : goûter avant de doser. Si douce, +50 % ; si très piquante, -50 %. Énormes écarts entre marques.
- **Piment ancho séché** → 1 c. à thé de paprika doux fumé.
- **Noix de coco fraîche râpée** → flocons séchés (griller 2-3 min au lieu de 6-7).
- **Vin de riz shaoxing** → xérès.

### Usage Gemini
- consulter quand : un ingrédient signature manque, ou pour ajuster les doses d'épices fortes

**Les 10 ingrédients signature Ottolenghi (garde-manger)**

## Les 10 ingrédients signature Ottolenghi [référence garde-manger]

Dix "bombes de saveur" qui transforment un plat banal en plat Ottolenghi. Tous se conservent longtemps au garde-manger ; une pincée ou un filet suffit. Provenance > marque : épicier moyen-oriental/iranien pour le meilleur sumac, zaatar, tahini, épine-vinette.

- **Sumac** : épice rouge acidulée. Sur œufs (classique), viandes, poissons, légumes grillés ; dans une vinaigrette ou une marinade. Marche même sur les desserts.
- **Zaatar** : mélange thym zaatar + sésame + sumac + sel (les bons n'ont que ces 4). Pincée sur viande/poisson/légumes, ou en huile aromatisée.
- **Piment d'Urfa en flocons** : turc, fumé, légèrement chocolaté, peu piquant. Sur œufs brouillés, avocat écrasé sur tartine, tomates rôties chaudes.
- **Cardamome** : note douce aromatique, plats salés et sucrés. Le livre part souvent des gousses entières (à écraser/broyer). Équivalence : ½ c. à thé de graines broyées = ¼ c. à thé de moulue (sinon trop explosif).
- **Mélasse de grenade** : sirop aigre-doux. Un trait sur légumes/viande, dans une marinade ou un mijoté pour un enrobage caramélisé. Excellente sur l'agneau haché (boulettes).
- **Harissa à la rose** : pâte de piment nord-africaine adoucie de pétales. Dans marinades, sur pâtes, omelettes, oignons caramélisés. Goûter avant de doser : si douce +50 %, si très piquante -50 % (énormes écarts entre marques).
- **Tahini** : pâte de sésame ; préférer le crémeux (libanais/israélien/palestinien). Base de sauces et vinaigrettes, croûte de hachis parmentier, arrosage de poisson poché, tartine miel.
- **Baies d'épine-vinette** : petites baies séchées acidulées. Beignets, frittatas/omelettes, salades de riz, salsa. À défaut : raisins de Corinthe trempés 30 min dans du jus de citron (30 ml pour 45 ml de raisins) puis égouttés.
- **Ail noir** : ail fermenté, doux, goût balsamique/réglisse, riche en umami. Sur pizza, dans un risotto, équilibre l'amertume des choux de Bruxelles.
- **Citron confit** (petits, peau fine) : punch citronné intense. Souvent on n'en hache que l'écorce, dans salades, vinaigrettes, betteraves rôties, œufs braisés.

### technique

**Pattern outil — Pâte fraîche aromatisée dans la masse (zeste + curcuma + safran)**

## Pattern outil — Pâte fraîche aromatisée dans la masse

**Intention** : pour qui fait sa pâte maison, parfumer la PÂTE elle-même (pas seulement la sauce) : zeste d'agrume, curcuma (couleur + note terreuse), safran infusé. La pâte devient un ingrédient de saveur.

### Formule
```text
farine 00 + œufs + huile + AROMATE INTÉGRÉ (zeste citron râpé / curcuma moulu / safran infusé 10 min dans eau chaude) → pétrir, reposer 30 min, abaisser
```

### Variantes
- zeste citron + curcuma → ravioli chèvre-citron (finition : pignons roses concassés, estragon, huile de pépins de raisin)
- safran infusé + curcuma → tagliatelles dorées (finition : beurre épicé)
- sans pâte maison : pincée de safran dans l'eau de cuisson de pâtes sèches de qualité

### Points critiques
- infuser le safran 10 min dans l'eau chaude avant de l'ajouter aux œufs
- curcuma colore fort : dosage modéré
- pâte ni collante ni sèche : ajuster farine/huile
- ravioli au fromage frais : sceller sans bulle d'air, fariner le plan

### Usage Gemini
- proposer : pâte maison, « pâtes parfumées/colorées », « ravioli maison »
- éviter : pas d'envie/matériel pour pâte maison (alors safran dans l'eau de cuisson)

**Pilaf de grain par absorption hors feu (boulgour, freekeh)**

Methode pilaf "feu coupe" pour boulgour/freekeh, plus fiable que la cuisson continue :
- Faire revenir oignons/legumes + griller epices et fruits secs dans la matiere grasse.
- Ajouter le grain, mouiller (boulgour ~1 vol grain pour 1,75 vol eau ; freekeh ~1 pour 1,25 de bouillon reduit).
- Boulgour : porter a ebullition, couvrir hermetiquement, RETIRER DU FEU et laisser gonfler au moins 20 min.
- Freekeh : porter a ebullition puis cuire 15 min a feu minimal couvert + 5 min hors feu couvert.
- Egrener a la fourchette ; si sec, ajouter un filet d'huile.
- Freekeh : tremper 5 min a l'eau froide puis rincer/egoutter avant cuisson (enleve amertume/poussiere de fumage).
Leve une erreur frequente : le grain qui colle/brule au fond.

**Cuire riz complet/rouge "comme des pates" et quinoa minute**

Pour les grains rustiques, abandonner l'absorption et cuire a grande eau (comme des pates) :
- Riz rouge de Camargue / riz complet : grand volume d'eau bouillante NON salee, ~20 min jusqu'a tendrete, puis egoutter.
- Quinoa : grande eau bouillante, fremir 9 min seulement, egoutter dans une passoire fine ; laisser secher encore tiede avant d'assaisonner (evite la bouillie).
- Pour parfumer un riz nature : cuire avec quelques tiges de basilic (feuilles attachees) qu'on retire apres cuisson.
Utile pour les salades de grains : etaler sur un plateau pour refroidir vite et garder les grains separes.

**Polenta : point de cuisson et repere instant vs traditionnelle**

Reperes concrets pour reussir une polenta cremeuse :
- Verser la polenta EN PLUIE dans le liquide bouillant, remuer constamment a la cuillere en bois, feu minimal.
- Temps : polenta instantanee ~5 min ; traditionnelle jusqu'a 50 min.
- Point de cuisson : prete quand elle se decolle des parois mais reste coulante. Si elle seche, rallonger avec un peu de bouillon/eau pour garder une consistance de "porridge epais".
- Finir hors feu avec beurre + parmesan (ou feta) pour le cremeux.
- Restes : etaler sur surface huilee, laisser figer, couper en morceaux et poeler a l'huile le lendemain (deuxieme repas).

**Reussir des champignons bien dores (poelee)**

Pour des champignons colores (et pas bouillis) :
- Poele large bien chaude, huile chaude, cuire en 2 fournees : ne pas surcharger.
- Ne presque pas remuer pour laisser des plaques dorees se former sur la surface.
- Ail, herbes fraiches et huile parfumee (truffe) ajoutes HORS FEU a la fin (l'ail ne brule pas, les herbes restent vives).
Meme logique que pour saisir une viande : la vapeur empeche la coloration si la poele est trop pleine.

**Courgettes frites puis marinees au vinaigre (salade de pates)**

Pour une salade de pates/legumes fraiche et acidulee :
- Couper les courgettes en tranches de ~0,5 cm.
- Frire a l'huile chaude en plusieurs fournees sans surcharger, ~3 min, dore des deux cotes, RETOURNER UNE SEULE FOIS.
- Egoutter en passoire, puis arroser de vinaigre de vin rouge encore tiedes : elles s'impregnent (marinade express).
- Pour les pates en salade : cuire al dente, rincer a l'eau froide pour stopper la cuisson, puis assaisonner.
Astuce sauce verte : mixer basilic + persil + huile d'olive + sel/poivre pour une sauce lisse qui lie la salade.

**Panko grille a sec pour ajouter du croquant a une pate cremeuse**

Pour casser la lourdeur d'une pate a la creme sans alourdir la sauce :
- Faire griller du panko a sec dans une poele a feu moyen jusqu'a dore, en remuant.
- Le melanger a une gremolata (zeste de citron + ail + persil) et l'eparpiller GENEREUSEMENT au service.
- Sauce creme : elle seche vite, la garder coulante et la detendre avec de l'eau de cuisson des pates reservee.
- Sauce vin-creme : reduire le vin des deux tiers AVANT d'ajouter la creme (concentre sans soupe).

**Astuce — Chocolat noir comme exhausteur umami dans un mijoté**

## Astuce — Carré de chocolat noir dans un mijoté de viande à la tomate

Un petit morceau de chocolat noir (70 %) ajouté en fin de mijotage d'un ragoût tomate-épices (poulet, agneau) apporte profondeur, rondeur et une note umami sans goût sucré identifiable. Logique proche du mole mexicain.

### Repère
- ~15 g de chocolat noir pour un mijoté de ~6 portions
- ajouter en fin de cuisson, à découvert, laisser fondre et mijoter
- s'associe bien à harissa + paprika fumé + poivrons rôtis

### Usage Gemini
- proposer quand : « mijoté qui manque de profondeur », « ragoût tomate-épices », touche secrète
- déclencheurs : chocolat dans un plat salé, mole, ragoût poulet harissa

**Astuce — Extraire l'eau des légumes râpés avant de les lier**

## Astuce — Essorer les légumes râpés crus avant de les incorporer à un appareil

Pour un pain de viande, des boulettes ou des galettes incluant des légumes crus râpés (courgette, carotte, oignon, tomate), hacher les légumes au robot puis les **presser dans une passoire** pour en extraire le maximum de liquide avant de les mélanger à la viande/l'appareil. Sinon l'eau relâchée rend la préparation détrempée et empêche la tenue.

### Repère
- hacher les légumes à la taille du haché (consistance homogène)
- presser fort dans une passoire au-dessus d'un bol
- même principe que pour les galettes de légumes verts (presser petits pois, courgettes)

### Usage Gemini
- proposer quand : pain de viande, boulettes ou galettes avec légumes crus
- déclencheurs : légumes qui rendent de l'eau, galette qui s'effondre

**Astuce — Poisson à peau croustillante : presser et finir côté chair**

## Astuce — Filet de poisson à peau croustillante à la poêle

Pour une peau bien croustillante et plate : poser le filet **peau dessous** dans l'huile très chaude et **presser le filet avec une spatule** les premières secondes pour empêcher la peau de se rétracter. Cuire l'essentiel du temps côté peau (saumon ~3 min, maquereau ~2 min) jusqu'à ce qu'elle soit dorée et croustillante, puis retourner brièvement pour finir la chair (1-4 min selon épaisseur).

### Repère
- la majeure partie de la cuisson se fait côté peau
- huile chaude (feu vif au départ), réduire après le retournement
- ne pas bouger le filet tant que la peau n'est pas dorée

### Usage Gemini
- proposer quand : saumon, maquereau, bar, dorade à la poêle
- déclencheurs : peau de poisson croustillante, filet poêlé

**Technique — Panure noix de coco grillée pour poisson (bâtonnets enfants)**

## Technique — Panure croquante à la noix de coco grillée [complète Pattern 013]

Variante de panure pour le Pattern 013 (croquettes/galettes). Idéale pour des bâtonnets de poisson qui plaisent aux enfants.

```text
poisson blanc ferme mariné court (lime + crème de coco + sel, 1 h max) → essuyer l'excédent → tremper dans beurre fondu → rouler dans noix de coco grillée à sec + panko + chili broyé + sel → cuire sous le gril, retourner à mi-cuisson, 5-6 min
```

### Points critiques
- griller la noix de coco À SEC d'abord (6-7 min chair fraîche, 2-3 min flocons séchés) : sans ça, pas de goût grillé
- mariner 1 h MAX dans la crème de coco puis retirer l'excédent (sinon la panure n'adhère pas)
- chili broyé doux : réduire ou omettre pour les enfants
- si la panure dore avant que le poisson soit cuit : éteindre le gril, laisser finir 2-3 min sur chaleur résiduelle

### Usage Gemini
- proposer quand : "bâtonnets de poisson maison", "poisson qui plaît aux enfants", "j'ai de la noix de coco râpée"

**Technique — Yaourt grec égoutté (labneh express) en étamine**

## Technique — Égoutter le yaourt grec pour l'épaissir (labneh / base dessert) [pattern outil]

Geste de base récurrent chez Ottolenghi, salé comme sucré.

```text
yaourt grec (+ sucre glace + pincée de sel si dessert) → passoire tapissée d'étamine ou linge propre sur un bol → former un baluchon, déposer un poids dessus → frigo 30 min (express) à plusieurs heures → presser pour extraire le maximum de petit-lait → jeter le liquide
```

### Repères
- 900 g de yaourt → ~550 g de yaourt épaissi (perte d'~⅓ en petit-lait)
- 30 min = crémeux épais ; plusieurs heures = consistance labneh tartinable

### Usages
- base de cheesecake sans cuisson, crème de yaourt pour fruits rôtis, labneh salé pour mezze, lit froid sous tomates rôties chaudes

### Usage Gemini
- proposer quand : "épaissir du yaourt", "faire du labneh", "base crémeuse pour dessert aux fruits"

**Technique — Réfrigérer les croquettes avant cuisson pour qu'elles tiennent**

## Technique — Raffermir les croquettes/galettes au frigo avant cuisson [complète Pattern 013]

Détail décisif pour le Pattern 013 : façonner puis réfrigérer avant de cuire évite que les croquettes s'effondrent à la poêle, et permet de tout préparer la veille.

```text
façonner les croquettes → réfrigérer 15 min minimum (ou jusqu'au lendemain) pour les raffermir → cuire à la poêle dans une huile bien chaude (2-3 min/face) ou poêle + four
```

### Points critiques
- 15 min = minimum ; jusqu'à 24 h = avantage organisation (cuisson minute le jour J)
- on peut aussi cuire la veille et juste réchauffer au service
- mélange lié au robot par PULSATIONS courtes (pâte grossière, pas une purée)

### Usage Gemini
- proposer quand : "croquettes qui s'effondrent", "préparer des galettes à l'avance", "tacos/croquettes pour recevoir"

**Fenouil poêlé caramélisé mais ferme (beurre + sucre + graines de fenouil)**

Caraméliser le fenouil sans le ramollir : il garde du croquant.

Méthode :
- trancher les bulbes en tranches d'1 cm (garder la base qui tient les couches)
- saisir par lots dans beurre + huile chaude, sans surcharger, ~2 min par face jusqu'à doré clair, retirer
- une fois tout saisi : ajouter sucre + graines de fenouil + sel/poivre dans la poêle, 30 s
- remettre les tranches, enrober 1-2 min dans le sucre fondu (rester FERME à l'intérieur, juste glacé)

Finition à température ambiante : ail pressé + aneth + chèvre frais en cuillerées + zeste citron + pluches de fenouil.

Idée clé : la caramélisation est un glaçage de surface, pas une cuisson à cœur.

**Réduction sucrée-acide comme alternative au vinaigre (verjus, jus d'agrume)**

Vinaigrette à base d'un liquide acide RÉDUIT, plus rond et sirupeux qu'un vinaigre brut.

Principe : faire réduire un liquide acide-fruité à frémissement jusqu'à consistance sirop, refroidir, puis monter à l'huile.
- verjus (jus de raisin vert) réduit à ~3 c. à s. → vinaigrette douce-acide sur crudités fines (asperge crue, fenouil, betterave à la mandoline)
- jus d'orange sanguine + citron + sirop d'érable réduit 20-25 min → sirop pour salade amère (radicchio, trévise) + ricotta + grenade

La réduction concentre le fruit et adoucit l'acide : idéal sur légumes crus tranchés fin.

**Bouillon de légumes profond (sucs + pruneaux) [pattern outil]**

## Pattern outil — Bouillon de légumes à la saveur profonde

### Intention
Donner du corps et de l'umami à un bouillon végétarien souvent fade : colorer les légumes avant de mouiller, et ajouter quelques PRUNEAUX pour une douceur ronde et une profondeur quasi carnée. Idem avec des croûtes de parmesan.

### Pattern réutilisable
```text
légumes aromatiques (carotte, céleri, oignon, ail, céleri-rave) revenus jusqu'à coloration légère + herbes + poivre + laurier + QUELQUES PRUNEAUX → couvrir d'eau froide → mijoter ~1h30 en écumant → filtrer
(variante umami : ajouter des croûtes de parmesan pendant la cuisson, puis les retirer)
```

### Points critiques
- COLORER les légumes avant de mouiller = base de saveur
- les pruneaux apportent rondeur et profondeur sans sucrer franchement
- les croûtes de parmesan = levier umami gratuit (à congeler au fil du temps)
- écumer et compléter en eau pour un bouillon net

### Usage Gemini
- proposer quand : base de soupe végé, risotto, braisé sans viande ; comment relever un bouillon de légumes fade
- astuce : garder les croûtes de parmesan au congélateur pour cet usage

**Pocher un coing (preparer ce fruit "qui fait peur")**

Le coing est immangeable cru (dur, apre) : un pochage lent le transforme (chair rouge, parfumee, tendre).
- Sirop : eau + sucre (~1,75 vol eau pour 1,5 vol sucre) + grains de poivre, zestes d'orange, laurier, jus de citron, un peu de vin rouge ; chauffer juste pour dissoudre le sucre.
- Peler et epepiner, couper en quartiers/segments ; GARDER peau et coeurs et les ajouter au sirop (pectine + couleur rouge).
- Cuire couvert au four doux 135 C (275 F) environ 2 h jusqu'a tendrete complete.
- Le sirop restant se garde : chaud sur une glace vanille.
Va avec : Gorgonzola/fromage bleu, viandes grasses (agneau, gibier, porc), salade amere + pistaches.

**Polenta de mais frais (alternative douce a la semoule de mais)**

Polenta faite de mais frais : plus douce et plus legere que la polenta de semoule, texture puree.
- Egrener ~570 g de grains (env. 6 epis ; couteau, epi debout sur sa base).
- Cuire les grains couverts d'eau, fremissement bas 12 min.
- Mixer longuement au robot pour casser les enveloppes (ajouter un peu d'eau de cuisson si trop sec).
- Remettre la puree + l'eau de cuisson, cuire en remuant 10-15 min jusqu'a consistance de puree de pommes de terre.
- Finir avec beurre + feta.
Servir avec une sauce relevee (ex. sauce aubergine-tomate) car la base est tres douce.

**Beurre epice facon marocain pour pates/couscous**

Condiment polyvalent (sur pates fraiches, couscous, legumes vapeur) :
- Faire fondre beurre + huile d'olive, y cuire doucement des echalotes ~10 min jusqu'a ce qu'elles fondent et que le beurre brunisse legerement.
- Hors feu, incorporer un melange d'epices : gingembre, paprika doux, coriandre, cannelle, cayenne, flocons de piment, curcuma + sel.
- Verser sur les pates/grain, finir pignons grilles + menthe + persil.
Contre-intuitif (pates + beurre d'epices marocain) mais efficace ; raccourci : bonnes pates seches + une pincee de safran dans l'eau de cuisson.

**Légume amer caramélisé cut-side down + fromage fondu (endive, fenouil)**

Transformer un légume amer/anisé en gratin réconfortant.

Formule :
légume coupé en deux (endive) ou en tranches (fenouil) → poêle chaude beurre + huile + pincée de sucre → face coupée vers le bas, NE PAS BOUGER 3-5 min jusqu'à doré profond → transférer en plat → fromage fondu dessus → four jusqu'à bouillonnement → chapelure + poivre → four pour gratiner.

Points critiques :
- ne pas surcharger la poêle (sinon vapeur, pas de coloration ; cuire en deux fois)
- ne pas remuer pendant la saisie : la croûte caramélisée contre l'amertume
- sucre + beurre = caramélisation qui équilibre l'amer

Variantes : endive + gruyère (note piquante qui marche mieux avec l'amertume) / taleggio (plus crémeux) / raclette ; fenouil + chèvre frais + zeste citron + aneth.

**Blanchir en cascade : temps étagés, refroidir à l'eau glacée**

Cuire plusieurs légumes verts pour une salade de verts croquants.

Méthode :
- blanchir chaque vert selon son temps propre, refroidir IMMÉDIATEMENT à l'eau glacée (fixe la couleur + stoppe la cuisson)
- temps étagés courts : haricots verts ~4 min, pois mange-tout ~1 min, petits pois ~20 s
- on peut réutiliser la même eau pour les verts à temps proches (ex. petits pois juste après les pois mange-tout) ; changer d'eau si un vert l'a trop colorée
- bien égoutter et SÉCHER avant d'assaisonner (sinon vinaigrette diluée)

Résultat : verts éclatants, croquants. Base idéale pour salade graines + herbes.

**Graines entières grillées dans l'huile jusqu'à éclater, versées brûlantes**

Réveiller graines entières (moutarde, coriandre, cumin, nigelle) pour assaisonner une salade.

Méthode :
- graines + huile dans une petite casserole, chauffer
- attendre qu'elles commencent à ÉCLATER (popping)
- verser huile + graines BRÛLANTES directement sur les légumes

L'huile chaude libère les arômes ET sert de vinaigrette tiède. Ajouter ensuite les aromates crus (oignon, piment, ail, zeste, herbes).

Différent du grillage à sec : ici l'huile devient parfumée et fait partie de la sauce. (Variante du pattern outil 'huile infusée' : versée chaude sur cru.)

**Ail confit caramélisé [pattern outil]**

## Pattern outil — Ail confit caramélisé

### Intention
Transformer des gousses d'ail entières en perles fondantes, douces, enrobées d'un sirop foncé. Condiment puissant pour tartes, légumes rôtis, pâtes, tartines.

### Pattern réutilisable
```text
gousses pelées blanchies 3 min (enlève l'âcreté) → égoutter → revenir 2 min à l'huile → balsamique + eau → mijoter 10 min → ajouter sucre + romarin/thym + sel → réduire jusqu'à gousses enrobées d'un caramel foncé
```

### Points critiques
- BLANCHIR d'abord : enlève le piquant cru, garantit la douceur
- réduire jusqu'à sirop, pas jusqu'à brûlé (amertume)
- balsamique + sucre = base sucrée-acide qui caramélise

### Usage Gemini
- proposer quand : tarte/quiche, garniture de légumes rôtis, tartine, base de sauce
- se garde plusieurs jours au frigo dans son sirop

**Pattern outil — Vinaigrette mélasse de grenade (échalote + moutarde)**

## Pattern outil — Vinaigrette mélasse de grenade

**Intention** : vinaigrette signature sucrée-acide-fruitée, montée à l'échalote, qui réveille salades fruit-fromage, légumes rôtis, grains, lentilles.

### Formule
```text
échalote ciselée + moutarde (Dijon) + mélasse de grenade + sel/poivre → fouetter vigoureusement en versant l'huile d'olive en filet → émulsion homogène
```

### Variantes
- ajouts : trait de jus de citron, pincée de sumac, grains de grenade frais en finition
- supports : roquette + fruit + fromage frais, betterave rôtie, lentilles, grains, crudités
- simplifiée : mélasse de grenade + huile + sel (sans moutarde)

### Points critiques
- monter en émulsion (huile en filet) pour qu'elle nappe
- doser la mélasse : très concentrée, peu suffit
- l'échalote macère dans l'acide pendant qu'on fouette (s'adoucit)

### Usage Gemini
- proposer : « vinaigrette hors de l'ordinaire », « j'ai de la mélasse de grenade », « salade fromage-fruit ou betterave »

**Aubergine brûlée : chair fumée pour dip ou plat**

Technique signature : aubergine entière brûlée pour récupérer une chair fumée (base de dip, salade, plat).

Méthode :
- TOUJOURS percer l'aubergine en plusieurs points (sinon risque d'explosion sous le gril ; Ottolenghi a reçu des lettres de lecteurs à ce sujet)
- sur gaz (le plus efficace) : poser directement sur la flamme, 12-15 min, tourner souvent à la pince, jusqu'à peau noircie partout et chair molle/fumée ; surveiller pour éviter qu'elle prenne feu
- sur électrique : percer, plaque tapissée d'alu, sous gril chaud ~1h, tourner plusieurs fois, l'aubergine doit se dégonfler complètement
- fendre, récupérer la chair à la cuillère en évitant la peau noire
- ÉGOUTTER la chair en passoire 15-30 min avant d'assaisonner (sinon trop d'eau)

Usages : dip tahini, croquettes, lentilles + aubergine, sauce.

**Tempérer le yaourt pour une soupe chaude qui ne tranche pas**

Faire une soupe chaude à base de yaourt sans qu'il graine.

Méthode (le geste qui sauve) :
- fouetter yaourt + ail + 1 œuf dans un grand bol résistant à la chaleur
- ajouter UNE louche de soupe chaude en fouettant, puis une autre, progressivement, jusqu'à incorporer au moins la moitié de la soupe (le froid + chaud d'un coup = ça tranche)
- reverser ce mélange tempéré dans la casserole
- réchauffer à feu moyen en remuant CONSTAMMENT, sans jamais bouillir

L'œuf stabilise le yaourt et donne du corps. Finir : herbes, zeste citron, filet d'huile.

Applicable à toute soupe yaourt chaude.

### tip

**Préférer les tomates semi-séchées aux tomates séchées en salade**

Pour les salades : éviter les tomates séchées au soleil (dures, agressives en goût et texture). Préférer les tomates SEMI-séchées (mi-confites, moelleuses, type 'sun-blushed'/'sun-kissed').

On peut les faire soi-même et les conserver dans l'huile d'olive, ou acheter les versions commerciales moelleuses. Elles apportent concentration et umami sans le côté coriace qui déséquilibre une salade de feuilles.



<!-- ===== 20-planification-menus.md ===== -->

# Planification de repas — Composition & orchestration du timing

Ce fichier comble le plus gros angle mort d'un assistant cuisine domestique : les autres fichiers savent réussir **un plat**, celui-ci sait réussir **un repas**. Deux compétences distinctes :
1. **Composer** un menu cohérent (les plats vont ensemble).
2. **Orchestrer** plusieurs préparations dans le temps (tout est prêt en même temps, chaud quand il faut).

Il ne remplace pas les protocoles de cuisson (voir `cuissons_v1`), le goût (voir `nosrat_v1`) ni les associations d'ingrédients (voir `associations_v1`). Il s'appuie dessus.

---

## 1. Composer un repas équilibré (le contraste)

Un bon repas n'aligne pas des plats « bons » côte à côte : il les fait **contraster**. La monotonie est l'ennemi numéro un (tout fondant, tout chaud, tout riche = repas plat même si chaque plat est réussi).

### Les 5 axes de contraste à varier entre les plats
Faire varier au moins **3 des 5 axes** d'un plat à l'autre :

- **Texture** — croquant / fondant / crémeux / moelleux. Éviter deux plats mous d'affilée. Un repas tout-mou réclame un élément croquant (croûtons, noix torréfiées, crudité, tuile).
- **Température** — chaud / tiède / froid. Une entrée froide ou tiède soulage la cuisine quand le plat principal monopolise le four/les feux.
- **Richesse** — gras / frais. Si un plat est riche (crème, fromage, friture, viande grasse), encadrer avec du frais et de l'acide (salade vinaigrée, agrumes, légume vapeur).
- **Couleur** — éviter l'assiette monochrome (tout beige/brun). Ajouter du vert, du rouge, du jaune. Repère visuel rapide : si la table est uniformément beige, il manque une couleur.
- **Intensité (goût)** — puissant / doux. Alterner un plat marqué (épicé, fumé, très assaisonné) avec un plat plus neutre qui sert de respiration.

### Les deux règles de non-répétition
- **Pas le même ingrédient principal** dans deux plats (pas pomme de terre en entrée puis en accompagnement, pas tomate partout).
- **Pas la même technique** dans deux plats : pas deux gratins, pas deux fritures, pas tout-vapeur, pas deux plats en sauce. La répétition de technique surcharge aussi la cuisine (un seul four, un seul bain de friture).

### Équilibre global du repas (lien Nosrat)
- Si le **plat principal est riche** → entrée OU dessert **acidulé / frais** (agrumes, sorbet, salade vive, fruits). Le repas se rééquilibre dans la durée, pas seulement dans l'assiette.
- Si le plat principal est **léger / maigre** → on peut se permettre un dessert plus gourmand.
- Toujours au moins **un point d'acidité** dans le repas (vinaigrette, agrume, pickle, vin, cornichon) : l'acide « réveille » l'ensemble.

---

## 2. Règle d'or de la charge de travail : 1 plat « travail » + le reste simple

C'est la règle qui évite le naufrage du cuisinier seul.

- **Un seul plat exigeant** par repas (celui qui demande surveillance, minutage serré, technique, cuisson à la minute). Les autres composantes doivent être **simples ou faites à l'avance**.
- Ne **jamais chronométrer trois préparations exigeantes simultanément**. Trois cuissons « à la minute » en parallèle = échec assuré pour une personne seule.
- Autour du plat-vedette, choisir des accompagnements « tranquilles » :
  - prêts à l'avance (taboulé, salade composée, légumes rôtis, terrine, soupe) ;
  - sans surveillance (four lent, légumes vapeur, riz/féculent qui se garde) ;
  - assemblage simple (crudités, fromage, pain, fruits).
- Repère de difficulté par plat : compter le **nombre de minutes de surveillance active**. La somme des surveillances actives simultanées doit rester gérable (≈ ce qu'une personne peut tenir en regardant une seule chose à la fois).

---

## 3. Orchestration du timing (rétroplanning)

Objectif : **tout prêt à l'heure du service**, chaque plat à la bonne température.

### Méthode du rétroplanning (compte à rebours)
1. Fixer **H = heure de service** (l'heure où on passe à table).
2. Pour chaque plat, noter sa **durée totale** = préparation + cuisson + **repos éventuel**.
3. Placer chaque plat sur l'axe du temps **en partant de H et en remontant**. Heure de départ d'un plat = H − durée totale.
4. Le plat le plus long donne **l'heure de démarrage** du repas entier.
5. Repérer les **conflits de ressources** (même four, même feu, même plan de travail au même moment) et décaler/anticiper.

### Le piège du repos (ne pas l'oublier dans le calcul)
- Les **viandes/volailles épaisses** doivent reposer : prévoir ce temps AVANT le service, pas après.
  - Repère : repos ≈ égal au temps de cuisson, **minimum 15-30 min** selon la pièce (voir `cuissons_v1`).
- Une viande qui repose **libère le four** pour réchauffer/finir un accompagnement ou faire la sauce. Le repos n'est pas du temps mort : c'est une fenêtre d'orchestration.
- **Pâtes / riz / légumes verts vifs** = exactement l'inverse : **aucun report**, à servir immédiatement → ce sont les **dernières** choses qu'on lance.

### Ordre de lancement type (du plus tôt au plus tard)
1. Ce qui se garde / se mange froid ou tiède : entrées froides, desserts, sauces froides, vinaigrettes, marinades — **fait à l'avance**.
2. Cuissons longues sans surveillance : braisés, rôtis, plats au four lent, soupes, légumes rôtis.
3. Plat-vedette à cuisson moyenne + son **repos**.
4. Accompagnements qui patientent un peu : purées, gratins (se réchauffent), légumes vapeur.
5. **En tout dernier, juste avant de servir** : pâtes, riz, légumes verts, fritures, œufs, poisson minute, dressage, sauces chaudes émulsionnées.

### Préparer à l'avance (« mise en place »)
- Faire **tout le découpage, pesée, épluchage AVANT** d'allumer le moindre feu. La mise en place transforme une cuisson stressante en simple assemblage.
- Travaux délégables à l'avance (la veille ou quelques heures avant) : marinades, fonds/bouillons, sauces froides, vinaigrettes, légumes lavés/coupés, pâte à tarte, desserts, dressage des entrées froides.
- Garder pour la **dernière ligne droite** uniquement ce qui ne supporte pas l'attente.

---

## 4. Gérer les ressources limitées (cuisine domestique réelle)

La contrainte n'est pas la recette, c'est l'**équipement disponible**.

- **Un seul four** : ne pas planifier deux plats à températures différentes en même temps. Solutions : cuire en série (le plat qui se réchauffe ou se garde au chaud d'abord), choisir une température de compromis, ou basculer un plat sur les feux/plaque.
- **Nombre de feux limité (souvent 3-4)** : compter combien de casseroles/poêles tournent **en même temps**. Si ça déborde, anticiper une préparation (cuire le féculent un peu avant et le garder), ou supprimer une cuisson minute.
- **Maintien au chaud** : four à 70-80 °C (à confirmer selon four), couvercle, papier alu détendu, ou bain-marie. Le maintien doit rester **au-dessus de la zone de danger** : ne pas garder un plat tiède sous ce seuil pendant des heures (voir `securite_alimentaire_v1` pour le seuil de maintien chaud sûr). Attention : les fritures et légumes verts perdent vite leur intérêt au maintien → ne pas compter dessus pour eux.
- **Espace plan de travail / vaisselle** : nettoyer au fur et à mesure (« clean as you go ») pour ne pas se bloquer. Prévoir où poseront les plats finis.
- **Capacité du convive-cuisinier** : si on reçoit, choisir un menu où **on n'est pas coincé aux fourneaux** au moment où les invités arrivent → maximum de plats faits à l'avance, plat-vedette à finition rapide.

---

## 5. Trames de menus prêtes à l'emploi (anti-naufrage)

Modèles qui respectent d'office la règle « 1 plat travail + reste simple » :

- **Repas reçu sans stress** : entrée froide (préparée à l'avance) + un seul plat principal à finition rapide + dessert fait la veille. Le cuisinier n'a qu'**une** chose à surveiller au moment du service.
- **Tout au four** : un plat principal rôti + légumes rôtis sur la même plaque (même température) + salade froide en accompagnement frais. Un seul four, peu de feux, contraste chaud/froid assuré.
- **Plat unique complété** : un plat complet (gratin, plat mijoté, risotto, plat unique) + une salade acidulée pour le contraste + pain + fromage/fruits. Quasi aucune orchestration.
- **Mijoté du week-end** : braisé/ragoût fait la veille (meilleur réchauffé), réchauffé doucement le jour J ; on ne fait à la minute que le féculent d'accompagnement.

### Check-list rapide avant de valider un menu
- [ ] Au moins 3 axes de contraste varient entre les plats ?
- [ ] Aucun ingrédient principal répété ? Aucune technique répétée ?
- [ ] Un seul vrai plat « travail » ? Le reste simple/à l'avance ?
- [ ] Le repos des viandes est-il dans le rétroplanning ?
- [ ] Les conflits de four/feux sont-ils résolus ?
- [ ] Au moins un point d'acidité / de fraîcheur dans le repas ?
- [ ] Une couleur autre que beige dans l'assiette ?

---

## Méta / sources

- **Périmètre** : cuisine domestique, planification et orchestration d'un repas (non couvert par les autres fichiers du Gem, qui traitent l'exécution d'un seul plat).
- **Sources d'appui internes** : `gemini_cuisine_nosrat_v1` (équilibre sel/acide/gras/chaleur, contraste de goûts), `gemini_cuisine_cuissons_v1` (durées, repos des viandes, maintien), `gemini_cuisine_associations_v1` (cohérence des ingrédients entre plats).
- **Principe directeur** (Nosrat, *Salt Fat Acid Heat*) : l'équilibre d'un repas se joue sur la durée et le contraste, pas seulement dans une assiette.
- **À confirmer** : températures de maintien au chaud (70-80 °C) et nombre de feux (3-4) dépendent de l'équipement réel de l'utilisateur — à ajuster selon son inventaire/profil cuisinier.
- **Données chiffrées** : repos viande (≈ temps de cuisson, min. 15-30 min) repris du fichier `cuissons_v1`.
