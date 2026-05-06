"""Tests d'intégration : le graphe bout-en-bout, avec LLM mocké.

À ÉCRIRE EN DERNIER — quand tout le reste (state, edges, nœuds, tools) est vert.

Tests à écrire :
    test_happy_path_returns_answer_with_citations
        Mock le LLM pour qu'il réponde "X [src1]". Vérifie qu'on a une réponse
        ET au moins une citation valide.

    test_killswitch_caps_iterations
        Mock le retriever pour qu'il renvoie toujours vide. Vérifie qu'on n'itère
        pas plus que max_iterations.

    test_decisions_log_is_populated
        Vérifie qu'au moins N entrées sont présentes après un run réussi.

POURQUOI mocker le LLM ?
    - Tests reproductibles (LLM = non déterministe).
    - Pas de coût.
    - Tests rapides (CI).
    Garde un test E2E sans mock pour la démo, mais HORS de la suite CI.
"""
