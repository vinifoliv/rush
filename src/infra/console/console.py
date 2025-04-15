import logging
import os
import sys
from typing import Any, Dict, List
from rich import print as rprint
from rich.console import Console as RichConsole
from rich.logging import RichHandler
from rich.prompt import Confirm, Prompt
from rich.table import Table

from infra.cli.iconsole import IConsole


class Console(IConsole):
    """
    API de comunicação da CLI com o console.
    Expõe métodos para impressão, logging, limpeza e fechamento do console.
    """

    def __init__(self):
        self._console = RichConsole()

        FORMAT = "%(message)s"
        logging.basicConfig(
            level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
        )
        self._log = logging.getLogger("rich")

    def menu(
        self, opcoes: Dict[int, str], titulo: str = "", coluna: str = "Opção"
    ) -> int:
        table = Table(
            title=f"[bold yellow]{titulo}[/bold yellow]",
            title_justify="left",
            title_style="yellow",
            show_edge=False,
            box=None,
        )
        table.add_column("No.", style="magenta", justify="left")
        table.add_column(coluna, style="green", justify="left")
        if len(opcoes) == 0:
            self._console.print(f"[bold yellow]{titulo}[/bold yellow]")
            self._console.print(f"[bold cyan]Nenhum dado encontrado.[/bold cyan]")
            return
        for n, valor in opcoes.items():
            table.add_row(str(n), valor)
        self._console.print(table)

    def obter_opcao_escolhida(self, opcoes: Dict[int, str]):
        while True:
            opcao_escolhida = int(Prompt.ask("Selecione uma opção"))
            if not opcao_escolhida in opcoes.keys():
                self.error(f"Opção '{opcao_escolhida}' inválida!")
                continue
            return opcao_escolhida

    def tabela(self, titulo: str, colunas: List[str], linhas: List[Any]):
        table = Table(
            title=f"[bold yellow]{titulo}[/bold yellow]",
            title_justify="left",
            title_style="yellow",
            show_edge=False,
            box=None,
        )
        for i, coluna in enumerate(colunas, 0):
            color = "magenta" if i % 2 == 0 else "green"
            table.add_column(coluna, style=color, justify="left")
        for linha in linhas:
            table.add_row()

    def print(self, text: str):
        rprint(text)

    def perguntar(self, pergunta: str) -> str:
        return Prompt.ask(pergunta)

    def confirmar(self, pergunta: str) -> bool:
        return Confirm.ask(pergunta)

    def info(self, message: str):
        self._log.info(f"{message}")

    def error(self, message: str):
        self._console.print(f"[bold red blink]{message}[/]")

    def clear(self):
        os.system("cls")

    def exit(self, codigo: int = 0):
        sys.exit(codigo)

    def pressione_qualquer_tecla(self):
        rprint("Pressione qualquer tecla...")
        input()
