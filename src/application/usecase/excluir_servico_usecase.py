from application.repository.iservico_repository import IServicoRepository


class ExcluirServicoUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, id: int):
        self._servico_repository.excluir_servico(id)
