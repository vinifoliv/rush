from abc import ABC, abstractmethod
from typing import List

from domain.entity.rota import Rota
from domain.entity.servico import Servico


class IServicoRepository(ABC):
    @abstractmethod
    def criar_servico(self, servico: Servico) -> Servico:
        pass

    @abstractmethod
    def alterar_servico(self, servico: Servico) -> Servico:
        pass

    @abstractmethod
    def buscar_servicos(self) -> List[Servico]:
        pass

    @abstractmethod
    def buscar_servico_por_id(self, id: int) -> Servico | None:
        pass

    @abstractmethod
    def buscar_servico_por_nome(self, nome: str) -> Servico | None:
        pass

    @abstractmethod
    def excluir_servico(self, id: int) -> Servico:
        pass

    @abstractmethod
    def criar_rota(self, rota: Rota, servico_id: int) -> Rota:
        pass

    @abstractmethod
    def alterar_rota(self, rota: Rota) -> Rota:
        pass

    @abstractmethod
    def buscar_rota_por_caminho_e_servico_id(
        self, caminho: str, servico_id: int
    ) -> Rota | None:
        pass

    @abstractmethod
    def buscar_rotas_por_servico_id(self, servico_id: int) -> List[Rota]:
        pass

    @abstractmethod
    def buscar_rota_por_id(self, id: int) -> Rota | None:
        pass

    @abstractmethod
    def excluir_rota(self, id: int) -> Rota:
        pass
