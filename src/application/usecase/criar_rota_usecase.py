from typing import Optional
from application.repository.iservico_repository import IServicoRepository
from domain.entity.metodo_http import MetodoHTTP


class CriarRotaUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(
        self, metodo: MetodoHTTP, caminho: str, payload: Optional[str], servico_id: int
    ):
        rota_existe = self._servico_repository.buscar_rota_por_caminho_e_servico_id(
            caminho, servico_id
        )
        if rota_existe:
            raise ValueError("A rota já existe.")
        return self._servico_repository.criar_rota(metodo, caminho, payload, servico_id)
