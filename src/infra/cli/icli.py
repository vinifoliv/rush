from abc import ABC, abstractmethod


class ICLI(ABC):
    @abstractmethod
    def executar(self):
        pass
