class CaminhoRota:
    def __init__(self, valor: str):
        self._validar(valor)
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def _validar(self, valor: str):
        if valor == "":
            raise ValueError(f"Caminho '{valor}' inválido!")

    def __str__(self):
        return self._valor
