"""Tests des edges (routage conditionnel) — pas besoin de LLM ici.

POURQUOI les edges en premier (avant les nœuds) ?
    Ce sont des fonctions pures qui prennent un dict et renvoient une string.
    Trivial à tester. Ça te force à clarifier la logique de l'agent AVANT
    de te perdre dans les appels LLM.

Tests à écrire :
    test_route_after_retrieval_goes_to_synthesize_when_docs_present
    test_route_after_retrieval_goes_to_reformulate_when_empty_first_try
    test_route_after_retrieval_goes_to_web_when_already_reformulated
    test_route_after_retrieval_ends_when_killswitch
    test_route_after_validation_ends_when_ok
    test_route_after_validation_loops_back_when_validation_fails
"""
