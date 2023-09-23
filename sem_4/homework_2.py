def hashable_dicts(**kwargs):
    pets = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        pets[v] = k
    return pets


print(hashable_dicts(dog='Шарик', cat={'Барсик': 2, 'Мурка': 3}, turtle=['Эльза', 'Ящер', 'Толик'],
                     hamster={'Эдуард', 'Пух'}))
