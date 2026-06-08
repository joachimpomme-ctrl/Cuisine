# Knowledge — base de connaissances culinaire

20 fichiers Markdown distillés à la main depuis des ouvrages de référence, conçus pour être
ingérés par un agent IA (Gemini, Claude, ChatGPT) dans son champ *Knowledge / Project knowledge*.

Principe directeur : **transformer le savoir en action immédiate**.

| Fichier | Contenu |
|---|---|
| `01-rules-core.md` | Méta-règles de diagnostic et de correction |
| `02-regles-pratiques.md` | Assaisonnement, cuisson, rattrapage |
| `03-nosrat-gout.md` | Goût : sel, gras, acide, chaleur |
| `04-mcgee-science.md` | Science culinaire générale |
| `05-mcgee-viande.md` | Science de la viande : seuils, collagène, Maillard |
| `06-escoffier-structure.md` | Sauces nommées, garnitures, vocabulaire classique |
| `07-cuissons.md` | 7 méthodes de cuisson, protocoles, émulsions |
| `08-ottolenghi-patterns.md` | Patterns de plats, cuisines du monde |
| `09-associations.md` | Associations d'ingrédients (Flavor Bible & Thesaurus) |
| `10-securite-alimentaire.md` | ⭐ Sécurité : températures internes, zone de danger, poisson cru — **source de vérité** |
| `11-conservation.md` | Conservation, restes, congélation, batch cooking |
| `12-substitutions-regimes.md` | Substitutions & régimes (végé, végan, sans gluten/lactose, allergies) |
| `13-quantites-conversions.md` | Quantités par personne, conversions, mise à l'échelle |
| `14-poissons.md` | Poissons & fruits de mer (fraîcheur, cuisson, seuils) |
| `15-equipement-improvisation.md` | Équipement domestique & improvisation |
| `16-profils-saveurs-monde.md` | Profils de saveurs & bases aromatiques du monde |
| `17-grains-legumineuses.md` | Céréales, riz, pâtes & légumineuses |
| `18-fonds-bouillons.md` | Fonds, bouillons & soupes du quotidien |
| `19-boulangerie-patisserie.md` | Pain & pâtisserie de base domestique |
| `20-planification-menus.md` | Composition de repas & orchestration du timing |

## Chaîne de priorité

```
RAISONNEMENT → GOÛT → STRUCTURE → SCIENCE → TECHNIQUE → PATTERNS → ASSOCIATIONS
```
La **sécurité alimentaire** (`10-securite-alimentaire.md`) fait toujours autorité : en cas de conflit
entre un repère de texture (ex. poisson 50-55 °C) et un seuil sanitaire (63 °C), la sécurité prime.

## ⚠️ Limite Gemini Gem (10 fichiers)

Un Gem Gemini n'accepte qu'une dizaine de fichiers. Pour le Gem, utiliser le **bundle consolidé**
fourni dans `gem-gemini/` (les 20 fichiers fusionnés en thèmes). Claude (Projects) et ChatGPT
(Custom GPT / Projects) n'ont pas cette contrainte et peuvent charger les 20 fichiers.

## Note sur les sources

Notes de synthèse personnelles et reformulées (règles, heuristiques, repères), inspirées d'ouvrages
de référence : *Salt Fat Acid Heat* (Nosrat), *On Food and Cooking* (McGee), *Le Guide culinaire*
(Escoffier), *Répertoire de la cuisine* (Gringoire & Saulnier), *La Cuisine de référence*
(Maincent-Morel), *The Flavor Bible* & *The Flavor Thesaurus*, *Ottolenghi Simple* & *Plenty*,
*Grand Livre de Cuisine* (Ducasse). **Aucun texte intégral n'est redistribué.**
