SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf INTEGER,
        cnpj INTEGER,
        email TEXT NOT NULL UNIQUE,
        telefone INTEGER NOT NULL,
        cep INTEGER,
        senha TEXT NOT NULL,
        perfil INT NOT NULL,        
        token TEXT)
"""

SQL_INSERIR = """
    INSERT INTO usuario(nome, cpf, cnpj, email, telefone, cep, senha, perfil)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""
SQL_INSERIR_CREDITOS = """
    UPDATE usuario
    SET credito=?
    WHERE cpf=?
"""

SQL_ALTERAR = """
    UPDATE usuario
    SET nome=?, email=?
    WHERE id=?
"""

SQL_ALTERAR_TOKEN = """
    UPDATE usuario
    SET token=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM usuario    
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, email, perfil, token
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_POR_EMAIL = """
    SELECT id, nome, email, perfil, token
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_POR_TOKEN = """
    SELECT id, nome, email, perfil, token
    FROM usuario
    WHERE token=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*)
    FROM usuario
"""

SQL_EMAIL_EXISTE = """
    SELECT COUNT(*)
    FROM usuario
    WHERE email=?
"""

SQL_CHECAR_CREDENCIAIS = """
    SELECT email, senha, perfil
    FROM usuario
    WHERE email = ?
"""

SQL_CHECAR_CREDENCIAIS_CREDITO = """
    SELECT nome, cpf
    FROM usuario
    WHERE cpf = ?
"""
SQL_OBTER_CREDITO = """
    SELECT credito
    FROM usuario
    WHERE cpf = ?
"""