from application.repository.iservico_repository import IServicoRepository
from domain.entity.servico import Servico


class CriarServicoUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, nome: str) -> Servico:
        servico_existe = self._servico_repository.buscar_servico_por_nome(nome)
        if servico_existe:
            raise ValueError(f"O serviço {nome} já está cadastrado!")
        return self._servico_repository.criar_servico(nome)
