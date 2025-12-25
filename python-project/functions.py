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