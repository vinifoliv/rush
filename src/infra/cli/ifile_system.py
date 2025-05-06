from abc import ABC, abstractmethod


class IFileSystem(ABC):
    @abstractmethod
    def ler_arquivo(self, caminho: str) -> str:
        pass
