# Bundle Gemini Gem (consolidé)

Le Gem Gemini est limité à ~10 fichiers (ici **9 fichiers knowledge + 1 instructions**).
Ces 9 bundles regroupent les **20 fichiers** de `../knowledge/` par thème, sans rien perdre.

➡️ **Pour le Gem** : charger ces 9 fichiers dans le champ *Knowledge*, et
`../instructions/gemini.md` dans le champ *Instructions*.

➡️ **Pour Claude / ChatGPT** : pas de limite — préférer les 20 fichiers granulaires de `../knowledge/`.

| Bundle | Taille | Regroupe |
|---|---|---|
| `gem-1-regles-gout.md` | 69 Ko | 01-rules-core.md, 02-regles-pratiques.md, 03-nosrat-gout.md |
| `gem-2-science.md` | 81 Ko | 04-mcgee-science.md, 05-mcgee-viande.md |
| `gem-3-securite-conservation.md` | 27 Ko | 10-securite-alimentaire.md, 11-conservation.md |
| `gem-4-structure-fonds.md` | 85 Ko | 06-escoffier-structure.md, 18-fonds-bouillons.md |
| `gem-5-cuissons-equipement.md` | 81 Ko | 07-cuissons.md, 15-equipement-improvisation.md |
| `gem-6-patterns-menus.md` | 140 Ko | 08-ottolenghi-patterns.md (compressé), 20-planification-menus.md |
| `gem-7-associations-saveurs.md` | 140 Ko | 09-associations.md (allégé), 16-profils-saveurs-monde.md |
| `gem-8-poissons-grains.md` | 17 Ko | 14-poissons.md, 17-grains-legumineuses.md |
| `gem-9-substitutions-conversions-boulangerie.md` | 26 Ko | 12-substitutions-regimes.md, 13-quantites-conversions.md, 19-boulangerie-patisserie.md |

> ⚠️ Certains bundles sont volumineux (notamment patterns & associations). Si Gemini refuse un
> fichier trop gros, scinder le bundle concerné ou alléger le fichier source correspondant.

## Élagage stabilité (2026-08)

Un knowledge trop volumineux provoque des blocages et des pertes de contexte en cours de
conversation (silent token dropping du runtime Gemini). Correctifs appliqués :

- **gem-6** 173→140 Ko : patterns Ottolenghi 001-024 compressés au format compact
  (Intention / Formule / Variantes / Points critiques / Usage), contenu préservé.
  Le fichier source `../knowledge/08-ottolenghi-patterns.md` conserve la version longue
  (pour Claude/ChatGPT sans limite de contexte).
- **gem-7** 150→140 Ko : fiches occasions/rares (gibier, abats, foie gras, huîtres, truffe,
  yuzu, verjus…) déplacées dans `gem-7-annexe-occasions-HORS-GEM.md` — **ne PAS charger ce
  fichier dans le Gem**, il sert de référence manuelle. Fiches en triple exemplaire fusionnées.
- **Instructions** (`../instructions/gemini.md`) : protocole Drive tolérant aux échecs
  (1 appel/tour, pas de retry en boucle) + règle d'économie de contexte.
- Conseil d'usage : une conversation = une tâche ; repartir sur une conversation neuve dès
  que le Gem ralentit ou perd le fil.
