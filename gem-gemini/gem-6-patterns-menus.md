# Patterns de plats & planification

_Bundle Gem consolidé regroupant : 08-ottolenghi-patterns.md, 20-planification-menus.md_



<!-- ===== 08-ottolenghi-patterns.md ===== -->

# Ottolenghi SIMPLE — patterns culinaires V2

> Source : *SIMPLE* — Yotam Ottolenghi (2018). Patterns extraits, **aucune recette copiée**.
> Usage : base d'inspiration pour agent IA cuisine, pas livre de recettes.
> La logique de goût (sel / gras / acide / sucré / umami / aromatique) de chaque pattern suit les règles de `gem-1-regles-gout` : sel sur la base avant cuisson, acide et zeste en finition hors feu, gras porteur d'arômes, caramélisation = sucré + umami.

## Principes d'utilisation

**24 architectures de plats** (+ patterns cuisines du monde et compléments plus bas) : la grammaire culinaire distillée en formules réutilisables. Sert à inspirer un plat à partir d'ingrédients disponibles, adapter une recette, enrichir un plat simple. Ne remplace pas les règles de cuisson (gem-5), la science (gem-2) ni le goût (gem-1).

Chaque pattern : **formule réutilisable** → **variantes** (substituer sans perdre l'esprit) → **points critiques** (ce qui sépare réussi de raté) → **usage Gemini** (quand activer/éviter).

Familles : plats légumes/grains (1-9), plats protéines (10-16), formats légers (17-18), patterns outils (19-22), desserts (23-24).

---

## Pattern 001 — Légume rôti + sauce yaourt aromatisée + croquant + herbes

**Intention** : transformer un légume brut en pièce maîtresse : intensité par le four, fraîcheur par la sauce froide, contraste par le topping.

```text
légume dense rôti (monocouche, four 220°C+) + yaourt grec aromatisé (épice + zeste + ail pressé) + oignon caramélisé OU grenade + herbes fraîches abondantes + noix/graines grillées
```

### Variantes
- bases : aubergine, chou-fleur, courge butternut, patate douce, panais, carotte, betterave
- sauces : yaourt + sumac / cari / zaatar / harissa, labneh nature
- toppings : amandes effilées, pignons, pistaches, graines de courge, sésame, dukkah
- herbes/épices : coriandre, menthe, persil, aneth ; cumin, cardamome, ras-el-hanout
- protéines compatibles : agneau grillé, poulet rôti, féta, pois chiches grillés, halloumi
- simple : 1 légume + yaourt-zeste-sel + huile + persil | festive : 2-3 légumes + 2 toppings + grenade + herbes triples

### Points critiques
- bien sécher le légume avant huile + sel ; monocouche stricte (plaque surchargée → vapeur, pas de coloration)
- four vraiment chaud (220°C+) ; viser des bords franchement bruns, tendreté à la pointe du couteau
- ne pas saler le yaourt trop tôt (rend de l'eau) ; herbes au tout dernier moment (ramollissent sinon)
- servir avec contraste chaud/froid : légume chaud déposé dans un creux de yaourt froid

### Usage Gemini
- proposer quand : "j'ai un légume dense + du yaourt", "rendre des légumes rôtis intéressants", "idée style Ottolenghi"
- éviter quand : légume très aqueux, repas express < 25 min, intolérance lactose (→ basculer tahini, Pattern 003)
- adaptation rapide : version monoplaque tout cuit ensemble ; végan → tahini éclairci

---

## Pattern 002 — Tomates rôties chaudes sur base laitière froide

**Intention** : choc thermique + acide vivant + base apaisante : la tomate bouillonnante rencontre le yaourt froid, qui fond partiellement à son contact.

```text
yaourt épais froid en lit (creux au dos de cuillère) + tomates cerises (ou fruit/légume juteux) rôties four chaud avec ail-herbes-zeste + TOUTE l'huile et le jus de la plaque + herbes + piment doux (Urfa, Alep)
```

### Variantes
- bases : yaourt grec, labneh, ricotta battue, fromage frais, mascarpone détendu
- éléments rôtis : tomates cerises, prunes, raisins, figues, poivrons, oignons, abricots
- aromates plaque : ail tranché, thym, origan, zeste citron, graines de cumin ; pincée cassonade si tomates fades
- protéines compatibles : poulet rôti à part, pois chiches grillés, agneau
- simple : tomates cerises + ail + huile + yaourt + origan | festive : 3 fruits rôtis + labneh maison + double huile aromatique + pain plat chaud

### Points critiques
- yaourt vraiment froid, tomates posées brûlantes directement du four — ne pas mélanger (le contraste EST le plat)
- récupérer toute l'huile et le jus de la plaque : c'est la sauce ; plaque pas trop grande (jus évaporé sinon)
- tomates rôties jusqu'à éclater et noircir par endroits (concentration)

### Usage Gemini
- proposer quand : "tomates cerises et yaourt", "entrée d'été simple qui en jette", "végé impressionnant"
- éviter quand : pas de four, tomates hors saison, repas entièrement froid
- adaptation rapide : sous le gril 6-8 min en surveillant

---

## Pattern 003 — Légume rôti + sauce tahini éclaircie + herbes + grenade/zaatar

**Intention** : version végan/plus profonde du Pattern 001 : le tahini apporte le crémeux + une note grillée-amère en écho à la croûte rôtie.

```text
légume dense rôti brun franc + sauce tahini (tahini + citron + ail pressé + sel → eau en filet APRÈS, en fouettant, consistance crème) + grenade OU citron confit OU oignon caramélisé + herbes + graines/noix grillées
```

### Variantes
- bases : chou-fleur entier, aubergine en quartiers, brocoli, betterave, patate douce
- sauces : tahini classique, tahini-yaourt 50/50, tahini + harissa, tahini + miel (sucré-salé)
- toppings : grenade, oignons frits, pignons, amandes, sumac, zaatar
- protéines compatibles : agneau grillé, poulet rôti, pois chiches frits, œuf mollet
- simple : chou-fleur en bouquets + tahini base + persil + sumac | festive : chou-fleur entier + tahini + grenade + herbes triples + pignons frits + citron confit

### Points critiques
- ordre impératif : tahini + citron + ail + sel, mélanger (la sauce se solidifie, c'est normal), PUIS eau en filet
- consistance cible : ruban qui coule lentement de la cuillère ; goûter → presque toujours +sel +acide
- tahini de qualité (coulant, goût propre — rance = tout est ruiné) ; ne jamais chauffer la sauce (amère)

### Usage Gemini
- proposer quand : "du tahini, quoi en faire", "version végan d'un légume rôti", "plat partageable type mezze"
- éviter quand : allergie sésame, repas express
- adaptation rapide : sauce en 2 min, légume rôti en 25 min sur une plaque

---

## Pattern 004 — Soupe légume crémée + topping aromatique chaud final

**Intention** : une soupe qui n'est pas qu'une soupe : base mixée + topping qui craque ou aromatise au moment du service.

```text
oignon revenu + épices grillées dans l'huile + légume + bouillon, mijoté → (soupes vertes : herbes/feuilles ajoutées HORS feu) → mixage → crème/lait de coco/yaourt hors feu → topping croquant distinct À L'ASSIETTE + zeste agrume + herbes fraîches
```

### Variantes
- bases : courge, citrouille, courgette, chou-fleur, lentille corail/verte, panais, betterave, petits pois
- liquide crémeux : crème fraîche, lait de coco, yaourt grec, crème de cajou
- toppings : graines de courge sucrées-épicées, croûtons huile-ail, oignons frits, dukkah, herbes frites, pancetta, œuf poché
- épices : safran, harissa, cari, cumin, gingembre, cardamome
- simple : 1 légume + bouillon + crème + huile + zeste + herbe | festive : double légume + 2 toppings + harissa maison + 3 herbes

### Points critiques
- griller les épices avant le liquide ; saler et regoûter APRÈS mixage
- crème hors du feu ou à frémissement, jamais à ébullition (tranche)
- couleur verte vive : retirer du feu DÈS l'ajout des verts, mixer immédiatement (trop cuit → terne)
- topping préparé pendant la cuisson, jamais intégré au mix (perd l'effet)

### Usage Gemini
- proposer quand : "soupe qui change", "un légume qui tourne", "entrée chaude avant repas léger"
- éviter quand : pas de mixeur, repas "ça tient" recherché (sauf coco-lentille)
- adaptation rapide : oignon + légume surgelé + bouillon + lait de coco + cari = 25 min

---

## Pattern 005 — Soupe froide légume aqueux + yaourt + herbes

**Intention** : soupe d'été qu'on boit autant qu'on mange : fraîcheur, acide net, base laitière apaisante, garniture qui ajoute du relief.

```text
légume aqueux cru ou peu cuit + yaourt/labneh + acide (vinaigre/citron) + huile + sel → mixé à froid → repos frigo 1 h min → garniture SOLIDE en assiette (brunoise, croûtons, féta) + herbes + zeste + huile en filet
```

### Variantes
- bases : concombre, tomate mûre, melon d'eau + tomate, courgette blanchie, avocat, poivron rôti pelé, betterave crue
- laitiers : yaourt grec, labneh dilué, ayran, kéfir, lait ribot, crème de cajou (végan)
- garnitures : brunoise du même légume, croûtons huile-ail, féta, œuf dur, jambon, crevettes, raisins
- herbes/épices : aneth, menthe, basilic, coriandre ; sumac, cumin, piment d'Alep
- simple : concombre + yaourt + ail + citron + menthe + brunoise | festive : 3 légumes + labneh + huile aromatique + 3 garnitures + 4 herbes

### Points critiques
- légume très mûr/qualitatif (le cru ne masque rien) ; soupe VRAIMENT froide
- ré-ajuster acide-sel à la sortie du frigo (le froid masque le sel)
- garniture servie à part, ajoutée minute (ramollit sinon) ; herbes jamais mixées (couleur terne)
- huile fruitée en filet final, jamais mixée

### Usage Gemini
- proposer quand : "soupe froide d'été", "concombres et yaourt", "entrée fraîche temps chaud"
- éviter quand : hors saison, légumes pas mûrs, dîner d'hiver
- adaptation rapide : mixeur + 5 min ; le repos frigo se fait pendant la suite

---

## Pattern 006 — Salade composée crue + herbes en abondance + acide vif + croquant

**Intention** : salade qui tient debout comme plat : herbes traitées comme un légume, pas comme un décor.

```text
2-3 crus complémentaires en dés réguliers + échalote macérée dans l'acide + vinaigrette (tahini/yaourt OU citron-huile) + herbes multiples en quantité de salade + finition croquante (graines, noix, pita rôti)
```

### Variantes
- bases : tomate-concombre-poivron, melon-pomme verte, pêche-radicchio, fenouil-orange, betterave-pomme, carotte râpée-orange
- vinaigrettes : citron-huile, tahini-citron-eau, yaourt-gingembre-citron, Xérès-huile, lime-citronnelle
- toppings : pignons, amandes, sésame, dukkah, zaatar, croûtons de pita, nigelle
- herbes : 3-4 obligatoires (menthe, coriandre, persil, aneth, basilic, estragon)
- protéines compatibles : féta, halloumi grillé, poulet effiloché, crevettes, œuf mollet
- simple : tomate + concombre + 3 herbes + citron + huile | festive : 3 crus + 4 herbes + tahini-zaatar + féta + pignons + grenade

### Points critiques
- macérer l'échalote dans l'acide AVANT d'assembler (sinon agressive)
- sel au tout dernier moment (les légumes rendent l'eau) ; sauce versée tard (ramollit)
- dés réguliers pour la même bouchée ; les herbes pèsent presque autant qu'un légume — 1 seule herbe = le pattern s'effondre

### Usage Gemini
- proposer quand : "salade fraîche mais pas plate", "herbes qui traînent", "entrée d'été qui en impose"
- éviter quand : herbes manquantes, repas très consistant en suite
- adaptation rapide : 1 cru + 1 acide + 1 herbe + 1 graine = 5 min ; le pattern est cumulatif

---

## Pattern 007 — Mijoté légumineuse + tomate + épices Moyen-Orient + yaourt en finition

**Intention** : plat principal végétarien réconfortant, peu cher, meilleur le lendemain ; cuillerée de yaourt froid qui apaise.

```text
légumineuse fondante + oignons VRAIMENT caramélisés (8-12 min min) + ail + épices grillées dans l'huile + tomate longuement mijotée → cuillerée de yaourt grec froid au service + coriandre + huile + citron en toute fin
```

### Variantes
- bases : pois chiches, haricots blancs/cocos/d'Espagne, lentilles vertes/du Puy/corail
- épices dominantes : cumin + coriandre, paprika fort + carvi, ras-el-hanout, baharat, harissa rose
- légumes ajoutés : aubergine rôtie, bette à carde, épinards, courgettes, carottes
- protéines compatibles : tofu doré, agneau haché, merguez
- simple : pois chiches en boîte + tomate + cumin + ail + yaourt + coriandre | festive : double légumineuse + aubergine rôtie + harissa maison + herbes triples + pignons

### Points critiques
- yaourt AJOUTÉ en finition, jamais cuit (tranche) ; citron en toute fin pour relever
- épices grillées dans l'huile avant le liquide (sinon pas réveillées) ; lentilles : ne pas saler trop tôt
- sauce qui nappe les légumineuses (pas qui flotte) ; le plat est meilleur le lendemain — prévoir

### Usage Gemini
- proposer quand : "plat végé qui tient au corps", "dîner de semaine à préparer la veille", "pois chiches en boîte"
- éviter quand : besoin de léger, aversion cumin/coriandre
- adaptation rapide : tout en boîte, 25 min, sans rôtissage

---

## Pattern 008 — Grain pilaf + caramélisation + fruit sec + noix + zeste agrume

**Intention** : faire d'un grain neutre un plat principal aromatique : caramélisation comme socle, fruit sec comme pont sucré-salé, noix comme texture.

```text
grain gonflé et aéré + oignon longuement caramélisé (doré franc, pas blond) + fruit sec + noix grillées + zeste agrume au dernier moment + herbes fraîches abondantes
```

### Variantes
- bases : couscous, boulgour, riz basmati/brun, freekeh, perles de couscous, orzo
- caramélisation : oignon jaune/rouge, échalote, poireau confit
- fruits secs : raisin, abricot sec, datte, cerise séchée, grenade fraîche
- noix : amandes effilées, pignons, pistaches, noix de pécan, noisettes
- épices/herbes : ras-el-hanout, baharat, cinq-épices, cumin ; menthe, coriandre, persil, aneth
- protéines compatibles : agneau, poulet, halloumi, féta, pois chiches frits
- simple : couscous + oignon caramélisé + raisins + amandes + persil + zeste | festive : freekeh + abricot sec + pistaches + grenade + 3 herbes + ras-el-hanout

### Points critiques
- oignon doré franc (pas assez cuit → goût cru) ; noix grillées jusqu'au parfum (sinon texture sans goût)
- zeste au dernier moment, jamais cuit (perd ses huiles) ; grain aéré à la fourchette, jamais compact
- assaisonner le grain AVANT herbes/zeste ; viser 3 couleurs visibles (grain pâle, oignon foncé, herbes vertes)

### Usage Gemini
- proposer quand : "accompagnement qui n'en est pas un", "plat unique végé", "restes de viande à étirer"
- éviter quand : régime bas glucides, aversion fruits secs dans le salé
- adaptation rapide : couscous 5 min + oignons faits d'avance = 15 min

---

## Pattern 009 — Pâtes + huile aromatique infusée + agrume + croquant + herbes

**Intention** : pâtes minimalistes mais intenses : l'huile a fait le travail aromatique avant ; émulsion concentrée, pas sauce volumineuse.

```text
pâtes al dente + huile infusée feu doux (anchois/ail/piment — fondre, ne pas brûler) + élément vert + grosse louche d'eau de cuisson pour l'émulsion + zeste citron hors feu + noix concassées + herbes + parmesan/pecorino
```

### Variantes
- huiles infusées : anchois-ail-piment, ail-piment, sauge-beurre noisette, câpres-citron-ail, basilic-pistache (purée crue)
- éléments verts : pois mange-tout, salicorne, fanes, roquette, brocoli haché, basilic en purée
- noix : pistaches, pignons, noix, noisettes, amandes ; ou chapelure dorée
- protéines compatibles : ricotta, burrata, œuf cru sur pâtes chaudes, sardines, thon mi-cuit
- simple : spaghetti + ail-anchois-piment + persil + parmesan | festive : trofie + purée basilic-anchois-pistache + pois mange-tout + zeste + pecorino + pignons

### Points critiques
- ail/anchois à feu doux (brûlé = amer) ; réserver l'eau de cuisson AVANT d'égoutter
- finir les pâtes 1-2 min dans la sauce avec un peu d'eau ; zeste après le feu
- cible : sauce qui adhère en ruban, huile colorée par les aromates

### Usage Gemini
- proposer quand : "pâtes vite mais pas fades", "anchois et citron", "pasta qui change de la tomate"
- éviter quand : aversion anchois → remplacer par câpres ou olives, le pattern reste valide
- adaptation rapide : 15-20 min ; l'huile s'infuse pendant que les pâtes cuisent

---

## Pattern 010 — Protéine simple saisie + salsa fraîche acidulée

**Intention** : protéine neutre, propre, parfaitement cuite ; la salsa définit le plat et change la culture culinaire.

```text
protéine tendre séchée en surface, salée juste avant, saisie franche (repos 3-5 min) + salsa à CÔTÉ (herbes hachées + noix grillées du jour + acide dominant + huile + zeste, repos 10-15 min)
```

### Variantes
- bases : agneau (filet, côtelettes), bœuf, poulet, poisson blanc, saumon, truite, crevettes, calmars — interchangeables, la salsa est la signature
- salsas : pistache-cardamome, amandes-fleur d'oranger, pignons-mélasse de grenade, basilic-anchois, olives-grenade, menthe-noisettes
- épices : cardamome, cumin, sumac, piment fumé, fleur d'oranger
- simple : poulet saisi + salsa persil-citron-pignons | festive : filet d'agneau mariné + salsa amandes-fleur d'oranger-menthe + grenade

### Points critiques
- protéine sèche en surface (sinon ne saisit pas) ; repos après cuisson obligatoire
- salsa préparée avant la cuisson, jamais la veille (herbes flétries) ; noix grillées le jour même
- salsa déposée À CÔTÉ, pas sur la viande chaude (ramollit) ; contraste chaud/frais

### Usage Gemini
- proposer quand : "une belle protéine", "simple mais impressionnant", "recevoir sans stress"
- éviter quand : pas d'herbes fraîches, pas de noix
- adaptation rapide : la même salsa fonctionne sur 4-5 protéines — préparer une fois, varier la base

---

## Pattern 011 — Salade-repas grain ou pâtes + protéine + acide + croquant

**Intention** : salade qui constitue le plat entier : féculent + protéine + crus + sauce — l'architecture du "bowl".

```text
grain/pâtes assaisonné(e)s CHAUD(E)S puis tiédi(e)s (1/3) + protéine (1/3) + crus + herbes (1/3) + sauce dense montée à part à la dernière minute + croquant + sel en flocons
```

### Variantes
- bases : couscous, boulgour, freekeh, riz refroidi, lentilles, pâtes courtes (orzo, ditali)
- protéines : œuf dur, poulet poché/saisi, bifteck saignant, crevettes, féta, halloumi, thon en boîte, pois chiches grillés
- crus : tomates cerises, concombre, oignon rouge, radis, fenouil
- sauces : yaourt-mayo-cari, tahini-citron, vinaigrette anchois, fines herbes, mayo-citron-câpres
- croquants : amandes, pistaches, pignons, croûtons de pita, dukkah
- simple : couscous + thon + tomate + concombre + citron-huile + persil | festive : freekeh + agneau saignant + roquette + tahini-citron + pignons + grenade + 3 herbes

### Points critiques
- assaisonner le grain CHAUD (absorbe mieux), servir tiède/ambiant, pas froid frigo
- 4-5 composants visibles en couches, pas un mélange unique (bouillie sans relief sinon)
- sauce dense (trop liquide → noie) ; manque de croquant = texture monocorde

### Usage Gemini
- proposer quand : "déjeuner du lendemain", "lunch box qui tient", "dîner d'été léger mais rassasiant"
- éviter quand : besoin de chaud réconfortant, repas formel
- adaptation rapide : grain pré-cuit + protéine de la veille + crus + vinaigrette = 10 min d'assemblage

---

## Pattern 012 — Boulettes de viande aux épices + sauce yaourt/tahini + topping

**Intention** : boulettes hors de l'ordinaire : herbes et fromage DANS la viande, glaçage final acide, sauce crémeuse à part.

```text
viande hachée (agneau idéal) + liant (mie trempée, œuf) + épices + herbes + féta en option → peu pétri → saisie poêle + finition four → glaçage acide-sucré EN FIN (mélasse de grenade, harissa-miel) + sauce yaourt/tahini à côté + topping croquant + herbes
```

### Variantes
- bases : agneau, bœuf, mélanges, dinde-poulet (léger), version végé pois chiches/champignons
- fromages intégrés : féta, halloumi en dés, ricotta
- glaçages : mélasse de grenade, miel-cumin, tamarin, harissa-miel, balsamique réduit
- sauces : yaourt-citron-ail, tahini, tzatziki, harissa-yaourt
- toppings : pignons grillés, oignons frits, dukkah, sumac, menthe
- simple : boulettes agneau-féta-cumin + yaourt-citron + persil | festive : glaçage mélasse de grenade + tahini + pignons + sumac + 3 herbes

### Points critiques
- ne pas trop pétrir (boulettes dures) ; saisie vive puis four (tout poêle = brûlé dehors/cru dedans)
- glaçage en FIN de cuisson (brûle sinon) ; sauce jamais cuite, jamais versée chaude sur les boulettes
- cible : boulettes brun-acajou, glaçage qui brille, sauce blanche en contraste ; repos 3 min

### Usage Gemini
- proposer quand : "du haché et envie d'autre chose qu'une bolognaise", "recevoir avec viande facile", "pita-meal"
- éviter quand : végétarien strict (sauf adaptation), aversion cumin
- adaptation rapide : mélange la veille, cuisson 15 min, sauces d'avance

---
## Pattern 013 — Croquettes / galettes (protéine ou légume vert) + base liée + sauce crémeuse acidulée

**Intention** : confort food revisitée : croustillant dehors, fondant dedans, sauce acide qui empêche la lourdeur. Couvre aussi les beignets/galettes de légumes verts.

```text
base hachée (poisson, poulet, crevettes OU petits pois/courgettes/épinards PRESSÉS) + liant (purée de légume, œuf + chapelure, ou féta) + panure aux graines en option → frigo 15-30 min → poêle huile bien chaude + finition four → sauce yaourt/mayo/tahini acide + élément frais + citron
```

### Variantes
- bases : poisson fumé + panais, poisson blanc + œuf, poulet en lanières, crevettes, petits pois + féta, courgettes râpées + féta, pois chiches (végé), épinards-ricotta
- panures : panko + sésame + tournesol, noix de coco grillée + chili, semoule de maïs, parmesan + chapelure ; ou farine simple
- sauces : yaourt-cumin-lime, mayo-citron-aneth, tahini-citron-ail, harissa-yaourt, yaourt-menthe
- éléments frais : oignon mariné, mangue julienne, salade de chou, herbes
- simple : croquettes poisson + mayo-citron ; ou beignets petits pois-féta + yaourt-menthe | festive : poisson fumé + purée panais + panure graines + tahini-citron + oignons croustillants + 3 herbes

### Points critiques
- mélange ni trop sec ni trop humide ; légumes verts PRESSÉS/égouttés (sinon la galette s'effondre)
- réfrigérer avant cuisson (tenue) ; huile bien chaude (tiède → la croquette boit) ; finition four (centre cuit)
- sauce plus acide que ce qu'on pense (manque d'acide = plat plat)

### Usage Gemini
- proposer quand : "reste de poisson", "petits pois ou courgettes en trop", "brunch familial", "végé qui plaise aux enfants"
- éviter quand : pas de four, peu de matériel
- adaptation rapide : formées la veille, cuisson minute le jour J

---

## Pattern 014 — Œufs + base aromatique + verdure (œufs braisés, frittata, shakshuka)

**Intention** : l'œuf comme support de saveur : la base aromatique fait le plat, l'œuf lie et apaise. Couvre shakshuka rouge/verte, frittata, omelette plate, œufs au plat sur poêlée.

```text
base aromatique prête et CHAUDE (sauce tomate épicée / verts braisés bien réduits / champignons / frittata légumes-fromage) → œufs à température ambiante cuits doucement dedans (jaune coulant = surveillance 2 dernières min) → féta/yaourt + pain croustillant + sel en flocons + piment doux
```

### Variantes
- cuissons : pochés dans sauce (shakshuka rouge/verte), brouillés crémeux, frittata (feu doux puis four/gril), au plat, omelette
- bases rouges : tomate épicée, oignons-poivrons confits, harissa-tomate ; bases vertes : épinards-blette + ail, courgettes-petits pois-herbes
- frittatas : épinards-féta, courgettes-menthe-féta, herbes-parmesan
- laitiers : féta, ricotta, halloumi, yaourt, parmesan ; protéines : merguez, chorizo, saumon fumé
- simple : œufs au plat + champignons à l'ail + pain grillé | festive : shakshuka verte (épinards-courgettes-herbes-féta-zaatar) + pain plat maison

### Points critiques
- œufs à température ambiante (frigo → cuisson inégale) ; base chaude AVANT de casser les œufs
- shakshuka verte : verts tombés et réduits (sinon soupe verte avec œufs flottants)
- sel en flocons en finition, jamais sur le jaune cru (taches blanches) ; jaune trop ferme = raté

### Usage Gemini
- proposer quand : "brunch œufs et légumes verts", "frigo presque vide + boîte de tomates", "souper rapide"
- éviter quand : œufs pas frais, repas froid recherché
- adaptation rapide : 15 min ; un œuf transforme tout reste de légume cuit en plat

---

## Pattern 015 — Mijoté de viande à la cocotte + base tomate-épices + finition acide-herbes

**Intention** : plat de réception qui se prépare à l'avance, gagne en saveur le lendemain, libère le cuisinier au service.

```text
viande peu noble en morceaux (salée la veille si possible, saisie pour la profondeur) + oignons caramélisés 15-20 min + ail + épices grillées + tomate concentrée + liquide → mijotage long à FRÉMISSEMENT couvert puis découvert → finition acide HORS feu (citron, mélasse de grenade, Xérès) + herbes + topping optionnel
```

### Variantes
- bases : agneau (épaule, collier), bœuf (paleron, joue), poulet (cuisses), calmar, joue de porc
- épices : baharat, ras-el-hanout, harissa, paprika fumé + cumin, garam masala, berbéré
- liquides : vin rouge/blanc, bière, bouillon, eau + tomate
- toppings : croûte tahini gratinée, croûte de maïs, polenta, riz ; noix grillées, pain
- simple : cuisses de poulet + oignons + tomate + paprika fumé + 90 min + citron-coriandre | festive : épaule d'agneau + ras-el-hanout + vin rouge + 3 h + croûte tahini + pignons + grenade

### Points critiques
- oignons vraiment caramélisés (sinon goût plat) ; frémissement, jamais ébullition (viande sèche)
- acide TOUJOURS hors feu (cuit → perd son lift) ; sel par paliers
- cible : viande qui se défait à la fourchette, sauce qui nappe la cuillère ; meilleur le lendemain

### Usage Gemini
- proposer quand : "plat à préparer la veille", "recevoir 6+ sans stress", "dimanche d'hiver"
- éviter quand : peu de temps, pas de cocotte, repas léger
- adaptation rapide : version 90 min sur cuisinière ; slow-cooker 6 h

---

## Pattern 016 — Plat unique au four (one-tray bake)

**Intention** : le plat moindre-effort sublimé par les aromates : tout sur une plaque, le four travaille, vaisselle minimale.

```text
légumes denses coupés HOMOGÈNES + protéine assaisonnée (avec marge) + huile + épices + sel → monocouche stricte, protéine au-dessus si elle rend du gras → four chaud → finition fraîche OBLIGATOIRE (yaourt, salsa, oignons macérés, grenade, herbes) + zeste + huile fruitée
```

### Variantes
- protéines : cuisses de poulet, saucisses, pavés de saumon, halloumi, pois chiches en boîte
- légumes : pommes de terre nouvelles, poivrons, oignons, fenouil, courgettes, choux de Bruxelles, panais, patates douces
- épices : ras-el-hanout, harissa, paprika fumé, sumac, cari, mélange shawarma
- toppings : pignons sur la plaque les 5 dernières min, féta à la sortie
- simple : cuisses de poulet + pommes de terre + harissa + citron + persil | festive : agneau + 4 légumes + ras-el-hanout + grenade + tahini + 3 herbes

### Points critiques
- calibrage homogène des légumes (sinon cuisson inégale) ; plaque assez grande (surchargée → vapeur)
- assaisonner avec marge (la saveur se dilue) ; la finition fraîche est ce qui empêche le plat d'être plat
- cible : bords brun-noir, jus qui chante, peau croustillante

### Usage Gemini
- proposer quand : "dîner de semaine sans vaisselle", "une protéine + des légumes"
- éviter quand : besoin d'une cuisson précise par composant
- adaptation rapide : 10 min de prep, 40 min de four, finition 2 min

---

## Pattern 017 — Tartine crémeuse + salsa vive

**Intention** : brunch/apéro simplicité maximum, impact visuel fort : pain bien grillé + base crémeuse + salsa fraîche acide.

```text
pain rustique VRAIMENT grillé (doré franc), frotté à l'ail chaud + élément crémeux étalé (assaisonné lui-même : sel + acide) + salsa vive reposée 10 min (cru-acide-herbes, coupes fines uniformes) + sel en flocons + huile fruitée + zeste — assemblage MINUTE
```

### Variantes
- pains : levain, focaccia, pain plat, bagel toasté — jamais pain de mie/baguette industrielle
- crémeux : avocat citronné, labneh, ricotta-herbes, fromage frais ail-herbes, hummus, chèvre frais, beurre noisette + miso
- salsas : tomates-basilic-balsamique, oignon mariné-grenade, fenouil-orange, pêche-radicchio-menthe, champignons rôtis-thym, pois chiches écrasés-citron
- protéines compatibles : œuf poché/mollet, saumon fumé, anchois, jambon serrano, sardines
- simple : pain ail-huile + avocat + tomates cerises + basilic | festive : focaccia maison + labneh aux herbes + salsa pêche-fenouil-grenade + sumac + 3 herbes

### Points critiques
- pain pas assez grillé → ramollit instantanément ; assemblage minute uniquement
- crémeux non assaisonné = tartine plate malgré la salsa ; salsa trop liquide = tout détrempe
- huile fruitée de finition obligatoire — la signature ; viser le "crac" sonore en bouche

### Usage Gemini
- proposer quand : "pain, avocat, tomates", "brunch facile", "apéro qui n'en est pas un", "lunch simple mais beau"
- éviter quand : pas de bon pain, repas du soir consistant attendu
- adaptation rapide : 8-10 min, modulaire selon le frigo

---

## Pattern 018 — Burrata/féta + élément grillé sucré-acide + herbes

**Intention** : entrée minimaliste à fort impact : fromage frais lacté + élément grillé qui caramélise + herbes qui réveillent.

```text
fromage frais À TEMPÉRATURE AMBIANTE (30 min avant) + fruit/légume grillé bref avec marinade aigre-douce (vinaigre + sucre/miel + épice) servi chaud-tiède + jus rendus + huile fruitée de qualité + herbes + sel en flocons — composer, ne pas mélanger
```

### Variantes
- fromages : burrata, mozzarella di bufala, féta, ricotta, stracciatella, labneh
- grillés : raisins en brochettes, figues, prunes, abricots, tomates cerises, poivrons, asperges, pêches
- marinade : balsamique, Xérès, miel, sucre roux, graines de fenouil, cardamome, romarin
- herbes : basilic, menthe, origan, thym, estragon ; noix optionnelles ; prosciutto/anchois en option
- simple : burrata + tomates cerises grillées + basilic | festive : burrata + raisins et figues grillés + basilic rouge + pignons + balsamique vieux

### Points critiques
- fromage froid frigo = texture caoutchouteuse ; élément grillé refroidi = plat plat
- huile fruitée de qualité : c'est elle qui parfume tout ; sel en flocons juste avant service
- cible : contraste blanc lacté / coloration grillée, fromage qui se casse tendrement

### Usage Gemini
- proposer quand : "entrée pour recevoir, simple mais wow", "fromage de qualité", "fruits de saison"
- éviter quand : pas de fromage frais de qualité, allergie lactose
- adaptation rapide : 10 min, totalement modulaire

---

## Pattern 019 — Sauce yaourt aromatisée [pattern outil]

**Intention** : sauce universelle qui transforme un plat — à combiner avec toute base rôtie, grillée, frite ou crue.

```text
yaourt grec ÉPAIS entier + sel + jus citron/lime + 1 épice grillée à sec puis broyée (sumac, cumin, cari, harissa) + 1 zeste + 1 herbe ciselée + filet d'huile au service — repos 10-30 min
```

### Variantes
- yaourt-sumac-zeste-menthe / yaourt-cumin grillé-citron-coriandre / yaourt-cari-curcuma-lime-menthe / yaourt-citron confit-aneth / yaourt-harissa-coriandre / yaourt-ail-zaatar / yaourt-mayo-cari / yaourt-tahini-citron-ail

### Points critiques
- sel pas trop tôt si attente (rend l'eau) ; ail PRESSÉ, pas haché (texture)
- épices grillées à sec puis broyées (sinon arômes en surface) ; pas assez d'acide = sauce plate
- consistance : nappe la cuillère sans couler vite

### Usage Gemini
- proposer quand : "du yaourt, comment l'utiliser", "sauce rapide pour légume rôti"
- éviter quand : intolérance lactose → tahini (Pattern 020)
- adaptation rapide : 3 min de préparation

---

## Pattern 020 — Sauce tahini éclaircie [pattern outil]

**Intention** : LA sauce signature : une fois maîtrisée, mille variantes, porte presque tout plat de légume.

```text
tahini de qualité + jus citron généreux + ail pressé + sel → mélanger (se solidifie : normal) → eau froide en filet en fouettant → consistance crème/ruban lent — froide ou tiède, JAMAIS chauffée
```

### Variantes
- tahini-citron-ail (base) / + cumin grillé / + harissa / tahini-yaourt 50/50 / + herbes mixées ("sauce verte tahini") / tahini-miso (umami) / tahini-mélasse de grenade (sucré-salé)

### Points critiques
- ordre strict : eau APRÈS le citron (sinon mauvaise émulsion) ; tahini rance = tout est ruiné
- goûter : presque toujours +sel +acide ; chauffer = amère
- se garde 3-4 jours au frigo

### Usage Gemini
- proposer quand : "du tahini, quoi en faire", alternative végan au yaourt, plat moyen-oriental
- éviter quand : tahini sec/rance
- adaptation rapide : 2 minutes

---

## Pattern 021 — Macération aigre-douce d'oignon ou échalote [pattern outil]

**Intention** : enlever l'agressivité de l'oignon cru : tendre, légèrement sucré, note acide dans le plat final.

```text
oignon rouge/échalote tranché TRÈS fin + sel + acide (vinaigre ou citron) + (sucre + épice optionnels) → MASSER avec les doigts → 15-30 min minimum
```

### Variantes
- échalote + sumac + vinaigre blanc / oignon rouge + citron / échalote + citron + sucre (tartare) / oignon rouge + cidre + sucre + graines de moutarde / oignon + lime + piment broyé (mexicain)

### Points critiques
- trancher très fin (épais = reste cru) ; masser physiquement, pas juste remuer
- cible : translucide, un peu mou, couleur rose, ne fait plus pleurer

### Usage Gemini
- proposer quand : salade avec oignon cru, tartare, tacos, garniture vive
- adaptation rapide : geste de 30 secondes, fait à l'avance

---

## Pattern 022 — Huile aromatique infusée [pattern outil]

**Intention** : transformer une huile en condiment puissant : finition de plat, base de vinaigrette, ou élément à part entière.

```text
huile + aromates (ail, piment, gingembre, herbes, zestes, épices entières) à feu DOUX → juste dorés, jamais bruns → retirer les aromates à l'écumoire dès coloration → huile tiède ou refroidie + aromates croquants en garniture
```

### Variantes
- ail-piment-gingembre-tiges de coriandre (asiatique-MO) / anchois-ail-piment (méditerranéenne) / thym-ail-zeste citron (italienne) / cumin-graines / curry-curcuma-feuilles de cari / romarin-ail-piment (pizza)

### Points critiques
- feu doux impératif : l'ail brûle et devient amer en secondes ; aromates oubliés dans l'huile chaude → noircissent
- se garde 3-4 jours au frigo, ramener à température avant usage

### Usage Gemini
- proposer quand : "comment finir un plat", "rendre une tomate/un avocat exceptionnels", "vinaigrette de caractère"
- adaptation rapide : 5 min, garde 3 jours, transforme tout

---

## Pattern 023 — Fruits rôtis + base laitière épaisse + herbe inattendue [dessert]

**Intention** : dessert qui ne tombe pas dans le sucre : fruit rôti qui révèle son acide, base laitière apaisante, herbe/épice salée qui surprend.

```text
fruit de saison + sucre brun modéré + acide (citron/vinaigre/vin) + herbe/épice discrète (laurier, thym, sumac, cardamome) → rôti COURT (garde sa forme) → jus filtré réservé = sirop → base laitière froide + herbes fraîches + croquant en option
```

### Variantes
- accords : fraises-sumac, prunes-laurier, figues-thym, pêches-cardamome, raisins-romarin, abricots-lavande, cerises-balsamique
- laitiers : yaourt grec égoutté, mascarpone, crème fraîche, ricotta sucrée, glace vanille
- toppings : crumble d'amandes, granola, sablés émiettés, meringue
- simple : fraises + sucre + citron + thym + yaourt + miel | festive : 3 fruits rôtis + mascarpone + sablés + 3 herbes + sirop réservé

### Points critiques
- fruit pas trop cuit (forme gardée, pas purée) ; jus récupéré = le sirop final, ne pas le jeter
- herbe discrète, jamais dominante ; sucrer modérément (le but n'est pas une confiture)
- base laitière vraiment froide si fruit chaud

### Usage Gemini
- proposer quand : "dessert simple qui sort du lot", "fruits de saison", "sans pâtisserie compliquée"
- éviter quand : pas de four, fruits hors saison
- adaptation rapide : 15 min de four, dressage minute

---

## Pattern 024 — Gâteau moelleux amande-citron + fruit en garniture

**Intention** : gâteau accessible mais sophistiqué : moelleux par la poudre d'amandes, parfum par le zeste, fruit qui éclate, glaçage citronné.

```text
pâte poudre d'amandes fine + farine + beurre + sucre + œufs + zeste (peu battue après la farine) + fruit acidulé dont une partie ajoutée EN COURS de cuisson + four moyen → glaçage sucre glace-citron sur gâteau REFROIDI + zeste en surface
```

### Variantes
- bases : amande pure (friand), amande + farine, farine de riz (sans gluten)
- agrumes : citron, lime, orange sanguine, bergamote ; fruits : bleuets, framboises, prunes, mûres, cerises, abricots
- aromates : vanille, fleur d'oranger, cardamome, thym ; toppings : amandes effilées, sucre demerara
- simple : amande-citron + bleuets + glaçage | festive : amande-fleur d'oranger + 3 fruits + amandes effilées + 2 glaçages

### Points critiques
- amandes finement moulues (grossières = sableux) ; pâte peu battue (caoutchouteuse sinon)
- fruits lourds ajoutés en cours de cuisson (coulent au fond sinon) ; glaçage sur gâteau froid (fond sinon)
- cible : doré franc, cure-dent propre mais gâteau légèrement humide ; meilleur le 2e jour, 3 jours en boîte

### Usage Gemini
- proposer quand : "gâteau de week-end facile", "fruits de saison", "dessert qui voyage bien"
- éviter quand : allergie aux noix
- adaptation rapide : pâte 10 min, cuisson 40-45 min

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
