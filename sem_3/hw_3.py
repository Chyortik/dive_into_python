def backpack(shop: dict[str:int], size: int) -> list[list[str]]:
    pcs, weight = zip(*sorted(shop.items(), key=lambda x: x[1], reverse=True))
    result, temp, temp_w = [], [], 0
    for index, w in enumerate(weight, 0):
        temp_w += w
        temp.append((pcs[index]))
        for index_n, wn in enumerate(weight[index:], index):
            if wn + temp_w <= size:
                temp_w += wn
                temp.append(pcs[index_n])
        result.append(temp)
        temp, temp_w = [], 0
    return result


things_to_hike = {"спички": 1, "посуда": 2, "котелок": 3, "еда": 4, "палатка": 5}
backpack_size = int(input('Введите грузоподъемность рюкзака: '))
[print(i) for i in backpack(things_to_hike, backpack_size)]