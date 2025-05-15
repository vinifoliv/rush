class ID:
    def __init__(self, valor: int):
        self._validar(valor)

        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def _validar(self, valor: int):
        if valor <= 0:
            raise ValueError(f"ID '{valor}' inválido!")
