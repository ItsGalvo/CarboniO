SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS cupom (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        valor TEXT NOT NULL,
        descricao TEXT NOT NULL,
        id_empresa INTEGER,
        FOREIGN KEY(id_empresa) REFERENCES usuario(id))
"""

SQL_INSERIR = """
    INSERT INTO cupom(nome, valor, descricao, id_empresa)
    VALUES (?, ?, ?, ?)
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, valor, descricao, id_empresa
    FROM cupom
    WHERE id = ?
"""

SQL_ATUALIZAR = """
    UPDATE cupom
    SET nome = ?, valor = ?, descricao = ?
    WHERE id = ?
"""

SQL_EXCLUIR = """
    DELETE FROM cupom
    WHERE id = ?
"""