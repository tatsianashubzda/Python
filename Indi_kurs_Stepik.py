# 1
# Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том, являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.
# Программа должна выводить YES, когда клетки одного цвета, NO - разного. Гарантируется, что значение колонок это латинские буквы abcdefgh, а строки это символы цифр от 1-8

cl1, cl2 = input(), input()
# Извлекаем из каждой клетки координату столбца (букву) и строки (цифру).
column1, row1 = cl1[0], int(cl1[1])
column2, row2 = cl2[0], int(cl2[1])

# Вычисляем сумму координат каждой клетки.
sum1 = ord(column1) + row1
sum2 = ord(column2) + row2

if sum1 % 2 == sum2 % 2:
    print("YES")
else:
    print("NO")

# 2
# На вход программе поступает целое число
# Ваша задача сохранить в переменную text  строку Even, если введенное число четное, иначе сохраните строку Odd
# В качестве ответа необходимо вывести переменную text

n = int(input())
text = 'Even' if n % 2 == 0 else 'Odd'
print(text)



# 3
# На вход вашей программе поступает два неравных друг другу целых числа в отдельных строках
# Ваша задача сохранить наименьшее из этих чисел в переменную  minimum, а наибольшее - в maximum
# Использовать нужно, конечно же, тернарный оператор
# В качестве ответа выведите через пробел сперва minimum , а потом maximum

a, b = int(input()), int(input())
(minimum, maximum) = (a, b) if a < b else (b, a)
print(minimum, maximum)


# 4
# При игре в "Города" игроки по очереди называют названия городов так, чтобы первая буква каждого нового слова совпадала с последней буквой предыдущего. При этом считают, что если последняя буква предыдущего слова — мягкий знак, то с первой буквой следующего слова надо сравнивать букву, предшествующую мягкому знаку.
# Напишите программу, которая считывает подряд две строки, после чего выводит «Good», если последний символ первой строки совпадает с первым символом второй (с учётом правила про мягкий знак), и «Bad» в противном случае.

a, b = input().lower(), input().lower()

aa = a[-1]
bb = b[0]
if aa == bb:
    print('Good')
elif a[-1] == 'ь':
    if a[-2] == bb:
        print('Good')
    else:
        print('Bad')
else:
        print('Bad')




# 5
# Напишите программу, которая имитирует проверку пароля, придуманного пользователем. Пользователь сперва вводит пароль, потом вводит подтверждение пароля. Вам нужно обработать следующие ситуации:
#     если пароль, который ввёл пользователь (в первый раз) короче 7 символов, программа выводит Short
#     если пароль достаточно длинный, но введённый во второй раз пароль не совпадает с первым, программа выводит Difference
#     если же и эта проверка пройдена успешно, программа выводит латинскими буквами OK


p_1, p_2=input(), input()

if len(p_1)>=7 and p_1==p_2:
    print('OK')
elif len(p_1)<7:
    print('Short')
elif p_1!=p_2:
    print('Difference')



# 6
# На каждой отдельной строчке пользователь вводит друг за другом пароли в виде строки символов. Валидными паролями будем считать строки, у которых длина варьируется от 5 до 9 символов включительно. Как только вы встретите первый невалидный пароль, ваша программа должна закончить считывать пароли и вывести последний введенный валидный пароль.
# Гарантируется, что первый пароль всегда валидный

p = input()
while 5 <= len(p) <=9:
    valid_p = p
    p = input()
print(valid_p)



# 7
# Собираемся в поход
# У нас в наличии рюкзак, вместимость которого составляет n литров, и наша задача забить его до предела максимально возможно. Нам поступают вещи, объем которых измеряется также в литрах, и мы должны их складывать в наш рюкзак без возможности пропуска. Как только суммарный объем новой добавляемой вещи превысит вместимость рюкзака, ваша программа должна вывести слово "Довольно!" и затем на отдельных строчках суммарный объем вещей, которые мы смогли упаковать в рюкзак, и их количество
# Входные данные
# Число n – вместимость рюкзака. Далее идут произвольное количество строк – объем очередного предмета.
# Выходные данные
# Строка "Довольно!" и затем два числа – суммарный объем упакованных товаров и их количество. Каждое значение выводится в отдельной строке.

n = int(input())  
a = 0             
e = 0             
b = 0            

while a <= n:
    e = int(input())
    b = b + 1
    a += e
print('Довольно!')
print(a - e)
print(b - 1)



# 8
# В последний день уходящего 2016 года Лимак собирается принять участие в соревновании по спортивному программированию. Соревнование начнётся в 20:00 и будет продолжаться четыре часа, то есть ровно до полуночи. Участникам будет предложено n задач, упорядоченных по возрастанию сложности, то есть задача 1 будет самой лёгкой, а задача номер n — самой сложной. Лимак знает, что ему потребуется 5·i минут на решение i-й задачи.
# Друзья Лимака планирую устроить роскошную новогоднюю вечеринку и Лимак хочет прибыть в полночь или ранее. Он знает, что ему требуется ровно k минут чтобы добрать до места проведения вечеринки от своего дома, где он собирается участвовать в соревновании.
# Сколько максимум задач может успеть решить Лимак, так чтобы не опоздать на новогоднюю вечеринку?
# Входные данные
# В первой строке входных данных записаны два целых числа n и k (1 ≤ n ≤ 10, 1 ≤ k ≤ 240) — количество задач в соревновании и количество минут, за которое Лимак доберётся от дома до места проведения вечеринки.
# Выходные данные
# Выведите одно целое число, равное максимальному количеству задач, которое может решить Лимак, так чтобы прибыть на новогоднюю вечеринку ровно в полночь или раньше.
# Примечание
# В первом примере на соревновании участникам предложено 3 задачи и Лимаку требуется 222 минуты, чтобы доехать до места проведения вечеринки. Для решения задач требуется 5, 10 и 15 минут соответственно. Лимак может решить первые две задачи, потратив на это 5 + 10 = 15 минут, после чего выехать в 20:15 и приехать на вечеринку в 23:57 (через 222 минуты). Таким образом он решит две задачи, но на решение третьей времени уже не хватит и ответ равен 2.
# Во втором примере Лимак может решить все 4 задачи за 5 + 10 + 15 + 20 = 50 минут. В 20:50 он сможет выехать из дома и прибыть на вечеринку ровно в полночь.
# В третьем примере Лимаку нужна только 1 минута, чтобы оказаться на вечеринке, так что ему хватит времени для решения всех 7 задач.

a, b = map(int, input().split()) 
c = 0  
t = 240 - b  
while t > 0:
    c+=1
    t-=c*5
    if a == c: 
        break
if t<0:
    c-=1
print(c)



# 9

# Ване на день рождения подарили n кубиков. Он с друзьями решил построить из них пирамиду. Ваня хочет построить пирамиду следующим образом: на верхушке пирамиды должен находиться 1 кубик, на втором уровне — 1 + 2 = 3 кубика, на третьем — 1 + 2 + 3 = 6 кубиков, и так далее. Таким образом, на i-м уровне пирамиды должно располагаться 1 + 2 + ... + (i - 1) + i кубиков.
# Ваня хочет узнать, пирамиду какой максимальной высоты он может создать с использованием имеющихся кубиков.
# Входные данные
# В первой строке записано целое число n (1 ≤ n ≤ 104) — количество кубиков, подаренных Ване.
# Выходные данные
# Выведите единственной строкой максимально возможную высоту пирамиды

c = int(input())    
i = 0                      
s = 0             

while s + i + 1 <= c:  
    i += 1                 
    s += i        
    c -= s 

print(i)



# 10
# Слияние списков
# В вашем распоряжении имеется два отсортированных списка по неубыванию элементов, состоящих из n и m элементов
# Ваша задача слить их в один отсортированный список размером  n + m
# Входные данные
# Программа получает на вход два числа n и m - количество элементов первого списка и второго списков
# Затем с новой строки поступают элементы первого отсортированного списка, а со следующей строки - второго списка
#  Выходные данные
# Слить два списка в один в порядке неубывания и вывести элементы полученного списка
# P.S: пользоваться встроенной сортировкой запрещено

n, m = (int, input().split())  
list1 = list(map(int, input().split()))  
list2 = list(map(int, input().split()))  
list = list1 + list2  

res = []  

while len(list) != 0:
    a = min(list)      
    res.append(a)   
    list.remove(a)     

print(*res) 



# 11
# Бал в БерлГУ
# По случаю 100500-летия Берляндского государственного университета совсем скоро состоится бал! Уже n юношей и m девушек во всю репетируют вальс, менуэт, полонез и кадриль.
# Известно, что на бал будут приглашены несколько пар юноша-девушка, причем уровень умений танцевать партнеров в каждой паре должен отличаться не более чем на единицу.
# Для каждого юноши известен уровень его умения танцевать. Аналогично, для каждой девушки известен уровень ее умения танцевать. Напишите программу, которая определит наибольшее количество пар, которое можно образовать из n юношей и m девушек.
# Входные данные
# В первой строке записано целое число n (1 ≤ n ≤ 100) — количество юношей. Вторая строка содержит последовательность a1, a2, ..., an (1 ≤ ai ≤ 100), где ai — умение танцевать i-го юноши.
#  Аналогично, третья строка содержит целое m (1 ≤ m ≤ 100) – количество девушек. В четвертой строке содержится последовательность b1, b2, ..., bm (1 ≤ bj ≤ 100), где bj — умение танцевать j-й девушки.
# Выходные данные
# Выведите единственное число — искомое максимальное возможное количество пар.

b_count = int(input())     
b_list = list(map(int, input().split())) 

g_count = int(input())    
g_list = list(map(int, input().split())) 

b_list.sort()              
g_list.sort()

count = 0     # количество пар

while b_list != [] and g_list != []: 
    if abs(b_list[0] - g_list[0]) <= 1: #если разница скиллов <=1
        count += 1 
        b_list.pop(b_list.index(b_list[0]))
        g_list.pop(g_list.index(g_list[0])) 
    else: 
        if b_list[0] > g_list[0]: # если  мальчик лучше девочки, то пары не будет 
            g_list.pop(g_list.index(g_list[0])) # удаляем девочку из списка
            
        else: # если  девочка лучше мальчика, то пары не будет
            b_list.pop(b_list.index(b_list[0])) # удаляем мальчика
            
print(count)


# 12
# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.
# 
# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1
#       .....
# На вход программе подается число n. Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка (нумерация строк начинается с нуля).
# 
# Формат входных данных
# На вход программе подается число n (n≥0).
# 
# Формат выходных данных
# Программа должна вывести указанную строку треугольника Паскаля в виде списка.
# 


n = int(input())
s = []
for i in range(n+1):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=i and j!=0: row[j] = s[i-1][j-1]+s[i-1][j]
    s.append(row)
print(s[n] if n!=0 else [1])



# 13
# На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.

n = int(input())
s=[]
for i in range(0,n):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=0 and j!=i:
            row[j]=s[i-1][j-1]+s[i-1][j]
    s.append(row)

for k in s:
    print(*k)



# 14
# Проверить, является ли слово палиндомом

def is_palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrom(s[1:-1])

print(is_palindrom("шалаш"))



# 15
# Определите функцию print_from, которая принимает одно натуральное число n и распечатывает на экране убывающую последовательность целых чисел от n до 1 включительно. Каждое число необходимо выводить на отдельной строке. 

def print_from(n: int) -> None:
    print(n)
    if n>1:
        print_from(n-1)


# 16
# Определите функцию print_to, которая принимает одно натуральное число n и распечатывает на экране последовательность целых чисел от 1 до n включительно. Каждое число необходимо выводить на отдельной строке. 

def print_to(n: int) -> None:
        if n > 1:             # если заданное число больше нуля
            print_to(n - 1)   # вызываем функцию но переданную 
        print(n) 


# 17
#




