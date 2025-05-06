from typing import List

from domain.entity.dominio import Dominio
from domain.entity.metodo_http import MetodoHTTP
from domain.entity.rota import Rota


class Servico:
    def __init__(
        self, id: int | None, nome: str, dominio: Dominio, rotas: List[Rota] = []
    ):
        self.id = id
        self.nome = nome
        self.dominio = dominio
        self.rotas = rotas

    def obter_url(self, rota: Rota):
        url = "http://" + self.dominio.valor + rota.caminho
        return url

    def adicionar_rota(self, rota: Rota):
        self.rotas.append(rota)

    def atualizar_rota(self, rota_id: int, metodo: str, caminho: str, payload: str):
        rota = next((r for r in self.rotas if r.id == rota_id), None)
        if rota is None:
            raise ValueError(f"Rota {rota_id} não encontrada.")
        rota.metodo = MetodoHTTP(metodo)
        rota.caminho = caminho
        rota.payload = payload

    def remover_rota(self, rota_id: int):
        rota = next((r for r in self.rotas if r.id == rota_id), None)
        if rota is None:
            raise ValueError(f"Rota {rota_id} não encontrada.")
        self.rotas.remove(rota)
