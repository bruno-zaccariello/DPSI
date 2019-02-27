--
-- File generated with SQLiteStudio v3.2.1 on qua fev 27 09:09:35 2019
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: employee
CREATE TABLE IF NOT EXISTS employee (cpf INT PRIMARY KEY NOT NULL, cargo VARCHAR NOT NULL, nome VARCHAR NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
