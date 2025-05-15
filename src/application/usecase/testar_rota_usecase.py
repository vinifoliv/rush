from application.gateway.inetwork_gateway import INetworkGateway
from domain.entity.batch import Batch
from domain.entity.metodo_http import MetodoHTTP
from domain.entity.payload import Payload
from domain.entity.requisicao import Requisicao
from domain.entity.rota import Rota
from domain.entity.servico import Servico
from domain.entity.sessao import Sessao
from domain.entity.url import URL


class TestarRotaUsecase:
    def __init__(self, network_gateway: INetworkGateway):
        self._network_gateway = network_gateway

    def executar(
        self, servico: Servico, rota: Rota, qtde_requisicoes: int, qtde_batches: int
    ):
        metodo = MetodoHTTP(rota.metodo)
        url = URL(servico.obter_url(rota))
        payload = Payload(rota.payload)

        aquecimento = Requisicao(metodo, url, payload)
        self._network_gateway.requisitar(aquecimento)

        sessao = Sessao()
        for _ in range(qtde_batches):
            batch = Batch()

            for _ in range(qtde_requisicoes):
                requisicao = Requisicao(metodo, url, payload)

                requisicao.comecar()
                self._network_gateway.requisitar(requisicao)
                requisicao.finalizar()

                batch.adicionar_requisicao(requisicao)

            sessao.adicionar_batch(batch)
        return sessao
