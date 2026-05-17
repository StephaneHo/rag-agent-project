from agent.state import make_initial_state


def test_state_can_be_initialized_with_only_a_query():
    state = make_initial_state(query="...")
    assert state["query"] == "..."


def test_state_retrieved_docs_defaults_to_empty_list():
    state = make_initial_state(query="...")
    assert state["retrieved_docs"] == []
