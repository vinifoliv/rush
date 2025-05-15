from typing import List

from domain.entity.batch import Batch


class Sessao:
    def __init__(self):
        self._batches: List[Batch] = []

    @property
    def batches(self):
        return self._batches

    @property
    def tempo_resposta_medio(self):
        tempos_resposta = [b.tempo_resposta_medio for b in self._batches]
        media = sum(tempos_resposta) / len(tempos_resposta)
        return media

    @property
    def tempo_resposta_maximo(self):
        tempos_resposta = [b.tempo_resposta_maximo for b in self.batches]
        maximo = max(tempos_resposta)
        return maximo

    @property
    def tempo_resposta_minimo(self):
        tempos_resposta = [b.tempo_resposta_minimo for b in self.batches]
        minimo = min(tempos_resposta)
        return minimo

    def adicionar_batch(self, batch: Batch):
        self._batches.append(batch)
