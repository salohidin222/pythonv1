"1"
def determine_time_of_day(hour):
     if 6 <= hour <= 11:
         return "Утро"
     elif 12 <= hour <= 17:
         return "День"
     elif 18 <= hour <= 21:
         return "Вечер"
     elif (22 <= hour <= 23) or (0 <= hour <= 5):
         return "Ночь"
     else:
         return "Некорректный ввод"

try:
     hour = int(input("Введите часы (целое число от 0 до 23): "))
     if 0 <= hour <= 23:
         print(f"Сейчас {determine_time_of_day(hour)}.")
     else:
         print("Часы должны быть в диапазоне от 0 до 23.")
except ValueError:
     print("Некорректный ввод! Пожалуйста, введите целое число.")

"2"
 

def calculate_discount(price, age):
    if age < 18:
        discount = 0.10
    elif age >= 60:
        discount = 0.20
    else:
        discount = 0.0
    discounted_price = price * (1 - discount)
    return discounted_price, discount

try:
    price = float(input("Введите цену товара: "))
    age = int(input("Введите возраст покупателя: "))
    if price >= 0 and age >= 0:
        final_price, discount = calculate_discount(price, age)
        print(f"Скидка: {discount * 100:.0f}%. Цена со скидкой: {final_price:.2f}.")
    else:
        print("Цена и возраст должны быть неотрицательными.")
except ValueError:
    print("Некорректный ввод! Пожалуйста, введите числовые значения.")

"3"
def determine_triangle_type(a, b, c):
    if a == b == c:
        return "Равносторонний"
    elif a == b or b == c or a == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"

try:
    a = float(input("Введите первую сторону треугольника: "))
    b = float(input("Введите вторую сторону треугольника: "))
    c = float(input("Введите третью сторону треугольника: "))
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        triangle_type = determine_triangle_type(a, b, c)
        print(f"Треугольник {triangle_type}.")
    else:
        print("Заданные стороны не образуют треугольник.")
except ValueError:
    print("Некорректный ввод! Пожалуйста, введите числовые значения.")

"4"

def is_even(number):
    return "Четное" if number % 2 == 0 else "Нечетное"

try:
    number = int(input("Введите число: "))
    print(f"Число {number} - {is_even(number)}.")
except ValueError:
    print("Некорректный ввод! Пожалуйста, введите целое число.")

"5"

def determine_temperature(temp):
    return "Холодно" if temp < 15 else "Тепло"

try:
    temp = int(input("Введите температуру (°C): "))
    print(determine_temperature(temp))
except ValueError:
    print("Некорректный ввод! Пожалуйста, введите целое число.")

"6"

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

while True:
     action = input('Введите действие (+ - / *): ')

     if action == '+':
         print(a + b)
     elif action == '-':
         print(a - b)
     elif action == '/':
         print(a / b)
     elif action == '*':
         print(a * b)
     else:
         print('Вы вели неверное действие')




