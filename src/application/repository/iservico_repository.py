from abc import ABC, abstractmethod
from typing import List

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
    def excluir_servico(id: int):
        pass

    @abstractmethod
    def criar_rota(caminho: str, servico_id: int):
        pass

    @abstractmethod
    def alterar_rota(rota: Rota):
        pass

    @abstractmethod
    def buscar_rotas_por_servico_id(servico_id: int) -> List[Rota]:
        pass

    @abstractmethod
    def excluir_rota(id: int):
        pass
