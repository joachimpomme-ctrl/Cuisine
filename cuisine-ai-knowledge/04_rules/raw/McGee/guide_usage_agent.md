# Guide d'usage agent — McGee Knowledge Base

> Documentation pour intégration dans agent IA (Gemini, ChatGPT, Claude).

> Corpus : **421 entrées**, 4 types, 21 domaines.

## Philosophie d'appel

La base est un **moteur de réponse hiérarchisé**. Pour chaque requête utilisateur, l'agent doit :

1. **Classer la requête** dans une des 3 catégories d'usage
2. **Filtrer les entrées** par `niveau_utilite` et/ou `priorite_usage`
3. **Combiner les types** dans la réponse selon le besoin

## Mapping requête → type d'entrée

| Forme de la requête utilisateur | Type cible | Priorité |
|--------------------------------|-----------|---------:|
| « ma X a raté », « j'ai un problème avec », « comment rattraper » | `erreur` | 1 |
| « à quelle température », « combien de temps », « jusqu'à quel pH » | `seuil` | 1 |
| « pourquoi », « qu'est-ce qui fait que », « explique-moi pourquoi » | `cause_effet` | 2 |
| « comment fonctionne », « explique-moi le mécanisme », « théorie de » | `systeme` | 3 |

## Stratégie de réponse selon priorité

### Priorité 1 — Action immédiate

**Quand l'utilisateur a besoin d'une décision maintenant** (panique en cuisine, T à régler).

- Récupérer **uniquement** les `erreur` ou `seuil` du domaine pertinent
- Réponse courte et directe, format checklist
- Pas d'explication scientifique en première intention
- _Optionnel_ : proposer en fin de réponse un complément de type `cause_effet` ou `systeme`

### Priorité 2 — Diagnostic

**Quand l'utilisateur veut comprendre POURQUOI un phénomène se produit.**

- Récupérer les `cause_effet` du domaine
- Réponse structurée : cause → effet → explication mécanistique courte
- Combiner avec un `systeme` connexe pour ancrer la compréhension

### Priorité 3 — Compréhension fondamentale

**Quand l'utilisateur veut apprendre un mécanisme.**

- Récupérer le `systeme` pertinent
- Réponse longue, structurée par sections (principe, règles pratiques, applications)
- Lien vers les `cause_effet` qui en découlent

## Exemple de routage RAG

```python
def route_query(user_query: str, kb: list[dict]) -> list[dict]:
    # 1. Détection d'intention
    if any(w in user_query.lower() for w in ['raté', 'problème', 'comment rattraper', 'comment éviter']):
        target_type, target_prio = 'erreur', 1
    elif any(w in user_query.lower() for w in ['à quelle température', 'combien', 'jusqu\'à']):
        target_type, target_prio = 'seuil', 1
    elif any(w in user_query.lower() for w in ['pourquoi', 'qu\'est-ce qui fait']):
        target_type, target_prio = 'cause_effet', 2
    else:
        target_type, target_prio = 'systeme', 3
    
    # 2. Filtre par type prioritaire + matching domaine/keywords
    candidates = [e for e in kb if e['type'] == target_type]
    # 3. Vector search/keyword search dans candidates
    return ranked_candidates
```

## Anatomie des entrées

### Entrée `erreur` (priorité 1, action)

```json
{
  "type": "erreur",
  "domaine": "oeuf",
  "probleme": "Œufs durs avec cerne grise/verte autour du jaune",
  "cause": "Cuisson trop longue OU trop chaude OU pas refroidi rapidement",
  "correction": "Œuf moyen: porter à ébullition, couper le feu, COUVRIR, attendre 9-10 min; choc glacé immédiat 5 min; rouler pour craqueler, éplucher sous filet d'eau",
  "niveau_utilite": "action",
  "priorite_usage": 1
}
```

### Entrée `seuil` (priorité 1, action)

```json
{
  "type": "seuil",
  "domaine": "transversal",
  "T_celsius": 60,
  "T_fahrenheit": 140,
  "phenomene": "Pasteurisation des aliments — équivalence temps/température",
  "implication": "Élimine bactéries pathogènes (Salmonella, E.coli, Campylobacter, Listeria) selon binôme T+temps. Choisir selon contrainte thermique du produit.",
  "variantes": [
    {
      "T_celsius": 60,
      "T_fahrenheit": 140,
      "duree": "5 min",
      "usage": "Cuissons douces, sous-vide, jaune d'œuf restant coulant"
    },
    {
      "T_celsius": 70,
      "T_fahrenheit": 158,
      "duree": "1 min",
      "usage": "Cuissons rapides, simmering, blanchiment de viandes"
    }
  ],
  "niveau_utilite": "action",
  "priorite_usage": 1
}
```

### Entrée `cause_effet` (priorité 2, diagnostic)

```json
{
  "type": "cause_effet",
  "domaine": "oeuf",
  "cause": "Œufs surcuits (T cœur >75°C plusieurs minutes)",
  "effet": "Texture caoutchouteuse, blanc qui pleure (jus aqueux), jaune pulvérulent",
  "explication": "Les protéines coagulées trop intensément se contractent fortement et expulsent l'eau retenue dans le réseau, qui se sépare en lambeaux solides + liquide aqueux.",
  "niveau_utilite": "diagnostic",
  "priorite_usage": 2
}
```

### Entrée `systeme` (priorité 3, compréhension)

Voir `corpus_clean.jsonl` pour les exemples complets (souvent volumineux avec champs imbriqués).

## Statistiques

### Par type

| Type | Effectif |
|------|---------:|
| `erreur` | 109 |
| `seuil` | 61 |
| `cause_effet` | 140 |
| `systeme` | 111 |

### Par priorité d'usage

| Priorité | Effectif | Usage |
|---------:|---------:|-------|
| **1** | 170 | Réponse immédiate (erreur, seuil) |
| **2** | 140 | Diagnostic (cause_effet) |
| **3** | 111 | Compréhension (systeme) |

## Bonnes pratiques d'intégration

1. **Validation systématique** : tous nouveaux ajouts doivent passer `schema_clean.json`.
2. **Embeddings séparés par type** : indexer `erreur` à part de `systeme` permet des recherches plus précises (les `systeme` sont longs et noient la similarité sémantique des `erreur` courtes).
3. **Champ-clé pour matching** : `probleme` pour `erreur`, `cause` pour `cause_effet`, `nom` pour `systeme`, `phenomene` pour `seuil`.
4. **Variantes** : toujours dérouler le contenu des `variantes[]` au moment de répondre. Ne pas les présenter comme des sous-entrées séparées.
5. **Domaine comme filtre fort** : la requête mentionne « œuf » → restreindre à `domaine in ['oeuf', 'foam', 'transversal']` avant le vector search.
6. **Chaînage de types** : pour une réponse complète, l'agent peut combiner :
   - `erreur` pour l'action immédiate
   - + `cause_effet` pour expliquer pourquoi
   - + `systeme` (extrait court) pour la compréhension de fond

## Limites connues

- **Source** : Harold McGee, _On Food and Cooking_, édition révisée 2004. Quelques savoirs ont évolué (techniques sous-vide, risque Salmonella, etc.).
- **Couverture inégale** : poisson (63), végétaux (43), œufs (36) très couverts ; viande (8) et sauces (7) plus légers (la majeure partie était déjà dans batch 1, hors corpus actuel).
- **Pas de version anglaise** : tout est en français ; pour multilangue, prévoir une couche de traduction.
- **Pas de quantitatif strict** : les ratios sont indicatifs, pas calibrés à la décimale.
