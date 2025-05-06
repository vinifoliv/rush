import re


class Dominio:
    def __init__(self, valor: str):
        valor = valor.strip()
        if valor == "":
            raise ValueError("Domínio vazio!")
        if not self._validar_dominio(valor):
            raise ValueError(f"Domínio '{valor}' inválido!")
        self.valor = valor

    def _validar_dominio(self, valor: str):
        padrao = re.compile(
            r"^(localhost|\b(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,})(:\d{1,5})?$"
        )
        return bool(padrao.match(valor))
