"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********
    """
    separator = '*' * 10
    print(separator)
    return separator

# simple_separator()

print(simple_separator() == '**********')  # True


def long_separator(count):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    separator = '*' * count
    print(separator)
    return separator


print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True


def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    separator = simbol * count
    print(separator)
    return separator


print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    star_separator = '*' * 10
    hash_separator = '#' * 10
    message = "Hello World!"

    print(star_separator)
    print()
    print(message)
    print()
    print(hash_separator)


hello_world()


'''
**********

Hello World!

##########
'''



def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    star_separator = '*' * 10
    hash_separator = '#' * 10
    message = f"Hello {who}!"

    print(star_separator)
    print()
    print(message)
    print()
    print(hash_separator)


'''
**********

Hello World!

##########
'''
hello_who()
'''
**********

Hello Max!

##########
'''
hello_who('Max')
'''
**********

Hello Kate!

##########
'''
hello_who('Kate')


def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    total = sum(args)
    result = total ** power
    print(f"Сумма чисел: {total}")
    print(f"Результата возведения суммы в степень {power}: {result}")
    return result


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в виде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, value in kwargs.items():
        print(f"{key} --> {value}")


"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входная последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    filtered_list = []
    for item in iterable:
        if function(item):
            filtered_list.append(item)
    print(filtered_list)
    return filtered_list


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True