from typing import Optional
from models.cupom_model import Cupom
from sql.cupom_sql import *
from util.db import obter_conexao


class CupomRepo:

    @staticmethod
    def criar_tabela():
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @staticmethod
    def inserir(cupom: Cupom) -> Optional[Cupom]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(
                SQL_INSERIR,
                (
                    cupom.nome,
                    cupom.valor,
                    cupom.descricao,
                    cupom.id_empresa,
                ),
            )
            if cursor.rowcount == 0:
                return None
            cupom.id = cursor.lastrowid
            return cupom
        
        
    @staticmethod
    def obter_por_id(id: int) -> Optional[Cupom]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_POR_ID, (id,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            return Cupom(**dados)

    @staticmethod
    def atualizar_dados(cupom: Cupom) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(
                SQL_ATUALIZAR,
                (
                    cupom.nome,
                    cupom.valor,
                    cupom.descricao,
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
