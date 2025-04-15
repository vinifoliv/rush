from infra.cli.icli import ICLI
from infra.cli.iconsole import IConsole
from infra.db.database import Database


class DatabaseCLI(ICLI):
    def __init__(self, console: IConsole, db: Database):
        self._console = console
        self._db = db

    def executar(self):
        opcoes = {1: "Inicializar", 2: "Limpar", 3: "Sair"}

        while True:
            try:
                self._console.clear()
                self._console.menu(
                    opcoes=opcoes,
                    titulo="Banco de Dados",
                )
                opcao_escolhida = self._console.obter_opcao_escolhida(opcoes)
                match opcao_escolhida:
                    case 1:
                        self._db.inicializar()
                        self._console.print("Banco de dados inicializado com sucesso!")
                        self._console.pressione_qualquer_tecla()
                    case 2:
                        self._db.limpar()
                        self._console.print("Banco de dados limpo com sucesso!")
                        self._console.pressione_qualquer_tecla()
                    case 3:
                        return
            except ValueError as e:
                self._console.error(e)
                continuar = self._console.confirmar("Continuar?")
                if not continuar:
                    break
