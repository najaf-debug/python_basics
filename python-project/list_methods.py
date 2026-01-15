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

# Here is another most helpful method is extend method basically what you can do with extend method is you can add multiple number of elements to a list.
# it is very similar to append() method

numbers = [1,2,3,4,5]
extend_numbers = [6,8,10]

numbers.append(extend_numbers)
print(numbers)

# Another most helpful method is insert in python insert() basically what insert method does is.
# it takes two indexes or values from us one is the index where we want to insert our value and the second one is that value that what we 
# want to insert

numbers = [1,2,3,4,5]

# first one is index while second is the value
numbers.insert(5,6)
print(numbers)

# if you want to remove a value from a list index you can use remove() method. The remove() method takes the value of the element to  
# remove as an argument

numbers= [10,20,30,40,50,50]

numbers.remove(50)
print(numbers)

# Pop() method to remove an element at a specific index in the list, you can use the pop() method like this

numbers = [1,2,3,4,5]

numbers.pop(2)
print(numbers)

# if you don't specify an element it will automatically pop the last element

numbers.pop()
print(numbers)

# if you need to empty the whole list you can use the clear method() like this

numbers = [1,2,3,4,5]
numbers.clear()

print(numbers)

# The next method we will take a look at is the sort() method there is a sorted function which works for any

unsorted_nums = [49,30,1,6,2]

unsorted_nums.sort()

print(unsorted_nums)

# In contrast with sort method we use sort function() which works for any iterable and returns a new sorted list without modifying the 
# original ones

numbers = [19,2,35,1,67,41]
sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)

# The next method we are going to learn about is reverse() this method will reverse a list of elements in a place like this

numbers = [6,5,4,3,2,1]
numbers.reverse()

print(numbers)

# The last Method in list methods is gonna be index method which is used to find the index of the first method where an element can be found
# Here is an example of using the index method to find the language in a programming_languages list

programming_languages = ['Java', 'Rust', 'Python', 'C++']
languages = programming_languages.index('Rust')

print(languages)