def cash_bonus(names: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
    return {name: money / 100 * perc
            for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}


if __name__ == '__main__':
    names = ["Иванов", "Петров", "Сидоров"]
    cash = [70000, 90000, 80000]
    percent = ['10.25%', '9.55%', '9.65%']
    print(cash_bonus(names, cash, percent))
