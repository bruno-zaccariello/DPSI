import requests as r

menu = """
1 - Cadastrar Funcionário
2 - Buscar Funcionário
3 - Deletar Funcionário
4 - Editar Funcionário
0 - Sair
"""
url = 'http://localhost:8080/funcionario/'

def get_cpf():
    cpf = input('Insira o cpf do funcionário: ')
    while not cpf or len(cpf) != 11 or not cpf.isdigit():
        cpf = input('Insira um cpf válido: ')
    return cpf

def show_msg(body):
    status = body.get('status')
    if status == 'success':
        print(f'\nResposta: {body.get("message")}\n')
        print(f'Detalhes: {body.get("details")}\n')
        return None
    if status == 'error':
        print(f'\nResposta: {body.get("message")}\n')
        return None
    if status == 'error-list':
        for message in body.get('messages'):
            print(f'\nResposta: {message.get("message")}\n')
            print(f'Detalhes: {message.get("details")}\n')
        return None

def register_employee():
    nome, cargo = '', ''
    cpf = get_cpf()
    while not nome:
        nome = input('Insira o nome do funcionário: ')
    while not cargo:
        cargo = input('Insira o cargo do funcionário: ')
    funcionario = {
        'nome': nome,
        'cargo': cargo
    }
    post = r.post(url+cpf, json=funcionario)
    body = post.json()
    employee = body.get('employee')
    if post.status_code == 200:
        print('Funcionário cadastrado com sucesso')
        print(f'''
        Nome: {employee.get("nome")}
        Cargo: {employee.get("cargo")} 
        CPF: {employee.get("cpf")}
        ''') 
        return None
    show_msg(body)
    return None

def search_employee():
    cpf = get_cpf()
    get = r.get(url + cpf)
    body = get.json()
    if get.status_code == 200:
        employee = body.get('employee')
        print(f'''
        Nome: {employee["nome"]}
        Cargo: {employee["cargo"]} 
        CPF: {employee["cpf"]}
        ''') 
        return None
    show_msg(body)

def delete_employee():
    cpf = get_cpf()
    delete = r.delete(url + cpf)
    show_msg(delete.json())
    return None

def update_employee():
    cpf = get_cpf()
    nome = input('Insira o nome (Deixe vazio para pular): ')
    cargo = input('Insira o cargo (Deixe vazio para pular): ')
    data = {
        'nome': nome,
        'cargo': cargo
    }
    update = r.put(url + cpf, json=data)
    show_msg(update.json())
    return None


def menu_show():
    print(menu)
    opt = input('Selecionar opção: ')
    while not opt.isdigit():
        print(menu)
        opt = input('Selecione uma opção válida: ')
    opt = int(opt)
    if opt == 1:
        register_employee()
        return menu_show()
    if opt == 2:
        search_employee()
        return menu_show()
    if opt == 3:
        delete_employee()
        return menu_show()
    if opt == 4:
        update_employee()
        return menu_show()
    if opt == 0:
        return None
    return menu_show()

menu_show()