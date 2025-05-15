class URL:
    def __init__(self, valor: str):
        self._validar(valor)

        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def _validar(self, valor: str):
        if not valor:
            raise ValueError("URL vazia!")

    def __str__(self):
        return self._valor
