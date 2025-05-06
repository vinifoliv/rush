class MetodoHTTP:
    def __init__(self, valor: str):
        self._validar(valor)
        self.valor = valor

    def _validar(self, valor: str):
        if (
            valor == "POST"
            or valor == "GET"
            or valor == "PUT"
            or valor == "PATCH"
            or valor == "DELETE"
        ):
            return
        raise ValueError(f"Método HTTP '{valor}' é inválido")
