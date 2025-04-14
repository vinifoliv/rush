from application.repository.iservico_repository import IServicoRepository
from domain.entity.servico import Servico


class AlterarServicoUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, id: int, nome: str):
        servico_existe = self._servico_repository.buscar_servico_por_id(id)
        if not servico_existe:
            raise ValueError(f"O serviço {nome} não encontrado.")
        servico = Servico(id, nome)
        self._servico_repository.alterar_servico(servico)
