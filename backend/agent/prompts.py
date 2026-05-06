"""Prompts LLM utilisés par les nœuds du graphe.

POURQUOI centraliser ?
    Un prompt audité au même endroit que le code = relecture facile (utile pour
    un cas d'usage défense). Versioning, A/B tests, détection de régression
    deviennent possibles.

À implémenter (constantes ou fonctions de rendu) :
    PLANNER_SYSTEM      — guide le nœud planner (que chercher d'abord ?)
    REFORMULATOR_SYSTEM — réécrit la query si la première recherche n'a rien donné
    SYNTHESIZER_SYSTEM  — synthèse finale, doit IMPOSER le format "réponse + citations"
    VALIDATOR_SYSTEM    — vérifie que la réponse cite ses sources (judge prompt)
"""
