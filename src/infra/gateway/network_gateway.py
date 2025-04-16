import json
import requests
from application.gateway.inetwork_gateway import INetworkGateway


class NetworkGateway(INetworkGateway):
    def __init__(self):
        self._sessao = requests.Session()

    def aquecer(self, url, payload):
        self._sessao.post(url, payload)

    def post(self, url, payload):
        resposta = self._sessao.post(url, payload)
        return resposta

    def get(self, url):
        resposta = self._sessao.get(url)
        return resposta

    def requisitar(self, url, payload):
        return self._sessao.post(url, json.load(payload))


# import requests
# import json
# import time
# import os
# import gc
# from dotenv import load_dotenv

# gc.disable()
# load_dotenv()


# def carregar_url():
#     return os.getenv("URL_SAP")


# def carregar_payload():
#     with open("payload.json", "r") as payload:
#         return json.load(payload)


# def converter_em_milissegundos(segundos):
#     return round(segundos * 1000)


# def aquecimento(url, session):
#     session.post(url, json=payload)


# def imprimir_resultados(duracao, media, minimo, maximo):
#     os.system("cls")
#     print("===== RESULTADOS =====")
#     print(f"- DURAÇÃO: {duracao}ms")
#     print(f"- MÉDIA:  {media}ms")
#     print(f"- MÍNIMO: {minimo}ms")
#     print(f"- MÁXIMO: {maximo}ms")


# os.system("cls")
# with requests.Session() as session:
#     print("===== INICIALIZAÃ‡ÃƒO =====")
#     print("Carregando URL...")
#     url = carregar_url()
#     print("Carregando payload...")
#     payload = carregar_payload()
#     qtde_requisicoes = 1000
#     tempos_resposta = []
#     print("Aquecendo...")
#     aquecimento(url, session)
#     inicio_teste = time.time()
#     print("===== COMEÃ‡AR! =====")
#     for i in range(qtde_requisicoes):
#         print(f"- RequisiÃ§Ã£o {i + 1}...")
#         inicio = time.time()
#         response = session.post(url, json=payload)
#         fim = time.time()
#         print(response.json())
#         tempos_resposta.append(fim - inicio)
#     fim_teste = time.time()

#     duracao = converter_em_milissegundos(fim_teste - inicio_teste)
#     media = converter_em_milissegundos(sum(tempos_resposta) / len(tempos_resposta))
#     minimo = converter_em_milissegundos(min(tempos_resposta))
#     maximo = converter_em_milissegundos(max(tempos_resposta))
#     imprimir_resultados(duracao, media, minimo, maximo)
