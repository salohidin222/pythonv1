#1

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

A.add(10)

B.discard(4)

removed_element = A.pop()
print("Удалённый элемент из A:", removed_element)

A.update(B)
difference_method = A.difference(B) 
difference_operator = A - B      
print("Разность множеств (метод):", difference_method)
print("Разность множеств (оператор):", difference_operator)

union_result = A.union(B)
print("Объединение A и B:", union_result)
intersection_result = A.intersection(B)
print("Пересечение A и B:", intersection_result)
symmetric_difference_result = A.symmetric_difference(B)
print("Симметрическая разность A и B:", symmetric_difference_result)

A.intersection_update(B)
print("Обновленное A после intersection_update:", A)

A = {1, 2, 3, 4, 5} 
A.difference_update(B)
print("Обновленное A после difference_update:", A)


A = {1, 2, 3, 4, 5} 
A.symmetric_difference_update(B)
print("Обновленное A после symmetric_difference_update:", A)

#2
numbers = input("Введите числа через пробел: ")

unique_numbers = set(map(int, numbers.split()))
print("Уникальные числа:", unique_numbers)
#3
numbers = input("Введите числа через пробел: ").split()
total_count = len(numbers)
unique_count = len(set(numbers))
duplicate_count = total_count - unique_count

print("Количество повторяющихся элементов:", duplicate_count)
#4
numbers = (3, 6, 3, 7, 9, 3, 10)
index_of_7 = numbers.index(7)
print("Индекс первого появления числа 7:", index_of_7)
count_of_3 = numbers.count(3)
print("Число 3 встречается:", count_of_3, "раз(а)")
#5

my_tuple = (1, 2, 3, 4, 5)

try:
    my_tuple[0] = 10
except TypeError as a:
    print("Ошибка:", a)
#6
total_sum = 0

while True:
    number = int(input("Введите число: "))
    if number == 0:
        break  
    total_sum += number

print("Сумма чисел:", total_sum)
#7
correct_password = '2202240320807'

attempts = 3

while attempts > 0:
    password = input("Введите пароль: ")
    if password == correct_password:
        print("Доступ разрешен.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Неверный пароль. Осталось попыток: {attempts}.")
        else:
            print("Попытки исчерпаны. Доступ запрещен.")




