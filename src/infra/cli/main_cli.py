from infra.cli.icli import ICLI
from infra.cli.iconsole import IConsole


class MainCLI(ICLI):
    _OPCOES = {
        1: "Testar",
        2: "Menu de serviços",
        3: "Banco de dados",
        4: "Sair",
    }

    def __init__(
        self,
        console: IConsole,
        teste_cli: ICLI,
        servico_cli: ICLI,
        database_cli: ICLI,
    ):
        self._console = console
        self._teste_cli = teste_cli
        self._servico_cli = servico_cli
        self._database_cli = database_cli

    def executar(self):

        while True:
            try:
                self._console.clear()
                self._console.menu(
                    opcoes=self._OPCOES,
                    titulo="Bem vindo",
                )
                opcao_escolhida = self._console.obter_opcao_escolhida(self._OPCOES)
                match opcao_escolhida:
                    case 1:
                        self._teste_cli.executar()
                    case 2:
                        self._servico_cli.executar()
                    case 3:
                        self._database_cli.executar()
                    case 4:
                        self._console.exit()
                    case _:
                        self._console.error(f"Opção inválida")
            except ValueError as e:
                self._console.error(e.args[0])
                continuar = self._console.confirmar("Continuar?")
                if not continuar:
                    break
            except KeyboardInterrupt as e:
                self._console.print("\n[info]Encerrando...[/]")
                break
