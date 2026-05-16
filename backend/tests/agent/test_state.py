from agent.state import AgentState

"""Tests de la structure AgentState — Red en premier !

POURQUOI commencer par les tests du state ?
    Le state est le contrat. Si tu changes sa forme après avoir écrit des nœuds,
    tu casses tout. Lock-le d'abord, code les nœuds après.

Tests à écrire :
    test_state_can_be_initialized_with_only_a_query
        Un AgentState doit être valide avec juste {"query": "..."}.
        POURQUOI : le point d'entrée du graphe ne fournira que ça.

    test_state_retrieved_docs_defaults_to_empty_list
        Pas None, liste vide.
        POURQUOI : éviter `if state.get("retrieved_docs")` partout dans les nœuds.

    test_state_iteration_defaults_to_zero
        POURQUOI : le kill switch compare à un max ; un None planterait.

    test_state_decisions_log_is_a_list_of_dicts
        POURQUOI : on veut pouvoir faire `state["decisions_log"].append({...})`.
"""


def test_state_can_be_initialized_with_only_a_query():
    state = AgentState(query="...")
    assert state["query"] == "..."
