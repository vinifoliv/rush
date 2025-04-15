from abc import ABC, abstractmethod
from typing import List

from domain.entity.metodo_http import MetodoHTTP
from domain.entity.rota import Rota
from domain.entity.servico import Servico


class IServicoRepository(ABC):
    @abstractmethod
    def criar_servico(nome: str, rotas: List[str]) -> Servico:
        pass

    @abstractmethod
    def alterar_servico(servico: Servico):
        pass

    @abstractmethod
    def buscar_servicos() -> List[Servico]:
        pass

    @abstractmethod
    def buscar_servico_por_id(id: int) -> Servico:
        pass

    @abstractmethod
    def buscar_servico_por_nome(nome: str) -> Servico:
        pass

    @abstractmethod
    def excluir_servico(id: int):
        pass

    @abstractmethod
    def criar_rota(metodo: MetodoHTTP, caminho: str, payload: str, servico_id: int):
        pass

    @abstractmethod
    def alterar_rota(rota: Rota):
        pass

    @abstractmethod
    def buscar_rota_por_caminho_e_servico_id(caminho: str, servico_id: int) -> Rota:
        pass

    @abstractmethod
    def buscar_rotas_por_servico_id(servico_id: int) -> List[Rota]:
        pass

    @abstractmethod
    def buscar_rota_por_id(id: int) -> Rota:
        pass

    @abstractmethod
    def excluir_rota(id: int):
        pass
