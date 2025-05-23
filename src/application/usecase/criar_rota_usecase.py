from application.repository.iservico_repository import IServicoRepository
from domain.entity.caminho import CaminhoRota
from domain.entity.metodo_http import MetodoHTTP
from domain.entity.payload import Payload
from domain.entity.rota import Rota


class CriarRotaUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(
        self, metodo: str, caminho: str, payload: str | None, servico_id: int
    ) -> Rota:
        servico_existe = self._servico_repository.buscar_servico_por_id(servico_id)
        if not servico_existe:
            raise ValueError("Serviço não encontrado!")

        rota_existe = self._servico_repository.buscar_rota_por_caminho_e_servico_id(
            caminho, servico_id
        )
        if rota_existe:
            raise ValueError("A rota já existe.")

        rota = Rota(
            id=None,
            metodo=MetodoHTTP(metodo),
            caminho=CaminhoRota(caminho),
            payload=Payload(payload),
        )

        rota_criada = self._servico_repository.criar_rota(rota, servico_id)
        return rota_criada
