# functions learning

def hello():
    print("Hello World")

hello()

# sum calculate with parameters

def sum_calculate(a, b):
    print(a + b)

sum_calculate(4, 5)

# we can also use return keyword to exit function and it will also return a value

# without return keyword

def sum_two(a, z):
    print(a + z)

sum = sum_two(3, 3)
print(sum) # Output is None as we didn't call return keyword

def sum_nums(d, z):
    return (d + z)

sum_off = sum_nums(3, 3)
print(sum_off)

# Defining a function

def get_sum(num_1, num_2):
    return num_1 + num_2

result = get_sum(4,4) # function call
print(result) # 7

def greet():
    print('hello')

result = greet() #hello
print(result)

# applying default values to parameters

def get_sum(num_1, num_2=4):
    return num_1 + num_2
result = get_sum(4)
print(result)

# if you call a function without the correct number of arguments it will show a type error

def calculate_sum(a,b):
    print(a+b)

calculate_sum()