#1
num1 = [x**2 for x in range(1, 11)]
print(num1)

#2
num2 = [x for x in range(10, 41) if x % 2 != 0]
print(num2)

#3
num3 = [x**2 for x in range(1, 11) if x % 3 == 0]
print(num3)

#4
num4 = {x: x**2 for x in range(1, 6)}
print(num4)

#5
fuits = ["apple", "banana", "cherry"]
fruits1 = {word: len(word) for word in words}
print(fruits1)

#6
num5 = {x: x**2 for x in range(1, 11) if x > 5}
print(num5)

#7
num6 = {x**2 for x in range(1, 11)}
print(num6)

#8
fructi = {word for word in ["apple", "banana", "apple", "cherry"]}
print(fructi)

#9
input = "hello world"

vowels = set("aeiou")


num8 = set(char for char in input if char in vowels)

print(num8)


#10
cubes = (x**3 for x in range(1, 11))
for cube in cubes:
    print(cube)
cubes1 = list(cubes)
print(cubes1)

#11
numbers = (x for x in range(1, 21) if x % 2 == 0)
for num in numbers:
    print(num)
list = list(numbers)
print(list)







