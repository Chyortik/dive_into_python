# Задание к семинару 1
1. Решить задачи, которые не успели решить на семинаре.
2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним. [code](./sem_1/hw_1.py)
3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. [code](./sem_1/hw_2.py)
4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT) [code](./sem_1/hw_3.py)


# Задание к семинару 2. Простые типы данных
1. Решить задачи, которые не успели решить на семинаре.
2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата. [code](./sem_2/hw_1.py)
3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions [code](./sem_2/hw_2.py)

# Задание к семинару 3. Коллекции
Условие
1. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.[code](./sem_3/hw_1.py)
2. В большой текстовой строке подсчитать количество встречаемых слов
и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.[code](./sem_3/hw_2.py)
3. Создайте словарь со списком вещей для похода в качестве ключа и их массой
в качестве значения. Определите какие вещи влезут в рюкзак передав его
максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.[code](./sem_3/hw_3.py)

# Задание к семинару 4. Функции
Условие
1. Напишите функцию для транспонирования матрицы [code](./sem_4/homework_1.py)
2. Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.[code](./sem_4/homework_2.py)
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список. [code](./sem_4/homework_3.py)


# Задание к семинару 5. Итераторы и генераторы
## Задание 1
* Пользователь вводит строку из четырёх или более целых чисел,
разделённых символом “/”. Сформируйте словарь, где:
второе и третье число являются ключами.
первое число является значением для первого ключа.
четвертое и все возможные последующие числа хранятся в кортеже,
как значения второго ключа [code](./sem_5/classwork_1.py).

## Задание 2
* Самостоятельно сохраните в переменной строку текста. 
Создайте из строки словарь, где ключ — буква, а значение — код буквы. 
Напишите преобразование в одну строку [code](./sem_5/classwork_2.py).

## Задание 3
* Продолжаем развивать задачу 2. 
Возьмите словарь, который вы получили. Сохраните его итератор. 
Далее выведите первые 5 пар ключ-значение, обращаясь к итератору,
а не к словарю [code](./sem_5/classwork_3.py).

## Задание 4
* Создайте генератор чётных чисел от нуля до 100. 
Из последовательности исключите числа, сумма цифр которых равна 8. 
Решение в одну строку [code](./sem_5/classwork_4.py).

## Задание 5
* Напишите программу, которая выводит на экран числа от 1 до 100. 
При этом вместо чисел, кратных трем, программа должна выводить 
слово «Fizz».
Вместо чисел, кратных пяти — слово «Buzz». 
Если число кратно и 3, и 5, то программа должна выводить слово
«FizzBuzz».
*Превратите решение в генераторное выражение [code](./sem_5/classwork_5.py).

## Задание 6
* Выведите в консоль таблицу умножения от 2х2 до 9х10,
как на школьной тетрадке. 
Таблицу создайте в виде однострочного генератора, 
где каждый элемент генератора — отдельный пример таблицы умножения. 
Для вывода результата используйте «принт» без перехода на новую строку
[code](./sem_5/classwork_6.py).

## Задание 7
* Создайте функцию-генератор. 
Функция генерирует N простых чисел, начиная с числа 2. 
Для проверки числа на простоту используйте правило: 
«число является простым, если делится нацело только 
на единицу и на себя» [code](./sem_5/classwork_7.py).

## Домашнее задание
* Напишите функцию, которая принимает на вход строку — абсолютный
путь до файла. Функция возвращает кортеж из трёх элементов:
путь, имя файла, расширение файла [code](./sem_5/homework_1.py).
* Напишите однострочный генератор словаря, который принимает 
на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов
вида «10.25%». В результате получаем словарь с именем
в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается, как ставка умноженная на процент премии
[code](./sem_5/homework_2.py).
* Создайте функцию генератор чисел Фибоначчи (см. Википедию)
[code](./sem_5/homework_3.py)   
_


# Задание к семинару 6. Модули
### Задание №1
* Вспомните какие модули вы уже проходили на курсе.
  * Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).
[code](./sem_6/task_01_import.py)

### Задание №2
* Создайте модуль с функцией внутри.
* Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
* Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за
заданное число попыток. Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь
[code](./sem_6/task_02_binary_random_search.py).

### Задание №3
* Улучшаем задачу 2
* Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
* Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
[code](./sem_6/task_03_search_script.py)

### Задание №4
* Создайте модуль с функцией внутри.
* Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
* Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
[code](./sem_6/tasks_03_04_05_06_one_hundred_for_one.py)

### Задание №5
* Добавьте в модуль с загадками функцию, которая хранит словарь списков.
* Ключ словаря - загадка, значение - список с отгадками.
* Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.  
[code](./sem_6/tasks_03_04_05_06_one_hundred_for_one.py)

### Задание №6
* Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
* Функция формирует словарь с информацией о результатах отгадывания.
* Для хранения используйте защищённый словарь уровня модуля.
* Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
* Для формирования результатов используйте генераторное выражение. 
[code](./sem_6/tasks_03_04_05_06_one_hundred_for_one.py)

### Задание №7
* Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
* Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
* Для простоты договоримся, что год может быть в диапазоне [1, 9999].
* Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
*Проверку года на високосность вынести в отдельную защищённую функцию.
[code](./sem_6/task_07_date_validate.py)

### Задание №8
* Создайте пакет с всеми модулями, которые вы создали за время занятия.
* Добавьте в __ init__ пакета имена модулей внутри дандер __ all__.
* В модулях создайте дандер __ all__ и укажите только те функции, которые могут верно работать за пределами модуля.
[code](./sem_6/__init__.py)

# Домашнее задание.
* Решить задачи, которые не успели решить на семинаре.
* В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
[code](./sem_6/main.py)
* Добавьте в пакет, созданный на семинаре, шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
[code](./sem_6/eight_queens.py)
* Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
[code](./sem_6/eight_queens.py)


