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
        batches = []
        self._aquecer(servico, rota)
        for i in range(qtde_batches):
            requisicoes = []
            for j in range(qtde_requisicoes):
                inicio = time.time()
                self._requisitar(servico, rota)
                fim = time.time()
                requisicoes.append(Requisicao(inicio * 1000, fim * 1000))
            batches.append(Batch(requisicoes))
        sessao = Sessao(batches)
        return sessao

    def _aquecer(self, servico: Servico, rota: Rota):
        self._requisitar(servico, rota)

    def _requisitar(self, servico: Servico, rota: Rota):
        metodo = rota.obter_metodo().obter_valor()
        url = servico.obter_url(rota)
        payload = rota.obter_payload()
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
