# Strip Method in python 
# Returns a new string with specified leading and trailing characters removed if nos argument is passed removes leading and trailing whitespace e.g given below

my_str = '  Hello World  '

trimmed_str = my_str.strip()
print(trimmed_str) # Whitespaces removed 

# replace old with new (old, new)
my_str = 'hello world'

replaced_str = my_str.replace('hello', 'hi')
print(replaced_str)

# Split Seperator splits up something into a list of strings

my_str = "hello world"
split_words = my_str.split()
print(split_words)

# Iterable (join) Joins elements into a string of a seperator

my_List = ['hello', 'world']

joined_str = ' '.join(my_List)
print(joined_str)

# Starts with(prefix) returns a boolean indicating if a string starts with the specified prefix.

my_str = 'Hello World'

starts_with_hello = my_str.startswith('Hello')
print(starts_with_hello)

# ends with (suffix) returns a boolean indicating if a string with the speicified suffix

my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)

# capitalize () returns a new string with the first character capitalized and other character lower cased
# title () Method also does the same but the only thing is it makes both of the characters capital of words like Hello World!
my_str = 'hello world'

capitalized_characters = my_str.capitalize()
print(capitalized_characters)

# isUpper() returns true if all the letters in the string are uppercase and false if not
# isLower() returns true if all the letters in the string are lowercase and false if not
my_str =  'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)

# Str.find() this method returns the index of the first occurences. if one is not found it returns -1

developer = 'Najaf'

result = developer.find('H')
print(result)

# str.count(substring) this counts how many times a string has been appears in a string
city = 'Los Angeles'
print(city.count("e"))

# Upper() returns with all characters capital 
dessert = "safari"
new_dessert = dessert.upper()
print(new_dessert)

# str.maketrans()

trans_table = str.maketrans('abc', '123')
print(trans_table)

result = 'abcabc'.translate(trans_table)
print(result)