# Урок №4 float, int и арифметические операции

# Задание №1
print("Задание №1")
a, b = map(float, input("Введите длинну и ширину прямоугольника через пробел: ").split())
s = a * b # прощадь
p = 2 * (a + b) # периметр
print("Площадь равна: " , s)
print("Периметр равен: ", p)

# либо ввод сторон через Enter:

a = float(input("Введите одну сторону прямоугольника: "))
b = float(input("Введите вторую сторону прямоугольника: "))
s = a * b  # площадь
p = 2 * (a + b) # периметр
print("площадь равна: ", s)
print("периметр равен: ", p)


# Задание #2
print("Задание №2")
a, b, c, d, e, = map(int, input("Введите пятизначное целое число: "))
print(d**e * c / (a - b))  # при делении число автоматически становится float.
