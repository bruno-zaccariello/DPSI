from flask import jsonify


class DataHandler():
    def __init__(self):
        self.errors = []

    DEFAULT_ERROR_MSG = jsonify(
        {'status': 'error', 'message': 'Houve um erro interno ao processar sua solicitação'}), 500
    INVALID_CPF_MESSAGE = jsonify(
        {'status': 'error', 'message': 'CPF Inválido'}), 400

    def success(self, key, message, status, extraData=dict()):
        return jsonify({'status': 'success', key: message, 'details': extraData}), status

    def throw(self, status):
        response = jsonify({'status': 'error-list', 'messages': self.errors}), status
        self.errors = []
        return response

    def toThrow(self):
        return len(self.errors) > 0

    def fieldError(self, field):
        self.errors.append({
            'message': f'{field} - Campo inválido ou faltando',
            'field': field
        })
        return self

    def addError(self, message, extraData=dict()):
        self.errors.append({
            'message': message,
            'details': extraData
        })
        return self

    def checkCPF(self, cpf):
        if len(str(cpf)) != 11:
            return False
        else:
            return True
