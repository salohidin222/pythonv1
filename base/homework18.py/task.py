#1) 

names = ['Nikita', 'Katana', 'Toma']
ages = [25, 30, 35]
result = dict(zip(names, ages))
print(result)

#2) 

text = "python"
for index, char in enumerate(text, start=1):
    print(f"Index: {index}, Character: {char}")

#3)

numbers = ["10", "20", "30", "40"]
numbers_int = list(map(int, numbers))
print(numbers_int)

#4) 

words = ["apple", "banana", "cherry", "dog", "elephant"]
filtered_words = list(filter(lambda word: word.startswith('d'), words))
print(filtered_words)

#5) 

numbers = [1, -2, 3, -4, 5, -6]
positive_numbers = filter(lambda x: x > 0, numbers)
squared_numbers = list(map(lambda x: x ** 2, positive_numbers))
print(squared_numbers)

#6) 

students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]


student_scores = zip(students, scores)


filtered_students = filter(lambda x: x[1] > 80, student_scores)


numbered_students = list(enumerate(filtered_students, start=1))


result = [(num, name, score) for num, (name, score) in numbered_students]
print(result)