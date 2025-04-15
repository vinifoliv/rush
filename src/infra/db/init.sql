CREATE TABLE IF NOT EXISTS servicos (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome" VARCHAR(255) NOT NULL,
    UNIQUE ("nome")
);

CREATE TABLE IF NOT EXISTS rotas (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "metodo" VARCHAR(6) NOT NULL,
    "caminho" VARCHAR(255) NOT NULL,
    "payload" TEXT,
    "servico_id" INT NOT NULL,
    FOREIGN KEY ("servico_id") REFERENCES servicos ("id")
);
