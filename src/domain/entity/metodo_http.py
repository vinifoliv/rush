class MetodoHTTP:
    _METODOS_VALIDOS = {"POST", "GET", "PUT", "PATCH", "DELETE"}

    def __init__(self, valor: str):
        self._validar(valor)
        self._valor = valor

    def _validar(self, valor: str):
        if not valor in self._METODOS_VALIDOS:
            raise ValueError(f"Método HTTP '{valor}' inválido!")

    @property
    def valor(self) -> str:
        return self._valor

    def __eq__(self, outro_metodo: object) -> bool:
        if not isinstance(outro_metodo, MetodoHTTP):
            return NotImplemented

        return outro_metodo.valor == self.valor

    def __hash__(self) -> int:
        return hash(self._valor)

    def __str__(self) -> str:
        return self._valor

    def __repr__(self) -> str:
        return f"MetodoHttp(valor='{self._valor}')"
