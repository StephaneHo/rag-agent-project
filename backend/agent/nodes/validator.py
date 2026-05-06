"""Nœud validator — vérifie que la réponse est citée et grounded.

Responsabilité :
    - Vérifie has_citations(state) (cf. guardrails).
    - Mesure faithfulness (cf. monitoring.measure_faithfulness).
    - Si KO : log + l'edge de routage relance reformulation.
    - Si OK : laisse le state, l'edge route vers END.

POURQUOI un nœud, pas juste une fonction d'edge ?
    Les edges renvoient juste une route (string). Le validator écrit dans le state
    (decisions_log, faithfulness_score) — donc c'est un nœud à part entière.
"""
