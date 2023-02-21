# Магический шар 8
# Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее. Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.
#
# Составляющие проекта:
#
# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл while;
# Бесконечный цикл;
# Операторы break, continue;
# Работа с модулем random для генерации случайных чисел.
# Варианты ответов
# Традиционно шар имеет
# 20
# 20 ответов, которые можно разделить на четыре группы.
#
# Положительные	Нерешительно положительные	Нейтральные	Отрицательные
# Бесспорно	Мне кажется - да	Пока неясно, попробуй снова	Даже не думай
# Предрешено	Вероятнее всего	Спроси позже	Мой ответ - нет
# Никаких сомнений	Хорошие перспективы	Лучше не рассказывать	По моим данным - нет
# Определённо да	Знаки говорят - да	Сейчас нельзя предсказать	Перспективы не очень хорошие
# Можешь быть уверен в этом	Да	Сконцентрируйся и спроси опять	Весьма сомнительно

from random import *

answer = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
          "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input("Введите Ваше имя: ")
print("Привет, " + name)
while True:
    question = input('Задай свой вопрос  ')
    if question != '':
        print(choice(answer))
    else:
        continue
    question = input("Хочешь задать еще  вопрос? д/н")
    if question == 'д':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break

