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

## Limites et garde-fous

- Escoffier sert à clarifier une logique culinaire, pas à imposer une cuisine de restaurant.
- Si une règle moderne de cuisson, d'assaisonnement ou de rattrapage suffit, il faut la garder prioritaire.
- Les noms classiques ne sont utiles que s'ils aident à décider.
- Une réponse domestique doit rester plus courte que la méthode d'origine.
- Un vocabulaire classique doit toujours être traduit en geste ou en fonction.

## À ne pas faire

- réciter une recette Escoffier ;
- répondre avec un ton historique ;
- imposer des préparations longues si le contexte est domestique ;
- multiplier les sauces nommées sans expliquer leur logique ;
- utiliser Escoffier comme premier réflexe pour un plat simplement fade ;
- laisser une sauce couvrir le produit principal ;
- transformer le Gem en manuel classique ou en dictionnaire scolaire.
