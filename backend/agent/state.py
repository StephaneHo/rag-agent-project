"""État partagé du graphe agent (AgentState).

POURQUOI ce fichier en premier ?
    LangGraph est une *state machine*. Chaque nœud reçoit un State et renvoie
    une mise à jour partielle (LangGraph la merge). Le State est donc le contrat
    de tout le graphe : si tu changes sa forme à mi-chemin, tu casses tous les
    nœuds. Verrouille-le avant d'écrire un seul nœud.

À implémenter :
    AgentState — TypedDict (recommandé pour LangGraph) avec, a priori :
        - query           : str        — question utilisateur d'origine
        - messages        : list       — historique conversationnel (LLM-friendly)
        - retrieved_docs  : list       — chunks ramenés du store ArXiv
        - web_results     : list       — résultats du fallback web (si déclenché)
        - citations       : list       — sources que la réponse finale doit citer
        - decisions_log   : list[dict] — trace structurée des décisions de l'agent
        - iteration       : int        — compteur (kill switch)
        - final_answer    : str | None — None tant que pas synthétisé

PIÈGE CLASSIQUE :
    Mettre des dicts profondément imbriqués. Le merge LangGraph se fait au niveau
    racine ; les sous-objets mutables = headaches. Garde plat.
"""

from typing import TypedDict


class AgentState(TypedDict):
    query: str
