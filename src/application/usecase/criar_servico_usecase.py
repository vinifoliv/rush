from application.repository.iservico_repository import IServicoRepository
from domain.entity.servico import Servico


class CriarServicoUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, nome: str) -> Servico:
        return self._servico_repository.criar_servico(nome)
