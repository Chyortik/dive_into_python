def simple_numbers(number: int):
    yield 2
    for i in range(3, number + 1):
        simple = True
        for j in range(2, i - 1):
            if not i % j:
                simple = False
        if simple:
            yield i


if __name__ == '__main__':
    print(*simple_numbers(50))
