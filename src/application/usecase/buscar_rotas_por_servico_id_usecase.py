from typing import List

from application.repository.iservico_repository import IServicoRepository
from domain.entity.rota import Rota


class BuscarRotasPorServicoIdUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, servico_id: int) -> List[Rota]:
        return self._servico_repository.buscar_rotas_por_servico_id(servico_id)
