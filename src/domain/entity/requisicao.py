from typing import List


class Requisicao:
    def __init__(self, inicio: int, fim: int):
        self._inicio = inicio
        self._fim = fim

    def calcular_tempo_resposta(self) -> List[int]:
        return round(self._fim - self._inicio)
