# Rapport de normalisation `assaisonnement_v1`

## Résumé

- Nombre de règles dans le lot normalisé : `36`
- Suppressions pour doublon évident : `0`
- Erreurs JSON : `0`
- Doublons exacts contre `final` : `0`
- Quasi-doublons contre `final` : `0`
- Décision : `prêt pour audit`

Le lot a été normalisé sans ajout de règles ni enrichissement métier. La passe a porté sur :

- la clarté des formulations ;
- la réduction des termes trop abstraits ;
- la simplification de certaines règles trop conceptuelles ;
- le maintien de la frontière entre `assaisonnement` et `rattrapage`.

## Fichier produit

- `04_rules/normalized/assaisonnement/assaisonnement_v1_normalized.jsonl`

## Validation structure

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/validate_jsonl.py \
cuisine-ai-knowledge/04_rules/normalized/assaisonnement/assaisonnement_v1_normalized.jsonl
```

Résultat :

- validation : `OK`
- enregistrements validés : `36`
- erreurs : `0`

## Détection de doublons

Commande exécutée :

```bash
python3 cuisine-ai-knowledge/08_scripts/detect_duplicates.py \
cuisine-ai-knowledge/04_rules/normalized/assaisonnement/assaisonnement_v1_normalized.jsonl \
cuisine-ai-knowledge/04_rules/final \
--report cuisine-ai-knowledge/07_tests/reports/assaisonnement_v1_normalized_duplicates.md
```

Résultat :

- doublons exacts : `0`
- quasi-doublons : `0`

Le lot normalisé ne collisionne pas avec les lots déjà publiés dans `final`.

## Nettoyage éditorial réalisé

Les principales corrections ont visé :

- les titres trop conceptuels ;
- les formulations trop générales ;
- les règles qui mélangeaient plusieurs idées ;
- les expressions peu actionnables.

Sous-ensemble retouché :

- `ASSAISONNEMENT_POIVRE_002`
- `ASSAISONNEMENT_SUCRE_001`
- `ASSAISONNEMENT_AMERTUME_002`
- `ASSAISONNEMENT_HERBES_SECHES_002`
- `ASSAISONNEMENT_EPICES_001`
- `ASSAISONNEMENT_ALCOOL_001`
- `ASSAISONNEMENT_ALCOOL_002`
- `ASSAISONNEMENT_EQUILIBRE_003`
- `ASSAISONNEMENT_DEGUSTATION_001`

Effets de la normalisation :

- moins de vocabulaire flou ;
- gestes plus concrets ;
- meilleure séparation entre diagnostic, procédure et erreur à éviter ;
- meilleure cohérence avec un usage agentique.

## Règles encore un peu abstraites

Les règles suivantes restent utilisables mais devront être relues à l'audit :

- `ASSAISONNEMENT_AMERTUME_002`
  Le levier de `rondeur` est plus concret qu'avant, mais reste un peu interprétatif.

- `ASSAISONNEMENT_EPICES_001`
  Bonne règle, mais encore assez générale car elle repose sur la définition du rôle de l'épice.

- `ASSAISONNEMENT_ALCOOL_001`
  La règle est plus nette, mais le sous-ensemble `alcool` reste plus contextuel que le coeur du lot.

- `ASSAISONNEMENT_ALCOOL_002`
  Claire, mais proche conceptuellement de `ALCOOL_001`.

## Règles faibles à surveiller

- `ASSAISONNEMENT_POIVRE_002`
- `ASSAISONNEMENT_AMERTUME_002`
- `ASSAISONNEMENT_ALCOOL_001`
- `ASSAISONNEMENT_ALCOOL_002`

Ces règles ne sont pas mauvaises, mais elles sont moins universelles ou moins immédiatement concrètes que le noyau fort du lot.

## Chevauchements avec `rattrapage`

Le lot normalisé reste globalement dans une logique de :

- prévention ;
- construction du goût ;
- diagnostic précoce ;
- ajustement progressif.

Le risque de recouvrement avec `rattrapage` existe surtout sur :

- `ASSAISONNEMENT_SUCRE_001`
- `ASSAISONNEMENT_AMERTUME_002`
- `ASSAISONNEMENT_EQUILIBRE_003`

Mais ces règles restent côté `assaisonnement` car elles parlent encore d'ajustements mesurés, pas de réparation d'un échec déjà installé.

## Problèmes de clarté restants

- proximité éditoriale entre `equilibre_global`, `assaisonnement_progressif` et `degustation_ajustement`
- sous-ensemble `alcool` plus contextuel et moins central
- quelques règles encore plus fortes sur le diagnostic que sur l'action

Ces points ne bloquent pas la suite, mais devront être arbitrés dans l'audit.

## Conclusion

Le lot `assaisonnement_v1_normalized.jsonl` est structurellement propre, éditorialement resserré et sans doublon détecté contre `final`.

Décision :

`prêt pour audit`
