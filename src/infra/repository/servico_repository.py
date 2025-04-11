from typing import List
from application.repository.iservico_repository import IServicoRepository
from domain.entity.rota import Rota
from domain.entity.servico import Servico
from infra.db.database import Database


class ServicoRepository(IServicoRepository):
    def __init__(self, db: Database):
        self._db = db

    def criar_servico(self, nome: str) -> Servico:
        servico = self._db.executar(
            f"INSERT INTO servicos(nome) VALUES('{nome}') RETURNING *",
        )[0]
        self._db.commit()
        return self._montar_servico(servico, [])

    def alterar_servico(self, servico: Servico):
        self._db.executar(
            f"UPDATE servicos SET nome='{servico.obter_nome()}' WHERE id={servico.obter_id()}"
        )
        self._db.commit()

    def buscar_servicos(self):
        servicos = self._db.executar(f"SELECT * FROM servicos")
        return list(map(lambda s: self._montar_servico(s, []), servicos))

    def excluir_servico(self, id: int):
        self._db.executar(f"DELETE FROM servicos WHERE id={id}")
        self._db.commit()

    def criar_rota(self, caminho: str, servico_id: int):
        self._db.executar(
            f"INSERT INTO rotas (caminho, servico_id) VALUES ('{caminho}', {servico_id})"
        )
        self._db.commit()

    def alterar_rota(self, rota: Rota):
        self._db.executar(
            f"UPDATE rotas SET caminho='{rota.obter_caminho()}', payload='{rota.obter_payload()}' WHERE id={rota.obter_id()}"
        )
        self._db.commit()

    def buscar_rotas_por_servico_id(self, servico_id: int) -> List[Rota]:
        rotas = self._db.executar(f"SELECT * FROM rotas WHERE servico_id={servico_id}")
        return list(map(lambda r: self._montar_rota(r), rotas))

    def excluir_rota(self, id: int):
        self._db.executar(f"DELETE FROM rotas WHERE id={id}")
        self._db.commit()

    def _montar_servico(self, servico, rotas) -> Servico:
        return Servico(id=servico[0], nome=servico[1], rotas=rotas)

    def _montar_rota(self, rota) -> Rota:
        return Rota(id=rota[0], caminho=rota[1], payload=rota[2])
