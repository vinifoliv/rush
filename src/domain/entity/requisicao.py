from typing import List


class Requisicao:
    def __init__(self, inicio: int, fim: int):
        if inicio < 0:
            raise ValueError("Horário de início da requisição negativo!")
        if fim < 0:
            raise ValueError("Horário de fim da requisição negativo!")
        self._inicio = inicio
        self._fim = fim

    def calcular_tempo_resposta(self) -> List[int]:
        return round(self._fim - self._inicio)
