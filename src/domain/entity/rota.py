class Rota:
    def __init__(self, id: int, caminho: str, payload: str = ""):
        self._id = id
        self._caminho = caminho
        self._payload = payload

    def obter_id(self):
        return self._id

    def obter_caminho(self):
        return self._caminho

    def obter_payload(self):
        return self._payload

    def definir_caminho(self, caminho: str):
        self._caminho = caminho
