from abc import ABC, abstractmethod
from typing import Any

from domain.entity.requisicao import Requisicao


class INetworkGateway(ABC):
    @abstractmethod
    def requisitar(self, requisicao: Requisicao) -> Any:
        pass

    # @abstractmethod
    # def aquecer(self, url: str, payload: str = "") -> Any:
    #     pass
    #
    # @abstractmethod
    # def post(self, url: str, payload: str = "") -> Any:
    #     pass
    #
    # @abstractmethod
    # def get(self, url: str) -> Any:
    #     pass
    #
    # @abstractmethod
    # def put(self, url: str, payload: str) -> Any:
    #     pass
    #
    # @abstractmethod
    # def patch(self, url: str, payload: str) -> Any:
    #     pass
    #
    # @abstractmethod
    # def delete(self, url: str) -> Any:
    #     pass
