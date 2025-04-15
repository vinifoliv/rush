from domain.entity.metodo_http import MetodoHTTP


class Rota:
    def __init__(self, id: int, metodo: MetodoHTTP, caminho: str, payload: str = ""):
        self._id = id
        self._metodo = metodo
        self._caminho = caminho
        self._payload = payload

    def obter_id(self):
        return self._id

    def obter_metodo(self):
        return self._metodo

    def obter_caminho(self):
        return self._caminho

    def obter_payload(self):
        return self._payload

    def definir_caminho(self, caminho: str):
        self._caminho = caminho
