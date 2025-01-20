#1
user_string = input("Введите слово: ")
centered_string = user_string.center(50)
print(f"Отцентрированная строка: '{centered_string}'")


count_a = user_string.lower().count('а') 
print(f"Количество букв 'а' в строке: {count_a}")

#2
user_string = input("Введите слово: ")
starts_with_hello = user_string.startswith("Привет")
ends_with_exclamation = user_string.endswith("!")

print(f"Строка начинается с 'Привет': {starts_with_hello}")
print(f"Строка заканчивается на '!': {ends_with_exclamation}")
is_lower = user_string.islower()
is_upper = user_string.isupper()

print(f"Строка написана полностью в нижнем регистре: {is_lower}")
print(f"Строка написана полностью в верхнем регистре: {is_upper}")

#3

user_string = input("Введите слово: ")
is_digit = user_string.isdigit()
is_alpha = user_string.isalpha()
is_alnum = user_string.isalnum()


print(f"Строка состоит только из цифр: {is_digit}")
print(f"Строка состоит только из букв: {is_alpha}")
print(f"Строка состоит только из букв и цифр: {is_alnum}")

#4
user_string = input("Введите строку: ")
modified_string = user_string.replace(" ", "_")


print(f"Строка с заменёнными пробелами: {modified_string}")

