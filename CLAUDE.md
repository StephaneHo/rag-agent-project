# CLAUDE.md — instructions pour Claude

## Contexte du projet

Évolution d'un RAG existant vers un **agentic RAG** (LangGraph) sur un cas d'usage de
veille documentaire défense (papiers ArXiv AI/ML/cybersec à orientation défense).

Projet d'apprentissage personnel dans le cadre d'un process de recrutement
**Capgemini Défense** (CDI consultant 70/30, suite à un entretien avec Vincent Moreau,
expert agents IA). Délai cible : 1 à 2 semaines.

L'utilisateur connaît bien le RAG classique (cf. projet jumeau `rag-project`,
au même niveau hiérarchique). Il découvre les agents et veut **comprendre LangGraph
en profondeur**, pas juste l'utiliser.

## Mode de collaboration

### Pédagogie d'abord
- Toujours **POURQUOI avant COMMENT**.
- Avant d'écrire du code, expliquer le concept LangGraph en jeu (state machine,
  nœud pur, edge conditionnel, merge de state, …) et le piège qu'il évite.

### TDD strict
- **Red → Green → Refactor**, sans exception.
- Pour chaque nouveau comportement : écrire d'abord le test qui échoue, puis
  l'implémentation minimale qui le fait passer, puis refactor.
- Ne jamais écrire d'implémentation "au cas où" sans test qui la justifie.
- Ordre d'attaque suggéré : `state.py` → `edges.py` → `guardrails.py` → `nodes/planner.py`
  → `tools/arxiv_retrieval.py` → `nodes/retriever.py` → `nodes/synthesizer.py`
  → premier graphe end-to-end → reformulator → web_searcher → validator.

### Squelettes avec trous
- Quand l'utilisateur demande un module, livrer **la structure et les signatures,
  pas le corps**.
- Préférer `raise NotImplementedError("...")` ou `...` avec un docstring d'intention,
  plutôt qu'une implémentation clé en main.
- L'utilisateur veut coder lui-même — son apprentissage passe par l'écriture,
  pas la lecture.

### Tests d'intégration vs mocks
- Pour les tools qui touchent une DB (pgvector) : tests d'intégration avec
  vraie DB seedée. **Pas de mocks.** (Mocks DB → bugs prod cachés.)
- Pour les nœuds qui appellent un LLM : mocks (reproductible, gratuit, rapide).
- Test E2E sans mock = OK pour la démo, hors suite CI.

## Architecture du projet

Voir `README.md` pour le plan haut niveau. Code à coder dans `backend/agent/`.
La couche RAG d'origine (`backend/rag/`) a été supprimée volontairement — elle est
remplacée from scratch par `backend/agent/` pour permettre la comparaison directe
RAG basique vs agentic RAG sur le même corpus ArXiv.

## Cas d'usage défense — à garder en tête

- **Auditabilité** : chaque décision de l'agent doit être loggée et inspectable
  (cf. `agent/guardrails.py::log_decision`).
- **Citations obligatoires** : pas de réponse sans source citée et VÉRIFIÉE.
- **Web search** : documenter ce qui sort en clair (point bloquant en déploiement
  réel défense).
