from application.repository.iservico_repository import IServicoRepository
from domain.entity.caminho import CaminhoRota
from domain.entity.id import ID
from domain.entity.metodo_http import MetodoHTTP
from domain.entity.payload import Payload
from domain.entity.rota import Rota


class AlterarRotaUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, id: int, metodo: str, caminho: str, payload: str | None) -> Rota:
        rota_existe = self._servico_repository.buscar_rota_por_id(id)
        if not rota_existe:
            raise ValueError("Rota não encontrada!")

        rota = Rota(ID(id), MetodoHTTP(metodo), CaminhoRota(caminho), Payload(payload))
        rota_alterada = self._servico_repository.alterar_rota(rota)
        return rota_alterada
