#1
squares = [x**2 for x in range(1, 11)]
#2
evens = [x for x in range(1, 21) if x % 2 == 0]
#3
squares_dict = {x: x**2 for x in range(1, 6)}
#4
words = ["python", "java", "swift", "golang", "javascript"]
long_words = [word for word in words if len(word) > 5]
#5
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]
#6
try:
    pass
except ExceptionType1 as e1:
    pass
except ExceptionType2 as e2:
    pass
else:
    pass
finally:
    pass
#7
try:
    print(undefined_variable)
except NameError:
    print("Такой переменной не существует!")
#8
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("Результат деления:", a / b)
except ZeroDivisionError:
    print("На ноль делить нельзя")
#9
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("Сумма:", a + b)
except ValueError:
    print("Введите число!")
#10
data = {"name": "Alice", "age": 25}
try:
    key = input("Введите ключ: ")
    print("Значение:", data[key])
except KeyError:
    print("Нет такого ключа!")
#11
my_list = [10, 20, 30, 40]
try:
    index = int(input("Введите индекс: "))
    print("Элемент:", my_list[index])
except IndexError:
    print("Нет такого элемента!")
#12
try:
    age = int(input("Введите ваш возраст: "))
    if age < 18:
        raise ValueError("Доступ запрещён")
except ValueError:
    print("Введён некорректный возраст")
else:
    print("Спасибо")
finally:
    print("До свидания!")
#13
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("Результат деления:", a / b)
except (ValueError, ZeroDivisionError):
    print("Произошла ошибка!")
#14
try:
    amount = float(input("Введите сумму денег: "))
    if amount < 0:
        raise ValueError("Сумма не может быть отрицательной!")
except ValueError as e:
    print(e)
else:
    print("Введённая сумма:", amount)
#15
try:
    result = "hello" + 5
except TypeError:
    print("Unsupported option")
