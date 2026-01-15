# Lists are comma seperated,within Square brackets and these are comprised of strings numbers and so on Lists are zero indexed which means lists first string is indexed at 0

cities = ['Los Angeles', 'London', 'Tokyo']

print(cities[-1])

# List constructor (constructor can turn any iterable into list)

developer = 'Jessica'

print(list(developer))

# len function to get number or length of list or string

numbers = [0,1,2,3,4,5]
print(len(numbers))

# Lists are mutable which means you can update any element as long as you pass in a valid syntax

programming_languages = ['python', 'C++', 'Java', 'Rust']
programming_languages[0] = 'JavaScript'

print(list(programming_languages))

# if you pass in an index either positive or negative that is out of bounds for the list, then you will recieve an IndexError

# fruits = ['orange', 'mango', 'dates']
# fruits[10] = "watermelon"
# print(fruits)

# Del Keyword in pythons list

developer = ['NajaF Ali Haider', 23, 'Python Developer']
del developer[1]

print(developer)

# Sometimes its very helpful when we search or try to find any keyword and see if its present that list

programming_languages = ['Python', 'JavaScript', 'Java', 'Rust']

print('Rust'in(programming_languages))
print('Dart'in(programming_languages))

# Nested Lists sometimes we have lists nested inside other lists

developer = ['Najaf', 24, ['Python Developer', 'JavaScript']]
print(developer)

# for example we want to access only nested list as lists are zero based
print (developer[2][0])

# Unpacking a list you can simply unpack a list in python and then assign those values to a new variables
# here is an example of unpacking list

developer = ['Najaf', 24, 'Python Developer']

name, age, job= developer

print(name, age, job)

# in this example we have used aestrisk for fetching or collecting all the two remaining elements as remaining here is list
name, *remaining = developer

print(name, remaining)

# List Slicing the last concept
# in the lists method our last function is list slicing

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Cream']
print(desserts[1:3])

# Another thing you can do with the slice operator is you can specify a interval which determines how much to increment btw indices
# for example if you have a list of numbers and you just want to print even numbers then you can do it like this

numbers = [0,1,2,3,4,5,6,7,8,9,10]

print(numbers[0::2])