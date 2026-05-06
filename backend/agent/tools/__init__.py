"""Tools (capacités) appelables par les nœuds du graphe.

Différence nœud / tool :
    - Un nœud orchestre (lit state, log, route).
    - Un tool exécute une capacité technique (cherche dans une DB, appelle une API).
    Le nœud appelle un ou plusieurs tools.

Convention : un tool est une fonction pure, sans dépendance au state.
    Cela les rend réutilisables (CLI, exposition MCP, tests unitaires).
"""
