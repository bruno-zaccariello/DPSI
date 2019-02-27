import sqlite3
from flask import Flask, jsonify, g
from flask import request as r

app = Flask(__name__)

with app.app_context():
    import queries
    from dataHandler import DataHandler
    DATABASE = ''.join(x + '\\' for x in __file__.split('\\')[:-1]) + 'employee.sqlite3'
    dataHandler = DataHandler()

# ======================================================================
# = Database Setup                                                     =
# ======================================================================

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('db_mount.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

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

# ======================================================================
# = Paths Below                                                        =
# ======================================================================

@app.route('/funcionario/<int:cpf>', methods=['GET'])
def get_employee(cpf):
    try:
        if not dataHandler.checkCPF(cpf):
            return dataHandler.INVALID_CPF_MESSAGE
        employee = doQuery(queries.SELECT_CPF, (cpf,))
        if employee:
            return dataHandler.success('employee', employee[0], 200)
        return dataHandler.addError('Empregado não encontrado').throw(404)
    except:
        return dataHandler.DEFAULT_ERROR_MSG

@app.route('/funcionario/<int:cpf>', methods=['POST'])
def post_employee(cpf):
    try:
        if not dataHandler.checkCPF(cpf):
            return dataHandler.INVALID_CPF_MESSAGE
        if doQuery(queries.SELECT_CPF, (cpf,)):
            return dataHandler.addError('CPF já cadastrado no sistema').throw(400)
        data = r.get_json()

        cargo = data.get('cargo', None)
        nome = data.get('nome', None)
        
        if not cargo:
            dataHandler.fieldError('cargo')
        if not nome:
            dataHandler.fieldError('nome')
        if dataHandler.toThrow():
            return dataHandler.throw(400)

        q = doQuery(queries.INSERT_EMPLOYEE, (cpf, nome, cargo))

        response = {
            'nome': nome,
            'cpf': cpf,
            'cargo': cargo
        }
        return dataHandler.success('employee', response, 200)
    except:
        return dataHandler.DEFAULT_ERROR_MSG

@app.route('/funcionario/<int:cpf>', methods=['DELETE'])
def delete_employee(cpf):
    try:
        if not dataHandler.checkCPF(cpf):
            return dataHandler.INVALID_CPF_MESSAGE
        
        checkExistence = doQuery(queries.SELECT_CPF, (cpf,))
        if not checkExistence:
            return dataHandler.addError('Empregado não existe no banco de dados').throw(400)

        q = doQuery(queries.DELETE_EMPLOYEE, (cpf,))
        testDelete = doQuery(queries.SELECT_CPF, (cpf,))

        if testDelete:
            return dataHandler.addError('Houve um erro ao deletar o empregado').throw(500)
        else:
            return dataHandler.success('message', 'Empregado deletado com sucesso', 200)
    except:
        return dataHandler.DEFAULT_ERROR_MSG

@app.route('/funcionario/<int:cpf>', methods=['PUT'])
def update_employee(cpf):

    if not dataHandler.checkCPF(cpf):
        return dataHandler.INVALID_CPF_MESSAGE
    employee = doQuery(queries.SELECT_CPF, (cpf,))[0]
    if not employee:
        return dataHandler.addError('CPF não cadastrado no sistema').throw(400)
    data = r.get_json()

    cargo = data.get('cargo') if data.get('cargo') else employee.get('cargo', '')
    nome = data.get('nome') if data.get('nome') else employee.get('nome', '')

    q = doQuery(queries.UPDATE_EMPLOYEE, (cpf, nome, cargo, cpf))

    response = {
        'nome': nome,
        'cpf': cpf,
        'cargo': cargo
    }
    return dataHandler.success('message', 'Funcionário atualizado com sucesso', 200, response)


@app.route('/funcionario/<string:invalid_cpf>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def fake_url_employee(invalid_cpf):
    return dataHandler.addError('Favor utilizar um CPF numérico válido').throw(400)

init_db()

if __name__ == "__main__":
    app.run(port=8080)
