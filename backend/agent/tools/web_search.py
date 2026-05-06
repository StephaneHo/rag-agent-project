"""Tool : recherche web (fallback quand ArXiv n'a rien).

Signature attendue :
    def search(query: str, k: int = 3) -> list[dict]:
        '''Renvoie k résultats web. Format : {title, url, snippet}'''

Choix d'implémentation possibles :
    - DuckDuckGo (lib `duckduckgo-search`) — gratuit, pas de clé API.
    - Tavily — meilleur pour usage agent, mais clé API requise.

ATTENTION :
    Logger les requêtes et les domaines retournés (audit + démo défense).
"""
