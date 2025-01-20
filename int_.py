# # # 'Числа(int)'
# # # #integers(int)-Целое число 

# # # num = 10
# # # print(type(num))# int 

# # # #float - вешественные числа (с плаваюшей точкой, десятичные )

# # # num2 = 0.5
# # # print(type(num2))# float-Выводит тип данных пременной 
# # # print(float(num))#10.0-int ->float
# # # print(int(num2))#0-float->int,без округления

# # # num3='0.5'
# # # num4=float(num3)
# # # print(int(num4))

# # # num5=0.5
# # # print(str(num5))

# # # print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1)
# # #1)0.99999999999

# # #decimal - точное вещественное число 
# # #Что бы работать с Decimal его нужно импортировать 

# # from decimal import Decimal 

# # num6='0.1'
# # num2=Decimal(num6)
# # num3=num2+num2+num2+num2+num2+num2+num2+num2+num2+num2
# # print(type(num3))


# 'Операции над числами '
# 5+7
# 10-5
# 2*10
# 50/10
# 50//10
# 7%2#ostatoc
# 5**5#25
# 25**0.5#Нахождение кв корня числа

# print(abs(-5))
# print(abs(10))
# print(abs(-0.5))

# round-округления числа 
# print(round(5.6))
# print(round(5.5))
# print(round(5.4))
# print(round(5.499999))

# print(round(round(5.49)))

# round округляет один раз до таго числа , до которго вы указали округление 

# sqrt- функция для нахождении кв корня числа 
# from math import sqrt

# print(sqrt(25))#5
# print(sqrt(81))#9

# #pow
# #1.возводит число в степень 
# #2.находит остаток от деление на 3 число 

# print(pow(2,5))#2 ** 5 = 32
# print(pow(2, 5, 4))#(2 ** 5)% 4 = 0

# # divmod -  функция которое  возращает 2 числа, где 1- целая часть от деления,2-остаток от деления 
# print(divmod(5, 2))#2, 1
# print(divmod(44, 3))#14, 2







