from typing import List

from domain.entity.rota import Rota


class Servico:
    def __init__(self, id: int, nome: str, rotas: List[Rota] = []):
        self._id = id
        self._nome = nome
        self._rotas = rotas

    def obter_id(self):
        return self._id

    def obter_nome(self):
        return self._nome

    def obter_rotas(self):
        return self._rotas

    def adicionar_rota(self, rota: Rota):
        self._rotas.append(rota)

    def remover_rota(self, index: int):
        self._rotas.pop(index)
