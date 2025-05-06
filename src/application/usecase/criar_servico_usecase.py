from application.repository.iservico_repository import IServicoRepository
from domain.entity.dominio import Dominio
from domain.entity.servico import Servico


class CriarServicoUsecase:
    def __init__(self, servico_repository: IServicoRepository):
        self._servico_repository = servico_repository

    def executar(self, nome: str, valor_dominio: str) -> Servico:
        servico_existe = self._servico_repository.buscar_servico_por_nome(nome)
        if servico_existe:
            raise ValueError(f"Serviço {nome} já cadastrado!")

        servico = Servico(None, nome, Dominio(valor_dominio))
        servico_criado = self._servico_repository.criar_servico(servico)
        return servico_criado
