# Nosrat V1 — Équilibre du goût

> Source : *Salt, Fat, Acid, Heat* — Samin Nosrat (2017)
> Format : règles de décision exploitables par un agent IA
> Version : v1.0 — 2026-04

---

## Rôle

Module de **diagnostic et correction du goût** pour un agent culinaire.
Permet à l'agent de :

- détecter un déséquilibre dans un plat (fade / lourd / acide / brûlé / fade-mou)
- proposer la correction la plus probable en 1 à 2 phrases
- choisir l'ingrédient ou le geste correctif (sel, gras, acide, chaleur)
- raisonner sur le bon moment d'application (en cours / fin de cuisson)

Ce module ne remplace ni la recette ni la technique — il sert à **arbitrer le goût** une fois la base posée.

---

## Règles fondamentales

### Sel (priorité absolue)

1. Plat fade → suspect n°1 : manque de sel. Saler progressivement, regoûter.
2. Salage de l'intérieur : saler tôt, à chaque étape, pas seulement à la fin.
3. Viande : saler la veille si possible, sinon le matin pour le soir.
4. Plus une pièce est grosse ou dense, plus tôt on sale (1 à 3 jours pour grosses pièces).
5. Poisson délicat : saler 15 min avant cuisson, pas plus.
6. Légumes aqueux (courgette, aubergine, tomate) : saler 15 min avant, sécher avant cuisson.
7. Champignons : saler seulement quand ils ont commencé à dorer.
8. Eau de cuisson (pâtes, légumes, légumineuses) : saler généreusement, "salé comme la mer".
9. Le temps de diffusion compte plus que la quantité.

#### Idées reçues & techniques de salage par contexte

- **Le sel ne durcit PAS les légumineuses (idée reçue).** Saler les haricots secs ne les durcit pas : au contraire, le sel affaiblit la pectine des parois et les ramollit (comme pour les légumes). Donc saler les légumineuses dès le trempage ou dès le début de la cuisson. La vraie cause des haricots durs = sous-cuisson (continuer à mijoter doucement) ; autres causes : haricots vieux/mal stockés, eau calcaire, milieu acide. Cas particulier riz/grains où TOUTE l'eau (et tout le sel) est absorbée : saler plus prudemment pour ne pas sursaler.
- **Le manque de sel à cœur ne se rattrape pas en surface.** Saupoudrer du sel en surface d'un plat déjà cuit ne compense pas un manque de sel à cœur. Pâtes cuites dans une eau fade : aucune sauce/fromage salé ne rattrapera, la langue sait que l'eau n'était pas assez salée. Rôtis, viandes braisées, lasagnes : l'assaisonnement insuffisant à cœur ne se rattrape pas en surface. Conséquence : bien saler l'eau de cuisson et saler les viandes AVANT/PENDANT. Si une viande braisée fade est déjà cuite : l'émietter, la resaler et la transformer (ragù).
- **Saler dans le gras : le sel a besoin d'eau pour se dissoudre.** Le sel ne fond pas dans le gras pur. Dans une vinaigrette, une mayo ou du beurre, c'est l'eau présente (vinaigre, jus de citron, eau du beurre) qui dissout lentement le sel : saler tôt, attendre et goûter avant d'en rajouter. Astuce express pour les préparations grasses/épaisses (mayonnaise, sauce à base d'œuf) : dissoudre d'abord le sel dans un peu d'eau ou dans l'acide prévu (vinaigre, citron), PUIS l'incorporer → distribution immédiate et homogène, pas de cristaux qui faussent la dégustation. Sur une pièce grasse (échine, côte de bœuf) : le maigre absorbe le sel, pas le gras → goûter maigre ET gras ensemble avant de resaler.
- **Saler les œufs avant cuisson.** Les œufs absorbent bien le sel, ce qui aide les protéines à coaguler plus bas et plus vite → moins d'eau expulsée → texture plus moelleuse. Brouillés, omelette, flan/custard, frittata : une pincée de sel AVANT cuisson. Œufs pochés : saler légèrement l'eau. Œufs en coquille ou au plat : saler juste avant de servir. (Sécurité : cuire les œufs jusqu'à prise ; pour publics fragiles, pas d'œuf cru ni coulant.)
- **Saler en couches (layering salt).** Beaucoup d'ingrédients apportent du sel : câpres, anchois, lard, miso, parmesan, sauce soja, Worcestershire, olives. Avant de cuisiner, recenser TOUTES les sources de sel prévues pour ne pas sursaler. Méthode : ajouter d'abord les ingrédients salants (et acides), goûter, et n'ajouter des cristaux de sel qu'en TOUT dernier, une fois le reste équilibré. Si un plat manque de sel, se demander d'où ce sel devrait venir (parmesan ? anchois ? soja ?) avant d'ajouter des cristaux.

#### Repères chiffrés de salage (points de départ, à ajuster au goût)

Quand on ne peut pas goûter (pâte crue, grosse pièce, saumure) :

- Assaisonnement général d'un plat/farce : viser **~1 % de sel** par rapport au poids total (1 g de sel / 100 g) ; charcuterie/saucisses ~1,5-2 %.
- Eau de cuisson des pâtes : **~10 g de sel par litre** (1 %).
- Saumure humide rapide (volaille, porc) : **~5-8 % de sel** (50-80 g/L), de 30 min à quelques heures.
- Saumure à sec (dry brine) viande : **~1 % du poids**, repos au frais 12-48 h.
- Conversion volume : le sel fin est ~2x plus dense que le gros sel/flocons à volume égal — **toujours raisonner en POIDS** (peser le sel), sinon risque de sur/sous-salage selon le type. _(à confirmer : densité exacte selon le type de sel)_
- Pour un plat impossible à goûter cru : se baser sur le % au poids, puis rectifier à la première bouchée cuite.

### Gras

10. Le gras transporte les arômes : faire infuser aromates dans le gras de cuisson.
11. Choisir le gras selon la cuisine (olive = méditerranéen, beurre = nord, ghee = indien, sésame = asiatique).
12. Préchauffer la poêle, puis le gras, puis l'aliment.
13. Aliment dans la poêle = sizzle immédiat, sinon retirer et réchauffer.
14. Ne jamais empiler — une seule couche pour permettre le brunissement.
15. Sécher la surface de l'aliment avant de le saisir.

### Acide

16. Plat lourd ou gras → ajouter de l'acide (citron, vinaigre, tomate).
17. Plat trop sucré → ajouter une pointe d'acide.
18. Plat trop acide → équilibrer avec gras, sucre ou sel (jamais en diluant).
19. Acide en cuisson (vin, tomate, vinaigre) → travailler tôt pour mellower.
20. Acide de finition (citron, vinaigre frais) → ajouter au dernier moment, hors feu.
21. Acide ralentit la cuisson des légumes et légumineuses → toujours cuire à tendreté avant d'ajouter l'acide.
22. Acide ternit les verts → presser le citron juste avant de servir.

### Chaleur

23. Objectif universel : surface et cœur cuits en même temps.
24. Surface brûle avant que le cœur soit cuit → baisser la chaleur.
25. Cœur cuit mais surface pâle → monter la chaleur ou prolonger à découvert.
26. Aliment tendre (filet, œuf, poisson, légume vert) → chaleur intense, courte.
27. Aliment dur ou collagéneux (bœuf braisé, légumineuse, racine) → chaleur douce, longue.
28. Tempérer la viande (sortie frigo) avant cuisson rapide. ⚠️ 30-60 min suffisent pour des pièces moyennes ; la règle des 2 h à température ambiante est CUMULATIVE sur toute la vie de l'aliment et tombe à 1 h au-dessus de 32°C. Inutile et risqué de pousser jusqu'à 2 h (zone de danger 4-60°C).
29. Carryover : sortir l'aliment légèrement avant la cuisson cible (la cuisson continue).
30. La plupart des cuissons en liquide → mijoter, pas bouillir.

> ⚠️ Rappel sécurité (le goût ne prime jamais sur le sanitaire) : volaille (entière, morceaux ou hachée) **74°C à cœur** ; viande rouge hachée **71°C** ; pièce entière bœuf/agneau **63°C + 3 min de repos** ; porc **63°C + 3 min** ; poisson **63°C à cœur** pour la sécurité (les cibles texture 50-55°C sont du confort, pas du sanitaire). Se fier au thermomètre, pas aux tests sensoriels (toucher, jus clair), qui ne garantissent rien pour la volaille et les hachés. Zone de danger 4-60°C ; refroidissement rapide 60→21°C en ≤2 h puis 21→4°C en ≤4 h. Voir le fichier sécurité alimentaire pour les cibles faisant autorité.

---

## Construction des saveurs en couches (layering — quoi assaisonner quand)

Séquence générale de mise en couches, valable pour la plupart des plats mijotés/sautés :

1. **FOND (début, dans le gras chaud)** : aromates durs + épices entières torréfiées + pâte d'épices/curry → chaleur diffuse et profondeur.
2. **CORPS (cuisson)** : liquides, umami long (tomate concentrée, soja, fond), sel par paliers, acides « à mellower » (vin, vinaigre de cuisson).
3. **AJUSTEMENT (mi-fin)** : épices « chaudes » fragiles (garam masala, sumac), rééquilibrage sel/sucré.
4. **FINITION (hors feu)** : acide frais (jus d'agrume, vinaigre cru), herbes fraîches, zeste, huile crue parfumée, condiment fermenté/croquant, sel en flocons.

Règle mnémonique : **« le dur et le sec d'abord dans le gras, le frais et l'acide en dernier hors du feu ».**
Goûter et corriger à chaque transition, jamais seulement à la fin.

---

## Diagnostic rapide

Format : `symptôme → cause probable → action`

### Goût

- plat plat / fade → manque de sel → saler progressivement, regoûter.
- plat fade malgré sel → manque d'acide → ajouter quelques gouttes de citron ou vinaigre.
- plat lourd / écœurant → excès de gras non équilibré → ajouter acide + sel.
- plat trop salé → reculer le sel impossible → diluer (liquide neutre, féculent, gras non salé).
- plat trop acide → manque de gras ou sucre → ajouter beurre, crème, ou pincée de sucre.
- plat trop sucré → manque d'acide → ajouter citron ou vinaigre.
- plat amer → ajouter sel (masque mieux l'amertume que le sucre).
- plat ennuyeux mais "techniquement correct" → manque de contraste → introduire acide ou texture croquante.
- plat manquant de profondeur → manque d'umami → parmesan, sauce soja, anchois, champignon, tomate concentrée.

### Texture

- viande sèche → trop cuit ou pas salé en avance → la prochaine fois, saler la veille + sortir avant cible.
- viande tough → cuisson trop rapide pour le morceau → braiser long et doux.
- légume vert terne → acide ajouté trop tôt → ajouter en fin, hors feu.
- friture grasse, pâle → gras pas assez chaud → préchauffer plus, frire en petites portions.
- friture brûlée à l'extérieur, crue dedans → gras trop chaud → baisser, finir au four.
- panure molle → vapeur emprisonnée → ne pas couvrir, ne pas empiler après cuisson.
- sauce qui tranche (lait + acide) → coagulation → ajouter dairy en fin, hors feu.
- légumineuses dures malgré cuisson longue → acide ajouté avant tendreté → cuire d'abord, acidifier après.

---

## Compléments aux 4 piliers : sucré, amer, umami

_(à confirmer : ces axes étendent les principes Nosrat au-delà du traitement initial sel/gras/acide/chaleur)_

- **SUCRÉ (levier d'équilibre, pas seulement dessert)** : corrige l'acidité excessive et l'amertume ; arrondit une sauce tomate ; le sucré « salé » (miel, mélasse de grenade, sucre de palme, caramélisation) crée de la profondeur. Sources non-sucre : oignon caramélisé, carotte, tomate mûre, fruits secs.
- **AMER (souvent oublié, pourtant structurant)** : apporté par café, cacao, agrumes (zeste/pith), légumes (radicchio, endive, roquette, chou kale), thé, bière, herbes (estragon). Rôle : coupe le gras, ajoute de la complexité « adulte ». Trop d'amer → corriger par sel + gras + sucré.
- **UMAMI (à traiter comme un pilier, pas en transverse)** : leviers concrets = parmesan/affinés, tomate concentrée, champignons (surtout séchés), sauce soja/poisson, miso, anchois, algues/dashi, viande saisie. Empiler 2 sources umami compatibles décuple (« umami synergie » glutamate + inosinate/guanylate : ex. dashi kombu+bonite, tomate+parmesan, champignon+viande). Garde-fou : ne pas dépasser ~3 sources (« toomami »).

---

## Corrections typiques

### Équilibrer une sauce / vinaigrette

1. Goûter sur une feuille de salade, pas à la cuillère.
2. Trop acide → ajouter gras (huile) ou pincée de sucre.
3. Trop grasse / lourde → ajouter acide + sel.
4. Plate → saler en premier, regoûter, puis acide.
5. Pour stabiliser : macérer l'échalote/oignon dans l'acide 15 min AVANT d'ajouter l'huile.
6. **Fade ? Tester sur une bouchée AVANT de saler tout le plat.** Prélever une cuillère/petite bouchée, la saler, regoûter. Si le « zing » apparaît (les saveurs se réveillent), saler toute la casserole ; sinon, le problème n'est pas le sel. Laisser au sel le temps de se dissoudre : un sel à dissolution lente peut faire croire qu'il en manque alors qu'il faut juste attendre → risque de sursaler. Mantra : **remuer, goûter, ajuster** — faire du sel la première chose qu'on remarque en goûtant et la dernière qu'on ajuste avant de servir.

### Corriger un plat trop salé

1. Ne pas re-saler "pour compenser".
2. Augmenter le volume : ajouter féculent neutre (pomme de terre, riz, pâte), liquide non salé, ou gras (crème, beurre, yaourt).
3. Ajouter acide pour réduire la perception du sel.
4. Si soupe : retirer une partie, diluer avec bouillon non salé.

**Les 6 leviers (la fadeur ne corrige rien)** — Servir du fade à côté du salé NE corrige RIEN (la fadeur intentionnelle n'annule jamais le sur-salage). Vraies options :

1. **DILUER** — augmenter le volume avec du non-salé (riz, pomme de terre, féculent, liquide neutre) ; soupe réduite trop salée → rajouter eau/bouillon.
2. **DIVISER** — ne corriger que la moitié, garder/congeler le reste plutôt que tout diluer.
3. **ÉQUILIBRER** — parfois ce n'est pas trop salé, juste à rééquilibrer avec acide (citron/vinaigre) et/ou gras ; tester sur une cuillère d'abord.
4. **SÉLECTIONNER** — jeter le liquide de cuisson salé (haricots : changer l'eau ; viande braisée : servir sans le jus, avec un condiment acide type crème fraîche et un féculent peu salé).
5. **TRANSFORMER** — émietter une viande trop salée dans un plat où elle n'est qu'un ingrédient (ragù, chili, hachis, farce).
6. **RENONCER** — parfois mieux vaut recommencer.

### Corriger une acidité excessive

1. Ajouter gras (beurre, crème, huile) pour adoucir.
2. Ajouter sucre par très petites pincées.
3. Ajouter sel : réduit la perception acide et relève l'ensemble.
4. Allonger la cuisson : la chaleur mellow l'acide (vinaigre, vin).

### Ajuster une cuisson

1. Surface trop sombre, cœur cru → baisser chaleur, couvrir, ou finir au four doux.
2. Cœur cuit, surface pâle → monter chaleur, à découvert, dernier coup de feu.
3. Tough après cuisson rapide → on est sur le mauvais mode → braiser/mijoter à la place.
4. Sec après cuisson longue → trop cuit ou pas assez de liquide → arroser, sauce, regraisser.
5. Légume mou et terne → trop bouilli ou acide trop tôt → écourter, acide en finition.

---

## Recettes de base (sauces & condiments)

Gabarits polyvalents pour rattraper, relever ou accompagner presque tout plat.

- **Salsa d'herbes universelle : le gabarit qui sauve presque tout plat.** Sauce express qui améliore presque n'importe quel plat (œufs, riz, haricots, viande, poisson, légume). Gabarit mémorisable : échalote finement coupée + acide (vinaigre ou jus de citron/lime) + herbes hachées + huile + sel. Faire macérer l'échalote dans l'acide 15 min à part ; mélanger herbes + huile + sel à part. Juste avant de servir : ajouter l'échalote à la cuillère à trous (SANS le vinaigre), mélanger, goûter, puis ajouter l'acide petit à petit jusqu'au bon équilibre, ajuster le sel. Décliner par région en changeant herbe + acide : persil/vinaigre rouge (italien), coriandre+lime+jalapeño+oignon (mexicain), coriandre+lime+gingembre (asiatique) ; ajouter anchois+câpres = salsa verde italienne classique. Se garde 3 jours au frigo, couvert.
- **Sauces tahini/crémeuses : continuer à fouetter, détendre à l'eau.** Les sauces type tahini qui semblent « tranchées » ou trop épaisses au départ deviennent crémeuses si l'on continue à fouetter/mixer. Détendre à l'eau (par petites doses) jusqu'à la consistance voulue : épaisse pour un dip, fluide pour assaisonner salades/légumes/viande. Goûter sur une feuille de laitue, puis ajuster sel et acide.
- **Mayonnaise maison : réussir et rattraper une émulsion.** Base : 1 jaune d'œuf à température ambiante pour 175 ml d'huile. Verser l'huile goutte à goutte au début, sans cesser de fouetter ; passer à un filet plus large une fois la moitié incorporée. Si ça devient trop épais à fouetter : ajouter 1 c. à café d'eau (ou l'acide prévu) pour détendre. Caler le bol avec un torchon humide roulé en couronne pour avoir les deux mains libres. Mayonnaise comme base d'une autre sauce (tartare, césar) : la laisser NON salée et la faire la plus ferme possible, car les ajouts vont la saler et la détendre. ⚠️ Sécurité : la mayo maison contient de l'œuf CRU → conserver au froid, consommer dans les 24 h ; pour publics fragiles, utiliser des œufs pasteurisés.
- **Sauce yaourt : crème + acidité pour rafraîchir un plat riche ou sec.** Une sauce yaourt apporte à la fois crémeux et acidité : elle complète aussi bien un plat riche/gras qu'un plat sec, et sert à tempérer un plat très chaud ou épicé. Base : yaourt épais (grec/lebné) + ail râpé (pilé avec sel) + herbes (persil/coriandre/menthe) + huile d'olive + sel. Décliner en raita : + carotte râpée + gingembre + graines (cumin/moutarde/coriandre) sautées au ghee. Se garde 3 jours au frigo.
- **Pesto : ne jamais chauffer, et le fromage est la source d'acide.** Le pesto est la rare sauce à pâtes qu'on NE chauffe PAS, pour garder le vert (la chaleur brunit le basilic). Au mixeur : mettre la moitié de l'huile au fond pour que le basilic se liquéfie vite ; passer un coup de couteau dans le basilic avant ; mixer par à-coups sans insister (chaleur du moteur + oxydation brunissent), puis finir à la main dans un bol avec ail/pignons/parmesan. Le fromage dur (parmesan, pecorino) apporte sel + gras + acide ; dans un pesto basilic classique c'est souvent la SEULE source d'acide → ne pas lésiner. Détendre avec un peu d'eau de cuisson des pâtes. Couvrir la surface d'huile pour éviter l'oxydation. Le goût se concentre et l'ail ressort en reposant → regoûter après quelques minutes. Se garde 3 jours au frigo, 3 mois au congélateur.
- **Pâte de piment maison : base de condiment polyvalent.** Piments secs (guajillo, ancho, New Mexico, Anaheim) équeutés/épépinés/rincés, réhydratés à l'eau bouillante 30-60 min (assiette dessus pour immerger), puis mixés lisses 3+ min avec huile d'olive + sel (ajouter un peu d'eau de trempage réservée si trop épais ; passer au tamis si encore granuleux). Usage : en cuillère dans haricots, riz, soupes, ragoûts ; frottée sur viande avant rôtissage/grill ; dans un braisage ; mélangée à de la mayo = rouille. Déclinaisons : + cumin/coriandre/carvi torréfiés + tomates séchées + ail = harissa ; version catalane aux noix/amandes grillées + vinaigre = romesco ; + noix + mélasse de grenade + citron = muhammara. Se garde 10 jours au frigo sous huile, 3 mois au congélateur.

---

## Desserts (salage & équilibre domestiques)

_(Reste du domaine domestique de base — saler une pâte, sucrer une glace, ne pas bouillir un custard — hors pâtisserie de précision, exclue par le module.)_

- **Saler les desserts : le sel sublime le sucre.** Les bases des desserts (farine, beurre, œufs, crème) sont fades : les saler aussi. Une ou deux pincées de sel dans une pâte, un appareil ou une crème suffisent à révéler les notes de noisette, caramel, beurre. Sel fin pour qu'il se dissolve dans la pâte ; sel en flocons (Maldon) par-dessus à l'enfournement pour le croquant. Dans un caramel/dessert sucré, une pincée de sel réduit l'amertume ET crée un contraste avec le sucre → passe de « bon » à irrésistible. Doser le sel par petites touches, le laisser se dissoudre, goûter, recommencer ; si on ne sait plus si ça en a besoin, c'est probablement déjà bon, s'arrêter là.
- **Le froid atténue le sucre : sucrer plus les desserts glacés.** Tout paraît moins sucré une fois congelé. Pour granita, sorbet, glace maison : sucrer un peu PLUS que ce qui semble juste à température ambiante. Équilibrer aussi l'acidité avec un trait de citron/lime avant de congeler.
- **Compote minute : macérer le fruit avec sucre, équilibrer au citron.** Compote la plus simple = fruit mûr coupé + un peu de sucre, laissé macérer (il rend son jus, pas besoin de cuire). Sucrer « au goût » : commencer par une bonne pincée, laisser absorber, goûter, ajouter si besoin. Trop sucré → rattraper avec quelques gouttes de citron, de vin ou de vinaigre.
- **Ne pas faire bouillir le lait/crème + tempérer les œufs (custard / crème anglaise).** Chauffer crème/lait doucement et arrêter dès l'apparition de vapeur (juste avant le frémissement) : bouillir casse l'émulsion et coagule les protéines → texture jamais lisse. Tempérer les œufs : verser lentement une partie de la préparation chaude sur les œufs en fouettant sans arrêt, PUIS reverser le tout dans la casserole sur feu doux (évite l'œuf brouillé). Repère d'épaississement pour une crème **ANGLAISE** (jaunes, sans amidon) : tracer un trait au doigt au dos de la cuillère, il doit tenir — **« à la nappe » à ~82-85°C au thermomètre**. ⚠️ NE PAS monter à 97°C : à cette température une crème anglaise tranche/graine (les jaunes coagulent dès ~80-85°C). Le seuil ~97-100°C (ébullition) est réservé à la crème **PÂTISSIÈRE**, qui contient de la farine (l'amidon protège de la coagulation et la crème DOIT bouillir ~2 min). Complète l'erreur existante « faire bouillir le lait avec un acide → ça tranche ».

---

## Patterns de goût

Combinaisons qui marchent presque toujours :

- **gras + acide** → équilibre (vinaigrette, beurre + citron, huile + vinaigre)
- **sel + chaleur** → intensité (saisir une viande bien salée)
- **sel + amertume** → l'amertume recule (café, chocolat, agrumes)
- **acide + sucré** → réveil (citron sur fruit, vinaigre balsamique sur fraise)
- **gras + sel + acide** → triade de base (toute vinaigrette, tout poisson grillé)
- **brunissement + acide final** → profondeur + lift (rôti + déglaçage vin + jus citron)
- **umami + acide + sel** → "deliciousness" (parmesan, sauce soja, miso, tomate)
- **chaleur intense + chaleur douce séquentielles** → croûte + cœur tendre (saisir puis braiser)
- **sucré + sel + gras + acide** → caramel salé (4 saveurs activées en une bouchée)

Techniques concrètes de pattern :

- **Équilibrer le sucre avec l'acide (légumes rôtis, fruits).** Toujours équilibrer le sucre avec un acide, pas seulement en pâtisserie. Légumes devenus sucrés par le brunissement (carottes, chou-fleur, brocoli, betteraves rôtis) : un trait de citron ou de vinaigre les réveille. Betterave rôtie : un filet de vinaigre de vin rouge masque le côté terreux. Tarte aux pommes : choisir des variétés acidulées plutôt que les plus sucrées. Modèle : une pêche parfaite est sucrée ET acide — viser ce contraste.
- **Équilibre acide à l'échelle du repas (pas seulement du plat).** Chaque plat doit être équilibré (sel/gras/acide), mais le repas entier aussi. Un plat riche se pense AVEC son accompagnement acide : tarte à l'oignon confit → salade + vinaigrette moutardée vive ; porc effiloché → slaw acidulé et croquant ; curry thaï au lait de coco → précédé d'une salade de concombre légère. Une salade servie avec des plats riches a besoin de PLUS d'acide pour nettoyer le palais.
- **Booster l'umami discrètement avec des anchois fondus.** Pour relever des légumes verts ou une sauce sans goût identifiable de poisson : faire fondre 4 à 6 filets d'anchois hachés avec l'oignon/l'ail en début de cuisson. Résultat : tout le monde trouve le plat « étonnamment savoureux » sans pouvoir dire pourquoi. Fonctionne aussi dans une sauce, un ragù, des verts longuement cuits.

Patterns à éviter :

- gras + gras sans acide → écœurement
- acide + acide sans gras → agression
- sucre + sucre sans acide → mièvrerie
- umami + umami + umami → "toomami" (saturation, perte de lisibilité)

---

## Raccourcis de décision

Heuristiques pour décider en moins de 2 secondes :

```text
si doute sur la saveur     → ajouter sel d'abord, regoûter
si plat fade après sel     → ajouter acide
si trop riche / lourd      → ajouter acide
si trop acide              → ajouter gras ou sel
si trop sucré              → ajouter acide
si trop salé               → ajouter volume (féculent, gras, liquide)
si trop amer               → ajouter sel (pas sucre)
si plat plat ET correct    → manque contraste → acide final + texture
si surface brûle           → baisser feu
si cœur cru                → couvrir, baisser, prolonger
si tough                   → mauvais mode de cuisson, basculer en braise
si sec                     → la prochaine fois, saler plus tôt
si manque de profondeur    → ajouter umami (parmesan, soja, anchois)
```

**Improviser un plat avec Sel / Gras / Acide selon la cuisine.** Pour transformer un reste (ex : poulet rôti → salade) sans recette : choisir la cuisine, puis la forme de sel/gras/acide qui va avec.

- Inde : yaourt entier, coriandre, oignons macérés au jus de citron vert, sel, pointe de curry.
- Sicile : jus + zeste de citron, oignons macérés au vinaigre de vin rouge, graines de fenouil, sel marin.
- US (Cobb) : bacon, bleu, œuf dur, avocat, vinaigrette de vin rouge.

Rôle de chacun : le sel rehausse, le gras transporte, l'acide équilibre. Rattraper un plat fade : ajouter un condiment qui apporte acide + sel (crème aigre, cornichons, salsa, yaourt, oignons au vinaigre).

Hiérarchie en cas d'ambiguïté :

1. Sel d'abord (impact le plus fort sur la perception).
2. Acide ensuite (équilibre et lift).
3. Gras (richesse, transport des arômes).
4. Chaleur (irréversible, à anticiper).
5. Umami (booster, à doser).

---

## Erreurs fréquentes

- **Sous-saler** par peur du "trop salé". Le sel s'apprend en goûtant, pas en mesurant.
- **Saler trop tard.** Le sel a besoin de temps pour diffuser dans la viande.
- **Corriger trop tard**, après plating. Goûter et ajuster en cours de cuisson.
- **Empiler les correctifs** : ajouter sel + sucre + acide + crème en même temps. Une variable à la fois.
- **Confondre texture et goût.** Si c'est mou, ce n'est pas le sel qui sauve.
- **Acidifier les légumineuses ou onions trop tôt** → ils restent durs.
- **Ajouter du citron sur le vert en avance** → il ternit.
- **Faire bouillir le lait avec un acide** → ça tranche.
- **Faire bouillir une crème anglaise** (jaunes sans amidon) → elle tranche ; viser ~82-85°C à la nappe.
- **Cuire la viande sortie du frigo** → cuisson inégale, surface trop cuite.
- **Faire confiance au cadran du four** plutôt qu'aux signes (sizzle, couleur, vapeur, parfum).
- **Surcharger la poêle** → vapeur emprisonnée, pas de brunissement.
- **Oublier le carryover** → sortir trop tard, dépasser la cible.
- **Empiler les sources d'umami** ("toomami") → perte de lisibilité.
- **Goûter une vinaigrette à la cuillère** → toujours sur une feuille.
- **Bottled juice** au lieu de jus frais → perte de lift.
- **Saupoudrer du sel en surface** pour rattraper un manque à cœur → inefficace ; saler l'eau/la masse avant et pendant.
- **Saler "pour compenser" un plat déjà trop salé** → aggrave ; diluer / diviser / transformer.

---

## Limites

Ce que ce module **ne couvre pas** :

- Recettes spécifiques (le livre en contient, mais elles ne sont pas extraites ici, hormis les gabarits de base ci-dessus).
- Pâtisserie de précision (sucre cuit, tempérage chocolat, levée précise).
- Sécurité alimentaire et températures internes critiques (voir le fichier sécurité alimentaire, source de vérité). Les repères de température donnés ici (ex. nappe ~82-85°C) sont des repères de TEXTURE, pas des seuils sanitaires.
- Spécificités d'allergies et de régimes.
- Choix d'ingrédients selon saison/marché local.
- Cuissons sous vide, fermentations longues, techniques de chef avancées.

Ce que ce module **suppose** :

- L'utilisateur a une recette ou une intention de plat de départ.
- L'utilisateur peut goûter et décrire ce qu'il goûte.
- L'agent intervient en correction ou conseil, pas en exécution autonome.
- Les principes sont **des heuristiques**, pas des lois — la dégustation finale arbitre. La sécurité sanitaire, elle, n'est jamais une heuristique : suivre les cibles de température du fichier sécurité.

---

## Méta

- Règles totales : **30 règles fondamentales** + idées reçues/contextes de salage + repères chiffrés + **~25 patterns/raccourcis** + **~18 erreurs** + 2 sections recettes/desserts + séquence de layering.
- Couverture : sel ✅ — gras ✅ — acide ✅ — chaleur ✅ — sucré ✅ — amer ✅ — umami ✅.
- Format compatible : ingestion par agent IA (Gemini, Claude, GPT).
- Source : *Salt, Fat, Acid, Heat*, Samin Nosrat, 2017 (chapitres "Salt", "Fat", "Acid", "Heat").
- Repo cible : `joachimpomme-ctrl/Cuisine`.
