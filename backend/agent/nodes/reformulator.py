"""Nœud reformulator — réécrit la query quand le retriever n'a rien trouvé.

Responsabilité :
    - Vérifie state["retrieved_docs"] vide ET iteration < max.
    - Demande au LLM de reformuler state["query"] (synonymes, élargissement…).
    - Met à jour state["query"], incrémente state["iteration"].
    - Log la décision avec la NOUVELLE query (auditabilité).

POURQUOI un nœud séparé du planner ?
    Le planner décide la première action. Le reformulator gère le cas "ma première
    tentative a échoué". Mêmes outils, intentions différentes — donc nœuds différents.
"""
