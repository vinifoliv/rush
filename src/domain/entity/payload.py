class Payload:
    def __init__(self, valor: str | None):
        self._validar(valor)

        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def _validar(self, valor: str | None):
        if not valor or isinstance(valor, str):
            return
