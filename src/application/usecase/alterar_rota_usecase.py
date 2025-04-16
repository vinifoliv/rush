from application.repository.iservico_repository import IServicoRepository
from domain.entity.metodo_http import MetodoHTTP
from domain.entity.rota import Rota


class AlterarRotaUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, id: int, metodo: MetodoHTTP, caminho: str, payload: str):
        rota = Rota(id, metodo, caminho, payload)
        self._servico_repository.alterar_rota(rota)
