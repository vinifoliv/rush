import time
from application.gateway.inetwork_gateway import INetworkGateway
from domain.entity.batch import Batch
from domain.entity.requisicao import Requisicao
from domain.entity.rota import Rota
from domain.entity.servico import Servico
from domain.entity.sessao import Sessao


class TestarRotaUsecase:
    def __init__(self, network_gateway: INetworkGateway):
        self._network_gateway = network_gateway

    def executar(
        self, servico: Servico, rota: Rota, qtde_requisicoes: int, qtde_batches: int
    ):
        url = servico.obter_url(rota)
        batches = []
        self._aquecer(url)
        for i in range(qtde_batches):
            requisicoes = []
            for j in range(qtde_requisicoes):
                inicio = time.time()
                self._requisitar(url)
                fim = time.time()
                requisicoes.append(Requisicao(inicio * 1000, fim * 1000))
            batches.append(Batch(requisicoes))
        sessao = Sessao(batches)
        return sessao

    def _aquecer(self, rota: Rota):
        self._requisitar(rota)

    def _requisitar(self, rota: Rota):
        metodo = rota.metodo.valor
        url = rota.caminho
        payload = rota.payload
        match metodo:
            case "POST":
                self._network_gateway.post(url, payload)
            case "GET":
                self._network_gateway.get(url)
            case "PUT":
                self._network_gateway.put(url, payload)
            case "PATCH":
                self._network_gateway.patch(url, payload)
            case "DELETE":
                self._network_gateway.patch(url)
