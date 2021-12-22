import random
import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Исходные данные
N = 200
a = 1
b = 1
n = 11

# Списки данных
x_values = []  # Список значений x
y_values = []  # Список значений y - дельта t
y_intervals = []  # Список интервалов
y_intervalsMid = []  # Список середин интервалов
y_density = []  # Список плотностей распределения
counts = []  # Список относительной частоты попаданий
pk_list = []  # Список теоретической вероятности попадания случайной величины
x2list = []  # Список критерия Пирсона
tk_values = []  # Список tk
event = list(range(1, 201))  # Список 200 событий

tk0 = 0
# Генерация чисел и информационного потока
for i in range(N):
    x = random.random()
    y = (-1 / b * math.log(1 - x)) ** (1 / a)
    tk = tk0+y  #Для построения таблицы
    tk0 = tk
    y_values.append(y)
    x_values.append(x)
    tk_values.append(tk)

# Информационный поток
mytable = PrettyTable()
mytable.add_column("Событие", event)
mytable.add_column("tk", tk_values)
mytable.add_column("дельта t", y_values)

# Поиск точек экстремума
yMax = max(y_values)
yMin = min(y_values)
step = (yMax - yMin) / n

# Статистическая плотность вероятности
yMin0 = yMin
for interval in range(n):
    interval = yMin0 + step
    intervalmid = (interval - (step/2))
    count = sum(True for y in y_values if y <= interval and y > yMin0)
    counts.append(count/N)
    yMin0 = interval
    y_intervals.append(interval)
    y_intervalsMid.append(intervalmid)

# Теоритическая плотность вероятности
yMin1 = yMin
for density in range(n):
    interval = yMin1 + step
    z = ((a*b*interval)**(a-1))*math.exp((-b*interval)**a)
    yMin1 = interval
    y_density.append(z)

# Вычисление значения критерия согласия
yMin2 = yMin
for x2 in range(n):
    interval = yMin2 + step
    pk = (1-math.exp(-b*interval**a))-(1-math.exp(-b*(interval-step)**a))
    count = sum(True for y in y_values if y <= interval and y > yMin2)
    countOtn=count/N
    x2 = ((countOtn-pk)**(2))/pk
    yMin2 = interval
    pk_list.append(pk)
    x2list.append(x2)
x2sum = sum(x2list)

# Вывод информации
print('Контрольная работа студента 6199-090401Z Мыльникова Е.Н.')
print("Моделирование информационных потоков")
print("Задание №3, вариант №1")
print("Информационный поток из 200 событий")
print(mytable)
print("Список значений x", x_values)
print("Список значений y", y_values)
print("ymin =", yMin)
print("ymax =", yMax)
print("Шаг =", step)
print("Интервалы =", y_intervals)
print("Середины интервалов =", y_intervalsMid)
print("Список относительной частоты попаданий =", counts)
print("Список плотностей распределения=", y_density)
print("Список теоретической вероятности попадания случайной величины Pк=", pk_list)
print("Список критерия Пирсона x2=", x2list)
print("Критерий Пирсона x2 =", x2sum, )
print("Вывод: расчетный критерий х2 = ", x2sum, 'меньше порогового значения х2 = 25,2.')
print('Реализации  xi (i = 1, 2, … , N) случайной величины X, получаемые с помощью цифровой модели, хорошо согласуются с законом распределения f(x)')

# Вывод графиков
width = step
plt.bar(y_intervalsMid, counts, width=step)
plt.plot(y_intervals, y_density, color='red')
plt.show()