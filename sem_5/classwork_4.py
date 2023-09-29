def gen_num():
    return (i for i in range(0, 101, 2) if i // 10 + i % 10 != 8)


if __name__ == '__main__':
    for i in gen_num():
        print(i)
