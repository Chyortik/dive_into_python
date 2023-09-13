my_list = [2, 4, 2, 8, 3, 5, 4, 10, 5]
print(list(set(filter(lambda x: my_list.count(x) > 1, my_list))))
