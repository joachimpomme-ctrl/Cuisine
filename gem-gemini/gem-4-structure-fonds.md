# Structure classique, sauces & fonds

_Bundle Gem consolidé regroupant : 06-escoffier-structure.md, 18-fonds-bouillons.md_



<!-- ===== 06-escoffier-structure.md ===== -->

# Escoffier V1 — Grammaire culinaire utile

## Rôle de ce fichier

Ce fichier sert à injecter dans le Gem une logique classique de structure culinaire, sans transformer la réponse en cours d'histoire ni en fiche de recette.

Il aide surtout à :
- comprendre la structure d'un plat ;
- choisir une famille de sauce ou de finition ;
- vérifier la cohérence produit / sauce / garniture ;
- éviter qu'une sauce couvre ou brouille le produit principal ;
- enrichir une réponse sans remplacer la méthode principale.

La méthode principale reste toujours :
diagnostic -> une correction -> degustation -> ajustement.

## Comment utiliser Escoffier dans le Gem

Utiliser Escoffier si :
- l'utilisateur demande une sauce ou une finition ;
- l'utilisateur demande quelle garniture ou quelle famille de sauce convient ;
- un plat semble incohérent entre produit, sauce et accompagnement ;
- une sauce couvre le produit ;
- il faut choisir entre jus, sauce courte, sauce liée, émulsion, crème ou beurre ;
- il faut expliquer un mot classique sans jargon inutile.

Ne pas utiliser Escoffier en priorité si :
- le plat est simplement fade ;
- le problème est d'abord une erreur de cuisson ;
- le problème relève surtout du geste technique ;
- l'utilisateur veut une réponse très rapide et très pratique ;
- une règle moderne de cuisson, d'assaisonnement ou de rattrapage suffit déjà.

## Principes fondamentaux

- Une bonne sauce part d'une bonne base.
- Une base nette vaut mieux qu'une finition flatteuse.
- Une sauce doit prolonger le produit principal, pas le couvrir.
- Avant de nommer une sauce classique, choisir sa famille utile.
- Réduire sert à concentrer goût et texture en même temps.
- Si la réduction durcit le goût, il faut s'arrêter ou détendre.
- Une liaison doit rester sobre et ne pas cacher une base faible.
- Clarifier ne sert que si la netteté change vraiment l'usage.
- Les aromates orientent la sauce ; ils ne remplacent pas la base.
- La finition doit confirmer une base juste, pas ouvrir une seconde cuisine.
- Les concentrés servent d'appoint ; ils ne sauvent pas une base ratée.
- Une sauce trop neutre uniformise les plats.
- La logique classique ne vaut que si elle reste utile en contexte domestique.

## Logique des sauces

Une sauce utile se choisit par structure.

- Base : fond, fumet, lait, jus de cuisson, réduction, liquide de braisage.
- Liaison : aucune si possible ; sinon liaison légère, réduction, roux ou émulsion selon le besoin.
- Acidité : vin blanc, citron, vinaigre, tomate ou autre note vive pour relancer sans casser la ligne du plat.
- Aromatique : herbes, échalote, moutarde, oignon, mirepoix ou autre accent lisible.
- Finition : beurre, crème, herbes, condiments, glace ou concentré seulement si cela précise la sauce.
- Usage : grillade, braisage, pochage, service froid, légumes, oeufs, potage.

Pour choisir une sauce :
1. partir du produit principal ;
2. choisir une famille de base ;
3. ajouter une liaison seulement si nécessaire ;
4. ajuster acidité, gras et aromatique ;
5. finir sans couvrir le produit.

Repères utiles :
- grillade : jus court ou réduction courte ;
- produit délicat : sauce claire, plus courte, plus nette ;
- braisage : partir du fond du plat avant d'ajouter autre chose ;
- service froid : penser tenue, fraîcheur et lisibilité ;
- sauce fragile : ne la garder que si le service est proche.

## Associations produit / sauce / garniture

### Poisson blanc
- Famille utile : fumet, vin blanc réduit, beurre, citron bref.
- Mauvais signe : la sauce masque le goût délicat ou alourdit la bouchée.
- Correction : revenir à une sauce plus claire, plus courte ou plus acidulée.

### Crustacés
- Famille utile : fumet ou carapace, beurre, crème légère.
- Mauvais signe : la sauce écrase le goût de carapace ou la douceur iodée.
- Correction : revenir à une base plus courte et plus nette.

### Coquillages
- Famille utile : vin blanc, beurre, sauce courte nette.
- Mauvais signe : la sauce brouille leur jus naturel.
- Correction : simplifier vers une sauce courte et lisible.

### Viande rouge grillée
- Famille utile : jus court, réduction vineuse, sauce brune courte.
- Mauvais signe : la sauce efface la croûte ou la saveur grillée.
- Correction : revenir à un jus court ou à une réduction plus sèche.

### Volaille pochée
- Famille utile : velouté, suprême, crème légère.
- Mauvais signe : la sauce assombrit le plat ou couvre sa douceur.
- Correction : revenir à une sauce claire ou plus légère.

### Volaille rôtie
- Famille utile : jus court, glace légère, jus du plat.
- Mauvais signe : une sauce extérieure prend le dessus sur les sucs du rôti.
- Correction : revenir au jus de cuisson avant d'ajouter une autre famille.

### Porc
- Famille utile : moutarde, oignon, acidité mesurée, sauce vive.
- Mauvais signe : la sauce accentue seulement le gras.
- Correction : réintroduire une note plus vive ou moutardée.

### Agneau
- Famille utile : jus, herbes, note fraîche.
- Mauvais signe : une sauce épaisse ou lourde durcit le plat.
- Correction : revenir à un jus plus simple et plus herbacé.

### Gibier
- Famille utile : sauce brune vive, vin, fruit discret, poivrade légère.
- Mauvais signe : la sauce n'assume plus la puissance du produit.
- Correction : revenir à une sauce du même registre, plus courte et plus nette.

### Oeufs chauds
- Famille utile : hollandaise, Mornay, béchamel ou beurre selon la cuisson.
- Mauvais signe : la sauce alourdit les oeufs ou les fait disparaître.
- Correction : alléger la sauce ou en mettre moins.

### Oeufs froids
- Famille utile : mayonnaise, gribiche, ravigote, sauce froide structurée.
- Mauvais signe : on recycle une sauce chaude refroidie.
- Correction : revenir à une sauce froide prévue pour tenir.

### Légumes verts
- Famille utile : beurre, crème légère, acidité légère, herbes.
- Mauvais signe : la sauce couvre la fraîcheur végétale.
- Correction : raccourcir la finition et alléger la sauce.

### Légumes racines
- Famille utile : sauce courte beurrée, crème légère, jus de cuisson.
- Mauvais signe : la sauce est plus lourde que le légume.
- Correction : revenir à une sauce qui enrobe sans masquer.

### Rôti
- Famille utile : jus du plat, réduction des sucs.
- Mauvais signe : une sauce ajoutée efface la logique du rôti.
- Correction : repartir du jus de cuisson.

### Poisson froid
- Famille utile : mayonnaise, tartare, gribiche.
- Mauvais signe : une sauce chaude recyclée brouille le service.
- Correction : revenir à une sauce froide tenue et fraîche.

## Patterns de plats

### Viande grillée
- Structure : grillade + jus ou sauce courte.
- Point de vigilance : le produit saisi doit rester au centre.
- Erreur fréquente : une sauce lourde prend la place de la grillade.

### Viande braisée
- Structure : cuisson lente + fond de cuisson réduit.
- Point de vigilance : la sauce doit venir du braisage lui-même.
- Erreur fréquente : ajouter une seconde sauce qui brouille le fond du plat.

### Poisson poché
- Structure : cuisson douce + fumet repris en sauce claire.
- Point de vigilance : la netteté du liquide compte autant que la cuisson.
- Erreur fréquente : une sauce ou une garniture plus lourde que le poisson.

### Volaille pochée
- Structure : cuisson blanche + velouté, suprême ou crème courte.
- Point de vigilance : garder une cohérence claire.
- Erreur fréquente : assombrir inutilement la sauce.

### Gibier
- Structure : produit puissant + base brune vive.
- Point de vigilance : la sauce doit rester dans le même registre que le produit.
- Erreur fréquente : adoucir ou sucrer au point d'effacer le gibier.

### Légumes
- Structure : légume cuit + finition courte.
- Point de vigilance : le légume décide de la richesse de la sauce.
- Erreur fréquente : donner plus d'importance à la sauce qu'au légume.

### Oeufs
- Structure : oeuf + sauce choisie selon température et fragilité.
- Point de vigilance : la cuisson de l'oeuf passe avant l'envie de sauce.
- Erreur fréquente : traiter l'oeuf comme simple support.

### Rôti
- Structure : cuisson sèche + récupération des sucs.
- Point de vigilance : le jus du plat a priorité.
- Erreur fréquente : ajouter une sauce extérieure trop tôt.

### Potage clair
- Structure : base limpide + garniture discrète.
- Point de vigilance : la clarté du liquide reste centrale.
- Erreur fréquente : charger la garniture ou troubler la base.

### Potage lié
- Structure : base de goût + liaison modérée.
- Point de vigilance : la texture doit servir la base, pas l'inverse.
- Erreur fréquente : lier jusqu'à étouffer le goût.

### Sauce courte
- Structure : base réduite, peu d'éléments, lecture rapide.
- Point de vigilance : garder la lisibilité du produit.
- Erreur fréquente : multiplier les finitions et aromates.

### Sauce de déglaçage
- Structure : sucs + liquide court + réduction.
- Point de vigilance : partir des sucs du plat.
- Erreur fréquente : noyer les sucs dans trop de liquide.

### Sauce montée au beurre
- Structure : base déjà juste + beurre ajouté en fin de parcours.
- Point de vigilance : monter hors feu fort et servir vite.
- Erreur fréquente : utiliser le beurre pour masquer une base faible.

## Sauces nommées — lignées et usages

### Lignée brune (base : Espagnole / Demi-glace)

- `Bordelaise` : demi-glace + réduction vin rouge + échalotes + moelle pochée en finition. → viande rouge grillée.
- `Chasseur` : demi-glace tomatée + champignons sautés + vin blanc + échalotes + estragon. → volaille sautée.
- `Périgueux` : demi-glace corsée + lamelles ou brunoise de truffe + madère. → petites entrées, timbales, pâtés chauds.
- `Madère` : demi-glace réduite, madère ajouté hors feu. → viande braisée, ris de veau, rognons.
- `Lyonnaise` : demi-glace + oignons blondis + réduction vinaigre. → desserte de viandes bouillies.
- `Robert` : demi-glace + oignons + vin blanc + moutarde ajoutée hors feu (ne doit pas bouillir). → porc grillé.
- `Poivrade` : demi-glace + marinade + mirepoix + grains de poivre concassés. → gibier.
- `Grand-Veneur` : poivrade au fumet de venaison + sang ou gelée de groseilles + crème. → grosses pièces de gibier.
- `Italienne` : demi-glace tomatée + duxelles + jambon + fines herbes. → petites entrées et poissons (sans jambon).

### Lignée blanche (base : Velouté)

- `Allemande` : velouté ordinaire lié aux jaunes d'œufs + jus de champignons. → volaille pochée, légumes.
- `Suprême` : velouté de volaille monté à la crème, réduit jusqu'à nappe. → volaille pochée, ris de veau.
- `Normande` : velouté de poisson + fumet + champignons + huîtres + crème + jaunes. → sole pochée, poissons nobles.
- `Mornay` : béchamel + gruyère et parmesan râpés. → œufs, poisson gratin, légumes gratinés, Florentine.
- `Cardinal` : béchamel + beurre de homard + truffe. → poissons et crustacés.
- `Soubise` : béchamel + oignons étuvés réduits en purée. → agneau, œufs, légumes.
- `Nantua` : béchamel ou velouté + beurre d'écrevisses + crème. → quenelles, poissons, garniture Nantua.

### Lignée émulsionnée (base : jaunes d'œufs + beurre)

- `Hollandaise` : jaunes + beurre clarifié monté au bain-marie + citron. → asperges, poisson poché, œufs pochés.
- `Béarnaise` : réduction vinaigre + estragon + échalotes, montée comme hollandaise. → viande grillée (bœuf, agneau).
- `Choron` : béarnaise tomatée. → tournedos et noisettes.
- `Foyot` : béarnaise + glace de viande. → viandes grillées.
- `Noisette` : hollandaise + beurre noisette en finition. → saumon et truite pochés.

### Règle de lignée
Chaque sauce dérivée part d'une base mère — ne jamais inventer une sauce dérivée sans sa base.
Si la base est absente, proposer la sauce la plus simple de la même famille plutôt qu'une imitation.

### Sauces froides — famille mayonnaise

- `Gribiche` : mayonnaise montée aux jaunes d'œufs durs + moutarde. Garnie : cornichons, câpres, cerfeuil, persil, estragon hachés, julienne de blancs durs. → poissons froids, œufs, langues, pieds.
- `Rémoulade` : mayonnaise + moutarde forte. Garnie : câpres, cornichons, persil, cerfeuil, estragon hachés + goutte d'essence d'anchois. → viandes froides, céleri rémoulade, fruits de mer.
- `Ravigote` (froide) : huile + vinaigre + câpres + persil, cerfeuil, estragon, oignons hachés + sel et poivre. → viandes bouillies, pieds, tête de veau, légumes cuits.
- `Verte` : mayonnaise teinté d'une purée d'aromates blanchis et pressés (épinards, cresson, persil, cerfeuil, estragon). → saumon froid, truite, légumes.
- `Tartare` : mayonnaise aux jaunes d'œufs durs + oignons et ciboulettes finement hachés, assaisonnée de haut goût. → fritures, viandes froides.
- `Vincent` : ½ sauce Tartare + ½ sauce Verte mélangées. → poissons froids, crustacés.

Règle d'usage des sauces froides :
- Toujours assaisonner de haut goût (elles perdent en puissance au froid).
- Gribiche et Rémoulade se distinguent par leur texture (Gribiche est plus rustique, Rémoulade plus lisse).
- En contexte domestique : Rémoulade = moutarde + câpres + cornichons + herbes dans une mayo ; Gribiche = même base mais montée sur jaunes durs.

> **Sécurité (sauces froides à base d'œuf cru)** : mayonnaise, gribiche montée à cru, etc. = œuf cru. À consommer dans la journée, gardées au froid (≤4°C). Pour les publics fragiles (enfants en bas âge, femmes enceintes, personnes âgées ou immunodéprimées), utiliser des œufs pasteurisés ou éviter. Voir fichier sécurité.

#### Sauces froides — complément

En plus de la famille mayonnaise déjà détaillée :
- Raifort (froide) : raifort râpé fin + sel + poivre + crème + jus de citron. → viandes bouillies, poisson fumé.
- Menthe (mint sauce) : menthe hachée + un peu de sucre + vinaigre + eau. → agneau chaud ou froid.
- Cumberland : gelée de groseilles fondue + porto + échalote blanchie + julienne de zestes orange/citron blanchis + jus d'orange et citron + moutarde + pointe de cayenne et gingembre, tout à froid. → gibier/venaison froide, jambon, viandes froides, terrines. Variante Oxford = mêmes éléments, zestes râpés.
- Moutarde à la crème : moutarde en poudre + jus de citron + sel + poivre, incorporer doucement la crème fraîche. → crudités, céleri, poissons froids.
- Règle de stabilisation (mayo qui doit attendre) : terminer par 3 cuillerées d'eau bouillante par litre.

---

## Garnitures nommées — référence rapide

Format : `Nom` → produits associés | composants | sauce d'accompagnement suggérée

### Garnitures légumes (rustiques et bistrot)

- `Boulangère` → mouton, agneau, volaille | pommes de terre en quartiers + oignons émincés cuits autour de la pièce | jus de la pièce.
- `Bourgeoise` → bœuf braisé | carottes tournées + petits oignons glacés + lardons | fond de braisage.
- `Bourguignonne` → bœuf | petits oignons glacés + champignons + lardons + vin rouge | sauce de braisage au vin rouge.
- `Flamande` → bœuf, porc | boules de choux braisés + carottes + navets + lardons + saucisses | fond de la pièce.
- `Berrichonne` → gros relevés de boucherie | choux braisés + petites tranches de lard + oignons glacés + marrons | fond de braisage.
- `Bretonne` → mouton, agneau | haricots blancs ou flageolets liés à la sauce Bretonne (oignon + tomate + ail) | jus de la pièce.
- `Conti` → bœuf et veau braisés | purée de lentilles + lardons | fond de braisage.
- `Forestière` → bœuf, volaille | morilles sautées + lardons + pommes de terre sautées | sauce Duxelles + fond.
- `Lyonnaise` (garniture) → viandes de boucherie | oignons émincés et blondis | jus lié.

### Garnitures légumes (classiques de restaurant)

- `Bouquetière` → gros relevés de boucherie | carottes + navets + haricots verts + petits pois + pommes château + chou-fleur | jus clair de la pièce.
- `Jardinière` → bœuf, veau | macédoine de légumes frais (carottes, navets, haricots, petits pois) liés au beurre | jus lié.
- `Dubarry` → bœuf, tournedos | bouquets de chou-fleur masqués de sauce Mornay et glacés | fond ou déglaçage.
- `Florentine` → poissons, œufs, viandes blanches | épinards étuvés au beurre + sauce Mornay en nappe | sauce Mornay.
- `Clamart` → bœuf | tartelettes de petits pois à la française | jus lié.

### Garnitures festives

- `Financière` → bœuf, volaille, ris de veau | quenelles + champignons tournés + truffes + crêtes de coq + olives | sauce Financière (demi-glace + madère + truffe).
- `Godard` → gros relevés | quenelles truffées + champignons + crêtes de coq + quenelles en forme de grosses olives | sauce Godard (champagne + demi-glace).
- `Gastronome` → bœuf, volaille | marrons glacés + truffes + crêtes de coq + champignons | demi-glace à l'essence de truffes.
- `Régence` → volaille, poisson | quenelles + truffes + foie gras ou huîtres selon produit | sauce Régence (demi-glace ou normande + truffe).

### Garnitures pour poissons

- `Normande` → sole, turbot | huîtres + moules + queues d'écrevisses + champignons + lames de truffe | sauce Normande.
- `Cancalaise` → poissons pochés | huîtres pochées + queues de crevettes | sauce Normande.
- `Dieppoise` → poissons | queues de crevettes + moules | sauce vin blanc.
- `Florentine` → poissons (voir ci-dessus).

### Garnitures d'expression régionale et bistrot étendu

- `Provençale` → tomates mondées cuites au four à l'huile + champignons farcis à la duxelles + ail. → agneau, volaille, viandes grillées.
- `Niçoise` → tomates concassées + haricots verts + câpres + lames de citron sur le poisson. Autour : beurre d'anchois. → poissons grillés ou rôtis, agneau.
- `Languedocienne` → rondelles d'aubergines frites + cèpes sautés à l'huile + tomates concassées + persil. → agneau, viandes grillées du Sud.
- `Printanière` → carottes + navets + oignons glacés + petits pois + haricots verts liés au beurre. → entrées, agneau de printemps, volaille.
- `Doria` → concombres tournés en gousses d'ail, étuvés au beurre. → poissons blancs, truite, saumon.
- `Vert-Pré` (grillades) → bouquets de cresson + pommes pailles. → grillades viande rouge, côtelettes.
- `Chipolata` → oignons glacés + chipolatas + marrons entiers cuits + lardons. → porc, volaille, viandes d'automne-hiver.
- `Mexicaine` → champignons grillés garnis tomates concassées + poivrons grillés + aubergines grillées. → volaille, viande rouge grillée.
- `Portugaise` → petites tomates farcies + pommes château. → volaille, porc, agneau.
- `Tyrolienne` → rondelles d'oignons frits + tomates concassées tombées à l'huile. → tournedos, noisettes d'agneau, escalopes.
- `Andalouse` → demi-poivrons grillés farci riz à la grecque + tronçons d'aubergines sautés + tomates concassées. → volaille, grosses pièces.

### Garnitures pour poissons — complément

- `Marinière` → moules ébarbées + queues de crevettes. → filets et pièces de poisson à la vapeur ou pochés.
- `Boitelle` → champignons émincés crus cuits directement avec le poisson. → poissons au four ou à la poêle, cuisson intégrée.
- `Niçoise` → voir ci-dessus (aussi bien poisson que viande).

### Règle d'usage des garnitures
- La garniture se choisit en cohérence avec le produit et la sauce : même registre, même intensité.
- Une garniture de légumes simples (Bouquetière, Jardinière, Printanière) convient à un jus clair.
- Une garniture riche (Financière, Godard) appelle une sauce de même rang.
- Les garnitures régionales (Provençale, Niçoise, Languedocienne) appellent l'huile d'olive et les herbes du sud — cohérentes avec les plats chauds estivaux.
- En contexte domestique, retenir la logique (produit + légume dominant + sauce courte) plutôt que le nom exact.

---

## Vocabulaire utile

- `fonds` : base liquide structurante pour sauces, jus ou potages.
- `fumet` : base courte et précise, surtout pour poisson ou crustacés.
- `glace` : fond très réduit, utilisé en petite quantité.
- `roux` : base farine + matière grasse pour lier une sauce.
- `jus lié` : jus légèrement lié qui doit rester d'abord un jus.
- `demi-glace` : base brune déjà préparée pour des sauces courtes.
- `velouté` : sauce claire liée sur base de fond.
- `béchamel` : sauce blanche lactée liée.
- `dépouiller` : écumer et dégraisser pour garder une cuisson nette.
- `vanner` : remuer pour lisser ou refroidir doucement.
- `réduire` : faire évaporer pour concentrer.
- `tomber à glace` : pousser une réduction très loin avant de remouiller.
- `mouiller` : ajouter le liquide qui construit cuisson ou sauce.
- `lier` : épaissir juste assez pour que la sauce nappe.
- `monter au beurre` : finir au beurre hors feu fort.
- `passer à l'étamine` : filtrer très finement.
- `suer` : cuire doucement sans brunir.
- `étuver` : cuire doucement à couvert avec peu de liquide.
- `braiser` : colorer puis cuire doucement avec fond et couvercle.
- `poêler` : cuire une pièce délicate dans un milieu gras et protégé.
- `clarifier` : retirer le trouble ou les dépôts pour obtenir plus de netteté.
- `appareil` : préparation de base avant montage ou cuisson.
- `farce` : mélange qui garnit ou structure une pièce.
- `garniture` : accompagnement ou relais de texture et de goût.
- `singer` : saupoudrer de farine une viande ou un légume déjà revenu, pour lier la sauce en cours de cuisson sans faire de roux séparé.
- `pincer` : colorer légèrement au four des os, légumes ou une viande avant de mouiller — sert à foncer et à donner de l'arôme à un fond ou un braisage.
- `tomber` : cuire des légumes à feu doux dans peu de beurre jusqu'à évaporation complète du liquide rendu — ils restent fondants sans colorer.
- `larder` : introduire à la lardoire des bâtonnets de lard dans une viande pour l'arroser de l'intérieur pendant la cuisson.
- `blanchir` : plonger brièvement dans l'eau bouillante — pour attendrir, atténuer l'âcreté ou fixer la couleur d'un légume vert avant finition.
- `mortifier` : laisser reposer une viande ou un gibier après abattage pour que les fibres se relâchent et s'attendrissent.
- `aiguillette` : tranche de chair coupée longue et mince dans le sens du grain.

### Vocabulaire utile — complément (gestes et coupes)

Verbes et bases de gestes (singer, étuver, tomber, aiguillette déjà définis ci-dessus — non répétés) :
- `beurre manié` : beurre mou malaxé avec autant de farine crue, ajouté hors feu en fin de cuisson pour lier rapidement une sauce (ne pas faire bouillir longtemps après).
- `étouffer` : cuire à court mouillement et à couvert (légumes fondants, peu de liquide).
- `court-mouillement` : cuire avec très peu de liquide, qu'on arrose et renouvelle au besoin (braisé serré, poitrine de veau).
- `rissoler` : sauter en poussant plus loin la coloration (croûte dorée).
- `revenir` : sauter vivement viande/légume pour colorer avant de mouiller.
- `concasser` : hacher grossièrement.
- `mijoter` : cuire doucement et lentement.
- `luter` : sceller le couvercle avec une pâte (farine + eau), petit trou pour la vapeur (mijotés longs).
- `vert-cuit` : saisi vif et gardé rosé/saignant à cœur (rognon, foie) — à ne plus faire bouillir ensuite. (Note sécurité : « rosé à cœur » est un choix de texture sur abats ; ce n'est pas une garantie sanitaire — voir fichier sécurité.)
- `dégorger` : tremper longuement à l'eau froide (souvent changée) pour purger sang et impuretés (ris, cervelle, tripes).
- `duxelles sèche` : oignons revenus au beurre + échalotes + champignons hachés et pressés, cuits jusqu'à évaporation complète (farces, sauces) — concentre le goût, évite une farce aqueuse.
- `fondue de tomates` (tomates concassées) : tomates mondées, pressées, concassées tombées au beurre + ail + sel/poivre jusqu'à évaporation complète — base qui ne détrempe pas.

Coupes : tailles normalisées et termes de veau :
- `brunoise` : petits dés de 1 à 3 mm → base aromatique fine ou garniture.
- `julienne` : bâtonnets de 3 à 5 cm de long, 1 à 2 mm d'épaisseur.
- `mirepoix` : carottes + oignons (parfois lard/jambon) en dés, base aromatique d'une sauce/d'un braisage.
- `fricandeau` : tranche épaisse de noix de veau (≤4 cm), coupée dans le sens du fil, battue et piquée, toujours braisée.
- `grenadins` : petits fricandeaux, piqués et braisés.
- `tendron` : extrémité cartilagineuse des côtes (sur la poitrine), pris sur toute la largeur.
- `quasi` : haut du cuissot, cuit lentement au beurre presque sans mouillement.
- `rouelle` : tranche en travers du cuissot, cuite comme le quasi.
- `escalope` : tranche fine prise de préférence dans le filet/contrefilet (100-110 g), aplatie, souvent panée et sautée vite.
- Règle : plus la coupe est fine, plus elle fond vite et parfume sans rester en bouche.

## Limites et garde-fous

- Escoffier sert à clarifier une logique culinaire, pas à imposer une cuisine de restaurant.
- Si une règle moderne de cuisson, d'assaisonnement ou de rattrapage suffit, il faut la garder prioritaire.
- Les noms classiques ne sont utiles que s'ils aident à décider.
- Une réponse domestique doit rester plus courte que la méthode d'origine.
- Un vocabulaire classique doit toujours être traduit en geste ou en fonction.

## Règle de traduction domestique

Les sauces et garnitures nommées servent à choisir une logique, pas à faire étalage de nomenclature.

En contexte domestique, toujours traduire en action simple :
- "Bordelaise" → réduction vin rouge + échalotes + beurre + moelle
- "Boulangère" → pommes de terre + oignons cuits autour de la viande
- "Financière" → quenelles + champignons + madère (simplifiable en champignons + madère si contexte léger)

Si l'utilisateur n'a pas demandé le nom classique, ne pas l'utiliser. Donner directement la description concrète.

## À ne pas faire

- réciter une recette Escoffier ;
- répondre avec un ton historique ;
- imposer des préparations longues si le contexte est domestique ;
- multiplier les sauces nommées sans expliquer leur logique ;
- utiliser Escoffier comme premier réflexe pour un plat simplement fade ;
- laisser une sauce couvrir le produit principal ;
- transformer le Gem en manuel classique ou en dictionnaire scolaire ;
- citer un nom de garniture sans le traduire en ingrédients concrets.

---

# Couche technique — méthodes, ratios, diagnostics

> Les sections ci-dessus restent la « grammaire de décision ». Les sections ci-dessous ajoutent la couche exécutable (ratios, méthodes mères, diagnostics et rattrapages). En contexte domestique, garder la réponse courte : donner d'abord le geste utile, le ratio seulement si l'utilisateur le demande. Les seuils sanitaires renvoient toujours au fichier sécurité (source de vérité unique).

## Techniques de base — sauces et liaisons

### Roux : ratio unique et cuisson douce, jamais feu vif
- Ratio Escoffier : ~600 g farine pour 500 g beurre (env. 6 farine pour 5 gras), pour les trois roux.
- La couleur (et donc le goût + le pouvoir liant) dépend du temps de cuisson :
  - Blanc : quelques minutes, sans coloration → béchamel, sauces blanches.
  - Blond : cuire très doucement, arrêter dès teinte légèrement blonde → veloutés.
  - Brun : cuisson plus longue à feu doux/four modéré jusqu'à couleur noisette claire → sauces brunes (espagnole) ; à préparer à l'avance.
- Cuire TOUJOURS doucement, jamais à feu vif : une chaleur trop forte racornit la farine et casse la liaison (sauce qui ne prend pas ou reste farineuse). Ne jamais brûler un roux brun (goût amer).
- Repère : plus le roux colore, plus il parfume mais moins il épaissit.
- Toujours cuire assez pour enlever le goût de farine crue avant de mouiller ; verser le lait/fond froid sur roux chaud (ou inverse) pour éviter les grumeaux.

### Beurre manié : liaison express et rattrapage d'une sauce trop liquide
- Beurre mou malaxé avec de la farine crue, ratio 100 beurre pour 75 farine (env. parts égales en pratique).
- Usage : lier vite une sauce déjà cuite ou trop liquide (matelote, sauce au vin, jus de gibier/poisson) → incorporer par parcelles dans le liquide frémissant, en fouettant, hors gros bouillon ; la sauce nappe en quelques secondes.
- Une fois lié au beurre manié, NE PLUS faire bouillir longtemps : risque de goût de farine crue.

### Liaison aux jaunes d'œufs : prendre comme une crème anglaise, ne jamais bouillir après
- Délayer les jaunes avec un peu de liquide FROID (fonds blanc, jus de champignons, crème selon la sauce) AVANT de les mélanger à la sauce/au potage.
- Verser hors gros bouillon, chauffer doucement « comme une crème anglaise » jusqu'à léger épaississement (nappe la spatule) — repère 82-85°C, jamais l'ébullition : si ça bout, les jaunes coagulent en grumeaux.
- Couper le feu dès que ça nappe.
- Finir au beurre frais hors feu juste avant de servir ; tamponner la surface d'un peu de beurre pour éviter la peau.
- Repère potage-velouté PAR LITRE : 3 jaunes + 1 dl crème, beurre 80 à 100 g/litre.
- Rattrapage si ça commence à grainer : retirer du feu aussitôt, fouetter vif, passer/mixer si besoin.
- Note : pour l'Allemande, la liaison se fait jaunes + fonds blanc + jus de champignons (PAS de crème ; la crème appartient à la Suprême/Normande) et elle prend l'ébullition.

### Vins, alcools et moutarde aromatiques : toujours hors du feu, en finition
- Madère, porto, cognac, vin de finition : ajouter HORS DU FEU, en toute fin. L'ébullition fait évaporer l'arôme du vin → on perd ce qu'on cherchait.
- Vaut pour toute sauce qu'on veut parfumer au vin (Madère, Porto, sauce au vin de finition).
- Toute sauce finie à la moutarde (Robert, charcutière, sauce moutarde) : incorporer la moutarde hors du feu, en toute fin ; une fois moutardée, la sauce ne doit plus bouillir (la moutarde tourne, devient amère).

### Béchamel : oignon clouté, temps de cuisson, et méthode express
- Base : roux blanc mouillé au lait + sel + un oignon piqué de clous de girofle (le retirer avant service), cuisson 20-25 min à feu doux (enlève le goût de farine, lisse la sauce). Ajouter le lait froid sur roux chaud (ou l'inverse) pour éviter les grumeaux.
- Méthode express : infuser dans le lait bouilli oignon émincé + thym + muscade + poivre, à couvert ~10 min, passer ce lait infusé sur le roux blanc, cuire 15-20 min seulement.
- Version maigre : garder les aromates, supprimer le veau de la version longue.
- Dérivés directs (déjà nommés ailleurs dans le fichier) : Mornay, Soubise, Crème.

### Sauce crème maison (béchamel + crème réduite + citron)
- À 1 L de béchamel, ajouter de la crème et réduire à la spatule jusqu'à ~3/4 L, passer, puis détendre avec un peu de crème crue fraîche + un demi-jus de citron.
- Le citron en fin relève et évite la lourdeur. → poissons bouillis, légumes, volaille, œufs.

## Émulsions — méthode, diagnostic et rattrapage

### Mayonnaise : méthode, causes d'échec, rattrapage
- Méthode : jaunes crus + sel, poivre, moutarde, pointe de cayenne, quelques gouttes de vinaigre ; incorporer l'huile goutte à goutte au début, puis en mince filet. Détendre de temps en temps avec un peu de vinaigre quand elle devient trop ferme. Tous les ingrédients à température ambiante. Saler dès le départ (le sel augmente le pouvoir liant des jaunes).
- 3 causes de mayo qui tranche : huile versée trop vite au départ, huile trop froide, trop d'huile par jaune.
- Limite : 1 jaune assimile env. 1,75 dl d'huile (2 dl si usage immédiat). Au-delà, elle tranche.
- NE PAS faire au froid ni sur glace (1re cause de décomposition) ; en hiver, tiédir légèrement l'huile.
- Rattraper une mayo tranchée : repartir d'un jaune neuf et réincorporer la mayo ratée goutte à goutte.
- Pour la garder en réserve : terminer par 3 cuillerées d'eau bouillante (pour 1 L) → assure la cohésion, prévient la décomposition.
- Variante simple : Chantilly = mayo + crème fouettée au moment de servir.
- **Sécurité** : mayonnaise maison = œuf cru. À consommer dans la journée, gardée au froid (≤4°C) ; œufs frais ou pasteurisés. Pour les publics fragiles, utiliser des œufs pasteurisés ou éviter. Voir fichier sécurité.

### Aïoli et rouille : émulsions à l'ail
- Aïoli (froid, pour légumes, poisson poché, œufs durs) : broyer l'ail au mortier avec une pomme de terre en robe des champs épluchée et CHAUDE, ajouter jaunes + sel + poivre + jus de citron, monter lentement au pilon, huile goutte à goutte. La pomme de terre chaude assouplit l'ail et stabilise l'émulsion. (Même précaution œuf cru que la mayonnaise.)
- Rouille (pour soupe/bouillon de poisson) : piler ail + 1 piment rouge, ajouter gros comme une noix de mie de pain trempée et pressée, monter à l'huile d'olive comme un aïoli, puis détendre avec quelques cuillerées de bouillon de poisson chaud. Se sert sur du pain dans la soupe de poisson.

### Hollandaise / Béarnaise : feu doux, montage, mousseline, rattrapage
- C'est une émulsion tiède (« mayonnaise au beurre ») : inutile et risqué de la servir très chaude. Trop chauffée, elle tranche.
- Monter à feu TRÈS doux / bain-marie tiède : la liaison vient de la cuisson progressive des jaunes (réduction poivre + vinaigre presque à sec, jaunes, puis beurre frais/fondu incorporé peu à peu).
- Alléger en montant avec quelques cuillerées d'eau ajoutées par petites parties.
- Mousseline (= mousseuse) : hollandaise fouettée en incorporant de l'eau (ou crème fouettée / blancs en neige en fin) pour l'aérer → plus légère.
- Rattraper une sauce tranchée/trop chaude : ajouter quelques gouttes d'eau froide et refouetter.
- Tenir au chaud seulement tiède (bain-marie), sinon elle se décompose.
- **Sécurité** : sauce à base d'œuf maintenue tiède = zone de compromis (ni assez chaude pour être sûre dans la durée, ni stable longtemps). La servir rapidement ; ne pas la garder en zone tiède (entre 4°C et ~63°C) pendant des heures (risque microbien sur base d'œuf). Voir fichier sécurité.
- Dérivés non encore listés : Maltaise (jus + zeste d'orange), Moutarde (+ moutarde).

## Règles de sécurité texture

### Ne jamais faire bouillir : jaunes, sang, foies, abats sautés, viande déjà cuite
Principe transversal : une fois l'élément fragile incorporé à la sauce, plus d'ébullition.
- Liaison aux jaunes (allemande, poulette, potages veloutés) : pocher sans bouillir, sinon grumeaux.
- Sang (civet, grand-veneur) et purée de foie (rouennaise) : incorporer hors gros bouillon, pocher sur le côté du feu sans ébullition (sinon ça granule/caille instantanément).
- Abats sautés (rognon, cœur de veau, foie) : saisir vif, garder rosé, égoutter ; une fois dans la sauce, aucune ébullition (l'abat durcit immédiatement). Réchauffer doucement, finir au beurre hors feu (50-60 g pour une portion de rognon).
- Émincés et hachis de viande déjà cuite (rôti, braisé), capilotade : réchauffer en sauce à feu doux, jamais à ébullition, sinon la viande sèche et durcit.

> **Précision sécurité (texture ≠ sanitaire)** : « garder rosé » est un choix de texture sur les abats et la viande rouge en pièce, pas une garantie sanitaire. Pour la volaille, les hachés et les farces, l'aspect/le toucher ne garantissent rien : se fier au thermomètre (volaille 74°C à cœur, viande rouge hachée 71°C, bœuf/agneau en pièce 63°C + 3 min de repos, porc 63°C + 3 min). Voir fichier sécurité.

## Potages — méthodes et ratios

### Crème de légumes : la méthode mère
Une crème de légumes se construit toujours pareil, quel que soit le légume :
- Cuire/étuver le légume, le réduire en purée, l'incorporer à une béchamel un peu claire.
- Cuire doucement ensemble 7-10 min, mixer fin (passer au tamis si besoin).
- Détendre à la consistance voulue avec un peu de bouillon ou de lait.
- Crémer SEULEMENT au moment de servir, sans laisser bouillir.
Marche pour champignons, asperges, laitue, cresson, poireaux, maïs, carotte, etc. : on change le légume dominant.

### Crème vs Velouté : la différence concrète + finition
- Crème : base liée à la béchamel (lait), finie à la crème. Plus douce, plus lactée.
- Velouté : base liée au fond/roux, finie d'une liaison jaunes + crème + beurre. Plus fin, plus « sauce ».
- Même légume, deux rendus.
- Finition (les deux) : la crème et le beurre s'ajoutent au moment de servir, sur potage chaud, SANS faire bouillir (sinon ça tranche / perd sa rondeur). Si le potage est déjà lié aux jaunes, ne pas re-bouillir.

### Potage lié : diagnostic de consistance
- Le dosage de l'élément liant (riz, tapioca, semoule, fécule, purée de légume) décide tout.
- Trop épais → pâteux, colle en bouche → détendre au bouillon ou lait bouillant.
- Trop clair → fade et plat → resserrer (réduire) ou ajouter de la purée.
- Viser une consistance de crème qui nappe la cuillère sans coller : c'est la consistance, pas la quantité d'aromates, qui fait le corps d'un potage lié.

### Soupes de légumes : étuver au beurre, ratio, garder le vert
- Étuver doucement et assez longuement les légumes émincés au beurre AVANT de mouiller : fait sortir l'eau de végétation et imprègne le beurre de l'arôme → goût plus profond. (Exception : légumes verts/délicats qu'on veut garder frais → direct au mouillement.)
- Ratio repère (paysanne) : ~600 g de légumes crus pour 1,5 L de liquide ; ~500 g si on ajoute une garniture qui gonfle (pâtes, riz, vermicelle). Cadre, pas pesée stricte.
- Garder un légume vert (pois, haricots verts, cresson, oseille) bien vert : cuisson courte et vive « à l'anglaise » (eau bouillante salée, à découvert), mixer/ajouter tard. Arbitrage : couleur = cuisson courte et vive ; profondeur de goût = étuvage lent.
- La paysanne est la matrice : tous légumes de saison, émincés en paysanne, étuvés au beurre puis cuits, pommes de terre ajoutées ensuite.

### Soupes de poisson : à faire vite et servir aussitôt
- Toute soupe/velouté à base de poisson ou mouillée au fumet se prépare au dernier moment : l'attente décompose le goût.
- Repère : ne lancer une soupe de poisson qu'environ 30 min avant de servir ; pas de réchauffage long ni de maintien au chaud prolongé.

## Potages — recettes de référence

### Soupe à l'oignon gratinée (méthode maison)
Base (~2 L) :
- Faire revenir 250 g d'oignon finement émincé au beurre ; à mi-coloration, singer de 25 g de farine, cuire jusqu'à roux blond ; mouiller de 2 L de bouillon, cuire 10 min. Option : remplacer un peu de bouillon par du lait (1 dl/L) pour adoucir.
- Gratin : rondelles de pain (flûte) sur le potage, fromage râpé, gratiner vif.
- Variante express (sans roux) : oignon fondu au beurre, mouillé, cuit 10 min, passé en pressant l'oignon ; pain + fromage, beurre fondu, gratiner et servir aussitôt.

### Soupes poireaux-pommes de terre, cresson, cultivateur
- Bonne-femme (poireaux-pdt) : blanc de 5 poireaux émincé sué au beurre, mouiller 1,75 L eau tiède/bouillon, 500 g pommes de terre finement émincées, saler (15 g si mouillé à l'eau), cuire doux, finir ~75 g beurre. Mixer pour une velouté ou laisser rustique.
- Cultivateur : ~400 g brunoise grossière (carotte, navet, blanc de poireau, oignon) étuvée au beurre, mouiller ~1,5 L bouillon ; à mi-cuisson, 2 petites pdt émincées + 125 g lard de poitrine maigre en lardons bien blanchis (le lard porte le goût).
- Cresson (façon Parmentier) : 500 g pdt en quartiers cuites vif à l'eau salée, écraser au fouet, + 1,5 L lait bouilli + 15 g sel + 100 g cresson effeuillé, cuire 5-6 min seulement, monter au beurre (100 g) hors feu + cerfeuil. Même logique pour épinards, chicorée, ortie.

### Potage Germiny (oseille) et soupes à l'ail provençales
- Germiny : faire fondre 250 g d'oseille ciselée au beurre, mouiller 1,5 L bouillon ; au moment, liaison de 10 jaunes + 2,5 dl crème prise sur le feu comme une crème anglaise (sans bouillir, ~82-85°C), puis 150 g beurre + cerfeuil hors feu. L'oseille apporte l'acidité (inutile d'ajouter du citron).
- Aïgo bouido : 2 L d'eau, 25 g sel, 12 gousses d'ail écrasées, brin de sauge, 1 dl huile d'olive, pincée de poivre ; bouillir 7-8 min ; verser sur des tranches de pain, persil. Variante aux œufs pochés : bouillir l'eau 15 min avec ail/huile/thym/laurier/sauge, pocher 1 œuf par personne dans le bouillon, dresser sur pain et arroser.

### Garbure, potée et purées de légumes secs
- Garbure (potage) : réduire une purée de légume bien serrée, en masquer des tranches de pain séchées/frites, saupoudrer de fromage, gratiner, puis mitonner avec du bouillon. N'importe quelle purée convient (oignon, Crécy, courge, marrons) ; prend le nom de l'ingrédient dominant. Idée : recycler un reste de purée en soupe gratinée rustique.
- Potée / soupe-pot : viandes salées/fumées (lard, jambon, petit salé, confit) départ à l'eau FROIDE, saler très peu (la salaison sale déjà le bouillon) ; légumes rustiques ajoutés en cours ; cuisson très douce ~3 h ; service en deux temps (bouillon sur pain, viandes + légumes à part).
- Purée de légumineuses (haricots blancs, lentilles, pois cassés) : cuire avec la garniture aromatique (oignon, carotte, lard, bouquet), égoutter, retirer la garniture, piler/mixer, alléger avec une partie de la cuisson (ne pas la jeter), passer, mettre au point bouillon + un peu de lait, beurrer ~125 g/litre.

## Bases dérivées et finitions

### Glace de viande maison : fond réduit en sirop
- Glace = fond brun (ou de volaille/gibier) réduit lentement jusqu'à consistance sirupeuse qui nappe la cuiller.
- Réduire à feu décroissant (vif au début, très doux en fin), en écumant, en transvasant dans des casseroles de plus en plus petites.
- Usage maison : 1 cuillerée pour corser une sauce trop faible, ou napper une viande d'une couche brillante, ou fondue dans un beurre. C'est un appoint : il précise une base juste, il ne sauve pas une sauce fade.
- Fond de veau ordinaire à la place du fond brun → glace plus blonde et légère.

### Dépouiller : pourquoi écumer, et repère
- Pendant la cuisson lente d'une sauce/fond/potage lié au roux, écumer souvent la mousse et le gras qui remontent.
- Effet : élimine roux et graisse en excès → sauce nette, lisse, non farineuse, plus digeste.
- Repère : plus le fond de départ est bon, plus le dépouillement est rapide. (Toutes les purées ne se dépouillent pas.)

### Jus lié maison (sans roux) : fond réduit + amidon
- Alternative légère à la sauce brune : réduire un bon fond de veau/volaille des 3/4 puis lier à froid avec un peu d'arrow-root ou fécule délayé (~30 g pour 1 L de jus fini).
- Avantage maison : liaison nette et rapide, sans long dépouillement de roux ; le jus garde un goût franc.
- Repère : un jus lié doit rester d'abord un jus (limpide, brun clair), pas une sauce épaisse.

### Sauce de déglaçage minute (vin + échalote + base + beurre)
- Trame commune (grillade/poêlée) : réduire fortement vin (rouge ou blanc) + échalote hachée (des 3/4), ajouter un peu de jus/fond, dépouiller ~15 min, monter au beurre hors feu, finir au citron.
- C'est la trame de la bordelaise, marchand de vin, sauce au vin : vin réduit + échalote + base + beurre.
- Bordelaise maison = ce schéma + moelle de bœuf pochée en dés (facultative).

### Purée de tomate au four pour casser l'acidité
- Pour casser l'acidité d'une purée/concentré de tomate avant de l'ajouter à une sauce : la passer au four jusqu'à teinte presque brune. Effet : détruit l'acidité, donne un ton plus chaud, aide la sauce à rester nette.
- Variante minute : une pincée de sucre dans une sauce tomate trop acide (repère : la sauce tomate Escoffier contient 30 g de sucre pour 5 L).

### Essences : souvent inutiles si le fond est bon
- Une « essence » n'est qu'un fond très peu mouillé, donc très concentré → inutile si le fond de base est déjà savoureux.
- Pour booster un plat, mieux vaut ajouter le produit lui-même (céleri, champignons, morilles) directement dans le fond pendant la cuisson, plutôt que de faire un extrait à part. Neuf fois sur dix, c'est préférable.

## Beurres composés

### Beurres composés maison : répertoire d'aromatisation rapide
Un beurre composé = beurre pommade + un élément parfumant ; sert à finir une sauce, napper une grillade/un poisson chaud, ou tartiner. Poser une noix sur la pièce chaude au moment de servir : il fond et fait sauce.
- Maître d'hôtel : beurre + persil haché + sel + poivre + jus de citron (repère : 250 g beurre, 1/4 citron). → grillades, poissons.
- Marchand de vin : réduction vin rouge + échalote, mélangée à beurre + glace de viande + persil + citron. → entrecôte grillée.
- Meunière : beurre cuit noisette + quelques gouttes de citron, versé sur le poisson.
- Noisette : beurre cuit jusqu'à belle couleur blonde.
- Beurre noir : beurre cuit jusqu'à couleur brune, fini au vinaigre réduit, servi avec persil frit + câpres (raie, cervelle).
- Beurres d'ail / d'estragon / d'herbe : blanchir fortement l'aromate, piler avec le beurre, passer.
- Beurre d'anchois : piler les filets SANS blanchir + beurre, passer. (Contrairement aux beurres d'ail/estragon/herbe, l'anchois ne se blanchit pas.)
- Beurre d'escargots : échalote + ail + persil + sel/poivre pétris au beurre (+ un peu d'alcool).

## Sauces minute et régionales

### Vraie sauce provençale = fondue de tomates
- La « provençale » authentique (bourgeoise) est une simple fondue de tomates : tomates pelées/pressées/épépinées/concassées fondues doucement à l'huile + ail écrasé + sel, poivre, pincée de sucre + persil, à couvert ~30 min.
- Pas une sauce compliquée : une base tomate-ail-huile pour poisson, œufs, viandes du Sud.
- Note : à distinguer de la GARNITURE Provençale du fichier (tomates au four + champignons farcis).

### Sauce curry maison (base + lait de coco optionnel)
- Faire revenir oignon (+ céleri, racine de persil) au beurre, singer de farine + poudre de curry, cuire sans colorer, mouiller de bouillon blanc, cuire doux ~45 min, passer, dégraisser.
- Option : ajouter du lait de coco (jusqu'à 1/4 du mouillement), ou un trait de crème + citron en fin.
- Doser le curry pour le goût européen (le mélange indien pur est jugé trop fort). → poissons, crustacés, volaille, œufs ; servir avec un riz.

### Sauce Smitane (crème aigre) pour gibier/volaille sautés
- Oignon haché revenu au beurre, mouillé de vin blanc réduit à fond, + crème aigre, frémir 5 min, passer, garder une pointe acidulée (citron si besoin). → gibiers sautés ou à la casserole.

## Sauces anglaises et accompagnements de rôtis

### Sauces anglaises simples pour rôtis (pain, pomme, airelles, menthe)
- Sauce au pain (bread sauce) : lait + mie de pain frais + oignon piqué d'un clou de girofle + beurre, cuit 15 min, fini d'un peu de crème. → volaille et gibier à plume rôtis.
- Sauce aux pommes : marmelade de pommes peu sucrée + pointe de cannelle, servie tiède. → canard, oie, porc rôtis.
- Sauce aux airelles (cranberries) : baies cuites, passées, sucrées au goût. → dinde rôtie.
- Sauce menthe : menthe hachée + sucre + vinaigre + eau. → agneau chaud ou froid.

## Marinades

### Marinades : choisir selon le délai, bannir le vinaigre pur sur viande tendre
- Ne PAS mariner viandes de boucherie / gibier tendre dans du vinaigre pur : son action corrode et détruit la saveur. Le vinaigre seul est réservé aux venaisons coriaces (sanglier, cerf, renne).
- Marinade crue équilibrée : carottes, oignons, échalotes, céleri + ail + persil + thym + laurier + poivre + clous de girofle ; mouiller moitié vin (blanc ou rouge) > 1/4 vinaigre + 1/4 huile (repère ~1,25 L vin / 0,5 L vinaigre). Genièvre/romarin pour le gros gibier ; écorce d'orange pour la provençale.
- Marinade CUITE : mêmes aromates revenus à l'huile, mouillés vin + vinaigre, cuire 30 min ; imprègne plus vite, mais TOUJOURS la verser FROIDE sur la pièce.
- Marinade instantanée (grillades) : échalote émincée + queues de persil, thym, laurier + sel + poivre ; arroser d'huile + jus de citron (1/2 citron par cuillerée d'huile) ; retourner souvent, cuire de suite.
- Conservation : au frais (≤4°C) ; en été, faire bouillir la marinade tous les 2 jours. Une marinade ayant été en contact avec de la viande crue ne se sert jamais crue : la cuire avant usage. Voir fichier sécurité.
- Une viande pochée prend mieux la marinade qu'une rôtie (chair plus poreuse).

## Poisson — cuissons et méthodes

### Trois court-bouillons selon le produit + dosage acidulé
- (A) Aromates + vin (rouge ou blanc) + fumet de poisson → matelotes.
- (B) Eau salée + lait + jus de citron → poissons de mer à chair blanche (le lait garde la chair blanche).
- (C) Eau salée + vinaigre + aromates → crustacés, saumons, truites, poissons de rivière.
- Court-bouillon acidulé repère : ~12 g de sel + 2 dl de vinaigre par litre d'eau (raffermit la chair, facilite le retrait de la peau juste après cuisson).
- Geste : pocher frémissant (jamais à gros bouillons) ; souvent, laisser refroidir le poisson dans sa cuisson pour qu'il reste moelleux.

> **Sécurité poisson** : la cible sanitaire est 63°C à cœur (repère de secours sans thermomètre : chair opaque qui s'effeuille). Les cibles texture plus basses (50-55°C, « mi-cuit ») relèvent du CONFORT et sont déconseillées aux publics fragiles. Tout poisson destiné à être consommé CRU ou peu cuit maison (tartare, gravlax, carpaccio, sushi) doit être congelé préventivement avant : −20°C pendant 7 jours, OU −35°C jusqu'à solidification puis −35°C pendant 15 h (à confirmer), OU −35°C jusqu'à solide puis −20°C pendant 24 h. Le sel et le sucre (gravlax) ne tuent PAS l'anisakis. Voir fichier sécurité.

### Poisson au vin blanc en plat (Bercy/Bonne-femme), sur le plat, gratin
- Bercy/Bonne-femme : semer au fond d'un plat beurré échalote hachée (Bercy) ou échalote + champignons crus émincés + persil (Bonne-femme) ; coucher le poisson, mouiller vin blanc + fumet en ajoutant ~15 g de beurre par dl de mouillement ; cuire au four en arrosant, en réglant pour que la réduction quasi complète coïncide avec la cuisson ; réduire/monter au beurre le fond restant, napper, glacer vivement, finir citron + persil. Le liquide de cuisson EST la sauce.
- Sur le plat : détacher légèrement les filets de l'arête, noisette de beurre sous chacun, mouiller d'1 dl de cuisson (ou vin + glace de viande) + filet de citron, cuire au four en arrosant jusqu'à réduction en sirop qui nappe d'une couche translucide légèrement glacée.
- Gratin : régler la chaleur pour que réduction de la sauce + cuisson du poisson + coloration du gratin se fassent EN MÊME TEMPS (four vif pour petits poissons, modéré pour gros). Erreur classique : gratin coloré mais poisson cru, ou poisson sec parce qu'on a attendu le gratin.

### Poisson au beurre noir/noisette : ordre des gestes
1. Pocher, égoutter, retirer la peau, sécher un instant sur le plat de service.
2. Saupoudrer de persil concassé, arroser d'un filet de jus de citron.
3. Couvrir du beurre cuit noisette (ou plus poussé « noir »), ~200 g pour un service.
- Citron + persil AVANT le beurre brûlant (il les saisit). Variante « à la portière » : finir d'un filet de vinaigre passé dans la poêle brûlante.

### Morue salée et brandade
- Morue salée : bien dessaler à l'eau froide, couper en gros carrés, pocher seulement ~8 min comptées dès que l'ébullition se prononce (la vouloir « vert cuite », pas desséchée), égoutter aussitôt, retirer peaux et arêtes, effeuiller chaud. Trop longtemps = chair sèche.
- Brandade : partir de morue vert cuite effeuillée ; chauffer ~2,5 dl d'huile jusqu'à ce qu'elle fume, y jeter morue + 1 gousse d'ail écrasée, travailler sur le feu jusqu'à pâte fine ; hors feu, absorber 5 à 6 dl d'huile en mince filet sans cesser de remuer, en « cassant » la pâte avec quelques cuillerées de lait bouillant (jusqu'à ~2,5 dl en tout). Version crème : remplacer huile + lait par ~7,5 dl de crème, cuillerée par cuillerée. Fini très blanc, consistance d'une purée de pommes de terre ; rectifier le sel en dernier.

### Friture de petits poissons et cuisson au bleu
- Friture (éperlans, blanchaille, nonats) : rouler dans beaucoup de farine, secouer dans un tamis pour faire tomber l'excédent (l'excès empâte), plonger par petites quantités dans une friture TRÈS chaude (fumante), ~1 min pour les plus petits, égoutter sur linge, saler fin, servir tout de suite.
- Au bleu (truite, carpe, brochet) : réservé au poisson vivant/ultra-frais (limon naturel intact). Court-bouillon fortement vinaigré déjà bouillant ; assommer, vider/nettoyer vite sans rincer ni frotter la peau ; plonger dans le liquide bouillant (la peau vire au bleu, le poisson se recroqueville) ; petite truite ~150 g : quelques minutes. Repli domestique : sinon, meunière ou pochage classique.

### Haddock, rouget, raie
- Haddock (églefin fumé) : plonger dans le liquide bouillant légèrement salé (eau OU lait), finir sur le côté du feu à couvert, court mouillement ; ~15 min pour 750 g. Le lait adoucit le côté fumé/salé.
- Rouget : mieux grillé ou sauté que poché ; dépourvu de fiel → retirer seulement les ouïes sans le vider, garder le foie ; foie écrasé monté au beurre pour la sauce.
- Raie : pocher à l'eau salée (~12 g/L) acidulée de 2 dl vinaigre/L ; aussitôt cuite, égoutter pour retirer la peau ; si elle doit attendre, la remettre dans sa cuisson passée (évite qu'elle sèche).

### Saumon/truite froids, mousses et farces de poisson
- Saumon/truite froids : cuire de préférence la pièce entière ou en gros tronçons et laisser refroidir dans le court-bouillon (chair moelleuse). Les tranches cuites à part sont plus jolies mais plus sèches. Refroidir dans le liquide, jamais à l'air.
- Mousses froides (poisson, légume) : n'incorporer la crème qu'à DEMI fouettée (entièrement montée = mousse sèche et « cotonneuse » ; à demi fouettée = onctueuse et fraîche).
- Farce d'un poisson au goût très marqué (éperlan) : ne mettre que 1/3 de sa chair, 2/3 de poisson neutre (sole, dorée) → goût équilibré + farce qui absorbe plus de crème (plus légère).

### Bouillabaisse : ordre des poissons et rôle du poisson blanc
- Poissons à chair ferme au départ, dans le bouillon aromatique (huile d'olive, oignon, tomate, ail, safran, fenouil/laurier).
- Poissons à chair tendre (merlan, rouget) ajoutés seulement après 7-8 min d'ébullition (sinon ils se défont).
- Cuire à grand feu, à découvert (l'huile s'émulsionne avec le bouillon).
- Un poisson blanc (type merlan) est nécessaire : sa chair assure la liaison du bouillon.
- Service : bouillon versé sur des tranches de pain, poissons à part.

## Poisson — accompagnements

### Sauces qui accompagnent saumon/brochet au court-bouillon
Un gros poisson poché appelle une sauce relevée et nette, servie à part (souvent deux sauces ensemble), pas une sauce lourde qui couvre :
- Saumon : anchois, câpres, crevettes, génevoise, hollandaise, homard, huîtres, mousseline, nantua, noisette, ravigote, vénitienne.
- Brochet : câpres, génevoise, hollandaise, huîtres, ravigote, vénitienne.
- Accompagnement quasi systématique : pommes de terre à l'anglaise (vapeur/eau).

### Garnitures meunière minute + Colbert/Richelieu
- Une sole/poisson « meunière » s'enrichit de garnitures posées au tout dernier moment (sinon elles ramollissent) : aubergines en rondelles de 7-8 mm farinées et frites au beurre clarifié ; cèpes/morilles escalopés sautés minute ; grains de muscat pelés tenus froids ; rondelles/quartiers d'orange pelés à vif. Arroser de beurre noisette et servir immédiatement.
- Colbert / Richelieu : poisson plat ouvert sur le dos, désarêté, pané à l'anglaise et frit, cavité garnie au moment. Colbert = beurre maître d'hôtel ; Richelieu = Colbert + lames de truffe sur le beurre.

## Viandes — choix du morceau et cuissons

### Choix du morceau de bœuf selon la cuisson
- Bouilli / pot-au-feu et braisés : pointe de culotte (le meilleur), plat-de-côte, poitrine, paleron.
- Braisés et daubes : paleron, culotte, gîte à la noix.
- Limiter les pièces à braiser/bouillir à 3-4 kg max, détaillées plutôt en longueur qu'en épaisseur (cuisson régulière).
- Le rognon de bœuf ne s'emploie que sauté (jamais bouilli).
- Braisé à sauce liée en gelée (bœuf mode, queue de bœuf) : ajouter pieds de veau désossés et blanchis au mouillement → la gélatine lie sans roux et fige à froid.

### Repères de cuisson à l'eau (viandes salées et abats)
Toujours tremper longuement les pièces salées avant cuisson :
- Bœuf salé/fumé : 30 min par kilo, à grande eau.
- Langue de bœuf salée : 2h30 à 3h selon grosseur.
- Gras-double cru : 5h à l'eau salée en légère ébullition.
- Museau de bœuf : 6h min, eau salée et acidulée.
- Palais de bœuf : 4h min dans un blanc léger.
- Foie de veau poché entier : 30 min/kg (eau salée 8 g/L), refroidir dans l'eau froide, trancher très mince au moment de servir.
- Cuire « dans un blanc » (eau + farine délayée + jus de citron) = abats (tête, pieds, ris) et légumes qui s'oxydent (salsifis, cardons, fonds d'artichauts), pour garder une chair blanche et brillante. Exception : pieds de porc → fond d'aromates.

## Viandes — mijotés et braisés

### Mijotés longs : luter, durées, et mise au point de la sauce
- Anti-dessèchement (tripes, daube au four irrégulier) : couvrir la surface de graisse, luter le couvercle avec une pâte simple (farine + eau) en laissant un petit trou pour la vapeur. Inutile avec une cocotte qui ferme bien et un four doux régulier.
- Daube/estouffade : viande en gros morceaux ; mariner 2h au vin (rouge pour daube simple, blanc pour provençale) ; éponger, colorer ; ranger en couches (couennes blanchies, lardons, carottes, oignons, tomates, ail, herbes) ; mouiller à la marinade, couvrir/luter. Four doux : daube simple 4h, provençale 6-7h, estouffade 2h30-3h. Astuce provençale : écorce d'orange séchée dans le bouquet.
- Tripes mode de Caen : pieds de BŒUF (gélatine), pas de veau (sinon le fond lie mal).
- Mise au point de la sauce avant de servir : laisser reposer 15 min, dégraisser ; trop claire → réduire ; trop épaisse → détendre avec un peu de fond ; repasser sur la viande, mijoter encore 15 min.

### Carbonade flamande et goulash : équilibre amertume/paprika
- Carbonade flamande : bœuf maigre en escalopes minces coloré vif ; oignons colorés à part (~5 gros oignons / 1,2 kg viande) ; couches viande/oignons, bouquet ; déglacer à la bière (1 bouteille) + autant de fond brun, lier au roux brun ; corriger avec ~50 g de cassonade/sucre (contre l'amertume de la bière) ; four doux à couvert 2h30-3h.
- Goulash : la valeur dépend du paprika (doux, très parfumé, fortement coloré). Bœuf en gros morceaux revenu au saindoux avec oignons jusqu'à blonds ; sel + ~1/2 c. à café de paprika pour ~1,2 kg, tomates pelées + un peu d'eau ; four doux 1h30, ajouter pdt en quartiers, finir jusqu'à réduction complète.

## Viandes — recyclage de desserte

### Émincé, hachis, Parmentier, fricadelles, hash
- Émincé = tranches très minces de viande rôtie, couvertes d'une sauce/garniture bouillante. Hachis (sens culinaire) = fin salpicon (petits dés), pas viande hachée fin ; lier ~2,5 dl de demi-glace par kilo. Règle commune : la viande déjà cuite ne BOUT JAMAIS dans la sauce (réchauffer doucement). Pour une sauce à réduction de vinaigre, border le plat de cornichons.
- Hachis Parmentier : pulpe de pdt cuite au four, écrasée et sautée au beurre (façon pomme Macaire), mélangée à parts égales avec viande en tout petits dés + oignon fondu + persil + filet de vinaigre ; humecter de sauce lyonnaise ou purée légère (la viande ne bout pas) ; gratiner ~10 min. Logique gratin : hachis lié d'une sauce, toujours recouvert (purée, chapelure, fromage). Moussaka = même hachis entouré de lames d'aubergines sautées/frites.
- Fricadelles/bitoks : viande hachée + mie de pain trempée au lait et pressée + oignon REVENU au beurre + œuf cru (si besoin) ; assaisonner (sel, poivre, muscade) ; disques épais, sauter au beurre clarifié. Avec viande cuite : remplacer une part par de la purée (repère : 1 kg viande cuite + 400 g purée + 2 oignons fondus + 2 œufs). Servir avec purée de légumes + sauce relevée (piquante, Robert).
- Corned beef hash : moitié pulpe de pdt cuite au four écrasée + moitié viande hachée + oignon revenu au beurre ; galette ronde, sauter au beurre clarifié des deux côtés, 15-20 min.

> **Sécurité (recyclage de desserte)** : un plat à base de viande déjà cuite doit avoir été refroidi rapidement (60→21°C en ≤2h, puis 21→4°C en ≤4h) et conservé au froid (≤4°C). Au réchauffage, même si la règle culinaire dit « ne pas faire bouillir » (texture), il faut remonter à cœur à 63°C minimum pour la sécurité. Les fricadelles/boulettes à base de VIANDE HACHÉE CRUE se cuisent à cœur : haché rouge 71°C, tout mélange contenant de la volaille 74°C. Voir fichier sécurité.

## Abats — préparations

### Rognon, foie, ris de veau, cervelle, fraise
- Rognon de bœuf (moins fort) : dénerver/dégraisser, détailler en lames pas trop minces ; saisir vif au beurre rosé, verser en passoire, laisser égoutter le sang (odeur alcaline) et le jeter ; déglacer (vin, madère, jus de champignons), réduire, remettre le rognon sans bouillir.
- Foie de veau sauté : tranches ~110 g, assaisonner, fariner (sèche la surface = belle coloration), sauter au beurre (ou beurre + huile), déglacer ; lyonnaise = oignons fondus à part + filet de vinaigre dans la poêle brûlante. Éviter la surcuisson.
- Ris de veau : choisir bien blancs ; dégorger longuement à l'eau froide ; blanchir juste pour raffermir l'épiderme, rafraîchir ; retirer cartilages/nerfs, presser entre deux linges ; puis braiser/pocher au fond blanc/griller. La « noix » est plus fine que la « gorge ».
- Cervelle : pocher d'abord, puis escaloper et finir (panée-sautée, beurre noisette, gratin Mornay).
- Fraise de veau : dégorger, blanchir, rafraîchir, cuire dans un « blanc » comme la tête de veau ; toujours servir brûlante avec un accompagnement relevé (poulette, ravigote, gribiche).

## Veau — règles de cuisson par morceau

### Quel morceau de veau pour quelle cuisson
- Médaillons, noisettes, escalopes (filet, contrefilet) : toujours SAUTÉS — le braisage les durcit et les sèche.
- Noix, fricandeau, grenadins : le braisage convient le mieux (fricandeau toujours piqué et braisé).
- Quasi et rouelle : cuisson lente au beurre, à la casserole, presque sans mouillement, en retournant souvent.
- Tendron : plutôt étuvé au beurre puis court-mouillement arrosé souvent, que braisé sec.
- Côte de veau : préférer le sauté au grillé ; déglacer IMPÉRATIVEMENT la poêle (vin blanc, madère…), le déglaçage réduit rejoint la sauce ; accompagner de glace de veau blonde (ou demi-glace beurrée) montée au beurre.

## Veau — préparations

### Panures (viennoise/milanaise), Pojarski, osso-buco, poitrine farcie
- Panures (côte/escalope aplatie mince) : viennoise = pané à l'anglaise, cuit doucement au beurre clarifié, garni citron + câpres + œuf dur ; milanaise = panure à l'anglaise avec mie fine MÉLANGÉE de parmesan, sauté au beurre clarifié. Toujours beurre CLARIFIÉ (ne brûle pas), cuisson douce.
- Pojarski (côte moelleuse reformée) : détacher la chair, dénerver, hacher avec 1/4 de son poids de beurre + autant de mie trempée pressée, reformer le long de l'os, cuire au beurre clarifié.
- Osso-buco : rouelles de jarret de 5-6 cm farinées, colorées ; oignons + tomates concassées (~1 kg/kg) + vin blanc réduit des 2/3 ; mouiller à mi-hauteur au fond blanc, bouquet, ~1h30 (fond réduit à point) ; finir citron + persil.
- Poitrine de veau farcie : désosser, farcir (chair à saucisse fine + duxelles sèche + beurre + herbes + 1 œuf), braiser doux à court-mouillement, four doux soutenu ; 3h30 à 4h pour 5 kg.

## Volaille — découpe et cuissons

### Découper et sauter un poulet ; le déglaçage des sautés
- Découpe : lever les cuisses (partager chacune en haut de cuisse + pilon), puis les ailes, séparer la poitrine de la carcasse.
- Sauté : ranger les morceaux assaisonnés dans un plat beurré, colorer une face puis l'autre ; sortir d'abord poitrine et ailes (cuisson plus rapide), laisser cuire plus longtemps cuisses et pilons.
- Règle générale des sautés (viande/volaille) : ne pas jeter les sucs ; déglacer (vin blanc/rouge, madère, cognac), réduire, ajouter à la sauce ou en faire la sauce. Le déglaçage distingue un sauté goûteux d'une viande simplement poêlée.
- Différence Fricassée / Blanquette : fricassée = l'élément cuit DIRECTEMENT dans la sauce ; blanquette = élément poché à part puis lié. Finition (les deux) : lier au dernier moment, hors gros feu, jaunes + crème + beurre, ne plus bouillir.

> **Sécurité volaille** : la volaille (entière, morceaux, hachée ou en farce) se cuit à 74°C à cœur. « Cuisses plus longtemps que poitrine » est un repère de texture ; le contrôle final reste le thermomètre, pas le jus clair ni le toucher. Voir fichier sécurité.

### Griller une volaille (crapaudine/diable), en cocotte, normande
- Crapaudine = ouvrir une petite volaille (poussin, pigeon, poulet) pour la griller à plat : inciser des deux côtés depuis la naissance des ailes jusqu'au bréchet (ou fendre le dos), aplatir, assaisonner. Méthode sûre : arroser de beurre fondu, cuire À MOITIÉ au four, finir doucement sur le gril (le four cuit le cœur, le gril donne croûte et couleur). Variante Diable : à mi-cuisson, enduire de moutarde + cayenne, paner de mie, ré-arroser de beurre, finir au gril ; sauce relevée à part.
- En cocotte (Bonne-femme) : colorer au beurre, cuire à couvert, garnir lardons + petits oignons (option champignons/pdt cocotte) ; flamber au cognac, déglacer d'une goutte de jus lié en grattant les sucs ; servir dans la cocotte.
- Normande (volaille, gibier à plume) : pommes-fruits émincées sautées au beurre, en cocotte couche pommes / pièce / couche pommes, déglacer à la crème, finir vivement (gras + sucre adoucissent une chair sèche/puissante ; trait de Calvados possible).

## Volaille — préparations

### Pilaf tout-en-un, capilotade, soufflé de volaille, farce aux marrons
- Pilaf de volaille (une cocotte) : faire revenir le poulet découpé au beurre, ajouter le riz passé au beurre + oignon haché + laurier + 2 tomates concassées, mouiller au bouillon « un peu plus qu'à couvert », four bien chaud ~25 min (poulet + riz cuits, riz à sec) ; détendre d'un filet de jus, mélanger À LA FOURCHETTE. Repère : ~100 g riz cru / poulet. (Cible volaille 74°C à cœur.)
- Capilotade : recycler une volaille cuite désossée en fines escalopes dans une sauce (tomate/italienne ou demi-glace) + champignons ; CHAUFFER SANS BOUILLIR (texture), mais remonter à 63°C à cœur pour la sécurité d'un reste.
- Soufflé de volaille : base ~500 g blanc pilé + 6 c. béchamel froide passé au tamis + 50 g beurre + 5 jaunes + 6 blancs montés ferme ; four doux 25-30 min (timbale 1 L) ; mieux vaut le cuire un peu plus que pas assez.
- Farce aux marrons (grosse volaille rôtie ~3 kg) : ~800 g chair à saucisse fine + ~1 kg marrons (épluchés, cuits aux 2/3 au bouillon, refroidis) ; rôtir à chaleur pas trop vive en arrosant souvent. (Volaille farcie : vérifier 74°C au cœur de la farce ET de la chair.)

## Légumes et féculents — méthodes

### Pommes de terre : frites, purée, gratin dauphinois, lyonnaise
- Frites : taille Pont-Neuf = bâtonnets d'1 cm ; allumettes plus fines ; pailles = julienne très fine. Bien essuyer avant friture. Objectif croustillant dehors/moelleux dedans. La double cuisson (1er bain pour cuire sans trop colorer, 2e bain en friture fumante juste avant de servir) est la méthode Escoffier pour les pommes pailles, transposable. Saler à la fin. (Escoffier ne donne pas de températures ; repères modernes courants : ~150-160 °C 1er bain, ~180 °C second.)
- Purée : pdt JUSTE cuites, passer au tamis/presse-purée brûlantes (jamais au mixeur), ~200 g beurre/kg, ajouter peu à peu ~2,5 dl lait bouillant, chauffer sans bouillir, servir au dernier moment.
- Gratin dauphinois (~1 kg pdt émincées fin) : pdt + sel/poivre/muscade + 1 œuf battu + ~750 ml lait bouilli + 125 g gruyère ; plat frotté d'ail et beurré ; gruyère + parcelles de beurre dessus ; four moyen 40-45 min. Savoyarde : lait remplacé par bouillon.
- Lyonnaise : pdt cuites à l'eau, en rondelles, sautées au beurre ; oignon émincé sauté à part (~1/4 du poids des pdt), réunir, finir au persil.

### Légumes glacés, petits pois à la française, marrons
- Glacer (oignons, carottes, navets) : à BLANC = cuire à couvert dans bouillon + beurre (~125 g/L), légumes presque couverts, le liquide réduit en glace qu'on roule sur les légumes ; à BRUN = cuire très doucement au beurre + pincée de sucre (cuisson et coloration ensemble).
- Petits pois à la française (1 L de pois écossés) : pois + 1 cœur de laitue + persil + cerfeuil + 12 petits oignons + 125 g beurre + 10 g sel + 20 g sucre, manier puis seulement 3 c. d'eau, cuire à couvert ; au service, retirer le bouquet, lier au beurre HORS FEU, couper la laitue dessus.
- Marrons : éplucher = inciser l'écorce, passer au four 7-8 min (ou friture fumante), écorcer brûlants (les deux peaux partent ensemble). Étuvés : à couvert, bouillon à hauteur + 1/2 branche céleri/livre ; pour farce, garder fermes. Braisés/glacés : un seul rang, fond de veau corsé à hauteur, remuer le moins possible, aux 3/4 réduire le liquide et rouler les marrons dans la glace.

### Pâtes, gnocchi romaine, polenta
- Pâtes (macaroni, nouilles) : cuire à l'eau bouillante salée à 10 g/L ; ne JAMAIS rafraîchir (pour stopper, ajouter un peu d'eau fraîche et retirer du feu) ; cuire au moment de servir (une pâte réchauffée donne un mauvais résultat). Liaison « à l'italienne » : égoutter, sécher à la poêle, lier hors feu vif avec ~150 g gruyère+parmesan (moitié/moitié) + 60 g beurre par 500 g de pâtes.
- Gnocchi à la romaine : 250 g semoule en pluie dans 1 L lait bouillant + sel/poivre/muscade, cuire 20 min ; hors feu, lier 2 jaunes ; étaler en couche d'1 cm, refroidir, détailler à l'emporte-pièce ; gruyère + parmesan + beurre fondu, gratiner.
- Polenta : 250 g farine de maïs en pluie dans 1 L eau bouillante salée (15 g), cuire 25 min, finir 60 g beurre + 75 g parmesan ; poêlée = étaler mince, refroidir, détailler, colorer au beurre + fromage + beurre noisette.

### Riz pilaf : méthode et ratio fiables
- Faire revenir oignon haché + riz au beurre (le riz devient nacré).
- Ratio liquide : 2 volumes de bouillon pour 1 volume de riz (mesurer le riz avant).
- Saler, bouquet garni, porter à ébullition, couvrir et finir au four (ou feu très doux) 17 minutes sans remuer.
- À la sortie : égrener à la fourchette en ajoutant quelques noisettes de beurre.
- Base du riz qui accompagne curry, volaille, poisson.

> **Sécurité (riz cuit)** : le riz cuit laissé à température ambiante développe Bacillus cereus dont la toxine émétique est THERMOSTABLE — le réchauffage ne la détruit pas. Refroidir vite, garder au froid, ne réchauffer qu'une fois. La prévention (refroidissement rapide + froid) est la seule protection. Voir fichier sécurité.

## Pâtes de base — pâtisserie salée et sucrée

### Pâte à choux, pâte brisée, feuilletage
- Pâte à choux (proportions complètes à diviser : 0,75 L eau / 375 g beurre / 15 g sel / 25 g sucre / 500 g farine / 16 œufs moyens) : eau + sel + sucre + beurre à ébullition ; hors feu, farine d'un coup, mélanger, puis DESSÉCHER à feu vif jusqu'à ce que la pâte n'attache plus et suinte ; hors feu, œufs DEUX PAR DEUX. Version salée (gougère) : eau remplacée par lait, sans sucre, + 250 g gruyère en fin.
- Pâte à foncer (brisée) : 500 g farine, 250 g beurre, 10 g sel, 2 dl eau ; farine en couronne, sel+eau+beurre manié au centre, incorporer la farine, FRAISER deux fois, repos au frais (à faire quelques heures à l'avance). Version fine (tartes fruits) : 500 g farine, 50 g sucre, 1 œuf, 300 g beurre, 1,5 dl eau.
- Feuilletage : détrempe 500 g farine + 10 g sel + 2,5-3 dl eau (repos 20 min) ; beurre 500 g (même poids), bien assoupli. Règle d'or : détrempe et beurre de MÊME consistance. 6 tours (replier en trois = 1 tour), donnés deux par deux, 10 min de repos entre chaque paire. Au frais mais jamais au contact direct de la glace. Ne pas trop travailler (sinon élastique, se rétracte). Rognures = demi-feuilletage.

### Cuire une croûte à blanc + pâtes à frire/crêpes
- Croûte à blanc : foncer le moule beurré, piquer le fond, tapisser de papier fin beurré, remplir de pois cassés ; four moyen ~25 min ; retirer papier et pois, dorer, sécher quelques minutes.
- Pâte à frire à la bière (beignets de fruits/fleurs) : 250 g farine + 5 g sel + 2 c. beurre fondu + 1,5 dl bière + 2 dl eau tiède + 1 c. cognac, sans trop travailler ; au DERNIER MOMENT, 2 blancs montés en neige (bière = croustillant, blancs = gonflant).
- Beignets de fruits juteux (fraises, cerises) : sucrer abondamment et macérer (kirsch) avant de frire (la chaleur fait suer le fruit ; mal sucré, il ressort aigrelet) ; bien éponger avant de tremper.
- Pâte à crêpes sucrées (base 500 g farine) : composition A = 200 g sucre + 12 œufs + 1,5 L lait + parfum ; composition plus moelleuse = 150 g sucre + 10 œufs + crème ; plus légère = blancs en neige. Crêpes Suzette = compo A + curaçao + jus de mandarine. Pannequets = crêpes fines tartinées, roulées, détaillées, glacées au four.
- Pain perdu : tranches de brioche/pain rassis d'1 cm imbibées de lait sucré vanillé FROID, trempées dans des œufs battus légèrement sucrés, cuites au beurre clarifié très chaud des deux côtés, saupoudrées de sucre.

## Crèmes et desserts — méthodes et seuils

### Crème anglaise, pâtissière, Chantilly : seuils critiques
- Crème anglaise (jaunes, SANS amidon) : sucre + jaunes au ruban, mouiller au lait chaud infusé, cuire jusqu'à ce qu'elle NAPPE la spatule → cible **82-85°C**. ÉVITER L'ÉBULLITION : au-delà (et a fortiori à ~97°C/ébullition) une crème anglaise tranche/graine. Filet de sécurité : une petite cuillère d'arrow-root dans le mélange sucre+jaunes prévient la décomposition. Vanner jusqu'au refroidissement (évite la peau). Ratio : 16 jaunes + 500 g sucre / litre (10 jaunes pour une version légère d'accompagnement).
- Crème pâtissière (AVEC farine — proportions complètes à diviser : 500 g sucre / 12 jaunes / 125 g farine / 1 L lait vanillé) : mélanger sucre + farine + jaunes, délayer au lait chaud, prendre sur le feu sans arrêt, **laisser bouillir ~2 min** (contrairement à l'anglaise, elle DOIT bouillir : l'amidon de la farine la stabilise et empêche les jaunes de cailler) ; tamponner la surface de beurre. Frangipane = formule propre (250 g sucre, 250 g farine, 4 œufs + 8 jaunes, 1,5 L lait) finie beurre + macarons.
- Chantilly : crème épaisse bien froide (24 h au froid idéale), fouetter jusqu'à doubler de volume et bien ferme, puis S'ARRÊTER (trop fouettée, elle tourne en beurre) ; sucrer après : 125 g/L (dont ~1/5 sucre vanillé).
- Repère mémo : ANGLAISE (jaunes seuls) = nappe à 82-85°C, ne bout PAS ; PÂTISSIÈRE (avec farine) = bout ~2 min. Ne jamais confondre les deux seuils.

### Crème renversée/flan, sucre cuit, soufflé/omelette norvégienne, charlotte
- Crème renversée / custard : base riche = 1 L lait vanillé + 200 g sucre + 4 œufs entiers + 8 jaunes ; version légère = ~6 œufs + 180 g sucre/L. Passer au tamis, ÔTER la mousse (sinon bulles), pocher au bain-marie au four. Plus d'œufs = plus ferme ; moins = plus crémeux.
- Degrés du sucre (test au doigt — ce sont des PLAGES conventionnelles, les bornes varient légèrement selon les sources) : petit/grand filet (fils) ; petit boulet « à la plume » (glu molle) ; grand boulet (boule, = meringue italienne) ; petit cassé (pellicule flexible qui colle) ; grand cassé (casse net comme du verre, = sucre filé) ; au-delà = caramel (quelques secondes). Anti-cristallisation : 1 c. de glucose/livre + écumer en début d'ébullition.
- Soufflé/omelette soufflé sucré : 250 g sucre + 6 jaunes au ruban + parfum, incorporer 8 blancs en neige TRÈS ferme délicatement, four moyen ; 2 min avant la fin, saupoudrer de sucre glace (croûte caramélisée).
- Omelette norvégienne : socle de génoise, glace en monticule, recouvrir entièrement de meringue ferme (~1,5 cm) qui isole, four TRÈS chaud très court (colorer la meringue sans atteindre la glace).
- Charlotte aux pommes (chaude) : chemiser le moule de tranches de pain de mie trempées au beurre, garnir d'une marmelade TRÈS serrée (trop liquide = pain ramolli, charlotte qui casse), remplir au max (la garniture s'affaisse), couvrir d'un rond de pain beurré, four moyen ; sauce abricot.

## Œufs — repères de cuisson

### Œufs : temps précis (durs, cocotte, frit, plat, brouillés)
- Durs : plonger à l'eau bouillante, 8 min à partir de la reprise de l'ébullition, rafraîchir aussitôt (jaune juste pris, non verdâtre ; écalage facile).
- En cocotte : cocotte beurrée, assaisonner, casser l'œuf, poser les cocottes dans un sautoir avec 1 cm d'eau bouillante, couvrir hermétiquement, porter vif à ébullition ; ~2 min 30 (blanc pris, jaune coulant).
- Frit à l'huile : glisser l'œuf dans l'huile fumante, rabattre les bavures du blanc sur le jaune sans le crever ; ~1 min 30.
- Au plat : casser sur assiette, cuire au beurre bien chaud, finir au four.
- Brouillés : battre, faire prendre doucement au bain-marie, finir beurre et crème (crémeux, pas sec).

> **Sécurité œufs** : les cuissons à jaune coulant (cocotte, plat, mollet) sont des choix de texture. Pour les publics fragiles (jeunes enfants, femmes enceintes, personnes âgées ou immunodéprimées), cuire l'œuf jusqu'à prise complète (blanc ET jaune) ou utiliser des œufs pasteurisés. Pas d'œuf cru ni coulant pour ces publics. Voir fichier sécurité.

### Soufflé salé : formule de base
- Base : purée de l'ingrédient (cuit ou cru) + béchamel chaude, liée aux jaunes crus, puis blancs montés en neige incorporés délicatement (sans casser la mousse), mouler, cuire au four jusqu'à ce qu'il gonfle. Même logique pour tous les parfums (volaille, poisson, fromage, légume) : on ne change que la purée.

## Friture, croquettes et beignets

### Croquettes/cromesquis, fritot, friture en général
- Croquettes : couper l'ingrédient (volaille, poisson, viande, riz) en petit salpicon + un complément (champignons), lier d'une sauce réduite épaisse + jaunes, REFROIDIR complètement (l'appareil doit être froid et ferme pour se façonner), façonner, paner à l'anglaise (farine, œuf, chapelure), frire à grande friture. Cromesquis = même appareil enveloppé dans une crêpe non sucrée ou une crépine, trempé en pâte à frire, frit.
- Fritot : petits morceaux (volaille, cervelle, abats, légumes) marinés 20-30 min (huile + citron + fines herbes) avant d'être trempés en pâte à frire et frits à grande friture ; persil frit + sauce tomate. La marinade évite un beignet fade.

> **Sécurité (appareils froids à base de viande cuite)** : un appareil à croquettes contenant de la viande/volaille cuite doit refroidir vite et rester au froid avant façonnage ; la friture finale doit le ramener chaud à cœur. Voir fichier sécurité.

## Fonds — repères de durée

### Temps de cuisson des fonds maison
Cuisson douce, écumer et dégraisser régulièrement (poisson vite, viandes lentement) :
- Fond blanc (os gélatineux de veau + carcasses de volaille) : ~3 h.
- Fond brun (os colorés au four + aromates) : 6 à 8 h, remettre de l'eau chaude au fur et à mesure.
- Fond de gibier : 4 à 5 h, mouillé vin blanc + eau.
- Fumet de poisson (arêtes + parures) : 20 à 25 minutes seulement (au-delà, amer).

> **Sécurité (fonds et bouillons)** : un fond destiné à être conservé doit être refroidi rapidement (60→21°C en ≤2h, puis 21→4°C en ≤4h) — ne jamais laisser une grande marmite tiédir lentement sur le plan de travail (zone de danger 4-60°C). Garder au froid (≤4°C), réchauffer à ébullition avant réutilisation. Voir fichier sécurité.



<!-- ===== 18-fonds-bouillons.md ===== -->

# Fonds, bouillons & soupes du quotidien

Guide maison, concis et actionnable, pour fabriquer les bases liquides de la cuisine domestique : fonds (à transformer), bouillons (à boire), liaisons, soupes et potages.

**Repère mental — les 3 familles de liquides**
- **Fond** : cuit longtemps, NON salé, destiné à être réduit/transformé en sauce (sauf le fumet, qui cuit court).
- **Bouillon** : assaisonné, destiné à être bu ou à servir de base de soupe.
- **Soupe/potage** : plat fini, liquide + légumes, goûté et ajusté comme une sauce.

---

## 1. Fonds de base — protocoles

**Règle commune à tous les fonds**
- **Départ EAU FROIDE** : extrait mieux la gélatine et l'arôme, garde le liquide clair.
- **Cuisson douce et frissonnante** : jamais de gros bouillon (qui émulsionne le gras et rend trouble).
- **Écumer régulièrement** les impuretés en surface.
- **NE PAS saler** : le fond sera réduit ensuite (sinon trop salé au final).
- **Passer au chinois sans fouler** (ne pas presser les solides, ça trouble).

### Fond blanc (volaille / veau)
- Os / carcasses + eau froide à hauteur, porter doucement, écumer.
- **Garniture aromatique** : carotte, oignon (piqué d'un clou de girofle), poireau, céleri, bouquet garni. **Pas de coloration.**
- **Cuisson frissonnante** : volaille 1 h 30 – 2 h ; veau 3 – 4 h.
- Résultat : liquide clair et pâle.
- **Usages** : veloutés, blanquette, potages, risotto.

### Fond brun (veau / bœuf)
- **Colorer** os + parures au four (~220 °C) jusqu'à brun doré (= « pincer »).
- Ajouter la garniture aromatique à colorer ; concentré de tomate facultatif.
- **Déglacer la plaque** (récupérer les sucs), tout mettre en marmite, mouiller à l'eau froide à hauteur.
- **Cuisson** : 4 – 6 h frissonnant, écumer / dégraisser.
- Résultat : liquide ambré-brun.
- **Usages** : sauces brunes, jus, braisages. Réduit → demi-glace, puis glace.

### Fumet de poisson
- Arêtes / parures de **poissons blancs maigres** (jamais de poissons gras = amertume / rancissement), bien rincées.
- **Suer sans coloration** avec échalote / oignon + blanc de poireau dans un peu de beurre.
- Mouiller à l'eau froide (+ vin blanc facultatif), bouquet garni.
- **Cuisson COURTE : 20 – 30 min max** (au-delà : amertume, colle). Ne pas trop écumer ni remuer.
- **Usages** : sauces poisson (vin blanc, normande), pochage, soupes de poisson.

> **Différence clé** : un fond cuit longtemps (sauf le fumet, court). Un bouillon est destiné à être bu, un fond à être transformé / réduit.

---

## 2. Roux et liaisons

### Le roux (farine + matière grasse)
- **Proportion de base** : poids égal beurre / farine. Cuire la farine dans le beurre fondu en remuant.
- **Roux blanc** (2 – 3 min, ne colore pas) → béchamel, sauces blanches.
- **Roux blond** (légèrement doré) → veloutés.
- **Roux brun** (cuit plus longtemps, couleur noisette) → sauces brunes.

**Dosage liaison pour 1 L de liquide**
| Texture | Roux |
|---|---|
| Léger | 60 – 70 g |
| Nappant | 80 – 100 g |
| Épais | 100 – 120 g |

### Règle anti-grumeaux (critique)
- L'un des deux doit être **FROID** quand on mélange : **roux chaud sur liquide froid**, OU **liquide chaud sur roux refroidi**. Jamais chaud sur chaud d'un coup.
- Verser **progressivement en fouettant**.
- Porter à **ébullition douce** pour que la farine « prenne » (l'amidon n'épaissit qu'à chaud).
- **Cuire 5 – 10 min** pour ôter le goût de farine crue.

### Autres liaisons
- **Maïzena / fécule** : délayer à froid dans un peu de liquide, verser dans le liquide chaud, ébullition brève. Lie clair et brillant.
- **Jaunes + crème** (blanquette, sauce allemande) : détendre les jaunes avec un peu de liquide chaud, incorporer hors gros bouillon, **NE PLUS BOUILLIR** (sinon coagulation / grains).
- **Beurre manié** (beurre + farine malaxés à cru) : ajouté en fin pour rattraper / épaissir une sauce trop claire ; fouetter.
- **Liaison végétale** : la purée du légume lui-même (pomme de terre, légume mixé) pour les soupes, sans amidon ajouté.

---

## 3. Bouillons, pot-au-feu et consommé

### Bouillon (à boire ou base de soupe)
- Comme un fond blanc, **mais on assaisonne** (il est consommé tel quel) et on peut inclure une viande à pot-au-feu.
- **Départ eau froide** pour un bouillon savoureux (échange des sucs vers le liquide) ; **départ eau bouillante** si l'on veut garder le goût DANS la viande.
- Écumer soigneusement les premières impuretés, frissonner, **ne jamais bouillir fort** (trouble + gras émulsionné).

### Pot-au-feu (bouillon + viande + légumes)
- **Viandes gélatineuses** (gîte, paleron, jarret, queue) : départ eau froide, écumer.
- Garniture aromatique d'abord (oignon clouté, poireau, céleri).
- **Légumes à manger ajoutés plus tard** pour rester entiers (carotte, navet, poireau ; pomme de terre cuite à part pour ne pas troubler le bouillon).
- **Cuisson 3 – 4 h frissonnant.** Le bouillon dégraissé sert de soupe / base.

### Consommé (bouillon clarifié, limpide)
- **Clarification** : viande hachée maigre + blancs d'œufs + mirepoix + un peu de bouillon froid.
- Incorporer au bouillon **FROID**, monter doucement en remuant jusqu'à formation d'un « radeau » (les blancs coagulent et piègent les impuretés).
- **NE PLUS REMUER**, laisser frissonner 30 – 45 min, passer délicatement au linge.
- Résultat : liquide parfaitement limpide.

> **Alternative domestique** : un bouillon bien écumé et passé au filtre / linge suffit pour l'usage courant.

---

## 4. Soupes et potages du quotidien

### Méthode générale (potage purée / velouté)
1. **Suer** les légumes (oignon / poireau + légume principal) dans un peu de beurre / huile **sans coloration** (garde la couleur et la douceur).
2. **Mouiller à hauteur** avec eau, bouillon ou fond. Saler légèrement.
3. **Cuire** jusqu'à ce que les légumes soient tendres (15 – 30 min).
4. **Mixer.** Détendre si trop épais, réduire si trop liquide.
5. **Finition** : crème, beurre, huile d'olive, herbes, croûtons.

> **Liaison naturelle** : la pomme de terre (ou un légume amylacé) lie sans roux ni farine. Pour un velouté classique, on peut aussi partir d'un roux blond + lait / fond.

### Les types
- **Potage purée** : légumes secs ou amylacés mixés (lentilles, pois cassés, potiron, carotte).
- **Velouté** : base liée + finition crème / jaunes, texture soyeuse, passée fine.
- **Soupe claire / minute** : légumes en petits dés dans un bouillon, sans mixer.
- **Soupe froide** (gaspacho, vichyssoise) : **assaisonner plus fort** (le froid atténue les saveurs).

### Équilibrer une soupe (comme une sauce)
1. **Sel** d'abord.
2. **Acidité** (filet de citron / vinaigre) pour réveiller.
3. **Gras** (crème / beurre / huile) pour la rondeur.
- Garder le goût du légume dominant **lisible**.

### Diagnostic express
| Problème | Correction |
|---|---|
| Fade | Sel + bouillon concentré + acidité finale |
| Trop épaisse | Allonger eau / bouillon / lait |
| Trop liquide | Réduire, ou ajouter pomme de terre cuite mixée |
| Goût « cuit » / terne | Herbes fraîches + matière grasse crue en fin |
| Trop salée | Allonger + pomme de terre |

---

## Méta / sources

- **Public visé** : cuisine domestique du quotidien (assistant cuisine maison).
- **Statut** : v1, fichier autonome créé pour combler 4 manques du domaine « Fonds, bouillons, soupes & familles de sauces ».
- **Origine du contenu** : techniques classiques de cuisine française (méthode Escoffier simplifiée pour l'usage domestique) ; les protocoles, proportions et règles (départ eau froide, règle anti-grumeaux chaud/froid, dosages de roux) sont des standards de base.
- **Repères chiffrés** : temps de cuisson et dosages donnés en fourchettes usuelles ; à adapter selon quantités et matériel. Aucune donnée n'a été inventée ; en cas de doute sur un repère précis, vérifier sur une source culinaire de référence.
- **À compléter ultérieurement (hors périmètre v1)** : recettes détaillées des sauces mères dérivées (béchamel, velouté, espagnole, demi-glace), conservation / congélation des fonds.
