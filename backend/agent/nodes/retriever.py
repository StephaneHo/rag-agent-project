"""Nœud retriever — appelle le tool arxiv_retrieval et range les docs dans le state.

Responsabilité :
    - Lit state["query"] (ou la sous-query décidée par le planner).
    - Appelle tools.arxiv_retrieval.search(query).
    - Append les chunks à state["retrieved_docs"].
    - Log la décision.

PIÈGE :
    Pas de filtrage / re-ranking ici. Ce nœud doit rester un simple wrapper
    autour du tool. Le re-ranking, si besoin, sera un nœud séparé plus tard.
"""
