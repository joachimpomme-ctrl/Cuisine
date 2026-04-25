# Rapport des modifications — Architecture finale

> Transformation McGee KB → cerveau culinaire opérationnel.
> 425 entrées avant → **421 entrées après**
> Réduction : 4 entrées (fusions et variantes)

## Synthèse des étapes

| Étape | Action | Compte |
|-------|--------|-------:|
| fusion | — | 4 |
| nettoyage_rag | — | 1 |

## ÉTAPE 1 — Normalisation structurelle

**0 entrées** ont eu leurs champs uniformisés (`effet`/`effets`, `seuil`/`seuils`).

## ÉTAPE 2 — Fusions de doublons

**4 fusions** appliquées sur les paires haute similarité du rapport initial.

### Pasteurisation

Fusion seuils 60°C+70°C en 1 entrée avec 2 variantes (équivalence bactériologique). Sources : seuils.jsonl L4+L5

### Myosine - dénaturation

Fusion seuils 40°C viande+poisson en 1 entrée avec 2 variantes. Sources : seuils.jsonl L7+L15

### Caramélisation des sucres

Fusion 2 seuils caramélisation (fructose, glucose, saccharose, lactose) en 1 entrée avec variantes par sucre.

### Blancs en neige qui ne montent pas

Fusion erreurs oeuf+foam (doublon strict). Conservé domaine='oeuf', plus précis. Source : erreurs_batch2.jsonl + erreurs_batch3.jsonl

### Paires arbitrées comme légitimement distinctes (NON fusionnées)

- **Amidons céréales vs tubercules** : caractéristiques opposées (gel opaque/cohésif vs gel transparent/élastique). Spécialisation utile.
- **Petit boulet 113°C vs Boulet 118°C** : paliers distincts du tableau confiserie. Précision opérationnelle.
- **Cuire fond viande >24h vs Cuire fond poisson >1h** : durées et espèces différentes. Diagnostic distinct.
- **Sucre tôt sur blancs vs Sucre tôt sur chantilly** : ingrédients de base différents (œuf vs crème). Phénomène similaire mais cas d'usage opposés.

## ÉTAPE 3 — Clarification sémantique (audit)

**1 entrées** signalées comme potentiellement longues (>350-400 caractères selon type).

Pas de réécriture automatique : risque de perdre du sens scientifique. ChatGPT peut arbitrer si reformulation nécessaire.

### Top 10 entrées les plus longues à reviewer

- **long_principe** (amidon) : `Gélatinisation, gonflement et amincissement de l'amidon` — 516 chars

## ÉTAPE 4 — Métadonnées critiques

Ajout de `niveau_utilite` et `priorite_usage` à **toutes les entrées** selon mapping :

| Type | niveau_utilite | priorite_usage |
|------|----------------|---------------:|
| `erreur` | `action` | 1 |
| `seuil` | `action` | 1 |
| `cause_effet` | `diagnostic` | 2 |
| `systeme` | `comprehension` | 3 |

## ÉTAPE 5 — Dédoublonnage conceptuel (variantes)

Le pattern `1 concept = 1 entrée principale + variantes[]` a été appliqué dans 3 fusions de l'étape 2 :

- **Pasteurisation** : 60°C 5min ↔ 70°C 1min (équivalence bactériologique)
- **Myosine** : viande ↔ poisson (même T, conséquences distinctes)
- **Caramélisation** : fructose, glucose, saccharose, lactose (paramètres par sucre)

## ÉTAPE 6 — Optimisation RAG

Nettoyage cosmétique : 297 champs nettoyés (espaces, ponctuation).

**Pas de réécriture massive** : préserver la précision scientifique l'emporte sur la concision artificielle. Les entrées identifiées en étape 3 peuvent faire l'objet d'une review ChatGPT ciblée.

## ÉTAPE 7 — Tests de robustesse

Simulation de 3 cas types pour vérifier que la base couvre les usages prioritaires :

### ✅ Test : Utilisateur en panique : 'ma sauce hollandaise a tranché'

- Type d'entrée attendu : `erreur`
- Matches trouvés : **3**
- Exemple de match : _Hollandaise tranchée pendant la cuisson_

### ✅ Test : Utilisateur curieux : 'pourquoi mon saumon est-il toujours sec ?'

- Type d'entrée attendu : `cause_effet`
- Matches trouvés : **2**
- Exemple de match : _Cuisson d'un poisson à T cœur >65°C_

### ✅ Test : Utilisateur apprenant : 'comment fonctionne le tempérage du chocolat ?'

- Type d'entrée attendu : `systeme`
- Matches trouvés : **1**
- Exemple de match : _Tempérage du chocolat_
