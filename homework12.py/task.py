#1
student = {
    "Имя": "Аружан",
    "Возраст": 20,
    "Группа": "IS-23"
}
print("Имя студента:", student["Имя"])
student["Группа"] = "CS-25"
student["hobby"] = "чтение"

print("Обновленный словарь студента:", student)
#2
grades = {'math': 90, 'history': 85, 'english': 88}
math_grade = grades.get('math')
print("Оценка по математике:", math_grade)
science_grade = grades.get('science', "Не найдено")
print("Оценка по предмету science:", science_grade)

history_grade = grades.pop('history', "Не найдено")
print("Оценка по истории:", history_grade)
last_subject = grades.popitem()
print("Удалённый предмет:", last_subject)
grades.update({'physics': 92})
print("Обновлённый словарь:", grades)
#3
keys = ['name', 'age', 'city']

dictionary = dict.fromkeys(keys, "unknown")
print("Словарь после создания:", dictionary)

dictionary['name'] = "Али"
dictionary['age'] = 25
dictionary['city'] = "Алматы"

print("Итоговый словарь:", dictionary)

#4
names = ['Али', 'Айдана', 'Ермек']


name_lengths = {name: len(name) for name in names}
print("Словарь с длиной имен:", name_lengths)

unknown_dict = dict.fromkeys(names, "unknown")
print("Словарь с 'unknown':", unknown_dict)

unknown_dict['Али'] = "student"
print("Обновленный словарь:", unknown_dict)

#5
user_info = {
    'name': 'Диана',
    'age': 22,
    'city': 'Алматы',
    'profession': 'дизайнер'
}

print("Ключи:")
for key in user_info:
    print(key)

print("\nЗначения:")
for value in user_info.values():
    print(value)

print("\nПары ключ:значение:")
for key, value in user_info.items():
    print(f"Ключ: {key}, Значение: {value}")

#6

products = {'apple': 50, 'banana': 30, 'cherry': 60}

for product in products:
    products[product] = round(products[product] * 1.10) 
print("Словарь после увеличения цен на 10%:", products)

min_price_product = min(products, key=products.get) 
del products[min_price_product]  
print("Словарь после удаления продукта с наименьшей ценой:", products)
products['orange'] = 40
print("Словарь после добавления нового продукта:", products)

print("Продукты с ценой выше 50:")
for product, price in products.items():
    if price > 50:
        print(f"{product}: {price}")
#7
dict1 = {'a': 1, 'b': 2, 'c': 3}

dict2 = {value: key for key, value in dict1.items()}

print(dict2)
