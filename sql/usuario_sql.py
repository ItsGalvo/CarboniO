SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf INTEGER,
        cnpj INTEGER,
        data_nasciomento TEXT,
        email TEXT NOT NULL UNIQUE,
        telefone INTEGER NOT NULL,
        cep INTEGER,
        senha TEXT NOT NULL,
        perfil INT NOT NULL,
        credito INT DEFAULT 0,        
        token TEXT)
"""

SQL_INSERIR = """
    INSERT INTO usuario(nome, cpf, cnpj, data_nascimento, email, telefone, cep, senha, perfil, credito)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
SQL_OBTER_SENHA_POR_EMAIL = """
    SELECT senha
    FROM usuario
    WHERE email = ?
"""

SQL_OBTER_DADOS_POR_EMAIL = """
    SELECT id, nome, cpf, cnpj, data_nascimento, email, telefone, cep, perfil, credito
    FROM usuario
    WHERE email = ?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, data_nascimento, email, telefone, perfil
    FROM usuario
    WHERE id = ?
"""

SQL_ATUALIZAR_DADOS = """
    UPDATE usuario
    SET nome = ?, cnpj = ?, cpf = ?, data_nascimento = ?, email = ?, telefone = ?, cep = ?
    WHERE id = ?
"""

SQL_ATUALIZAR_SENHA = """
    UPDATE usuario
    SET senha = ?
    WHERE id = ?
"""
SQL_ATUALIZAR_CREDITO = """
    UPDATE usuario
    SET credito = ?
    WHERE id = ?
"""

SQL_EXCLUIR = """
    DELETE FROM usuario
    WHERE id = ?
"""

SQL_SELECIONAR_POR_PERFIL = """
    SELECT * FROM usuario WHERE perfil = ?
"""