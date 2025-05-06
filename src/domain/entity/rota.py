from domain.entity.metodo_http import MetodoHTTP


class Rota:
    def __init__(
        self, id: int | None, metodo: MetodoHTTP, caminho: str, payload: str | None
    ):
        self.id = id
        self.metodo = metodo
        self.caminho = caminho
        self.payload = payload

    def definir_caminho(self, caminho: str):
        self.caminho = caminho
