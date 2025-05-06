from abc import ABC, abstractmethod
from typing import Dict


class IConsole(ABC):
    @abstractmethod
    def menu(self, opcoes: Dict[int, str], titulo: str = "", coluna: str = "Opção"):
        pass

    @abstractmethod
    def obter_opcao_escolhida(self, opcoes: Dict[int, str]) -> int:
        pass

    @abstractmethod
    def print(self, texto: str):
        pass

    @abstractmethod
    def perguntar(self, pergunta: str) -> str:
        pass

    @abstractmethod
    def confirmar(self, pergunta: str) -> bool:
        pass

    @abstractmethod
    def info(self, message: str):
        pass

    @abstractmethod
    def error(self, message: str):
        pass

    @abstractmethod
    def pressione_qualquer_tecla(self):
        pass

    @abstractmethod
    def clear(self):
        pass
