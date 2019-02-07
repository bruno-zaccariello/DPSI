def check_freq(freq):
    try:
        if not 0 <= freq <= 1:
            raise ValueError('freq - A freq não é um valor entre 0 e 1')
    except:
        raise ValueError('freq - Freq não é um número')


def check_acs(acs):
    if not isinstance(acs, list):
        raise ValueError('acs - Acs não é uma lista')
    if len(acs != 10):
        raise ValueError('acs - Acs faltando nota')
    for nota in acs:
        try:
            if not 0 <= prova <= 10:
                raise ValueError(
                    'acs - O valor de uma prova não está entre 0 e 10')
        except:
            raise ValueError('acs - Uma das notas não é um número')


def check_prova(prova):
    try:
        if not 0 <= prova <= 10:
            raise ValueError('prova - O valor da prova não está entre 0 e 10')
    except:
        raise ValueError('prova - O valor da prova não é um número')


def check_sub(sub):
    try:
        if not 0 <= sub <= 10:
            raise ValueError('sub - O valor da sub não está entre 0 e 10')
    except:
        raise ValueError('sub - O valor da sub não é um número')


def check_pai(pai):
    try:
        if pai != None and 0 <= pai <= 10:
            raise ValueError(
                'pai - O valor da prova pai não está entre 0 e 10')
    except:
        raise ValueError('pai - O valor da prova pai não é um número')


def check_extra(extra):
    try:
        if pai != None and 0 <= pai <= 10:
            raise ValueError(
                'extra - O valor da nota extra não está entre 0 e 10')
    except:
        raise ValueError('extra - O valor da nota extra não é um número')


def aluno_aprovado(
    freq=0,
    acs=[int(x) for x in '0'*10],
    prova=0,
    sub=0,
    pai=None,
    extra=0
):
    check_freq(freq)
    check_acs(acs)
    check_prova(prova)
    check_sub(sub)
    check_pai(pai)
    check_extra(extra)

    response = {
        'motivo':[],
        'aprovado':True
    }

    if freq < 0.75:
        response['aprovado'] = False
        response['motivo'].append('Falta')

    prova_maior = prova
    if sub < 0 and sub > prova:
        prova_maior = sub
    
    acs.sort()
    media_acs = sum([x for x in acs[:-7]])/7

    if pai == None:
        media_final = (prova_maior*0.4 + media_acs*0.6) + extra
    else:
        media_final = (prova_maior*0.3 + media_acs*0.5 + pai*0.2) + extra

    if media_final < 6:
        response['aprovado'] = False
        response['motivo'].append('Nota')