"""Traces et métriques d'exécution agent.

À implémenter :
    trace_tool_call(tool_name, inputs, outputs, latency_ms)
        Émet une trace (MLFlow, OpenTelemetry, ou simple JSON log).
        Permet de répondre à : "combien de fois l'agent a appelé arxiv_retrieval ?
        avec quelles requêtes ? quelle latence ?"

    measure_faithfulness(answer: str, citations: list, retrieved_docs: list) -> float
        Score [0,1]. Approches possibles :
        - règles  : % d'affirmations dont une citation existe ;
        - LLM-judge : prompt un LLM pour évaluer.
        COMMENCE PAR LES RÈGLES (mesurable, déterministe, gratuit).

PIÈGE :
    Tenter le LLM-judge en premier = coût + flakiness. Garde-le pour plus tard.
"""
