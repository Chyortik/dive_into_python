def from_str_to_dict_2(text: str) -> dict[str:int]:
    res_iter = iter({k: ord(k) for k in text}.items())
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))


if __name__ == '__main__':
    text = 'Дима'
    from_str_to_dict_2(text)
