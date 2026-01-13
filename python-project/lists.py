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

fruits = ['orange', 'mango', 'dates']
fruits[10] = "watermelon"
print(fruits)