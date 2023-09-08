"""
Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией,
даже ошибочной.
Любое действие выводит сумму денег
"""


def fill(money: int):
    while True:
        money_to_fill = int(input("Какую сумму (кратную 50 у.е.) вы хотите внести: "))
        if money_to_fill % 50 != 0:
            print("Введите сумму, кратную 50.")
        else:
            break

    return money + money_to_fill


def get_money(money: int):
    while True:
        money_to_take = int(input("Какую сумму (кратную 50 у.е.) вы хотите снять: "))
        percent = money_to_take * 0.015
        if percent < 30:
            money_with_percent = money_to_take + 30
        elif percent > 600:
            money_with_percent = money_to_take + 600
        else:
            money_with_percent = money_to_take + percent

        if money_to_take % 50 != 0:
            print("Введите сумму, кратную 50.")
        elif money_with_percent > money:
            print("Недостаточно средств. Введите меньшую сумму.")
        else:
            break

    return money - money_with_percent


def you_wont_be_rich(money: int):
    if money > 5000000:
        money *= 0.9
    return money


def check_counter(counter: int, money: int):
    counter += 1
    if counter == 3:
        money *= 1.03
        counter = 0
    return counter, money


def bank():
    money = 0
    counter = 0
    while True:
        print("1. Пополнить счет.")
        print("2. Снять наличные.")
        print("3. Выйти.")
        while True:
            user_choice = int(input("Выберите номер операции: "))
            if user_choice not in [1, 2, 3]:
                print("Неверный ввод. Попробуйте еще раз.")
                money = you_wont_be_rich(money)
                print(money)
            else:
                break

        if user_choice == 1:
            money = you_wont_be_rich(money)
            money = fill(money)
            counter, money = check_counter(counter, money)
            print(money)
        elif user_choice == 2:
            money = you_wont_be_rich(money)
            money = get_money(money)
            counter, money = check_counter(counter, money)
            print(money)
        else:
            money = f'Ваш баланс: {you_wont_be_rich(money)}'
            print("До свидания!")
            print(money)
            return


if __name__ == "__main__":
    bank()
