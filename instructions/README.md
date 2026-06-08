# Instructions — prompts système standardisés

Un prompt système par plateforme. La **logique métier est identique** dans les trois ; seule la section
d'interaction avec Google Drive change (chaque plateforme expose des outils différents).

| Fichier | Plateforme | Où coller |
|---|---|---|
| `gemini.md` | Google Gemini (Gems) | Champ **Instructions** ; knowledge = les **9 bundles** de `../gem-gemini/` (Gem limité à ~10 fichiers) |
| `claude.md` | Anthropic Claude (Projects) | **Custom instructions** ; knowledge = les **20 fichiers** de `../knowledge/` |
| `chatgpt.md` | OpenAI ChatGPT (Custom GPT / Projects) | Champ **Instructions** ; knowledge = les **20 fichiers** de `../knowledge/` |

> ⭐ `knowledge/10-securite-alimentaire.md` fait autorité sur la sécurité (la sécurité prime sur les repères de texture).

## ⚙️ Placeholders à remplacer

Chaque fichier commence par un bloc de configuration. Remplacez ces marqueurs par vos propres valeurs
avant de coller le prompt :

| Placeholder | Rôle | Exemple |
|---|---|---|
| `{{INVENTORY_DOC}}` | Nom exact de votre document Drive d'inventaire | `Inventaire_Cuisine_Actuel` |
| `{{RECIPE_PREFIX}}` | Préfixe de nommage des fiches recette (sert aussi à la recherche) | `Recette :` |
| `{{PROFILE_PREFIX}}` | Préfixe du document de profil cuisinier | `Profil_Cuisinier_` |

> Aucun lien Drive personnel n'est inclus : l'agent identifie vos documents **par leur nom**, pas par URL.

## Accès Google Drive

Les quatre modes (Inventaire, Sauvegarde, Bibliothèque, Profil) supposent un accès en lecture/écriture à Drive :

- **Gemini** : extension Google Workspace activée sur le Gem (natif).
- **Claude** : connecteur Google Drive (Settings → Connectors) ou serveur MCP.
- **ChatGPT** : connecteur Google Drive (Project) ou Action OpenAPI (Custom GPT).

Sans connecteur, les versions Claude et ChatGPT basculent automatiquement en **mode manuel** : l'agent
génère la fiche recette en Markdown et vous la copiez vous-même dans Drive. La version Gemini suppose
l'extension Workspace présente.

## Les 4 modes documentaires

1. **Inventaire (vide-frigo)** — lit votre doc d'inventaire, propose une idée 100 % réalisable.
2. **Sauvegarde** — archive une recette au format fiche structuré (ingrédients, mode opératoire, verdict, adaptations).
3. **Bibliothèque** — retrouve et restitue vos recettes archivées.
4. **Profil cuisinier** — distille vos recettes en patterns personnels réutilisables silencieusement.
