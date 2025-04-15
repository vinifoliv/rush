from typing import List
from application.repository.iservico_repository import IServicoRepository
from domain.entity.metodo_http import MetodoHTTP
from domain.entity.rota import Rota
from domain.entity.servico import Servico
from infra.db.database import Database


class ServicoRepository(IServicoRepository):
    def __init__(self, db: Database):
        self._db = db

    def criar_servico(self, nome: str) -> Servico:
        self._db.executar(f"INSERT INTO servicos(nome) VALUES(?) RETURNING *", (nome,))
        servico = self._db.buscarUm()
        self._db.commit()
        return self._montar_servico(servico, [])

    def alterar_servico(self, servico: Servico):
        self._db.executar(
            f"UPDATE servicos SET nome=? WHERE id=?",
            (servico.obter_nome(), servico.obter_id()),
        )
        self._db.commit()

    def buscar_servicos(self):
        self._db.executar(f"SELECT * FROM servicos")
        servicos = self._db.buscarMuitos()
        return list(map(lambda s: self._montar_servico(s, []), servicos))

    def buscar_servico_por_id(self, id: int) -> Servico:
        self._db.executar(f"SELECT * FROM servicos WHERE id=?", (id,))
        servico = self._db.buscarUm()
        if not servico:
            return None
        return self._montar_servico(servico, [])

    def buscar_servico_por_nome(self, nome: str) -> Servico:
        self._db.executar(f"SELECT * FROM servicos WHERE nome=?", (nome,))
        servico = self._db.buscarUm()
        if not servico:
            return None
        return self._montar_servico(servico, [])

    def excluir_servico(self, id: int):
        self._db.executar(f"DELETE FROM servicos WHERE id=?", (id,))
        self._db.commit()

    def criar_rota(
        self, metodo: MetodoHTTP, caminho: str, payload: str, servico_id: int
    ):
        self._db.executar(
            f"INSERT INTO rotas (metodo, caminho, payload, servico_id) VALUES (?, ?, ?, ?)",
            (metodo.obter_valor(), caminho, payload, servico_id),
        )
        self._db.commit()

    def alterar_rota(self, rota: Rota):
        self._db.executar(
            f"UPDATE rotas SET metodo=?, caminho=?, payload=? WHERE id=?",
            (
                rota.obter_metodo().obter_valor(),
                rota.obter_caminho(),
                rota.obter_payload(),
                rota.obter_id(),
            ),
        )
        self._db.commit()

    def buscar_rota_por_caminho_e_servico_id(
        self, caminho: str, servico_id: int
    ) -> Rota:
        self._db.executar(
            f"SELECT * FROM rotas WHERE caminho=? AND servico_id=?",
            (caminho, servico_id),
        )
        rota = self._db.buscarUm()
        if rota == None:
            return None
        return self._montar_rota(rota)

    def buscar_rotas_por_servico_id(self, servico_id: int) -> List[Rota]:
        self._db.executar(f"SELECT * FROM rotas WHERE servico_id=?", (servico_id,))
        rotas = self._db.buscarMuitos()
        return list(map(lambda r: self._montar_rota(r), rotas))

    def buscar_rota_por_id(self, id: int) -> Rota:
        self._db.executar(f"SELECT * FROM rotas WHERE id=?", (id,))
        rota = self._db.buscarUm()
        if rota == None:
            return None
        return self._montar_rota(rota)

    def excluir_rota(self, id: int):
        self._db.executar(f"DELETE FROM rotas WHERE id=?", (id,))
        self._db.commit()

    def _montar_servico(self, servico, rotas) -> Servico:
        return Servico(id=servico[0], nome=servico[1], rotas=rotas)

    def _montar_rota(self, rota) -> Rota:
        return Rota(id=rota[0], metodo=MetodoHTTP(rota[1]), caminho=rota[2], payload=rota[3])
