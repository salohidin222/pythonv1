def calculate_credit():
    amount = float(input("Введите сумму займа (не меньше 100 000): "))
    if amount < 100000:
        print("Ошибка: сумма должна быть не меньше 100 000!")
        return
    percent = 7.89
    overpayment = amount * (percent / 100)
    total_amount = amount + overpayment
    print(f"Итоговая сумма к возврату: {round(total_amount, 2)}")

def extract_numbers():
    text = input("Введите текст с цифрами: ")
    digits = ''.join(filter(str.isdigit, text))  
    
    if digits:
        print(f"Число из строки: {int(digits)}")
    else:
        print("Цифры в тексте не найдены.")


def convert_to_days():
    years = int(input("Введите количество лет: "))
    months = int(input("Введите количество месяцев: "))
    days = (years * 12 + months) * 30  
    print(f"Общее количество дней: {days}")


def cubes_dict():
    return {x: x**3 for x in range(1, 11)}


def sum_numbers():
    return sum(range(1, 51))


calculate_credit()
extract_numbers()
convert_to_days()
print(cubes_dict())
print(f"Сумма чисел от 1 до 50: {sum_numbers()}")

