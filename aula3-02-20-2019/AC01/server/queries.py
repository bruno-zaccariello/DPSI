INSERT_EMPLOYEE = "INSERT INTO employee (cpf, nome, cargo) VALUES (?, ?, ?)"

SELECT_ALL = "SELECT * FROM employee"

SELECT_CPF = "SELECT * FROM employee WHERE cpf = (?)"

DELETE_EMPLOYEE = "DELETE FROM employee WHERE cpf = (?)"

UPDATE_EMPLOYEE = "UPDATE employee SET cpf = ?, nome = ?, cargo = ? WHERE cpf = ?"