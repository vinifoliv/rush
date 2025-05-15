import re


class Dominio:
    _PADRAO_DOMINIO = re.compile(
        r"^(localhost|"
        r"(\d{1,3}\.){3}\d{1,3}|"  # IPv4
        r"(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,}"
        r")(:\d{1,5})?$"
    )

    def __init__(self, valor: str):
        valor_tratado = valor.strip()
        self._validar(valor_tratado)

        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def _validar(self, valor: str):
        if not valor:
            raise ValueError("Domínio vazio!")
        if not self._PADRAO_DOMINIO.match(valor):
            raise ValueError(f"Domínio '{valor}' inválido!")
