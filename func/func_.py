'Функции'
# функции - именнованный блок кода,который может принимать аргументы и возвращать результат

# def my_sum(x, y): # x, y = параметры 
#    return x + y 

# res = my_sum(5, 2) # 5, 2 аргументы 
# print(res)

# res2 = my_sum(10, 23)
# print(res2)


def my_len(posl):
    count = 0 
    for i in posl:
        count += 1 # count = count + 1
        return count 
    
res1 = my_len([34,1,34,2,2]) # 5
res2 = my_len('hello world') # 11
res3 = my_len({12,2,32,2,12}) # 4


def func(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

func()

















