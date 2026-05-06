"""Couche agentique du RAG basée sur LangGraph.

Décomposition (à compléter) :
    state.py      — AgentState : structure de données qui circule dans le graphe
    nodes/        — un fichier = un nœud du graphe (fonction State -> partial State)
    tools/        — capacités appelables par les nœuds (retrieval, web, …)
    edges.py      — logique de routage conditionnel entre nœuds
    graph.py      — assemblage final du StateGraph LangGraph
    guardrails.py — kill switch, citations obligatoires, validations
    monitoring.py — traces structurées, métriques (faithfulness)
    prompts.py    — prompts LLM par nœud
"""
