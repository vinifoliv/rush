from abc import ABC, abstractmethod
from typing import Dict


class IConsole(ABC):
    @abstractmethod
    def menu(opcoes: Dict[int, str], titulo: str = "", coluna: str = "Opção"):
        pass

    @abstractmethod
    def obter_opcao_escolhida(opcoes: Dict[int, str]):
        pass

    @abstractmethod
    def print(texto: str):
        pass

    @abstractmethod
    def perguntar(pergunta: str) -> str:
        pass

    @abstractmethod
    def confirmar(pergunta: str) -> bool:
        pass

    @abstractmethod
    def info(message: str):
        pass

    @abstractmethod
    def error(message: str):
        pass
