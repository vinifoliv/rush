from application.repository.iservico_repository import IServicoRepository
from domain.entity.servico import Servico


class AlterarServicoUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, id: int, nome: str):
        servico = Servico(id, nome)
        self._servico_repository.alterar_servico(servico)
