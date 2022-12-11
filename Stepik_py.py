--1
При регистрации на сайтах требуется вводить пароль дважды. 
Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.
Напишите программу, которая сравнивает пароль и его подтверждение. 
Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».

pass1, pass2 = input(), input()
if pass1==pass2:
    print('Пароль принят')
else:
    print ('Пароль не принят')


--2
Напишите программу, которая определяет, является число четным или нечетным.

num = int(input())
if num%2:
    print('Нечетное')
else:
    print('Четное')


--3
Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
сумма первой и последней цифр равна разности второй и третьей цифр.

num = int(input())
a=num//1000
b=(num//100)%10
c=(num//10)%10
d=num%10
if (a+d)==(b-c):
    print('ДА')
else:
    print('НЕТ')


--4
Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.

Формат входных данных
На вход программе подаётся целое число — возраст пользователя.
Формат выходных данных
Программа должна вывести текст «Доступ разрешен» если возраст не менее 18, и «Доступ запрещен» в противном случае.

age = int(input())
if age>=18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')


--5
Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.

Формат входных данных
На вход программе подаются три числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи. 

a,b,c = int(input()), int(input()), int(input())
if a-b==b-c:
    print('YES')
else:
    print('NO')


--6
Напишите программу, которая определяет наименьшее из двух чисел.

Формат входных данных
На вход программе подаётся два различных целых числа.
Формат выходных данных
Программа должна вывести наименьшее из двух чисел.

a,b = int(input()), int(input())
if a<b:
    print(a)
else:
    print(b)


--7
Напишите программу, которая определяет наименьшее из четырёх чисел.

Формат входных данных
На вход программе подаётся четыре целых числа.
Формат выходных данных
Программа должна вывести наименьшее из четырёх чисел.

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a<b:
    min1=a
else:
    min1=b
if c<d:
    min2=c
else:
    min2=d
if min1<min2:
    min_=min1
else:
    min_=min2
print(min_)


--8
Возрастная группа
Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
до 13 включительно – детство;
от 14 до 24 – молодость;
от 25 до 59 – зрелость;
от 60 – старость.

Формат входных данных
На вход программе подаётся одно целое число – возраст пользователя.
Формат выходных данных
Программа должна вывести название возрастной группы.

age = int(input())
if age<=13:
    print('детство')
if 14<=age<=24:
    print('молодость')
if 25<=age<=59:
    print('зрелость')
if 60<=age:
    print('старость')


--9
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

Формат входных данных
На вход программе подаются три целых числа.

Формат выходных данных
Программа должна вывести одно число – сумму положительных чисел.

Примечание. Если положительных чисел нет, то следует вывести 00.

a, b, c = int(input()), int(input()), int(input())
sum=0
if a>0:
    sum=sum+a
if b>0:
    sum=sum+b
if c>0:
    sum=sum+c
print(sum)


--10
Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.

Формат входных данных
На вход программе подаётся целое число xx.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
if -3>=x or x>=7:
    print('Принадлежит')
else:
    print('Не принадлежит')


--11
Назовем число красивым, если оно является четырехзначным и делится нацело на 77 или на 1717. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.

Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
if x%7==0 or x%17==0:
    print('YES')
else:
    print('NO')


--12
Назовем число красивым, если оно является четырехзначным и делится нацело на 77 или на 1717. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.

Формат входных данных
На вход программе подаётся натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
if 1000<=x<=9999 and (x%7==0 or x%17==0):
    print('YES')
else:
    print('NO')


--13
Неравенство треугольника
Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.

Формат входных данных
На вход программе подаётся три положительных целых числа.
Формат выходных данных
Программа должна вывести «YES» или «NO» в соответствии с условием задачи.

a, b, c = int(input()), int(input()), int(input())
if a<b+c and (b<a+c and c<a+b):
    print('YES')
else:
    print('NO')


--14
Високосный год
Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным, то выведите «YES», иначе выведите «NO».
Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.

Формат входных данных
На вход программе подаётся натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

year = int(input())
if (year%400==0 or year%100!=0) and (year%4==0):
    print('YES')


--15
Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматная ладья ходит по горизонтали или вертикали.


