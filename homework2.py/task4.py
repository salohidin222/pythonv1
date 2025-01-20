from decimal import Decimal
number_str=input("Введите дробное число:")
number=Decimal(number_str)
result=number*10

print("Результат сложения:",result)
print("Тип данных результата",type(result))