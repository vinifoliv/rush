from typing import List
from application.usecase.alterar_rota_usecase import AlterarRotaUsecase
from application.usecase.buscar_rotas_por_servico_id_usecase import (
    BuscarRotasPorServicoIdUsecase,
)
from application.usecase.criar_rota_usecase import CriarRotaUsecase
from application.usecase.excluir_rota_usecase import ExcluirRotaUsecase
from domain.entity.metodo_http import MetodoHTTP
from domain.entity.rota import Rota
from domain.entity.servico import Servico
from infra.cli.icli import ICLI
from infra.cli.iconsole import IConsole
from infra.cli.ifile_system import IFileSystem


class RotaCLI(ICLI):
    def __init__(
        self,
        console: IConsole,
        file_system: IFileSystem,
        criar_rota_usecase: CriarRotaUsecase,
        alterar_rota_usecase: AlterarRotaUsecase,
        buscar_rotas_por_servico_id_usecase: BuscarRotasPorServicoIdUsecase,
        excluir_rota_usecase: ExcluirRotaUsecase,
    ):
        self._console = console
        self._file_system = file_system
        self._criar_rota_usecase = criar_rota_usecase
        self._alterar_rota_usecase = alterar_rota_usecase
        self._buscar_rotas_por_servico_id_usecase = buscar_rotas_por_servico_id_usecase
        self._excluir_rota_usecase = excluir_rota_usecase
        self._titulo = "O que deseja fazer?"
        self._opcoes_rotas = {
            1: "Adicionar rota",
            2: "Alterar rota",
            3: "Excluir rota",
            4: "Finalizar",
        }

    def executar(self, servico: Servico):
        while True:
            try:
                self._console.clear()
                rotas = self._buscar_rotas_por_servico_id_usecase.executar(
                    servico.obter_id()
                )
                self._listar_rotas(
                    servico.obter_nome(),
                    rotas,
                )
                self._console.menu(self._opcoes_rotas)
                opcao_escolhida = self._console.obter_opcao_escolhida(
                    self._opcoes_rotas
                )
                match opcao_escolhida:
                    case 1:
                        self._criar_rota(servico)
                    case 2:
                        self._alterar_rota(rotas)
                    case 3:
                        self._excluir_rota()
                    case 4:
                        break
                    case _:
                        self._console.error("Operação inválida...")
                        input()
            except ValueError as e:
                self._console.error(e)
                continuar = self._console.confirmar("Continuar?")
                if not continuar:
                    break

    def _criar_rota(self, servico: Servico):
        metodo = MetodoHTTP(self._console.perguntar("Método").upper())
        caminho = self._console.perguntar("Caminho")
        if caminho == "":
            raise ValueError(f"O caminho '{caminho}' é inválido.")

        payload = None
        if self._console.confirmar("Adicionar payload?"):
            payload = self._obter_payload()

        self._criar_rota_usecase.executar(metodo, caminho, payload, servico.obter_id())

    def _alterar_rota(self, rotas: List[Rota]):
        rota_id = int(self._console.perguntar("Rota a alterar"))
        rota = next((r for r in rotas if r.obter_id() == rota_id), None)
        if rota == None:
            raise ValueError(f" A rota '{rota_id}' é inválida.")

        metodo = self._console.perguntar("Método")
        if metodo == "":
            metodo = rota.obter_metodo()
        else:
            metodo = MetodoHTTP(metodo)

        caminho = self._console.perguntar("Digite a rota")
        if caminho == "":
            caminho = rota.obter_caminho()

        alterar_payload = self._console.confirmar("Alterar payload?")
        if not alterar_payload:
            self._alterar_rota_usecase.executar(
                rota_id, metodo, caminho, rota.obter_payload()
            )
            return
        caminho_payload = self._console.perguntar("Digite o caminho")
        payload = self._file_system.ler_arquivo(caminho_payload)
        self._alterar_rota_usecase.executar(rota_id, metodo, caminho, payload)

    def _excluir_rota(self):
        rota_id = int(self._console.perguntar("Rota a excluir"))
        self._excluir_rota_usecase(rota_id)

    def _listar_rotas(self, nome: str, rotas: List[Rota]):
        self._console.print(f"[bold yellow]{nome}[/bold yellow]")
        for rota in rotas:
            self._console.print(
                f"[magenta]{rota.obter_id()}.[/magenta] [cyan]{rota.obter_metodo().obter_valor()}[/cyan] [green]{rota.obter_caminho()}[/green]"
            )
            payload = rota.obter_payload()
            if not payload:
                self._console.print("\t[cyan]Payload não cadastrado.[/cyan]")
                continue
            self._console.print(f"[cyan]{payload}[/cyan]")

    def _obter_payload(self):
        caminho = self._console.perguntar("Digite o caminho do payload")
        payload = self._file_system.ler_arquivo(caminho)
        return payload
