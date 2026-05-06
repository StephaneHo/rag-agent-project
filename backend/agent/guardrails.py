"""Garde-fous transverses (citations obligatoires, kill switch, logs).

POURQUOI séparé des nœuds ?
    Les garde-fous sont des invariants — ils s'appliquent partout. Les noyer
    dans les nœuds = duplication + risque d'oublier un cas. Centralisés, ils
    sont auditables (important pour un cas d'usage défense).

À implémenter :
    has_citations(state) -> bool
        Vérifie qu'au moins une citation référence un retrieved_doc connu.
        ATTRAPE LES HALLUCINATIONS de références (cas concret : le LLM invente
        une source qui n'existe pas dans retrieved_docs).

    is_killswitch_triggered(state, max_iterations: int = 5) -> bool
        True si state["iteration"] >= max_iterations.

    log_decision(state, *, node: str, decision: str, why: str) -> dict
        Renvoie un dict d'update à append à state["decisions_log"].
        Format : {"ts", "node", "decision", "why", "iteration"}.
"""
