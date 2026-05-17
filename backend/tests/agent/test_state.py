from agent.state import make_initial_state


def test_state_can_be_initialized_with_only_a_query():
    state = make_initial_state(query="...")
    assert state["query"] == "..."


def test_state_retrieved_docs_defaults_to_empty_list():
    state = make_initial_state(query="...")
    assert state["retrieved_docs"] == []


def test_state_iteration_defaults_to_zero():
    state = make_initial_state(query="...")
    assert state["iteration"] == 0


def test_state_decisions_log_is_appendable():
    state = make_initial_state(query="...")
    state["decisions_log"].append({"node": "planner", "decision": "search"})
    assert state["decisions_log"] == [{"node": "planner", "decision": "search"}]
