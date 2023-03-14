# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
#
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])




# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# total = 0
# with_a = []
# for item in list_1:
#     if isinstance(item, int):
#         total += item
#     elif isinstance(item, str) and 'a' in item:
#         with_a.append(item)
# print(total)
# print(*with_a, sep = '\n')
#


#
# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

# my_list = ['cat', 'dog', 'horse', 'cow']
# my_tuple = tuple(my_list)
# print(type(my_tuple))

#
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
#
# family_1 = input("Введите имена членов  семьи 1, разделенные запятой: ")
# family_2 = input("Введите имена членов  семьи 2, разделенные запятой: ")
# count_1 = len(family_1.split(','))
# count_2 = len(family_2.split(','))
# if count_1 > count_2:
#     print("Семья 1 больше")
# elif count_2 > count_1:
#     print("Семья 2 больше")
# else:
#     print("Семьи равны по численности")


#
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

film = {
    'title': 'Форрест Гамп',
    'director': 'Роберт Земекис',
    'year': 1994,
    'budget': None,
    'main_actor': 'Том Хэнкс',
    'slogan': None
}

print(film.keys())

print(film.values())

print(film.items())



#
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#
# total = 0
# for key in my_dictionary:
#     total += my_dictionary[key]
#
# print(total)
#
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# list1 = [1, 2, 3, 4, 5, 3, 2, 1]
# print (set(list1))


#
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#
# print("Значения, которые встречаются в обоих множествах: ", set1.intersection(set2))
#
# print("Значения, которые не встречаются в обоих множествах: ", set1.symmetric_difference(set2))
#
# print("Являются ли эти множества подмножествами друг друга: ", set1.issubset(set2) and set2.issubset(set1))