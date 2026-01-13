# Basic maths using python
int_1 = 56
int_2 = 12
float_1 = 5.4
float_2 = 12.0

# Addition

print("Sum addition is: ", int_1 + int_2)
print("Float addition is:", float_1 + float_2)

# Multiplications 

print("Multiplications int: ", int_1 * int_2)
print("Multiplication float: ", float_1 * float_2)

# subtraction minus

print("Subtraction int: ", int_1 - int_2)
print("Subtraction float: ", float_2 - float_1)

# Division

print("Division int: ", int_1 / int_2)
print("Division float: ", float_2 / float_1)

# Modulus operator in python gives the remainder when a number is divided by another number

print(int_1%int_2)

# floor division // this operator is used to divide two numbers and round down to nearest whole number

print(int_1//int_2)

# exponentiation operator **

int_3 = 4
int_4 = 2

print(int_3**int_4)

# round() function this is used to round a function to the nearest whole number
float_2 = 12.9

print(round(float_1))
print(round(float_2))

# Augmented assignments combines binary operation with an assignment in one step. it takes a variable, applies an operation to it with another value, and stores the result back into the same variable

# Addition assignment

my_var = 10
my_var += 5
print(my_var)

# subtraction assignment

count = 14
count -= 4
print(count)

# Multiplication assignment

product = 65
product *= 7
print(product)

# Division assignment

price = 100
price /= 4
print(price)
print(round(price))

# floor division assignment

total_pages = 23 
total_pages //= 5
print(total_pages)

# modulus assignment

bits = 35
bits %= 2

print(bits)

# Exponentiation assignment
power = 2
power **= 3 
print(power)