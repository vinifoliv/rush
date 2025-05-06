from typing import List, NamedTuple

from application.repository.iservico_repository import IServicoRepository
from domain.entity.dominio import Dominio
from domain.entity.metodo_http import MetodoHTTP
from domain.entity.rota import Rota
from domain.entity.servico import Servico
from infra.db.database import Database


class ServicoSQLite(NamedTuple):
    servico_id: int
    nome: str
    dominio: str


class RotaSQLite(NamedTuple):
    rota_id: int
    metodo: str
    caminho: str
    payload: str | None
    servico_id: int


class ServicoRepository(IServicoRepository):
    def __init__(self, db: Database):
        self._db = db

    def criar_servico(self, servico: Servico) -> Servico:
        self._db.executar(
            "INSERT INTO servicos(nome, dominio) VALUES(?, ?) RETURNING *",
            (servico.nome, servico.dominio.valor),
        )
        servico_sqlite = ServicoSQLite(*self._db.buscarUm())
        self._db.commit()

        servico_criado = self._montar_servico(servico_sqlite, [])
        return servico_criado

    def alterar_servico(self, servico: Servico) -> Servico:
        if not servico.id:
            raise ValueError("ID do serviço não informado!")

        self._db.executar(
            "UPDATE servicos SET nome=?, dominio=? WHERE id=? RETURNING *",
            (servico.nome, servico.dominio, servico.id),
        )
        servico_sqlite = self._db.buscarUm()
        self._db.commit()

        rotas = self.buscar_rotas_por_servico_id(servico.id)
        servico_alterado = self._montar_servico(servico_sqlite, rotas)
        return servico_alterado

    def buscar_servicos(self) -> List[Servico]:
        self._db.executar(
            """
            SELECT * FROM servicos s 
            """
        )
        servicos_sqlite = self._db.buscarMuitos()

        servicos = []
        for s in servicos_sqlite:
            servico_id = s[0]
            rotas = self.buscar_rotas_por_servico_id(servico_id)
            servicos.append(self._montar_servico(s, rotas))

        return servicos

    def buscar_servico_por_id(self, id: int) -> Servico | None:
        self._db.executar("SELECT * FROM servicos WHERE id=?", (id,))
        servico_sqlite = self._db.buscarUm()

        if not servico_sqlite:
            return None

        rotas = self.buscar_rotas_por_servico_id(id)

        servico = self._montar_servico(servico_sqlite, rotas)
        return servico

    def buscar_servico_por_nome(self, nome: str) -> Servico | None:
        self._db.executar("SELECT * FROM servicos WHERE nome=?", (nome,))
        servico_sqlite = self._db.buscarUm()

        if not servico_sqlite:
            return None

        servico_id = servico_sqlite[0]
        rotas = self.buscar_rotas_por_servico_id(servico_id)

        servico = self._montar_servico(servico_sqlite, rotas)
        return servico

    def excluir_servico(self, id: int) -> Servico:
        rotas = self.buscar_rotas_por_servico_id(id)

        self._db.executar(
            """
            DELETE FROM servicos WHERE id=?
            RETURNING *
            """,
            (id,),
        )
        servico_sqlite = self._db.buscarUm()
        self._db.commit()

        servico_excluido = self._montar_servico(servico_sqlite, rotas)
        return servico_excluido

    def criar_rota(self, rota: Rota, servico_id: int) -> Rota:
        self._db.executar(
            """
            INSERT INTO rotas (metodo, caminho, payload, servico_id) VALUES (?, ?, ?, ?)
            RETURNING *
            """,
            (rota.metodo.valor, rota.caminho, rota.payload, servico_id),
        )
        rota_sqlite = RotaSQLite(*self._db.buscarUm())
        self._db.commit()

        rota_criada = self._montar_rota(rota_sqlite)
        return rota_criada

    def alterar_rota(self, rota: Rota) -> Rota:
        self._db.executar(
            """
            UPDATE rotas SET metodo=?, caminho=?, payload=? WHERE id=?
            RETURNING * 
            """,
            (
                rota.metodo.valor,
                rota.caminho,
                rota.payload,
                rota.id,
            ),
        )
        rota_sqlite = RotaSQLite(*self._db.buscarUm())
        self._db.commit()

        rota_alterada = self._montar_rota(rota_sqlite)
        return rota_alterada

    def buscar_rota_por_caminho_e_servico_id(
        self, caminho: str, servico_id: int
    ) -> Rota | None:
        self._db.executar(
            """
            SELECT * FROM rotas WHERE caminho=? AND servico_id=?
            """,
            (caminho, servico_id),
        )
        rota_sqlite = self._db.buscarUm()
        if rota_sqlite is None:
            return None

        rota_sqlite = RotaSQLite(*rota_sqlite)
        rota = self._montar_rota(rota_sqlite)
        return rota

    def buscar_rotas_por_servico_id(self, servico_id: int) -> List[Rota]:
        self._db.executar("SELECT * FROM rotas WHERE servico_id=?", (servico_id,))

        rotas_sqlite = list(map(lambda r: RotaSQLite(*r), self._db.buscarMuitos()))

        rotas = list(map(lambda r: self._montar_rota(r), rotas_sqlite))
        return rotas

    def buscar_rota_por_id(self, id: int) -> Rota | None:
        self._db.executar(
            """
            SELECT * FROM rotas WHERE id=?
            """,
            (id,),
        )
        rota_sqlite = self._db.buscarUm()
        if not rota_sqlite:
            return None

        rota_sqlite = RotaSQLite(*rota_sqlite)

        rota = self._montar_rota(rota_sqlite)
        return rota

    def excluir_rota(self, id: int) -> Rota:
        self._db.executar(
            """
            DELETE FROM rotas WHERE id=?
            RETURNING *
            """,
            (id,),
        )
        rota_sqlite = RotaSQLite(*self._db.buscarUm())
        self._db.commit()

        rota = self._montar_rota(rota_sqlite)
        return rota

    def _montar_servico(self, servico: ServicoSQLite, rotas: List[Rota]) -> Servico:
        servico_id = servico[0]
        nome = servico[1]
        dominio = Dominio(servico[2])
        servico_montado = Servico(servico_id, nome, dominio, rotas)
        return servico_montado

    def _montar_rota(self, rota: RotaSQLite) -> Rota:
        rota_id = rota[0]
        metodo = MetodoHTTP(rota[1])
        caminho = rota[2]
        payload = rota[3]

        rota_montada = Rota(rota_id, metodo, caminho, payload)
        return rota_montada
