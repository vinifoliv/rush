from application.repository.iservico_repository import IServicoRepository


class CriarRotaUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, caminho: str, servico_id: int):
        return self._servico_repository.criar_rota(caminho, servico_id)
