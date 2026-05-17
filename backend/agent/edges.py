def route_after_retrieval(state) -> str:
    if state["retrieved_docs"]:
        return "synthesize"
    # "synthesize"   si retrieved_docs non vide
    # "reformulate"  si vide ET iteration < max ET pas encore reformulé
    # "web_search"   si reformulation déjà tentée
    # END            si kill switch


def route_after_validation(state) -> str:
    pass
    # END            si validation OK
    # "reformulate"  sinon
