"""Nœud web_searcher — fallback recherche web si ArXiv n'a rien d'utile.

Responsabilité :
    - Appelle tools.web_search.search(query).
    - Append les résultats à state["web_results"].
    - Log la décision.

ATTENTION (cas d'usage défense) :
    Documenter clairement quel moteur est utilisé et ce qui est envoyé en clair
    sur Internet. Pour une démo c'est OK, pour un déploiement réel ça peut être
    un point bloquant — mentionner dans le README et la démo.
"""
