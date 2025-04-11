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
from infra.cli.database_cli import DatabaseCLI
from infra.cli.main_cli import MainCLI
from infra.cli.servico_cli import ServicoCLI
from infra.console.console import Console
from infra.db.database import Database
from infra.repository.servico_repository import ServicoRepository

console = Console()
db = Database()

servico_repository = ServicoRepository(db)

criar_rota_usecase = CriarRotaUsecase(servico_repository)
alterar_rota_usecase = AlterarRotaUsecase(servico_repository)
buscar_rotas_por_servico_id_usecase = BuscarRotasPorServicoIdUsecase(servico_repository)
excluir_rota_usecase = ExcluirRotaUsecase(servico_repository)

criar_servico_usecase = CriarServicoUsecase(servico_repository)
alterar_servico_usecase = AlterarServicoUsecase(servico_repository)
buscar_servicos_usecase = BuscarServicosUsecase(servico_repository)
excluir_servico_usecase = ExcluirServicoUsecase(servico_repository)

servico_cli = ServicoCLI(
    console,
    criar_servico_usecase,
    alterar_servico_usecase,
    buscar_servicos_usecase,
    excluir_servico_usecase,
    criar_rota_usecase,
    alterar_rota_usecase,
    buscar_rotas_por_servico_id_usecase,
    excluir_rota_usecase,
)
database_cli = DatabaseCLI(console, db)

cli = MainCLI(console, servico_cli, database_cli)
cli.executar()
