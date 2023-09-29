def from_str_to_dict(text: str) -> dict[str:int]:
    return {k: ord(k) for k in text}


if __name__ == '__main__':
    text = 'Дима'
    print(from_str_to_dict(text))
