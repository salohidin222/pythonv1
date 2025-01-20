# # # 'Логические и условеые операторы'
# # # # логические операторы - выражения , которые возврашают True, есои выражение верно, False - если выражение не верно 


# # # 'Равенство'
# # # 10 == 5 # False
# # # 5 == 5 #True
# # # # print('hi' == 2)

# # # 'hi' == 'hi' # true
# # # 'Hi' == 'hi' # False
# # # '5' == 5 # False
# # # '+' == '+' # True


# # # 'Не равенство'
# # # 4 != 5 # True
# # # 5 != 5 # False

# # # 'Больше'
# # # 10 > 10 # False
# # # 4 > 1 # True

# # # 'Меньше'
# # # 5 < 4 # False
# # # 10 < 10 # False

# # # 'Больше или равно'
# # # 10 >= 4 # True 
# # # 10 >=10 # True
# # # 4 >= 5 # False

# # # 'Меньше или равно'
# # # 10 <= 10 # True
# # # 5 <= 10 # True
# # # 10 <= 5 # False

# # # 'And Or Not'

# # # a = 5
# # # b = 6

# # # #True  and    True
# # # a == 5 and b == 6 # True 

# # # #False and    True
# # # a == 7 and b ==6 # False 

# # # #False and True 
# # # a > 10 and b<= 6 

# # # #False and False 
# # # a == 0 and b == 0 #False 


# # # # если все части выражения возвращают True - будет True
# # # # если хотя бы одна часть вырадения фалсе 

# # # #True or True 
# # # a ==5 or b == 6 # True 

# # # #False or True 
# # # a > 10 or b == 6 # True

# # # #True or False 
# # # a < 20 or b == 10 # True 

# # # # False or False 
# # # a == 1 or b == 1 #False 

# # # a == 1 or b == 4 and a == 5 or b == 2

# # # # еслиодна часть выражения возврашает True - будет True

# # # not True # False
# # # not False #True 

# # #    #True 
# # # print(not a == 5) # False 


# # # not a < 20 or not b == 6 # False 


# # # # not b > 20 and a == 5 or b == 6 or a < 6 and b >= 6 or not a == 5 and 5 == 10 # True


# # # 'Bool Type '
# # # # Булевый тип данных имеет всего 2 значения True и False 

# # # bool(1) # True 
# # # bool(-12) # True 
# # # bool(0) # Fasle 

# # # bool('hello') # True 
# # # bool(' ') # True 
# # # bool('_') # True 
# # # bool('') # False 

# # # bool(True) # True 
# # # bool(False) # False 

# # # 'None type'
# # # # Ноне - неизменяемый тип данных с одгим значением Ноне, который используеися для облзначения отсуствия значения

# # # a = None   
# # # bool(None) # False 

# # # # print(bool())


# # # a = 5
# # # a = 5 

# # # a == b # True
# # # print(a is b) 

# # # a = 'hi'
# # # b = 'hi'
# # # print(id(a), id(b))

# # # 'Услвные операьоры'
# # # # Условные операторы - конструкция, котторая используется для того что бы при разных данных код работал по разному (в зависимости от условия)

# # # # if условие1:
# # # #    действие1

# # pogoda = input('Введите погоду:') # Ураган

# # if pogoda == 'солнечно':
# #    print('взять солнеч-очки')

# # elif pogoda == 'дождливо':
# #    print('Взять зонтик')
   
# # else:
# #    print('Пока')

   
# 'Тернарный оператор'
# # тернарный оператор - условие в одну строку

# num = -23



# if num > 0: 
#     chislo = 'положительное'
# else:
#     chislo = 'отрицательное'

# # chislo = действие1 if условие1 else действие2

# chislo = 'положительное' if num > 0 else 'отрицательное'