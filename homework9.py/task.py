# 1
list1 = [42, "Привет", True, [1, 2, 3, 4], None]

print("Первый элемент:", list1[0])
print("Последний элемент:", list1[-1])
if isinstance(list1[3], list):
    print("Третий элемент вложенного списка:", list1[3][2])
else:
    print("Вложенного списка нет")

# 2
my_list = [10, "Python", True, 3.14, "Список"]
my_list.append("Новый элемент 1")
my_list.append("Новый элемент 2")
my_list.pop(1)

my_list.remove(True)
print("Итоговый список:", my_list)

# 3
fruits = ['яблоко', 'груша', 'яблоко', 'банан', 'яблоко']
count1 = fruits.count('яблоко')
print("Количество 'яблоко':", count1)

numbers = [0, 1, 2, 0, 3, 4, 0, 5]
count2 = numbers.count(0)
print("Количество нулей:", count2)

# 4 
my_list = ['a', 'b', 'c', 1, 2, 3, 'b']
first_b_index = my_list.index('b')
print("Индекс первого появления 'b':", first_b_index)

second_b_index = my_list.index('b', 3)  
print("Индекс 'b' в диапазоне с третьего элемента:", second_b_index)

# 5
# Данный список
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

first_of_third = nested_list[2][0]
print("Первый элемент третьего вложенного списка:", first_of_third)

last_of_first = nested_list[0][-1]
print("Последний элемент первого вложенного списка:", last_of_first)

