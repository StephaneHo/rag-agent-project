# rag-agent-project

> Évolution d'un RAG vers un **agentic RAG** (LangGraph) pour la veille
> documentaire défense.

## Pourquoi ce projet

Démontrer une montée en compétence rapide sur les **agents IA** dans le cadre d'un
process de recrutement Capgemini Défense (CDI consultant 70/30, suite à un
entretien avec Vincent Moreau, expert agents IA).

Cas d'usage : veille documentaire défense via des papiers ArXiv (AI / ML /
cybersec à orientation défense).

## Capacités cibles

- **Boucle agentique** : le LLM décide quoi chercher, reformule si rien
  trouvé, croise plusieurs sources.
- **Multi-tools** : retrieval ArXiv (pgvector) + recherche web + synthèse
  avec citations.
- **Garde-fous** :
  - citations sources obligatoires en sortie ;
  - *kill switch* (timeout / nb max d'itérations) ;
  - logs structurés des décisions de l'agent.
- **Monitoring** : tracer chaque appel d'outil, mesurer la *faithfulness*
  des réponses.

## Stack

- **Couche agent** : LangGraph (state machine, nœuds, edges conditionnels) ;
  MCP envisagé pour brancher des outils si pertinent.
- **LLM** : à choisir (Anthropic Claude par défaut).
- **Backend** : Python 3.12, FastAPI.
- **Stockage** : PostgreSQL + pgvector.
- **Embeddings** : sentence-transformers.
- **Tracking** : MLFlow.
- **Déploiement** : Docker / Docker Compose.
- **Source** : ingestion ArXiv (existante, héritée de `rag-project`).

## Architecture cible

```
backend/
├── agent/                      # à coder en TDD : couche LangGraph
│   ├── state.py                # AgentState (state machine)
│   ├── nodes/                  # 1 fichier = 1 nœud du graphe
│   │   ├── planner.py
│   │   ├── retriever.py
│   │   ├── reformulator.py
│   │   ├── web_searcher.py
│   │   ├── synthesizer.py
│   │   └── validator.py
│   ├── tools/                  # capacités appelables par les nœuds
│   │   ├── arxiv_retrieval.py
│   │   └── web_search.py
│   ├── edges.py                # routage conditionnel
│   ├── graph.py                # assemblage final
│   ├── guardrails.py           # kill switch, citations obligatoires
│   ├── monitoring.py           # traces, faithfulness
│   └── prompts.py              # prompts par nœud
├── tests/agent/                # tests Red→Green→Refactor
├── api/                        # FastAPI (hérité)
├── collectors/                 # ArXiv (hérité)
├── pipeline/                   # ingestion (hérité)
└── database/                   # pgvector (hérité)
```

## Roadmap (cible 1-2 semaines)

| Semaine | Objectif |
|---------|----------|
| S1 | State + edges + 3 nœuds (planner, retriever, synthesizer) — happy path bout-en-bout |
| S2 | Reformulation, fallback web, garde-fous, monitoring, démo enregistrée |

## Démarrage rapide

```bash
# 1. PostgreSQL + pgvector
docker compose up db -d
docker compose ps   # db doit être "healthy"

# 2. FastAPI
cd backend
uv run uvicorn api.app:app --reload --port 8000
```

Pour les tests unitaires de la couche agent (à coder) :

```bash
cd backend
uv run pytest tests/agent
```

## Hérité de `rag-project`

L'infrastructure (ingestion ArXiv, store pgvector, FastAPI shell, Docker)
provient du projet précédent. La couche `backend/rag/` a été supprimée
volontairement — elle est remplacée *from scratch* par `backend/agent/`.
Cela permet une comparaison directe **RAG basique vs agentic RAG** sur le
même corpus, ce qui est aussi le récit de démo : "même infra, une couche
agent, voici ce que ça change".

## Mode de travail (cf. `CLAUDE.md`)

- POURQUOI avant COMMENT (pédagogique).
- TDD strict, Red → Green → Refactor.
- Squelettes avec trous : Claude livre les structures et docstrings, l'utilisateur
  code l'implémentation.
