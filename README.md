# 🍳 Cuisine — Assistant culinaire IA (knowledge + instructions)

Une base de connaissances culinaire et des prompts système standardisés pour transformer
**Gemini, Claude ou ChatGPT** en assistant de cuisine domestique : clair, direct, actionnable.

L'objectif n'est pas d'impressionner avec du vocabulaire, mais d'**aider à réussir un plat
maintenant** — corriger un défaut, proposer une idée réalisable, expliquer un raté de cuisson.

---

## 🎯 Ce que fait l'assistant

- **Corriger** un plat fade, trop salé, trop acide, trop lourd, mal équilibré.
- **Proposer** une recette simple à partir d'un ingrédient, d'une envie ou d'un fond de frigo.
- **Expliquer** un problème de cuisson, de texture ou d'assaisonnement, et donner la parade.
- **Suggérer** des associations et des variations crédibles.
- **Gérer vos recettes** : inventaire, archivage de fiches, bibliothèque, profil de préférences (via Google Drive).

---

## 🧠 Architecture

Deux briques complémentaires :

```
instructions/   →  COMMENT répondre  (le comportement de l'agent, par plateforme)
knowledge/      →  QUOI savoir        (20 fichiers de savoir culinaire distillé)
```

Les couches de connaissance, mobilisées dans cet ordre de priorité :

```
RAISONNEMENT → GOÛT → STRUCTURE → SCIENCE → TECHNIQUE → PATTERNS → ASSOCIATIONS
   (core)       (Nosrat)  (Escoffier)  (McGee)   (cuissons)  (Ottolenghi)  (Flavor Bible)
```

---

## 📂 Structure du dépôt

```
.
├── README.md
├── instructions/
│   ├── README.md          # guide de déploiement + placeholders
│   ├── gemini.md          # prompt système — Google Gemini (Gems)
│   ├── claude.md          # prompt système — Anthropic Claude (Projects)
│   └── chatgpt.md         # prompt système — OpenAI ChatGPT (Custom GPT / Projects)
├── knowledge/            # 20 fichiers (01-20) — voir knowledge/README.md
│   ├── 01-rules-core.md … 09-associations.md      # socle (goût, science, structure, patterns, associations)
│   └── 10-securite-alimentaire.md … 20-planification-menus.md   # sécurité, conservation, substitutions, poissons, etc.
└── gem-gemini/           # bundle consolidé (9 fichiers) pour le Gem Gemini bridé à 10 fichiers
```

---

## 🚀 Démarrage rapide

1. **Choisissez votre plateforme** et ouvrez le prompt correspondant dans `instructions/`.
2. **Remplacez les placeholders** en tête de fichier (`{{INVENTORY_DOC}}`, `{{RECIPE_PREFIX}}`, `{{PROFILE_PREFIX}}`) par vos valeurs. Voir [`instructions/README.md`](instructions/README.md).
3. **Collez le prompt** dans le champ Instructions de votre Gem / Project / GPT.
4. **Chargez les fichiers de connaissance** dans le champ Knowledge / Project knowledge :
   - **Claude / ChatGPT** (pas de limite) → les **20 fichiers** de `knowledge/`.
   - **Gemini Gem** (limite ~10 fichiers) → les **9 bundles** de `gem-gemini/`.
   - ⭐ `10-securite-alimentaire.md` fait autorité : la sécurité prime sur les repères de texture.
5. (Optionnel) **Activez l'accès Google Drive** pour les modes inventaire / sauvegarde / bibliothèque / profil. Sans connecteur, l'agent fonctionne en mode manuel (il génère, vous collez).

> Le prompt dit *comment* répondre, la knowledge base dit *quoi* savoir. L'agent combine les deux.

---

## 🧪 Exemples

> **« mon plat est fade »**
> Ajoute d'abord une petite pincée de sel, mélange, goûte à nouveau. S'il reste plat malgré le sel,
> c'est sans doute un manque d'acidité — une pointe de citron ou de vinaigre.

> **« une idée avec du poulet »**
> Poulet citron-ail à la poêle, riz ou légumes rôtis en garniture. Point clé : bien dorer le poulet
> *avant* d'ajouter le citron, sinon le résultat est bouilli et sans goût.

> **« pourquoi ma viande est dure ? »**
> Probablement trop cuite ou cuite trop fort. La prochaine fois : baisse la chaleur et arrête dès que
> la viande est encore légèrement souple au toucher, puis laisse reposer.

---

## ⚙️ Philosophie

- **L'action avant la théorie** : aider à agir maintenant.
- **Les règles avant les recettes** : elles s'adaptent à ce que vous avez réellement devant vous.
- **La simplicité avant l'exhaustivité** : une seule bonne action vaut mieux qu'une liste de possibilités.
- **Le test réel avant la perfection abstraite** : clair, utile, faisable, rapide.

---

## 📜 Sources & licence

Les fichiers `knowledge/` sont des **notes de synthèse personnelles et reformulées** (règles, heuristiques,
repères), inspirées d'ouvrages de référence cités dans [`knowledge/README.md`](knowledge/README.md)
(*Salt Fat Acid Heat*, *On Food and Cooking*, *Le Guide culinaire*, *The Flavor Bible*, *Ottolenghi Simple*,
*La Cuisine de référence*…). **Aucun texte intégral de ces ouvrages n'est redistribué ici** ; les droits
restent à leurs auteurs et éditeurs.

Le contenu original de ce dépôt (prompts, structure, synthèses) est partagé librement à des fins
personnelles et éducatives.
