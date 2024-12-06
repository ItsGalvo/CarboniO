from typing import Optional
from models.produto_model import Produto
from sql.produto_sql import *
from util.db import obter_conexao


class ProdutoRepo:

    @staticmethod
    def criar_tabela():
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @staticmethod
    def inserir(produto: Produto) -> Optional[Produto]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(
                SQL_INSERIR_PRODUTO,
                (
                    produto.nome,
                    produto.preco,
                    produto.descricao,
                    produto.id_empresa,
                ),
            )
            if cursor.rowcount == 0:
                return None
            produto.id = cursor.lastrowid
            return produto
        
        
    @staticmethod
    def obter_por_id(id: int) -> Optional[Produto]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_DADOS_POR_ID, (id,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            return Produto(**dados)

    @staticmethod
    def atualizar_dados(produto: Produto) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(
                SQL_ATUALIZAR_DADOS_PRODUTO,
                (
                    produto.nome,
                    produto.preco,
                    produto.descricao,
                ),
            )
            if cursor.rowcount == 0:
                return False
            return True


    @staticmethod
    def excluir(id: int) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_EXCLUIR, (id,))
            return cursor.rowcount > 0
