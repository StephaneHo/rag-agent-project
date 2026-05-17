from agent.edges import route_after_retrieval
from agent.state import make_initial_state


def test_route_after_retrieval_goes_to_synthesize_when_docs_present():
    # 1. ARRANGE : fabrique le state qui doit déclencher la décision
    state = make_initial_state(query="...")
    state["retrieved_docs"] = ["whatever"]

    # 2. ACT : appelle la fonction de routage
    decision = route_after_retrieval(state)

    # 3. ASSERT : vérifie la décision
    assert decision == "synthesize"
