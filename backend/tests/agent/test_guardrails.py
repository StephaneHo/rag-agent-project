"""Tests des garde-fous (citations, kill switch, log_decision).

Tests à écrire :
    test_has_citations_true_when_at_least_one_match
    test_has_citations_false_when_citation_references_unknown_source
        POURQUOI : le LLM peut HALLUCINER une référence. C'est exactement ce
        que ce guard doit attraper. Test critique.

    test_killswitch_not_triggered_when_below_max
    test_killswitch_triggered_when_at_max
    test_killswitch_triggered_when_above_max  # robustesse

    test_log_decision_returns_well_formed_entry
        Vérifie les clés : ts, node, decision, why, iteration.

    test_log_decision_does_not_mutate_existing_log
        POURQUOI : les nœuds doivent renvoyer des updates immutables, pas
        muter le state directement (sinon LangGraph perd le contrôle).
"""
