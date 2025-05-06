from typing import List

from domain.entity.requisicao import Requisicao


class Batch:
    def __init__(self, requisicoes: List[Requisicao]):
        self.requisicoes = requisicoes

    def obter_media(self):
        tempos_resposta = [r.calcular_tempo_resposta() for r in self.requisicoes]
        media = sum(tempos_resposta) / len(tempos_resposta)
        return media

    def obter_maximo(self):
        tempos_resposta = [r.calcular_tempo_resposta() for r in self.requisicoes]
        maximo = max(tempos_resposta)
        return maximo

    def obter_minimo(self):
        tempos_resposta = [r.calcular_tempo_resposta() for r in self.requisicoes]
        minimo = min(tempos_resposta)
        return minimo
