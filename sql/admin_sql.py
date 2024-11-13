SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS admin (
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