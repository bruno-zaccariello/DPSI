def counter(text):
    counting = dict()
    for word in text.split(' '):
        if word in counting:
            counting[word] += 1
        else:
            counting[word] = 1
    return counting


print(counter('''o doce perguntou ao doce qual é o doce mais doce e o doce respondeu ao doce que o doce mais doce é o doce de batata doce'''))
