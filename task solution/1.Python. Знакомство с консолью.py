# Задача №1
print('введите длину стороны квадрата:')
a = int(input())
p = a * 4  # так как квадрат
s = a**2
print('периметр:', p)
print('площадь:', s)
print()

# Задача №2
print('введите длину прямоугольника:')
a = int(input())
print('введите ширину прямоугольника:')
b = int(input())
p = 2 * (a + b)
s = a * b
print('периметр:', p)
print('площадь:', s)
print()

# Задача №3
salary =  float(input('Введите заработную плату в месяц: '))
mortgage = int(input('Введите, какой процент(%) уходит на ипотеку: '))
spending_life = int(input('Введите, какой процент(%) уходит на жизнь: '))
print("На ипотеку было потрачено за год:", (salary / 100 * mortgage) * 12)
print("Было накоплено за год:", (salary / 100 * (100 - mortgage - spending_life)) * 12)