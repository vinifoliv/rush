from application.repository.iservico_repository import IServicoRepository


class ExcluirServicoUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, id: int):
        servicoExiste = self._servico_repository.buscar_servico_por_id(id)
        if not servicoExiste:
            raise ValueError("Serviço não encontrado.")
        self._servico_repository.excluir_servico(id)
