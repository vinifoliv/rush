from typing import List

from domain.entity.batch import Batch


class Sessao:
    def __init__(self, batches: List[Batch]):
        self._batches = batches

    def obter_media(self):
        tempos_resposta = [b.obter_media() for b in self._batches]
        media = sum(tempos_resposta) / len(tempos_resposta)
        return media

    def obter_maximo(self):
        tempos_resposta = [b.obter_maximo() for b in self._batches]
        maximo = max(tempos_resposta)
        return maximo

    def obter_minimo(self):
        tempos_resposta = [b.obter_minimo() for b in self._batches]
        minimo = min(tempos_resposta)
        return minimo
