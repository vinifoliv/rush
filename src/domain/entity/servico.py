from typing import List

from domain.entity.dominio import Dominio
from domain.entity.id import ID
from domain.entity.rota import Rota


class Servico:
    def __init__(
        self, id: ID | None, nome: str, dominio: Dominio, rotas: List[Rota] = []
    ):
        self._id = id
        self._nome = nome
        self._dominio = dominio
        self._rotas = rotas

    @property
    def id(self):
        return self._id.valor if self._id else None

    @property
    def nome(self):
        return self._nome

    @property
    def dominio(self):
        return self._dominio.valor

    @property
    def rotas(self):
        return self._rotas

    def obter_url(self, rota: Rota):
        url = "http://" + self.dominio + rota.caminho
        return url
