import sqlite3
from flask import Flask, jsonify, g

from flask import request as r

app = Flask(__name__)

DATABASE = 'employee.sqlite3'

INSERT = "INSERT INTO employee (cpf, cargo) VALUES (?, ?)"

SELECT = "SELECT * FROM employee"

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
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/funcionario/<int:cpf>', methods=['GET'])
def get_employee(cpf):
    db = get_db().cursor()
    if len(str(cpf)) != 11:
        return jsonify({'status': 'error', 'errorMessage': 'CPF Inválido'}), 404
    try:
        # Database connect
        employeeData = {
            'cpf': cpf,
            'cargo': 'cargo'
        }
        return jsonify({'employee': employeeData, 'status': 'success'}), 200
    except:
        return jsonify({'status': 'error', 'errorMessage': 'Erro interno'}), 500


@app.route('/funcionario/<int:cpf>', methods=['POST'])
def post_employee(cpf):
    if len(str(cpf)) != 11:
        return jsonify({'status': 'error', 'errorMessage': 'CPF Inválido'}), 404
    cargo = "buceta"
    q = doQuery(SELECT)
    print(q)
    data = r.get_json()

    cargo = data.get('cargo', None)
    if not cargo:
        return jsonify({'status': 'error', 'errorMessage': 'Favor informar o cargo no corpo da requisição'}), 400
    return jsonify({'status': 'success', 'data': data}), 200


if __name__ == "__main__":
    app.run(port=8080)
