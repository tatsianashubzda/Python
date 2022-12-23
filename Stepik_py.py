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

x1,y1,x2,y2 = int(input()), int(input()), int(input()), int(input())
if (x1==x2 and y1!=y2) or (y1==y2 and x1!=x2):
    print('YES')
else:
    print('NO')


--16
Даны две различные клетки шахматной доски. Напишите программу,  которая определяет,
может ли король попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.

x1,y1,x2,y2 = int(input()), int(input()), int(input()), int(input())
if (-1<=x2-x1<=1) and (-1<=y2-y1<=1):
    print('YES')
else:
    print('NO')


--17
Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара. В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, поэтому Флэш решил не рисковать без причины, и узнать у своего друга Циско Рамона есть ли смысл принимать вызов. Циско получил данные, что скорость Зума равна nn, а скорость Флэша равна kk.

Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.

Формат входных данных
На вход программе подаётся два целых числа nn и kk, скорость Зума и Флэша.
Формат выходных данных
Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES»,
если их скорости равны нужно вывести "Don't know".

z_speed, f_speed = int(input()), int(input())
if z_speed > f_speed:
    print('NO')
elif z_speed < f_speed:
    print('YES')
else:
    print("Don't know")

--18
Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.

Формат входных данных
На вход программе подаются три числа – длины сторон существующего треугольника.
Формат выходных данных
Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).

a, b, c = int(input()), int(input()), int(input())
if a==b==c:
    print('Равносторонний')
elif a==b or a==c or c==b:
    print('Равнобедренный')
else:
    print('Разносторонний')


--19
Среднее число
Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

Формат входных данных
На вход программе подаётся три различных целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести среднее число.

Примечание. Средним называется число, которое будет вторым, если три числа отсортировать в порядке возрастания.

a, b, c = int(input()), int(input()), int(input())
if a<b<c or c<b<a:
    print(b)
elif b<c<a or a<c<b:
    print(c)
elif c<a<b or b<a<c:
    print(a)


--20
Количество дней
Дан порядковый номер месяца (1, \, 2, \ldots, 12)(1,2,…, 12). Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.

Примечание. Постарайтесь написать программу, так чтобы в ней было не более трех условий.

Формат входных данных
На вход программе подаётся одно целое число – порядковый номер месяца.
Формат выходных данных
Программа должна вывести количество дней в этом месяце.

month = int(input())
if month==2:
    print(28)
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(31)
else:
    print(30)



--21
Церемония взвешивания
Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:

Легкий вес – до 60 кг;
Первый полусредний вес – до 64 кг;
Полусредний вес – до 69 кг.
Напишите программу, определяющую, в какой категории будет выступать данный боксер.

Формат входных данных
На вход программе подаётся одно целое число.
Формат выходных данных
Программа должна вывести текст – название весовой категории.

weight = int(input())
if weight<60:
    print('Легкий вес')
elif weight<64:
    print('Первый полусредний вес')
elif weight<69:
    print('Полусредний вес')


--22
Самописный калькулятор 🌶️
Напишите программу, которая считывает с клавиатуры два целых числа и строку. Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция». Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».

Формат входных данных
На вход программе подаются два целых числа, каждое на отдельной строке, и строка.
Формат выходных данных
Программа должна вывести результат применения операции к введенным числам или соответствующий текст, если операция неверная либо если происходит деление на ноль.

a, b = int(input()), int(input())
s = input()
if b==0 and s=='/':
    print('На ноль делить нельзя!')
else:
    if s=='+':
        print(a+b)
    elif s=='-':
        print(a-b)
    elif s=='*':
        print(a*b)
    elif s=='/':
        print(a/b)
    else:
        print('Неверная операция')


--23
Цветовой микшер 🌶️
Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. При смешивании двух основных цветов получается вторичный цвет:

если смешать красный и синий, то получится фиолетовый;
если смешать красный и желтый, то получится оранжевый;
если смешать синий и желтый, то получится зеленый.
Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета, который получится в результате.

col1, col2 = input(), input()
if (col1 == 'синий' or col1 == 'красный' or col1 == 'желтый') and (col2 == 'синий' or col2 =='красный' or col2 =='желтый'):
    if col1 == 'красный':
        if col2 == 'красный':
            print('красный')
        elif col2 == 'желтый':
            print('оранжевый')
        elif col2 == 'синий':
            print('фиолетовый')
    elif col1 == 'синий':
        if col2 == 'красный':
            print('фиолетовый')
        elif col2 == 'желтый':
            print('зеленый')
        elif col2 == 'синий':
            print('синий')
    elif col1 == 'желтый':
        if col2 == 'красный':
            print('оранжевый')
        elif col2 == 'желтый':
            print('желтый')
        elif col2 == 'синий':
            print('зеленый')
else:
    print('ошибка цвета')


--24
Цвета колеса рулетки 🌶️
На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов: 

карман 0 зеленый;
для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

Формат входных данных
На вход программе подаётся одно целое число.

Формат выходных данных
Программа должна вывести цвет кармана либо сообщение «ошибка ввода», если введённое число лежит вне диапазона от 0 до 36.

k = int(input())
if k == 0:
    print('зеленый')
elif (1<=k<=10 or 19<=k<=28):
    if k%2==0:
        print('черный')
    else:
        print('красный')
elif (11<=k<=18 or 29<=k<=36):
    if k%2==0:
        print('красный')
    else:
        print('черный')
else:
    print('ошибка ввода')


--25
Пересечение отрезков 🌶️🌶️
На числовой прямой даны два отрезка: [a_1;  b_1] и [a_2; b_2]. Напишите программу, которая находит их пересечение.

Пересечением двух отрезков может быть:
отрезок;
точка;
пустое множество.

Формат входных данных
На вход программе подаются 4 целых числа a_1,  b_1, a_2,  b_2a,
 каждое на отдельной строке. Гарантируется, что a_1 < b_1a 
​ и a_2 < b_2a 

Формат выходных данных
Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a1<a2:
    if b1<a2:
        print('пустое множество')
    elif b1==a2:
        print(a2)
    elif a2<b1<=b2:
        print(a2, b1)
    else:
        print(a2,b2)
elif a2<=a1<b2:
    if b1<=b2:
        print(a1, b1)
    else:
        print(a1, b2)
elif a1==b2:
    print(a1)
else:
    print('пустое множество')


--26
Начало столетия

Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается, то выведите «YES», иначе выведите «NO».

Формат входных данных
На вход программе подаётся натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

year = int(input())
if year%100 == 0:
    print('YES')
else:
    print('NO')


--27

Шахматная доска

Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет. Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')



--28
Girls only

Футбольная команда набирает девочек от 10 до 15 лет включительно. Напишите программу, которая запрашивает возраст и пол претендента, используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина) и определяет подходит ли претендент для вступления в команду или нет. Если претендент подходит, то выведите «YES», иначе выведите «NO».

Формат входных данных
На вход программе подаётся натуральное число – возраст претендента и буква обозначающая пол m (мужчина) или f (женщина).
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

a = int(input())
b = input()
if a >= 10 and a <= 15 and b == 'f':
    print("YES")
else:
    print("NO")


--29
YES or NO вот в чем вопрос

Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».

Условия:

если число нечётное, то вывести «YES»;
если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
если число чётное и больше 20, то вывести «NO».

Формат входных данных
На вход программе подаётся натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

a = int(input())
if a % 2 != 0:
    print("YES")
if a % 2 == 0 and a >= 2 and a <= 5:
    print("NO")
if a % 2 == 0 and a >= 6 and a <= 20:
    print("YES")
if a % 2 == 0 and a > 20:
    print("NO")

--30

Ход слона ?️

Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный слон ходит по диагоналям.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')


--31

Ход коня

Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли конь попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный конь ходит буквой «Г».


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
    print("YES")
else:
    print("NO")


--32
Ход ферзя

Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли ферзь попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом ферзя можно попасть во вторую или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный ферзь ходит по диагонали, горизонтали или вертикали.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')


--33 
Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.

Формат входных данных
На вход программе подаётся два числа с плавающей точкой – длины катетов, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести одно число – площадь треугольника.

a, b = float(input()), float(input())
s = 0.5 * a * b
print(s)


--34
Две старушки
Две старушки идут навстречу друг другу с постоянными скоростями V_1 и V_2 км/ч. 
Определите, через какое время старушки встретятся, если расстояние между ними равно SS км.

s, v1, v2 = float(input()), float(input()), float(input())
t=s/(v1+v2)
print(t)


--35
Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).

Формат входных данных 
На вход программе подается одно действительное число.
Формат выходных данных
Программа должна вывести действительное число обратное данному, либо текст в соответствии с условием задачи.

n = float(input())
if n!=0:
    print(1/n)
else:
    print('Обратного числа не существует')


--36
451 градус по Фаренгейту 
У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.

Формат входных данных
На вход программе подаётся вещественное число градусов по шкале Фаренгейта.
Формат выходных данных
Программа должна вывести число градусов по шкале Цельсия.

f = float(input())
c = (f-32)*5/9
print(c)


--37
Dog age
На вход программе подается число nn – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах.

Формат входных данных
На вход программе подаётся натуральное число – количество собачьих лет.
Формат выходных данных
Программа должна вывести возраст собаки в человеческих годах.

Примечание. В течение первых двух лет собачий год равен 10.510.5 человеческим годам. После этого каждый год собаки равен 4 человеческим годам.

age = float(input())
if 0 < age <= 2:
    print(age * 10.5)
else:
    print(2 * 10.5 + (age - 2) * 4)


--38
Первая цифра после точки
Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

Формат входных данных
На вход программе подается положительное действительное число.
Формат выходных данных
Программа должна вывести цифру в соответствии с условием задачи.

x = float(input())
print(int(x*10)%10)


--39
Дробная часть
Дано положительное действительное число. Выведите его дробную часть.

Формат входных данных
На вход программе подается положительное действительное число.

Формат выходных данных
Программа должна вывести дробную часть числа в соответствии с условием задачи.

a = float(input())
print(a - int(a))


--40
Наибольшее и наименьшее
Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

Формат входных данных
На вход программе подается пять целых чисел, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести наименьшее и наибольшее число с поясняющей надписью.

a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))


--41
Сортировка трёх 🌶️
Напишите программу, которая упорядочивает три числа от большего к меньшему.

Формат входных данных
На вход программе подается три целых числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.

a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))


--42
Интересное число
Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

Формат входных данных
На вход программе подается целое трехзначное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
a = x % 10
b = x // 10 % 10
c = x // 100
if a + b + c == 2 * max(a, b, c):
    print("Число интересное")
else:
    print("Число неинтересное")


--44
Абсолютная сумма
Даны пять чисел ​
Напишите программу, которая вычисляет сумму их модулей 

Формат входных данных
На вход программе подается пять действительных чисел , каждое на отдельной строке.
Формат выходных данных
Программа должна вывести одно число – сумму модулей введённых чисел.

a = abs(float(input()))
b = abs(float(input()))
c = abs(float(input()))
d = abs(float(input()))
e = abs(float(input()))

print(a + b + c + d + e)


--45
Манхэттенское расстояние
Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути. Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.
На плоскости манхэттенское расстояние между двумя точками  
Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.


Формат входных данных
На вход программе подается четыре целых числа, каждое на отдельной строке 
Формат выходных данных
Программа должна вывести одно число – манхэттенское расстояние.

p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())

print(abs(p1 - q1) + abs(p2 - q2))


--46
Напишите программу, которая выводит текст:

"Python is a great language!", said Fred. "I don't ever remember having this much fun before."
Примечание. Используйте конкатенацию строк.

a='"Python is a great language!",'
b=" said Fred. "
c='"I'
d=" don't "
e= 'ever remember having this much fun before."'
print (a+b+c+d+e)



--47
What's Your Name?
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:

«Hello [введенное имя] [введенная фамилия]! You just delved into Python».

Формат входных данных
На вход программе подаётся две строки (имя и фамилия), каждая на отдельной строке.

name, surname = input(), input()
print('Hello '+ name+' '+surname+'! You just delved into Python')


--48
Футбольная команда
Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:

«Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

Формат входных данных
На вход программе подаётся строка – название футбольной команды.

team = input()
print('Футбольная команда', team, 'имеет длину', len(team), 'символов')


--49
Три города
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трех городов различны.

s1, s2, s3 = input(), input(), input()
l1=len(s1)
l2=len(s2)
l3=len(s3)
if min(l1, l2, l3) == l1:
    print(s1)
elif min(l1, l2, l3) == l2:
    print(s2)
else:
    print(s3)
if max(l1, l2, l3) == l1:
    print(s1)
elif max(l1, l2, l3) == l2:
    print(s2)
else:
    print(s3)


--50
Арифметические строки
Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.

a, b, c = input(), input(), input()
al=len(a)
bl=len(b)
cl=len(c)
maxl=max(al,bl,cl)
minl = min(al, bl, cl)
if (maxl+minl)/2==al or (maxl+minl)/2==bl or (maxl+minl)/2==cl:
    print('YES')
else:
    print('NO')


--51
Цвет настроения синий
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.

Формат входных данных
На вход программе подается одна строка.

st = input()
if 'синий' in st:
    print('YES')
else:
    print('NO')


--52
Отдыхаем ли?
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.

Формат входных данных
На вход программе подается одна строка.

st = input()
if ('суббота' in st) or ('воскресенье' in st):
    print('YES')
else:
    print('NO')


--53
Корректный email
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.

Формат входных данных
На вход программе подаётся одна строка – email адрес.

Формат выходных данных
Программа должна вывести строку «YES», если email адрес является корректным и «NO» в ином случае.

st = input()
if ('@' in st) and ('.' in st):
    print('YES')
else:
    print('NO')


--54
На плоскости евклидово расстояние между двумя точками (x1​;y1​) и (x2​;y2​) определяется 
Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

Формат входных данных
На вход программе подается четыре вещественных числа, каждое на отдельной строке x1​,y1​,x2​,y2​​.

Формат выходных данных
Программа должна вывести одно число – евклидово расстояние.

from math import sqrt
x1, y1, x2,y2 = float(input()), float(input()), float(input()), float(input())
s = sqrt((abs(x1-x2))**2+(abs(y1-y2))**2)
print(s)

--55
Площадь и длина
Напишите программу определяющую площадь круга и длину окружности по заданному радиусу RR.

Формат входных данных
На вход программе подается одно вещественное число RR​.
Формат выходных данных
Программа должна вывести два числа – площадь круга и длину окружности радиуса RR.

import math
r = float(input())
s = math.pi * r**2
l = 2 * math.pi * r
print(s,l, sep = '\n')


--56
Формат входных данных
На вход программе подается два вещественных числа aa и bb​, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

from math import *
a, b = float(input()), float(input())
ar = (a + b) / 2
geom = sqrt(a * b)
garm = 2 * a * b/(a + b)
kw = sqrt((a**2 + b**2) / 2)
print(ar, geom, garm, kw, sep = '\n')


--57
Напишите программу, вычисляющую значение тригонометрического выражения
sin x + cos x + tan^2 x
 по заданному числу градусов x.
Формат входных данных
На вход программе подается одно вещественное число xx измеряемое в градусах​. 

Формат выходных данных
Программа должна вывести одно число – значение тригонометрического выражения.

Примечание 1. Тригонометрические функции принимают аргумент в радианах. Чтобы перевести градусы в радианы, воспользуйтесь формулой 
r = {{x \cdot \pi } \over 180}
r= 
180
x⋅π
​
 Примечание 2. Модуль math содержит встроенную функцию radians(), которая переводит угол из градусов в угол в радианах.

from math import *
x = radians(float(input()))
a = (sin(x) + cos(x) + tan(x)**2)
print(a)


--58
Напишите программу, вычисляющую значение \lceil x\rceil + \lfloor x\rfloor⌈x⌉ +⌊x⌋ по заданному вещественному числу xx.

Формат входных данных
На вход программе подается одно вещественное число xx.

Формат выходных данных
Программа должна вывести одно число – значение указанного выражения.

Примечание. \lceil x\rceil⌈x⌉ – потолок числа, \lfloor x\rfloor⌊x⌋ – пол числа.

import math
a = float(input())
b = (math.ceil(a) + math.floor(a))
print(b)


--59
Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения 
ax^2 + bx + c = 0.
Формат входных данных
На вход программе подается три вещественных числа a , b, c
каждое на отдельной строке.

Формат выходных данных
Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.

Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

from math import *
a, b, c = float(input()), float(input()), float(input()) 
discr = b**2-4*a*c 
if discr < 0:
    print('Нет корней')
elif discr == 0: 
    x = -b / (2*a)
    print(x)
elif discr > 0:          
    x1 = (-b - discr ** 0.5) / (2*a)
    x2 = (-b + discr ** 0.5) / (2*a)
    print(min(x1, x2))
    print(max(x1, x2))


--60
Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между
 смежными сторонами. 
 
Даны два числа: натуральное число nn и вещественное число aa. 
Напишите программу, которая находит площадь указанного правильного многоугольника.

Формат входных данных
На вход программе подается два числа nn и aa, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести вещественное число – площадь многоугольника

from math import *
n, a = float(input()), float(input())
S = (n * a**2) / (4 * tan(pi / n))
print(S)


--61
Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.

Формат входных данных

Формат выходных данных
Программа должна вывести 10 раз текст «Python is awesome!», каждый на отдельной строке.

for i  in range(10):
    print ('Python is awesome!')


--62
Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.
Формат входных данных
В первой строке записано текстовое предложение, во второй — количество повторений.
Формат выходных данных
Программа должна вывести указанное текстовое предложение нужное количество раз. Каждое повторение должно начинаться с новой строки.

fr, n = input(), int(input())
for i in range(n):
    print(fr)



--63
На вход программе подается натуральное число nn.

Напишите программу, которая печатает звездный прямоугольник размерами n \times 19n×19.

Формат входных данных
На вход программе подаётся натуральное число n \in [1; \, 20]n∈[1;20] — высота звездного прямоугольника.

Формат выходных данных
Программа должна вывести звездный прямоугольник размерами n \times 19n×19.

Подсказка. Для печати звездной линии используйте умножение строки на число.

n = int(input())
for i in range(n):
    print('*'*19)


--64


