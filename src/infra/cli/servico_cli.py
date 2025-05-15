from typing import List

from application.usecase.alterar_servico_usecase import AlterarServicoUsecase

from application.usecase.buscar_servicos_usecase import BuscarServicosUsecase
from application.usecase.criar_servico_usecase import CriarServicoUsecase
from application.usecase.excluir_servico_usecase import ExcluirServicoUsecase
from domain.entity.servico import Servico
from infra.cli.icli import ICLI
from infra.cli.iconsole import IConsole
from infra.cli.rota_cli import RotaCLI


class ServicoCLI(ICLI):
    def __init__(
        self,
        console: IConsole,
        rota_cli: RotaCLI,
        criar_servico_usecase: CriarServicoUsecase,
        alterar_servico_usecase: AlterarServicoUsecase,
        buscar_servicos_usecase: BuscarServicosUsecase,
        excluir_servico_usecase: ExcluirServicoUsecase,
    ):
        self._console = console
        self._rota_cli = rota_cli
        self._criar_servico_usecase = criar_servico_usecase
        self._alterar_servico_usecase = alterar_servico_usecase
        self._buscar_servicos_usecase = buscar_servicos_usecase
        self._excluir_servico_usecase = excluir_servico_usecase

    def executar(self):
        opcoes = {
            1: "Criar um serviço",
            2: "Alterar um serviço",
            3: "Consultar serviços",
            4: "Excluir um serviço",
            5: "Sair",
        }

        while True:
            try:
                self._console.clear()

                servicos = self._buscar_servicos_usecase.executar()
                self._listar_servicos(servicos)

                self._console.menu(
                    opcoes=opcoes,
                    titulo="O que deseja fazer?",
                )
                opcao_escolhida = self._console.obter_opcao_escolhida(opcoes)
                match opcao_escolhida:
                    case 1:
                        self._criar_servico()
                    case 2:
                        self._alterar_servico(servicos)
                    case 4:
                        self._excluir()
                    case 5:
                        return
            except ValueError as e:
                self._console.error(e.args[0])
                continuar = self._console.confirmar("Continuar?")
                if not continuar:
                    break

    def _criar_servico(self):
        nome = self._console.perguntar("Nome")
        dominio = self._console.perguntar("Domínio")
        servico = self._criar_servico_usecase.executar(nome, dominio)
        self._rota_cli.executar(servico)

    def _alterar_servico(self, servicos: List[Servico]):
        id = int(self._console.perguntar("Digite o serviço"))

        servico = next((s for s in servicos if s.id == id), None)
        if servico is None:
            raise ValueError("Serviço não encontrado!")

        nome = self._console.perguntar(f"Digite o nome ({servico.nome})")
        if nome == "":
            nome = servico.nome

        dominio = self._console.perguntar(f"Domínio ({servico.dominio})")
        if dominio == "":
            dominio = servico.dominio

        self._alterar_servico_usecase.executar(id, nome, dominio)
        self._rota_cli.executar(servico)

    def _excluir(self):
        id = int(self._console.perguntar("Digite o serviço"))
        self._excluir_servico_usecase.executar(id)

    def _listar_servicos(self, servicos: List[Servico]):
        for s in servicos:
            self._console.print(
                f"[magenta]{s.id}[/] [cyan]{s.dominio}[/] [green]{s.nome}[/]"
            )
