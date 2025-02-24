'Строки(str)'
# строки - не изменяемый тип данных , который предназначен для хранения текста (последоватльности символов ),заключенного в одинарные или двойные кавычки

#  string1 = 'строка с одинарными кавычками '
# # string2 = "строка с двойными кавычками "

# # # error = 'не правильная строка'

# # string3 = "Don't"

# # string4 = "Мой никнейм 'Salohidin' "

# # string5 = '''
# # Привет 
# # как 
# # дела 
# # '''

# # string6 = """Привет 
# # как 
# # ты 
# # """

# # str7 = 'Привет' + ' ' + 'как дела?'
# # print(str7)

# # # Конкатинация - это склеиваеия строк

# # str8 = 'Hi ' * 100
# # print(str8)


'Экранизация'
# # '\n' - перенос на новую строку 
# print('hello world')# hello world
# print('hello\nworld')#hello 
#                      #world

# # '\t' - табуляция 
# print('hello\tworld') # hello   world

# 'Don\'t'

# print('Don\'t')
# print("Dont\"t")



#'\v' - перенос на новую строку со смещением на длину предудущей сроки
#  print('hello\vworld\metalabs')

# '\r' - перенос каретки на начало строки
#print('Hello world\rGO')

# 'Форматирование строк'
title = 'iPhone 16'
price = 150000
message = f'Я купил {title} за {price} сом'
print(message)

# message2 = 'Я купил {} за {} сом'
# print(message2.format(price, title))
# print(message2.format('Samung Z Flip', 120000))

# message3 = 'Я купил %s за %s сом '
# print(message3 % (title, price))


# 'Методы строк '
# # # методы - функции, которые относятся к определенному (типу данных ), к ним мы обращаемся через точку
# str1 = 'hello'
# print(str1.upper())
# print('HELLO'.lower())
# print('HeLlO'.swapcase())
# print('hello world'.capitalize())
# print('hello woRld'.title())

# print(dir(str))

# print('hello'.center(11))
# print('hello'.center(11, '*'))
# print('hello world'.count('l'))
# print('hello world'.count('ll'))
# print('hello world'.count('ll'))
# print('hello world'.startswith('he'))
# print('hello world'.startswith('H'))
# print('hello world'.endswith('rld'))
# print('hello world'.endswith('gsd'))
# print('hello world'.islower())
# print('heLlo world'.islower())
# print('hello world'.isupper())
# print('Hello world'.isupper())
# print('HELLO WORLD'.isupper())


# print('hello world'.startswith('he'))
# print('hello world'.startswith('H'))
# print('hello world'.endswith('rld'))
# print('hello world'.endswith('gsd'))
# # print('hello world'.islower())
# # print('heLlo world'.islower())
# # print('hello world'.isupper())
# # print('HELLO WORLD'.isupper())
# # print('hello43434'.isdigit())
# # print('43434'.isdigit())
# # print('hello1233'.isalpha())
# # print('1233'.isalpha())
# # print('hello 123'.isalnum())
# # print('hello123'.isalnum())
# # print('hello'.isalnum())
# # print('123'.isalnum())
# # print('hello world'.replace('e', 'i'))
# # print('hello world'.replace('o', 'i'))
# # print('hello world'.replace('o', 'i', 2))
# # print('hello world'.replace('l', 'i', 3))
# # ''.split()
# # ''.join()


# 'Индексы'
# # index - порядковый номер элемента в последовательности (символа в строке) индексации начинается с 0
# # 'h e l l o  w o r l d'
# #  0 1 2 3 4 5 6 7 8 9 10
# #               ... -2 -1

# string = 'hello world'
# print(string[0]) # h 
# print(string[10]) #d
# print(string[-1]) #d
# print(string[5]) # ' '
   
# # срез - подстрока строки (часть строки) str[start:end:step]
# print(string[2:5]) # llo
# print(string[0:4]) # hell
# print(string[4:]) # o world
# print(string[:]) # hello world
# print(string[ : :2]) # hlowrd
# print(string[::-1]) # dlrow olleh
# print(string[:-5:-1]) # dlro

# str10= 'hello'
# print(str10.replace('h', 'd')) # dello
# print(str10) #hello


 
 