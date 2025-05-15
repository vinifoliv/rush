from application.usecase.buscar_rotas_por_servico_id_usecase import (
    BuscarRotasPorServicoIdUsecase,
)
from application.usecase.buscar_servicos_usecase import BuscarServicosUsecase
from application.usecase.testar_rota_usecase import TestarRotaUsecase
from domain.entity.servico import Servico
from domain.entity.sessao import Sessao
from infra.cli.icli import ICLI
from infra.cli.iconsole import IConsole


class TesteCLI(ICLI):
    def __init__(
        self,
        console: IConsole,
        buscar_servicos_usecase: BuscarServicosUsecase,
        buscar_rotas_por_servico_id_usecase: BuscarRotasPorServicoIdUsecase,
        testar_rota_usecase: TestarRotaUsecase,
    ):
        self._console = console
        self._buscar_servicos_usecase = buscar_servicos_usecase
        self._buscar_rotas_por_servico_id_usecase = buscar_rotas_por_servico_id_usecase
        self._testar_rota_usecase = testar_rota_usecase

    def executar(self):
        while True:
            try:
                self._console.clear()

                servico = self._servico()
                rota = self._rota(servico)
                qtde_requisicoes = int(
                    self._console.perguntar("Quantidade de requisições")
                )
                qtde_batches = int(self._console.perguntar("Quantidade de batches"))

                sessao = self._testar_rota_usecase.executar(
                    servico, rota, qtde_requisicoes, qtde_batches
                )

                self._imprimir_sessao(sessao)
                continuar = self._console.confirmar("Continuar?")
                if not continuar:
                    break
            except ValueError as e:
                self._console.error(e.args[0])
                input()

    def _servico(self):
        servicos = self._buscar_servicos_usecase.executar()

        opcoes = {s.id: s.nome for s in servicos if s.id}
        self._console.menu(
            titulo="Qual serviço deseja testar?",
            opcoes=opcoes,
            coluna="Serviço",
        )

        servico_id = int(self._console.obter_opcao_escolhida(opcoes))
        servico = next((s for s in servicos if s.id == servico_id), None)

        if not servico:
            raise ValueError("Serviço não existe.")

        return servico

    def _rota(self, servico: Servico):
        if not servico.id:
            raise ValueError(f"Serviço {servico.nome} sem ID!")

        rotas = self._buscar_rotas_por_servico_id_usecase.executar(servico.id)

        opcoes = {r.id: r.caminho for r in rotas if r.id}
        self._console.menu(
            titulo="Qual rota deseja testar?", opcoes=opcoes, coluna="Rota"
        )

        rota_id = int(self._console.obter_opcao_escolhida(opcoes))
        rota = next((r for r in rotas if r.id == rota_id), None)

        if not rota:
            raise ValueError("Rota não encontrada.")

        return rota

    def _imprimir_sessao(self, sessao: Sessao):
        self._console.print(
            f"[green]Média:[/green] [magenta]{sessao.tempo_resposta_medio} ms[/magenta]"
        )
        self._console.print(
            f"[green]Máximo:[/green] [magenta]{sessao.tempo_resposta_maximo} ms[/magenta]"
        )
        self._console.print(
            f"[green]Mínimo:[/green] [magenta]{sessao.tempo_resposta_minimo} ms[/magenta]"
        )
