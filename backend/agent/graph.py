"""Assemblage du StateGraph LangGraph.

À implémenter en DERNIER : tu n'assembles que quand State + nœuds + edges
sont déjà testés unitairement.

À implémenter :
    build_graph() -> CompiledGraph
        - StateGraph(AgentState)
        - add_node("planner",      planner_node)
        - add_node("retrieve",     retriever_node)
        - add_node("reformulate",  reformulator_node)
        - add_node("web_search",   web_search_node)
        - add_node("synthesize",   synthesizer_node)
        - add_node("validate",     validator_node)
        - set_entry_point("planner")
        - add_conditional_edges("retrieve", route_after_retrieval, {…})
        - add_conditional_edges("validate", route_after_validation, {…})
        - compile()

    run(query: str) -> dict
        Point d'entrée pour l'API. Initialise un AgentState minimal,
        invoke le graphe, retourne {answer, citations, decisions_log}.
"""
