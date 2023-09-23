from datetime import date

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01


def exit_bank():
    print("Всего доброго, приходите к нам еще!\n")
    exit()


def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print(f'Начислены проценты в размере: {percent_add * bank}')


def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("Комиссия за снятие наличных: ", 30)
    elif cash * percent_take > 600:
        bank -= 600
        print("Комиссия за снятие наличных: ", 600)
    else:
        bank -= cash * percent_take
        print("Комиссия за снятие наличных: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере: ", percent_add * bank)


def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму операции, кратную 50\n"))
        if cash % 50 == 0:
            return cash


list_operation = []

while True:
    action = input("1 - снять\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("списан налог на богатство: ", bank * percent_tax)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("На Вашем счету недостаточно средств\n")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank)
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()
