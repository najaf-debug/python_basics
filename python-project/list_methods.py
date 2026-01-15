# in the lists.py we were introduced to how lists are declared how do they work and how to access list elements as well as list slicing

# in this file we will learn more methods about lists like list.append(), list.pop(), list.sort()
numbers = [1,2,3,4,5]
print(numbers)
numbers.append(6)
print(numbers)

# if you want to add another list at the end of another you can use append() method like this

numbers = [1,2,3,4,5]
even_numbers = [6,8,10]

numbers.append(even_numbers)
print(numbers[5][2])
