from application.repository.iservico_repository import IServicoRepository


class ExcluirRotaUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, id: int):
        rota_existe = self._servico_repository.buscar_rota_por_id(id)
        if not rota_existe:
            raise ValueError("Rota não encontrada.")
        self._servico_repository.excluir_rota(id)
