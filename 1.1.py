# Импортируем библиотеку math
import math

# Запрашиваем значения длины и количества сторон у пользователя
s = int(input('Введите длину стороны: '))
n = int(input('Введите количество сторон: '))
# Производим расчёты
area = n * s ** 2 / 4 / math.tan(math.pi / n)
# Выводим площадь многоугольника пользователю
print('Площадь данного многоугольника равна ', area)
