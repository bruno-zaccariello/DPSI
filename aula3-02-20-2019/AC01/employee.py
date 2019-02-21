import sqlite3
from flask import Flask, jsonify, g

from flask import request as r

app = Flask(__name__)

DATABASE = 'employee.sqlite3'

INSERT = "INSERT INTO employee (cpf, nome, cargo) VALUES (?, ?, ?)"

SELECT = "SELECT * FROM employee"

SELECT_CPF = "SELECT * FROM employee WHERE cpf = ?"

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = make_dicts
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def doQuery(query, args=(), one=False):
    cur = get_db().execute(query, args)
    get_db().commit()
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/funcionario/<int:cpf>', methods=['GET'])
def get_employee(cpf):
    if len(str(cpf)) != 11:
        return jsonify({'status': 'error', 'errorMessage': 'CPF Inválido'}), 404
    employee = doQuery(SELECT_CPF, (cpf))
    print(employee)
    employeeData = {
        'employee':employee
    }
    return jsonify({'employee': employeeData, 'status': 'success'}), 200


@app.route('/funcionario/<int:cpf>', methods=['POST'])
def post_employee(cpf):
    if len(str(cpf)) != 11:
        return jsonify({'status': 'error', 'errorMessage': 'CPF Inválido'}), 404
    data = r.get_json()

    cargo = data.get('cargo', None)
    nome = data.get('nome', None)
    if not cargo:
        return jsonify({'status': 'error', 'errorMessage': 'Favor informar o cargo no corpo da requisição'}), 400
    elif not nome:
        return jsonify({'status': 'error', 'errorMessage': 'Favor informar o nome no corpo da requisição'}), 400
    q = doQuery(INSERT, (cpf, nome, cargo))
    return jsonify({'status': 'success', 'data': data}), 200


if __name__ == "__main__":
    app.run(port=8080)
