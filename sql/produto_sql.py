SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco TEXT NOT NULL,
        descrcao TEXT NOT NULL,
        id_empresa INTEGER,
        FOREIGN KEY("id_empresa") REFERENCES "usuario"("id")
"""

SQL_INSERIR_PRODUTO = """
    INSERT INTO produto(nome, preco, descricao, id_empresa)
    VALUES (?, ?, ?, ?)
"""

SQL_OBTER_DADOS_POR_ID = """
    SELECT id, nome, preco, descricao, id_empresa
    FROM produto
    WHERE id = ?
"""

SQL_ATUALIZAR_DADOS_produto = """
    UPDATE produto
    SET nome = ?, preco = ?, descricao = ?
    WHERE id = ?
"""

SQL_EXCLUIR = """
    DELETE FROM produto
    WHERE id = ?
"""