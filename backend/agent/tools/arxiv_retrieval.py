"""Tool : recherche dans le store vectoriel ArXiv (PostgreSQL + pgvector).

Signature attendue :
    def search(query: str, k: int = 5) -> list[dict]:
        '''Renvoie k chunks les plus similaires.
        Format dict : {id, title, authors, abstract_chunk, score, source_url}
        '''

À implémenter :
    - Embed la query avec sentence-transformers (RÉUTILISER le même modèle que
      l'ingestion — sinon distances incohérentes, résultats absurdes).
    - Requête SQL : SELECT … ORDER BY embedding <-> :q LIMIT :k
    - Retourner la liste de dicts.

POURQUOI réutiliser l'infra de rag-project ?
    Embedding modèle, table, ingestion sont déjà debug. Recoder = perte de temps
    et de cohérence. Branche-toi simplement dessus (cf. backend/database/).
"""
