#1

items = input("Введите список товаров через запятую: ").split(", ")
additional_items = input("Введите дополнительные товары через пробел: ").split()
items.extend(additional_items)
print("\nВаш список:", items)
if input("Хотите удалить последний товар? (да/нет): ").lower() == "да":
    items.pop()
    print("Обновлённый список:", items)
if input("Хотите развернуть список? (да/нет): ").lower() == "да":
    items.reverse()
    print("Обновлённый список:", items)
if input("Хотите отсортировать список? (да/нет): ").lower() == "да":
    items.sort()
    print("Обновлённый список:", items)


print("Длина списка:", len(items))

if input("Хотите очистить список? (да/нет): ").lower() == "да":
    items.clear()
    print("Список очищен.")
else:
    print("Ваш список:", items)

if items:
    print("\nВаши товары по порядку:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")


if len(items) > 1:
    items[0], items[-1] = items[-1], items[0]
    print("\nМеняем местами первый и последний товары.")
    print("Обновлённый список:", items)


print("Объединённый список:", "; ".join(items))

# 2

vowels = "аеёиоуыэюя"
string = input("Введите строку: ").lower()
count = sum(1 for char in string if char in vowels)
print("Количество гласных букв:", count)

# 3

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
even_numbers = [num for num in numbers if num % 2 == 0]
print("Список чётных чисел:", even_numbers)

# 4

word = "python"
user_input = input("Введите строку: ")
result = "".join([char if char in user_input else "_" for char in word])
print("Результат:", result)
