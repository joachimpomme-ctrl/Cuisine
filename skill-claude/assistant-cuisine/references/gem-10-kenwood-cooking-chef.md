# Kenwood Cooking Chef (KM080 / KM099) — Référence opérationnelle

> Source : notice officielle Kenwood KM080 series (édition FR, réf. Darty KM099 Cooking Chef, codic 4082044)
> Format : référence agent — uniquement ce qui sert à décider et à agir
> Extraction : OCR de la notice scannée + vérification visuelle des pages clés (capacités, panneau de commandes)

## Rôle de ce fichier

Répondre à toute question impliquant le robot Cooking Chef de l'utilisateur : choix d'accessoire, réglage de vitesse, cuisson par induction dans le bol, réglages de mélange, capacités maximales, codes d'erreur, dépannage cuisson.

Principe : le Cooking Chef combine batteur planétaire et plaque à induction sous le bol. On mélange ET on cuit dans le même bol.

## Identité machine

- Robot pâtissier à mouvement planétaire + cuisson par induction intégrée sous le bol.
- Plage de température : **20 → 140°C** (cadran gradué de 10 en 10, position OFF).
- Précision température : ±5°C sur liquides et ingrédients aqueux ; varie avec consistance, volume, fréquence de mélange et accessoire.
- Les préparations à forte teneur en eau plafonnent à ~100°C (ébullition).
- Durée de cuisson maximale : **3 heures**, puis arrêt automatique.
- Capacité maximale en mode cuisson : **3 litres** (niveau marqué dans le bol).
- 4 sorties accessoires : ultra-rapide, moyenne, lente, planétaire.
- LED bleue : clignote tant que la température cible n'est pas atteinte ; fixe une fois atteinte ; re-clignote si on ajoute des ingrédients froids ou si on augmente la vitesse.
- Pas de friture en bain d'huile dans le bol (interdit par la notice).
- Champs magnétiques (induction) : précaution pacemakers et implants actifs ; pas de cartes bancaires ni d'appareils sensibles à proximité.

## Accessoires — quel outil pour quoi

| Accessoire | Usages | Hauteur |
|---|---|---|
| Batteur K inox | Gâteaux, biscuits, pâtes, glaçages, garnitures, éclairs, purée | Presque toucher le fond |
| Fouet | Œufs, crèmes, pâtes à frire, génoises sans gras, meringues, cheesecakes, mousses, soufflés. JAMAIS pour mélanges épais (beurre+sucre) : risque de casse | Presque toucher le fond |
| Crochet de pétrissage | Pâtes levées | Réglé usine, ne pas ajuster |
| Batteur souple haute température | Crème anglaise, œufs brouillés, sauces ; racle les parois pendant le mélange ; légumes sautés | DOIT toucher le fond |
| Mélangeur (stir tool) | Maintenir la consistance pendant la cuisson : poulet, poisson, légumes, fruits, ragoûts | Presque toucher le fond |

Astuce notice : changer d'accessoire en cours de recette améliore le résultat — ex. batteur souple pour faire revenir les légumes, puis mélangeur pour cuire les morceaux de viande.

Ajustement hauteur : appareil débranché, desserrer l'écrou avec la clé fournie, tourner l'axe (antihoraire = descendre, horaire = monter), resserrer.

## Vitesses recommandées

**Batteur K :**
- crémer beurre + sucre : min → max progressivement
- incorporer les œufs à une crème : 4 → max
- incorporer farine, fruits : min → 1
- battre tous les ingrédients d'un gâteau : min → max progressivement
- sabler (gras dans farine) : min → 2

**Batteur souple haute température :**
- crémer beurre + sucre : min → 8 progressivement
- racler mélanges chauds/froids : min → 3
- sauter légumes, risotto, polenta : réglage mélange ①

**Fouet :** min → max progressivement.
**Crochet :** min → 1 seulement.
**Mélangeur :** réglages ①②③ uniquement.

## Réglages de mélange (sens antihoraire du bouton vitesse)

Conçus pour le mode cuisson. Tous les couvercles doivent être installés.

- **①** : vitesse lente constante — sauces, chauffer vite un liquide, risotto, sauté.
- **②** : intermittent, ~2 tours toutes les 5 secondes.
- **③** : intermittent, ~2 tours toutes les 30 secondes — mijotés, ragoûts, maintien de consistance.

Retour sur 'O' pour arrêter.

## Boutons spéciaux

- **Pulse** : vitesse max tant qu'on appuie. Fonctionne uniquement si la vitesse est sur 'O'. Si le contenu est >60°C, la montée en vitesse est progressive (bips + voyants clignotants).
- **Fold** : appui bref = 2 tours à vitesse minimum puis arrêt (incorporer délicatement). Appui long ou répété pour prolonger. Pendant que le moteur tourne : fold puis retour à la vitesse sélectionnée.
- **Sélection minuteur/température** : chaque appui alterne l'affichage temps ↔ température du contenu du bol.

## Cuisson par induction — procédure

1. Zone d'induction, capteurs de température et base du bol propres et SECS (sinon mauvaise mesure → cuisson ratée).
2. Protège-chaleur installé (obligatoire, sinon erreur E:03) + tous les couvercles de sorties.
3. Régler la température (20-140°C).
4. La chauffe ne démarre que lorsqu'une vitesse est sélectionnée.
5. Voyant température : clignote pendant la montée, fixe à la cible, re-clignote pendant les régulations.
6. Arrêt/pause : vitesse sur 'O'. Reprise : re-sélectionner une vitesse.

Règles de sécurité automatiques :
- **>60°C dans le bol → vitesse automatiquement limitée**, même si une vitesse supérieure est sélectionnée. Ne remonte pas seule quand ça redescend : repasser par 'O' puis re-sélectionner.
- Fouetter à haute vitesse au-dessus de 60°C (ex. pâte à bombe, meringue suisse) : sélectionner la vitesse PUIS maintenir 'pulse' — la vitesse monte progressivement. UNIQUEMENT avec le fouet, max 3 litres, couvercle anti-projections en place, ne pas laisser sans surveillance.
- Jamais de cuisson bol vide.
- On peut cuire SANS accessoire installé (fondre beurre, chocolat) mais une vitesse doit quand même être sélectionnée.

Conseils cuisson (notice) :
- L'induction chauffe plus vite que le gaz/plaque : commencer chaud, surveiller, réduire — inutile de sur-régler la température pour aller plus vite.
- Ajouter des ingrédients en cours de cuisson : réduire la vitesse, verser lentement et régulièrement.
- Chauffer rapidement une sauce : mélange continu ①.
- Cuisson longue à feu doux : réglages ② ou ③ pour préserver la consistance.
- Soulever la tête lentement après cuisson : la condensation sous le protège-chaleur retombe dans le bol.
- Retirer le couvercle anti-projections AVANT de soulever la tête.

## Minuteur

- Maximum 3 h. Réglage par pas de 5 s (+ / −), défilement rapide en appui continu.
- Sans réglage : compte le temps écoulé en secondes.
- Compte à rebours dès qu'une vitesse est lancée ; pause quand la vitesse revient sur 'O'.
- Fin : arrêt automatique du mélange + 3 s de bips.
- Remise à zéro : + et − simultanément (vitesse sur 'O').
- Veille automatique après 10 min d'inactivité.

## Capacités maximales (vérifiées sur notice)

| Préparation | Maximum |
|---|---|
| Pâte brisée | 910 g de farine |
| Pâte levée | 1,5 kg de farine / 2,4 kg poids total |
| Pâte levée sucrée | 2,6 kg de farine / 5 kg poids total |
| Cake aux fruits | 4,55 kg poids total |
| Blancs d'œufs | 16 |
| Mode cuisson | 3 litres |

Pétrissage : ingrédients froids sauf indication contraire, liquides en premier, si le moteur force → diviser la pâte en deux et travailler séparément. Ne jamais dépasser les capacités (surcharge moteur).

## Codes d'erreur

| Code | Cause | Solution |
|---|---|---|
| E:01 | Tête du batteur relevée | Abaisser la tête, vitesse sur 'O', re-sélectionner |
| E:02 | Bol absent ou mal installé | Installer/verrouiller le bol Cooking Chef, 'O', re-sélectionner |
| E:03 | Protège-chaleur absent | Installer le protège-chaleur, 'O', re-sélectionner |
| E:04 | Couvercles de sorties absents | Installer tous les couvercles, 'O', re-sélectionner |
| E:09 | Capteurs de température (surchauffe détectée) | 'O', débrancher, laisser refroidir, nettoyer base du bol + capteurs, relancer |
| E:10 | Moteur calé ou en surchauffe | 'O', débrancher, retirer l'obstruction, vérifier grilles de ventilation, relancer |

Sécurité mécanique : tête relevée en marche = arrêt automatique + bip ; ne redémarre pas à l'abaissement — repasser par 'O'.

## Dépannage cuisson

**Ça brûle / colle au fond :**
1. température trop élevée → baisser ;
2. mauvais accessoire → batteur souple pour les liquides, mélangeur pour les morceaux ;
3. mélange trop lent → augmenter la fréquence (②→①) ou passer en continu ;
4. accessoire trop haut → ajuster vers le fond ;
5. cuisson trop longue → raccourcir ;
6. capteurs/base sales → nettoyer et sécher.

**Les aliments perdent leur consistance :** température trop élevée, mélange trop rapide, cuisson trop longue, ou mauvais accessoire (préférer ② ou ③ + mélangeur).

**La vitesse chute toute seule pendant la cuisson :** normal — limitation automatique à >60°C.

**Vitesse limitée alors qu'on ne cuit pas :** bol encore chaud installé → laisser refroidir sous 60°C.

**Ça chauffe pas alors qu'une température est réglée :** aucune vitesse sélectionnée — la chauffe est asservie à la sélection d'une vitesse.

**Mélange irrégulier :** morceaux trop gros/durs → couper plus petit, dénoyauter ; ajouter les ingrédients tête abaissée.

**Affichage température qui ne réagit pas après ajout d'ingrédients froids :** contenu mal homogénéisé → laisser mélanger, augmenter la vitesse de mélange.

## Après cuisson — manipulation

- Bol, couvercle anti-projections, accessoires et DESSOUS du bol restent chauds longtemps : gants, porter le bol par les poignées, tapis de protection sur le plan de travail.
- Vapeur au soulèvement du couvercle ou de la tête.
- Transfert vers le blender/mixeur : laisser refroidir à température ambiante d'abord.
- Consommer rapidement ou refroidir vite et réfrigérer (renvoi : gem-3-securite-conservation pour les règles détaillées).

## Nettoyage

- Toujours éteindre et débrancher avant nettoyage.
- Capteurs de température : chiffon humide puis séchage soigneux. Jamais d'abrasif ni d'objet pointu. Une usure de surface des capteurs est normale et sans effet.
- Bol inox : lavage main ou lave-vaisselle. Jamais de brosse métallique, paille de fer ou chlore. Calcaire → vinaigre. Brûlé au fond → spatule + trempage eau chaude savonneuse + brosse nylon. Une décoloration n'affecte pas les performances.
- Batteur souple HT : retirer la lame avant lavage ; lame + corps à l'eau chaude savonneuse ou lave-vaisselle ; inspecter la lame régulièrement et la remplacer si usée ; ne pas le laisser installé sur la machine hors utilisation.
- Robot et couvercles de sorties : chiffon humide, jamais d'immersion, jamais d'abrasif.
- Orifice d'écoulement : vérifier qu'il n'est pas obstrué (goupillon/coton-tige).
- Un peu de graisse à l'orifice de tête à la première utilisation : normal, essuyer.

## Accessoires optionnels (sorties)

Gamme AT sur les sorties ultra-rapide/moyenne/lente : appareils à pâtes (AT970A + matrices), trancheuse-râpe (AT643), hachoir multifonctions (AT950A/AT955), moulin à céréales (AT941A), robot culinaire (AT647), râpe éminceur pro (AT340), presse-agrumes (AT312), mixeurs 1,5 L (AT337 acrylique, AT358 verre, AT339 inox), mini-hachoir (AT320A), centrifugeuse (AT641), sorbetière (AT957A), passoire-tamis (AT930A), balance (AT850B). Bol inox supplémentaire : 36386A.

## Usage agent

- Proposer ce module quand : la question mentionne le Cooking Chef, le "robot", la cuisson au robot, le choix batteur K / fouet / crochet / batteur souple / mélangeur, un code E:xx, une recette à adapter au robot (risotto, crème anglaise, ragoût, pétrissage).
- Croiser avec gem-2 (science) pour les seuils : la crème anglaise se règle à 80-83°C au cadran avec batteur souple + mélange ① ; un ragoût se tient à 80-95°C avec mélangeur + ③.
- Croiser avec gem-3 (sécurité) : le cadran s'arrête à 140°C ; les cibles sanitaires internes (74°C volaille) se mesurent au thermomètre dans l'aliment, pas au cadran.
- Ne pas réciter la notice : donner le réglage (température + accessoire + réglage de mélange) et le point de vigilance.
