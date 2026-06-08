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
