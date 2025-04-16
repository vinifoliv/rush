class MetodoHTTP:
    def __init__(self, valor: str):
        self._validar_metodo(valor)
        self._valor = valor

    def obter_valor(self):
        return self._valor

    def _validar_metodo(self, valor: str):
        if (
            valor == "POST"
            or valor == "GET"
            or valor == "PUT"
            or valor == "PATCH"
            or valor == "DELETE"
        ):
            return
        raise ValueError(f"Método HTTP '{valor}' é inválido")
