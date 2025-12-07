#How do we declare variables in python? we just simply declare variable with name and assign it a value we dont need to give specific data types like int, float, boolean

# Integer
my_integer_var = 10
print('Integer:', my_integer_var)
# float 
my_float_var = 4.41
print('float:',my_float_var)
# complex
my_complex_var = 3+ 4j
print('Complex:',my_complex_var)
# String
my_string_var = "Hello, World"
print("String:", my_string_var)
# boolean
my_boolean_var = True
print('Boolean:', my_boolean_var)
# Set
# A Collection of UnOrdered Unique Elements like {7,8,9}
my_set_var = {7,8,9}
print('Set:', my_set_var)
# Dictionary
# A Collection of key-value pairs enclosed in curly braces, like{'name' : 'Najaf Ali Haider', 'age' : 24}
my_dictionary_var = {'name' : 'Najaf Ali Haider', 'age' : 24}
print("My Dictionary is:", my_dictionary_var)
# Tuple
# An Immutable ordered collection of key-value pairs enclosed in curly brackets, like (7,8,4)
my_tuple_var = (6,7,8)
print("Tuple:", my_tuple_var)
# Range
# A Sequence Of Numbers, Often used in Loops for example, [0,5]
my_range_var = range(5)
print('Range:', my_range_var)
# List
# A Ordered Collection of Elements consists of Different data types
my_list_var = [22, "Hello, World!", 0.14, True]
print(my_list_var)
# None 
#A Special value That represents the absence of value
my_var_none = None
print('None:', my_var_none)

# Updating Elements in an List 
nums = [1,2,3]
nums[0] = 4 # Changing element at zeroth index
print(nums)

# To get the data type of a variable using type() function in python
my_var_1 = "Najaf Ali Haider"
my_var_2 = 24
print(type(my_var_1))
print(type(my_var_2))

#String Concatation and Integers using f Strings
# f Strings are short for fomatted string literals 
name = "Najaf Ali Haider"
age = 24

my_name_and_age = f'My Name is: {name} and I Am {age} years old'
print(my_name_and_age)