from infra.cli.database_cli import DatabaseCLI
from infra.cli.icli import ICLI
from infra.cli.iconsole import IConsole
from infra.cli.servico_cli import ServicoCLI


class MainCLI(ICLI):
    def __init__(
        self, console: IConsole, servico_cli: ServicoCLI, database_cli: DatabaseCLI
    ):
        self._console = console
        self._servico_cli = servico_cli
        self._database_cli = database_cli
        self._titulo = "Bem vindo"
        self._opcoes = {
            1: "Testar",
            2: "Menu de serviços",
            3: "Banco de dados",
            4: "Sair",
        }

    def executar(self):
        while True:
            self._console.clear()
            self._console.menu(self._opcoes, self._titulo)
            opcao_escolhida = self._console.obter_opcao_escolhida(self._opcoes)
            match opcao_escolhida:
                case 1:
                    self._console.error("Testes ainda não estão disponíveis!")
                case 2:
                    self._servico_cli.executar()
                case 3:
                    self._database_cli.executar()
                case 4:
                    self._console.exit()
                case _:
                    self._console.error(f"Opção inválida")
