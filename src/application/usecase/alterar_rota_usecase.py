from application.repository.iservico_repository import IServicoRepository
from domain.entity.rota import Rota


class AlterarRotaUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, id: int, caminho: str):
        rota = Rota(id, caminho)
        self._servico_repository.alterar_rota(rota)
