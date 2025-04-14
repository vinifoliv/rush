from abc import ABC, abstractmethod


class IFileSystem(ABC):
    @abstractmethod
    def ler_arquivo(caminho: str) -> str:
        pass
