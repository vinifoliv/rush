from typing import List

from application.usecase.alterar_rota_usecase import AlterarRotaUsecase
from application.usecase.alterar_servico_usecase import AlterarServicoUsecase
from application.usecase.buscar_rotas_por_servico_id_usecase import (
    BuscarRotasPorServicoIdUsecase,
)
from application.usecase.buscar_servicos_usecase import BuscarServicosUsecase
from application.usecase.criar_rota_usecase import CriarRotaUsecase
from application.usecase.criar_servico_usecase import CriarServicoUsecase
from application.usecase.excluir_rota_usecase import ExcluirRotaUsecase
from application.usecase.excluir_servico_usecase import ExcluirServicoUsecase
from domain.entity.rota import Rota
from domain.entity.servico import Servico
from infra.cli.icli import ICLI
from infra.cli.iconsole import IConsole


class ServicoCLI(ICLI):
    def __init__(
        self,
        console: IConsole,
        criar_servico_usecase: CriarServicoUsecase,
        alterar_servico_usecase: AlterarServicoUsecase,
        buscar_servico_usecase: BuscarServicosUsecase,
        excluir_servico_usecase: ExcluirServicoUsecase,
        criar_rota_usecase: CriarRotaUsecase,
        alterar_rota_usecase: AlterarRotaUsecase,
        buscar_rotas_por_servico_id_usecase: BuscarRotasPorServicoIdUsecase,
        excluir_rota_usecase: ExcluirRotaUsecase,
    ):
        self._console = console
        self._criar_servico_usecase = criar_servico_usecase
        self._alterar_servico_usecase = alterar_servico_usecase
        self._buscar_servico_usecase = buscar_servico_usecase
        self._excluir_servico_usecase = excluir_servico_usecase
        self._criar_rota_usecase = criar_rota_usecase
        self._alterar_rota_usecase = alterar_rota_usecase
        self._buscar_rotas_por_servico_id_usecase = buscar_rotas_por_servico_id_usecase
        self._excluir_rota_usecase = excluir_rota_usecase
        self._titulo = "O que deseja fazer?"
        self._opcoes_servicos = {
            1: "Criar um serviço",
            2: "Alterar um serviço",
            3: "Consultar serviços",
            4: "Excluir um serviço",
            5: "Sair",
        }
        self._opcoes_rotas = {
            1: "Adicionar rota",
            2: "Alterar rota",
            3: "Excluir rota",
            4: "Finalizar",
        }

    def executar(self):
        while True:
            try:
                self._console.clear()
                servicos = self._buscar_servico_usecase.executar()
                self._listar_servicos(servicos)
                self._console.menu(self._opcoes_servicos, self._titulo)
                opcao_escolhida = self._console.obter_opcao_escolhida(
                    self._opcoes_servicos
                )
                match opcao_escolhida:
                    case 1:
                        self._criar_servico()
                    case 2:
                        self._alterar_servico(servicos)
                    case 3:
                        self._consultar()
                    case 4:
                        self._excluir()
                    case 5:
                        return
            except ValueError as e:
                self._console.error(e)
                input()

    def _criar_servico(self):
        nome = self._console.perguntar("Nome")
        servico = self._criar_servico_usecase.executar(nome)
        self._gerenciar_rotas(servico)

    def _alterar_servico(self, servicos: List[Servico]):
        id = int(self._console.perguntar("Digite o serviço"))
        servico = next((s for s in servicos if s.obter_id() == id), None)
        nome = self._console.perguntar(f"Digite o nome ({servico.obter_nome()})")
        if nome != "":
            self._alterar_servico_usecase.executar(
                servico.obter_id(), servico.obter_nome()
            )
        self._gerenciar_rotas(servico)

    def _excluir(self):
        id = int(self._console.perguntar("Digite o serviço"))
        self._excluir_servico_usecase.executar(id)

    def _listar_servicos(self, servicos: List[Servico]):
        dic_servicos = {s.obter_id(): s.obter_nome() for s in servicos}
        self._console.menu(
            dic_servicos,
            titulo="Serviços",
            coluna="Nome",
        )

    def _listar_rotas(self, nome: str, rotas: List[Rota]):
        self._console.menu(
            {r.obter_id(): r.obter_caminho() for r in rotas},
            titulo=nome,
            coluna="Rotas",
        )

    def _gerenciar_rotas(self, servico: Servico):
        while True:
            self._console.clear()
            rotas = self._buscar_rotas_por_servico_id_usecase.executar(
                servico.obter_id()
            )
            self._listar_rotas(
                servico.obter_nome(),
                rotas,
            )
            self._console.menu(self._opcoes_rotas)
            opcao_escolhida = self._console.obter_opcao_escolhida(self._opcoes_rotas)
            match opcao_escolhida:
                case 1:
                    caminho = self._console.perguntar("Caminho")
                    self._criar_rota_usecase.executar(caminho, servico.obter_id())
                case 2:
                    rota_id = int(self._console.perguntar("Rota a alterar"))
                    caminho = self._console.perguntar("Digite a rota")
                    self._alterar_rota_usecase.executar(rota_id, caminho)
                case 3:
                    rota_id = int(self._console.perguntar("Rota a excluir"))
                    self._excluir_rota_usecase(rota_id)
                case 4:
                    break
                case _:
                    self._console.error("Operação inválida...")
                    input()
