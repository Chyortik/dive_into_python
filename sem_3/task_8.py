data = {'Petya': {'нож', 'палатка', 'котелок', 'рюкзак'},
        'Vasya': {'нож', 'спички', 'консервы', 'рюкзак'},
        'Ivan': {'нож', 'палатка', 'чай'}
        }

result_for_all = list(data.values())[0]

value_counters = {}

for value in list(data.values())[1:]:
    result_for_all = result_for_all.intersection(value)

for values in data.values():
    for element in values:
        if element not in value_counters:
            value_counters[element] = 0
            value_counters[element] += 1

friends_without_one = len(data) - 1

item_for_friends_without_one = set()

print('Только у одного друга есть: ')
for key, value in value_counters.items():
    if value == 1:
        print(key, end='; ')
    if value == friends_without_one:
        item_for_friends_without_one.add(key)
print()
print(f'У всех в походе есть: {result_for_all}')

print()
for element in item_for_friends_without_one:
    for name in data:
        if element not in data[name]:
            print(f'Только у {name} нет {element}.')