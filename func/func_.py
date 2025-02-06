# '===============Функции==============='
# # функции - именнованный блок кода, который может принимать аргументы и возвращать результат

# # def my_sum(x, y): # x, y = параметры
# #     return x + y

# # res = my_sum(5, 2) # 5, 2 = аргументы
# # print(res)

# # res2 = my_sum(10, 23)
# # print(res2)


# def my_len(posl):
#     count = 0
#     for i in posl:
#         count += 1 # count = count + 1
#     print(count)

# # res1 = my_len([34, 1, 34, 2, 2])  # 5
# # print(res1)
# # res2 = my_len('hello world') # 11
# # print(res2)
# # res3 = my_len({12, 2, 32, 2, 12, 1}) # 4
# # print(res3)



# '==============Виды параметров==========='
# # 1. обязательные
# # 2. необязательные

# # 3. с дефолтом(со значением по умолчанию)
# # 4. *args - все позиционные аргументы, которые не попали в обязательные и с дефолтом)
# # 5. **kwargs - все лишние именнованные аргументы

# # def func_(x, y, z=4):
# #     return x + y + z

# # print(func_(10, 5, 3))

# '==========Виды аргументов==========='
# # 1. позиционные (по позиции)
# # 2. именнованные (по названию (параметр=аргумент))

# # def add_or_add_10(num1, num2=10):
# #     return num1 + num2 

# # print(add_or_add_10(5, 2)) # 7
# # print(add_or_add_10(40)) # 50

# def func(a, b=10, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)

# func(10)
# func(20, 30)
# func(b=30, a=40)
# func('hi', 50, True, False, 'hi', 12, 34)
# func(40, 50, 60, 70, hello=11, hi=10)



# 'Lambda'
# # lambda - анонимная функция, которая записывается в одну строку 

# lambda_func = lambda x: x ** 3
# print(lambda_func(5))

# def func_(x):
#     return x ** 3

# print(func_(5))


# 1. Напишите программу на функциях. Вы у пользователя спрашиваете что он хочет сделать 

# 1.Войти
# 2.Зарегистрироваться

# Смотря от того что введет пользователь, вы должны его зарегестрировать или залогинить


users = [
    {'username':'katana', 'password1':'205221sula', 'password2':'205221sula'}
    ]

# Регистрация:
# Вы запрашиваете username, password1, password2
# После того как пользователь введет данные, вам нужно сохранить эти данные в переменную users

# Логин:
# Запросить username, если такой username есть, запросить пароль и проверить правильно ли ввел этот пароль
# Если такого username нет в users то нужно сказать ему такого пользователя нет в базе

# users = [
#     {'username': 'katana', 'password1': '205221sula', 'password2': '205221sula'}
# ]

#1

users = [
    {'username': 'katana', 'password': '205221sula'}
]

def registerathia():
    username = input('Введите имя пользователя: ')
    password1 = input('Введите пароль: ')
    password2 = input('Подтвердите пароль: ')
    
    for user in users:
        if user['username'] == username:
            print('Такой пользователь уже существует')
            return
    
    if password1 != password2:
        print('Пароли не совпадают')
        return
    
    user.append({'username': username, 'password': password1})
    print('Вы успешно зарегистрировались')

def logining():
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    
    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                print("Вы успешно вошли!")
            else:
                print('Неверный пароль')
            return
    print('Такого пользователя нету')

def main():
    print('1 Войти')
    print('2 Зарегистрироваться')
    choice = input('Выберите действие 1 или 2: ')
    
    if choice == '1':
        logining()
    elif choice == '2':
        registerathia()
    else:
        print('Некорректный ввод')

if __name__ == '__main__':
    main()

#2
def kalculator():
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    operation1 = input('Введите  (+, -, *, /): ')
    
    if operation1 == '+':
        result = num1 + num2
    elif operation1 == '-':
        result = num1 - num2
    elif operation1 == '*':
        result = num1 * num2
    elif operation1 == '/':
        if num2 == 0:
            result = 'Ошибка: делить нельза ' 
        else:
            result = num1 / num2
    else:
        result = 'Ошибка: некорректн'
    
    print('Результат:', 'result')

if __name__ == "__main__":
    kalculator()
