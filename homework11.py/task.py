#1
numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

for num in numbers:
    if num % 2 == 0:  
        print("Первое четное число:", num)
        break
else:
    print("Четных чисел нет")
#2
a = [int(x) for x in input("Введите числа через пробел: ").split()]

i = 0  
while i < len(a):
    if a[i] < 0:  
        i += 1
        continue  
    print(a[i]) 
    i += 1
#3
text = input("Введите строку: ")

i = 0  
while i < len(text):
    if text[i].isdigit():  
        print(f"Цифра найдена: {text[i]}")
        break
    i += 1
else:
    print("Цифр в строке нет")

#4
numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:  
        print(f"Первое число, которое делится на 3 и 5: {num}")
        break
else:
    print("Чисел, делящихся на 3 и 5, нет")
#5
numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

sum_even = 0  

for num in numbers:
    if num % 2 != 0:  
        continue  
    sum_even += num  

print(f"Сумма четных чисел: {sum_even}")
