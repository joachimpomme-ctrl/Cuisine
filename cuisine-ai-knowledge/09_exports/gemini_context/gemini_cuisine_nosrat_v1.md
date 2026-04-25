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
28. Tempérer la viande (sortie frigo 1h+) avant cuisson rapide.
29. Carryover : sortir l'aliment légèrement avant la cuisson cible (la cuisson continue).
30. La plupart des cuissons en liquide → mijoter, pas bouillir.

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

## Corrections typiques

### Équilibrer une sauce / vinaigrette

1. Goûter sur une feuille de salade, pas à la cuillère.
2. Trop acide → ajouter gras (huile) ou pincée de sucre.
3. Trop grasse / lourde → ajouter acide + sel.
4. Plate → saler en premier, regoûter, puis acide.
5. Pour stabiliser : macérer l'échalote/oignon dans l'acide 15 min AVANT d'ajouter l'huile.

### Corriger un plat trop salé

1. Ne pas re-saler "pour compenser".
2. Augmenter le volume : ajouter féculent neutre (pomme de terre, riz, pâte), liquide non salé, ou gras (crème, beurre, yaourt).
3. Ajouter acide pour réduire la perception du sel.
4. Si soupe : retirer une partie, diluer avec bouillon non salé.

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
- **Cuire la viande sortie du frigo** → cuisson inégale, surface trop cuite.
- **Faire confiance au cadran du four** plutôt qu'aux signes (sizzle, couleur, vapeur, parfum).
- **Surcharger la poêle** → vapeur emprisonnée, pas de brunissement.
- **Oublier le carryover** → sortir trop tard, dépasser la cible.
- **Empiler les sources d'umami** ("toomami") → perte de lisibilité.
- **Goûter une vinaigrette à la cuillère** → toujours sur une feuille.
- **Bottled juice** au lieu de jus frais → perte de lift.

---

## Limites

Ce que ce module **ne couvre pas** :

- Recettes spécifiques (le livre en contient, mais elles ne sont pas extraites ici).
- Pâtisserie de précision (sucre cuit, tempérage chocolat, levée précise).
- Sécurité alimentaire et températures internes critiques.
- Spécificités d'allergies et de régimes.
- Choix d'ingrédients selon saison/marché local.
- Cuissons sous vide, fermentations longues, techniques de chef avancées.

Ce que ce module **suppose** :

- L'utilisateur a une recette ou une intention de plat de départ.
- L'utilisateur peut goûter et décrire ce qu'il goûte.
- L'agent intervient en correction ou conseil, pas en exécution autonome.
- Les principes sont **des heuristiques**, pas des lois — la dégustation finale arbitre.

---

## Méta

- Règles totales : **30 règles fondamentales** + **~25 patterns/raccourcis** + **~15 erreurs**.
- Couverture : sel ✅ — gras ✅ — acide ✅ — chaleur ✅ — umami (transverse) ✅.
- Format compatible : ingestion par agent IA (Gemini, Claude, GPT).
- Source : *Salt, Fat, Acid, Heat*, Samin Nosrat, 2017 (chapitres "Salt", "Fat", "Acid", "Heat").
- Repo cible : `joachimpomme-ctrl/Cuisine`.
