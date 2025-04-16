import sqlite3
from typing import Any, List


class Database:
    def __init__(self):
        self._conexao = sqlite3.connect("rush_db")
        self._cursor = self._conexao.cursor()

    def inicializar(self):
        with open("./src/infra/db/init.sql", "r") as arquivo:
            init_script = arquivo.read()
        self._cursor.executescript(init_script)
        self._conexao.commit()

    def limpar(self):
        self._cursor.execute("VACUUM")
        self._conexao.commit()

    def executar(self, query: str, parametros = ()):
        self._cursor.execute(query, parametros)

    def buscarUm(self) -> Any:
        return self._cursor.fetchone()

    def buscarMuitos(self) -> List[Any]:
        return self._cursor.fetchall()

    def commit(self):
        self._conexao.commit()

    def fechar_conexar(self):
        self._conexao.commit()
        self._conexao.close()
