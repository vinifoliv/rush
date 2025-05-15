from time import time
from domain.entity.metodo_http import MetodoHTTP
from domain.entity.payload import Payload
from domain.entity.url import URL


class Requisicao:
    def __init__(self, metodo: MetodoHTTP, url: URL, payload: Payload):
        self._metodo = metodo
        self._url = url
        self._payload = payload
        self._inicio = 0
        self._fim = 0

    @property
    def metodo(self):
        return self._metodo.valor

    @property
    def url(self):
        return self._url.valor

    @property
    def payload(self):
        return self._payload.valor

    @property
    def inicio(self):
        return self._inicio

    @property
    def fim(self):
        return self._fim

    @property
    def tempo_resposta(self) -> int:
        if not self._inicio:
            raise ValueError("A requisição ainda não foi feita!")

        if not self._fim:
            raise ValueError("A requisição ainda não terminou!")

        tempo_resposta = self._fim - self._inicio
        return round(tempo_resposta * 1000)

    def comecar(self):
        if self._inicio:
            raise ValueError("A requisição já começou!")
        self._inicio = time()

    def finalizar(self):
        if self._fim:
            raise ValueError("A requisição já  terminou!")
        self._fim = time()

    def _validar(self, inicio: int, fim: int):
        if inicio < 0:
            raise ValueError("Horário de início da requisição negativo!")
        if fim < 0:
            raise ValueError("Horário de fim da requisição negativo!")
