"""Nœuds du graphe agent.

Convention : 1 fichier = 1 nœud. Chaque nœud est une fonction
    node(state: AgentState) -> dict (partial update).

Ordre d'implémentation suggéré (TDD) :
    1. planner       (le plus simple : pose la question, log la décision)
    2. retriever     (appelle le tool arxiv_retrieval)
    3. synthesizer   (sort une réponse — premier graphe end-to-end)
    --- premier happy path bout-en-bout ici ---
    4. reformulator  (gère les cas "rien trouvé")
    5. web_searcher  (fallback)
    6. validator     (citations + faithfulness)
"""
