# Rapport anti-pollution `escoffier_v1`

## Contrôles réalisés

- pas de recettes longues recopiées ;
- pas de proportions historiques recopiées dans les JSONL ;
- pas de copier-coller massif du texte source ;
- pas de fichier unique encyclopédique ;
- pas de duplication exacte détectée contre `04_rules/final` ;
- pas de duplication exacte détectée contre `04_rules/raw/techniques_cap` ;
- vocabulaire systématiquement reformulé vers un usage agent IA ;
- procédés sensibles comme `saumure` traités avec prudence et sans détail opératoire risqué.

## Résultat par lot

- `escoffier_principes_v1_raw.jsonl`
  - doublons exacts : `0`
  - quasi-doublons : `51`
- `escoffier_systemes_v1_raw.jsonl`
  - doublons exacts : `0`
  - quasi-doublons : `124`
- `escoffier_associations_v1_raw.jsonl`
  - doublons exacts : `0`
  - quasi-doublons : `88`
- `escoffier_patterns_v1_raw.jsonl`
  - doublons exacts : `0`
  - quasi-doublons : `31`
- `escoffier_vocabulaire_v1_raw.jsonl`
  - doublons exacts : `0`
  - quasi-doublons : `0`

## Lecture des quasi-doublons

Les quasi-doublons viennent surtout de trois phénomènes normaux :

- proximité logique entre `cuisson`, `rattrapage`, `assaisonnement` et les principes Escoffier ;
- voisinage interne entre plusieurs systèmes classiques proches ;
- reformulations volontairement voisines entre une règle de principe et sa traduction domestique.

Ils ne signalent pas, à ce stade, un copier-coller brut du corpus existant.

## Risques encore présents

- un bruit conceptuel réel sur les familles `fonds`, `réduction`, `liaison`, `finition` ;
- un risque de surdensité sur `systemes` si la prochaine passe ne fusionne pas certains blocs ;
- quelques termes historiques encore trop ambitieux pour un usage purement domestique si on ne filtre pas à l'étape Gemini ou normalisation.

## Conclusion

Le lot reste compatible avec l'objectif du projet :

- il apporte une grammaire classique utile ;
- il ne transforme pas la base en livre de recettes ;
- il demande en revanche une vraie normalisation éditoriale avant tout passage ultérieur.
