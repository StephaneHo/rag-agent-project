"""Tests du tool arxiv_retrieval.

Tests à écrire :
    test_search_returns_list_of_dicts_with_expected_keys
        Champs attendus : id, title, authors, abstract_chunk, score, source_url.

    test_search_respects_k_parameter
        Demander k=3 doit renvoyer au plus 3 résultats.

    test_search_orders_by_similarity_descending
        Le 1er résultat doit avoir un score >= au dernier.

INFRA :
    Ces tests touchent une vraie DB pgvector — préfère un fixture pytest qui
    seede 5-10 docs connus dans une DB de test (cf. backend/database/).
    POURQUOI pas de mock ici : tester la couche pgvector contre une vraie DB
    attrape les bugs de SQL et d'embedding qu'un mock cacherait. Cf. feedback
    "intégration tests doivent toucher la vraie DB".
"""
