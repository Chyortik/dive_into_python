def fibonacci(n: int) -> list[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    n = int(input("Введите длину последовательности чисел Фибоначчи: "))
    print(*(fibonacci(n)))
