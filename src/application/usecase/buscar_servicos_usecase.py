from typing import List
from application.repository.iservico_repository import IServicoRepository
from domain.entity.servico import Servico


class BuscarServicosUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self) -> List[Servico]:
        servicos = self._servico_repository.buscar_servicos()
        return servicos
