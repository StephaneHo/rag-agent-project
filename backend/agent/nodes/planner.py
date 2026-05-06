"""Nœud planner — décide de la première action.

Responsabilité :
    - Reçoit la query utilisateur.
    - Décide si on doit chercher dans ArXiv directement, ou poser une sous-question.
    - Log la décision (cf. guardrails.log_decision).

Signature attendue :
    def planner_node(state: AgentState) -> dict:
        ...

POURQUOI ce nœud ?
    En agentic, le LLM ne *fait* pas la recherche directement. Il **planifie**.
    Séparer plan / exécution rend la trace lisible : "le LLM a choisi X parce que Y,
    puis le retriever a exécuté X". C'est ça la transparence agent — argument fort
    pour un cas défense.
"""
