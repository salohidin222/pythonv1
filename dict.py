# # # # # Dict(словари)
# # # # #dict - изменяемый, итеруруемый, ''неупорядочный', неиндексируемый типданных, для хранения данных в парах (ключ:значение)

# # # # user = {
# # # #     'name':'Salohidin', 
# # # #     'age':21, 
# # # #     'prof':'Dev'
# # # #     }
# # # # print(user['name']) # Salohidin

# # # # # ключами в словаре могут быть только не изменяемые типы данных
# # # # # если в словаре есть одинаковые ключи то сохранится последний

# # # # dict1 = {'a':1, 'b':2, 'c':3, 'a':4}
# # # # print(dict1) # {'a':4, 'b':2, 'c':3,}

# # # # print(dict1['f']) # KeyError

# # # # 'Создание'
# # # # user = {'a':1, 'b':2}

# # # # user = dict([('a', 1), ('b', 2), ('c':3)])

# # # # user = dict(['ab', 'cd', 'ef'])



# # # list1 = ['ab', 'cd', 'ef']
# # # dict1 = dict(list1) # {}

# # # int()
# # # str()
# # # list()
# # # dict()

# # 'Методы словаря'

# # # 'strasdsad'.islower()
# # # [1, 2, 3].append(5)
# # # {'a':1}.clear

# # # get - метод, который возврашает значение по ключу , если такого ключа нет , то вовращает None или дефлотное значение 
# # user = {
# #      'name':'Salohidin', 
# #      'age':21, 
# #     'prof':'Dev'
# # }
# # print(user.get('namehgygsyu', 'Такого ключа нету')) # Такого ключа нету 

# # # pop - удаляет пару по ключу и возврщает значение 
# # num = user.pop('age') # 21 
# # print(num)

# # # popitem - удаляет последнюю пару и возвращает ее
# # dict1 = {'a':1, 'b':2}
# # num = dict.popitem()

# # update - расширает словарь парами из вторго словаря

# # dict1 = {1:'a', 2:'b'}

# # dict2 = {3:'c', 4:"d"}

# # dict.update(dict2)
# # print(dict1)

# # fromkeys - метод для создания нового словаря , используя список ключей

# dict1 = dict.fromkeys('hi', 12)
# print(dict1)

# dict2 = dict.fromkeys([10, 20, 30], 'hello')
# print(dict2)


# keys - возвращяет все ключи 
# values - возвращяет все значения 
# items - возращяет все пары 

