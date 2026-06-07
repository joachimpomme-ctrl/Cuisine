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
