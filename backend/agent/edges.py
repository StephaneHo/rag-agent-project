"""Logique de routage conditionnel entre nœuds.

POURQUOI un fichier dédié ?
    Dans LangGraph, un *conditional edge* est une fonction qui prend un State
    et renvoie le nom du prochain nœud (ou END). C'est la **logique de l'agent**.
    La sortir des nœuds permet de la tester sans LLM — tests purs, rapides.

À implémenter :
    route_after_retrieval(state) -> str
        - "synthesize"   si retrieved_docs non vide
        - "reformulate"  si vide ET iteration < max ET pas encore reformulé
        - "web_search"   si reformulation déjà tentée
        - END            si kill switch

    route_after_validation(state) -> str
        - END            si validation OK (citations présentes, faithful)
        - "reformulate"  sinon (la réponse n'est pas grounded)

PIÈGE :
    Tester les edges avant les nœuds = trivial. Profite-en pour clarifier ta
    logique d'agent avant de te perdre dans le LLM.
"""
