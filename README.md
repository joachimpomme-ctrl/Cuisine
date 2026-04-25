# 🍳 Cuisine AI Knowledge

## 🎯 Vision

Cuisine AI Knowledge est une base de connaissances culinaire conçue pour alimenter un assistant IA de cuisine.
Le projet aide à transformer des savoirs culinaires fiables en réponses simples, rapides et actionnables.
Il répond à un besoin concret : aider un utilisateur à réussir un plat, corriger une erreur ou trouver une idée sans recevoir un cours inutile.
Il s’adresse aux créateurs d’agents IA, aux passionnés de cuisine et aux équipes qui veulent construire un assistant culinaire utile au quotidien.

## ⚡ Ce que fait le système

Le système permet de :

* corriger un plat trop fade, trop salé, trop acide, trop lourd ou mal équilibré ;
* proposer une recette simple à partir d’un besoin, d’un ingrédient ou d’une envie ;
* expliquer un problème de cuisson, de texture ou d’assaisonnement ;
* suggérer des idées de plats, d’associations ou de variations ;
* guider l’utilisateur vers une action principale claire.

## 🧠 Architecture

Le projet repose sur plusieurs couches complémentaires :

```text
Rules     → technique cuisine, gestes, cuisson, rattrapage
McGee     → science culinaire, compréhension des phénomènes
Nosrat    → goût, équilibre sel / acide / gras / chaleur / umami
Escoffier → structure des plats, sauces, garnitures, cohérence
Patterns  → créativité, associations, inspirations
Recipes   → exécution concrète, étapes, repères sensoriels
```

Chaque couche a un rôle précis.
L’objectif n’est pas d’accumuler de l’information, mais de produire des réponses utiles, courtes et fiables.

## 📂 Structure du repository

```text
cuisine-ai-knowledge/
  04_rules/
  09_exports/
  07_tests/
```

`04_rules/` contient les règles métier structurées : technique, goût, cuisson, rattrapage et logique culinaire.

`09_exports/` contient les fichiers prêts à charger dans un agent IA, notamment les contextes Gemini.

`07_tests/` contient les tests, rapports et validations utilisés pour vérifier la qualité des réponses.

## 🚀 Utilisation

Pour utiliser cette base avec Gemini, charger les fichiers d’export situés dans :

```text
cuisine-ai-knowledge/09_exports/gemini_context/
```

Les fichiers de connaissance apportent le contenu culinaire : règles, raisonnements, exemples et repères.

Le prompt d’instructions définit le comportement de l’assistant : style, priorité des réponses, niveau de détail et limites.

En pratique :

* le prompt dit comment répondre ;
* la knowledge base dit quoi savoir ;
* l’agent combine les deux pour produire une réponse claire et actionnable.

## 🧪 Exemple d’usage

Utilisateur :

```text
mon plat est fade
```

Réponse attendue :

```text
Ajoute d’abord une petite pincée de sel, mélange, puis goûte à nouveau.
Si le plat reste plat malgré le sel, il faudra probablement ajouter une touche d’acide.
```

Utilisateur :

```text
donne-moi une idée avec poulet
```

Réponse attendue :

```text
Fais un poulet citron-ail à la poêle avec une garniture de riz ou de légumes rôtis.
Point clé : bien dorer le poulet avant d’ajouter le citron pour garder du goût et éviter un résultat bouilli.
```

Utilisateur :

```text
pourquoi ma viande est dure
```

Réponse attendue :

```text
Elle a probablement été trop cuite ou cuite trop fort.
Pour la prochaine fois, baisse la chaleur et arrête la cuisson dès que la viande est encore légèrement souple au toucher.
```

## ⚙️ Philosophie

Le projet privilégie l’action plutôt que la théorie.

Un bon assistant cuisine doit aider à agir maintenant, pas impressionner avec du vocabulaire.

Les règles sont plus importantes que les recettes : elles permettent de s’adapter à ce que l’utilisateur a réellement devant lui.

La simplicité passe avant la complexité.
Une seule bonne action vaut mieux qu’une liste de possibilités difficiles à choisir.

Le test réel compte plus que la perfection abstraite.
Les réponses doivent être vérifiées par l’usage : est-ce clair, utile, faisable, rapide ?

## 🛣️ Roadmap

Priorités prévues :

* enrichir les recettes exploitables par l’assistant ;
* améliorer les patterns d’idées et d’associations ;
* ajouter davantage de tests utilisateurs ;
* optimiser les exports et instructions pour Gemini.

## 🤝 Contribution

Les contributions doivent rester simples, structurées et orientées usage.

Pour ajouter du contenu :

* placer les règles dans le dossier adapté ;
* écrire des formulations courtes et actionnables ;
* éviter les explications longues sans conséquence pratique ;
* privilégier les règles testables sur des cas réels ;
* vérifier que l’export final reste lisible par un agent IA.

Une bonne contribution doit aider l’assistant à mieux répondre à une vraie question de cuisine.
