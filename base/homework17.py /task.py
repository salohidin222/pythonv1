
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 
    else 'Ошибка: деление на ноль'
}


def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        op = input("Введите операцию (+, -, *, /): ")
        
        if op in operations:
            result = operations[op](num1, num2)
            print(f"Результат: {result}")
        else:
            print("Ошибка: Неверная операция")
    except ValueError:
        print("Ошибка: Введите корректные числа")

# Запуск программы
if __name__ == "__main__":
    calculator()

