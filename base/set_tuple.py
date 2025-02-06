my_set1 = {1, 2, 3, 4, 5}
print(my_set1)


empty_set = set()
empty_set.add("Python")
print(empty_set)


my_set = {1, 2, 3, 4, 5}
my_set.remove(3) 
print(my_set)


set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)


intersection_set = set1.intersection(set2)
print(intersection_set)


my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)

tuple1 = (10, 20, 30)

tuple2 = (1, 2, 3)
list_from_tuple = list(tuple2) 
list_from_tuple.append(4)  
tuple2 = tuple(list_from_tuple) 
print(tuple2)


tup = (100, 200, 300)
a, b, c = tup  
print(a, b, c)


nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))  
print(unique_nums)
