from typing import List

from domain.entity.requisicao import Requisicao


class Batch:
    def __init__(self):
        self._requisicoes: List[Requisicao] = []

    @property
    def requisicoes(self):
        return self._requisicoes

    @property
    def tempo_resposta_medio(self):
        tempos_resposta = [r.tempo_resposta for r in self._requisicoes]
        media = sum(tempos_resposta) / len(tempos_resposta)
        return media

    @property
    def tempo_resposta_maximo(self):
        tempos_resposta = [r.tempo_resposta for r in self._requisicoes]
        maximo = max(tempos_resposta)
        return maximo

    @property
    def tempo_resposta_minimo(self):
        tempos_resposta = [r.tempo_resposta for r in self._requisicoes]
        minimo = min(tempos_resposta)
        return minimo

    def adicionar_requisicao(self, requisicao: Requisicao):
        self._requisicoes.append(requisicao)
