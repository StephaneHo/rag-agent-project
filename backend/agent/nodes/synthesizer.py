"""Nœud synthesizer — produit la réponse finale avec citations.

Responsabilité :
    - Prend state["query"], state["retrieved_docs"], state["web_results"].
    - Appelle le LLM avec SYNTHESIZER_SYSTEM (cf. prompts.py).
    - Le prompt DOIT imposer le format "réponse + liste de citations [src_id]".
    - Met state["final_answer"] et state["citations"].

POURQUOI les citations sont-elles imposées par PROMPT puis VÉRIFIÉES par le validator ?
    Belt and suspenders. Le prompt rate parfois. Le validator est le filet de sécurité.
    Ne jamais faire confiance à un LLM seul pour un invariant critique.
"""
