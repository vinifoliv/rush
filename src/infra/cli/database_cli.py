from infra.cli.icli import ICLI
from infra.cli.iconsole import IConsole
from infra.db.database import Database


class DatabaseCLI(ICLI):
    def __init__(self, console: IConsole, db: Database):
        self._console = console
        self._db = db
        self._titulo = "Banco de Dados"
        self._opcoes = {1: "Inicializar", 2: "Limpar", 3: "Sair"}

    def executar(self):
        self._console.clear()
        while True:
            self._console.menu(self._opcoes, self._titulo)
            opcao_escolhida = self._console.obter_opcao_escolhida(self._opcoes)
            match opcao_escolhida:
                case 1:
                    self._db.inicializar()
                    self._console.print("Banco de dados inicializado com sucesso!")
                case 2:
                    self._db.limpar()
                    self._console.print("Banco de dados limpo com sucesso!")
                case 3:
                    return
                case _:
                    self._console.error(f"Opção inválida")
