"""Tests du nœud planner — premier nœud à coder.

POURQUOI ce nœud d'abord ?
    Le planner est le plus simple à mocker (1 appel LLM, pas de DB, pas de web).
    Premier nœud à passer en vert = première vraie victoire LangGraph.

Tests à écrire :
    test_planner_appends_a_decision_to_log
        Avec un LLM mocké qui renvoie "search arxiv", vérifier que decisions_log
        contient une entrée avec node="planner".

    test_planner_returns_partial_state_update_not_full_state
        POURQUOI : un nœud LangGraph doit renvoyer un dict d'updates, pas le
        state complet. Vérifier que les autres champs ne sont pas dans le retour.

    test_planner_does_not_mutate_input_state
        POURQUOI : la convention LangGraph est immutable. Mutation = bugs subtils.
"""
