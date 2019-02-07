import requests as r

def getAddress(cep):
    if len(cep) != 8:
        return 'CEP Inválido'
    if not cep.isdigit():
        return 'CEP Inválido - Letras encontradas'
    try:
        response = r.get(f'https://viacep.com.br/ws/{cep}/json/')
        rp = response.json()

        logradouro = rp.get('logradouro', '')
        complemento = rp.get('complemento', '')
        bairro = rp.get('bairro', '')
        localidade = rp.get('localidade', '')
        uf = rp.get('uf', '')

        address = f'{logradouro}; {complemento}; {bairro}; {localidade}; {uf}'
        return address
    except:
        return 'Erro Interno'

print(getAddress('02415002'))
print(getAddress('00'))
print(getAddress('00000000000'))
print(getAddress('a2415002'))
print(getAddress('00000000'))