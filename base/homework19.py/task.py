# 1) 
names = ['Nikita', 'Katana', 'Toma']
ages = [25, 30, 35]
name_age_dict = dict(zip(names, ages))
print(name_age_dict)

# 2) 
text = "python"
for index, char in enumerate(text, start=1):
    print(index, char)

# 3) 
numbers = ["10", "20", "30", "40"]
int_numbers = list(map(int, numbers))
print(int_numbers)

# 4) 
words = ["apple", "banana", "cherry", "dog", "elephant"]
filtered_words = list(filter(lambda word: word.startswith('d'), words))
print(filtered_words)

# 5) 
numbers = [1, -2, 3, -4, 5, -6]
positive_numbers = list(filter(lambda x: x > 0, numbers))
squared_numbers = list(map(lambda x: x ** 2, positive_numbers))
print(squared_numbers)

# 6) 
students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]


student_scores = list(zip(students, scores))

filtered_students = list(filter(lambda student: student[1] > 80, student_scores))


numbered_students = list(enumerate(filtered_students, start=1))
  
result = [(num, name, score) for num, (name, score) in numbered_students]
print(result)


