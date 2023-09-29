def make_dict(text: str) -> dict[int:int]:
    first, second, third, *other = (int(i) for i in text.split('/'))
    return {second: first, third: tuple(other)}


if __name__ == '__main__':
    text = '3/5/7/8/10/12/13'
    print(make_dict(text))
