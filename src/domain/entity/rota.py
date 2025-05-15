from domain.entity.caminho import CaminhoRota
from domain.entity.id import ID
from domain.entity.metodo_http import MetodoHTTP
from domain.entity.payload import Payload


class Rota:
    def __init__(
        self,
        id: ID | None,
        metodo: MetodoHTTP,
        caminho: CaminhoRota,
        payload: Payload,
    ):
        self._id = id
        self._metodo = metodo
        self._caminho = caminho
        self._payload = payload

    @property
    def id(self):
        return self._id.valor if self._id else None

    @property
    def caminho(self):
        return self._caminho.valor

    @property
    def metodo(self):
        return self._metodo.valor

    @property
    def payload(self):
        return self._payload.valor

    def __eq__(self, outra_rota: object) -> bool:
        if not isinstance(outra_rota, Rota):
            return NotImplemented

        caminho_eh_igual = self.caminho == outra_rota.caminho
        metodo_eh_igual = self.metodo == outra_rota.metodo

        return caminho_eh_igual and metodo_eh_igual

    def __str__(self):
        return f"{self.metodo} {self.caminho}"

    def __hash__(self):
        return hash((self.metodo, self.caminho))
