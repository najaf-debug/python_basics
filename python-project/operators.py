# And, Or and not operators

# and operator
# age = 19
# is_citizen = True

# print(is_citizen and age)

# and operator conditions

# and And or operators are short circuiting operators as they check values from left to right
age = 25
is_citizen = True

if is_citizen and age >= 18:
    print("You are Eligible to vote")
else:
    print("You are not Eligible to vote")

# Or Condition
or_age = 19
or_citizen = False

print(or_age or or_citizen)

# Not operator in python is opposite operator as it makes opposite of condition

print(not "")
print(not 'Hello')
print(not 0)
print(not 1)

# conditionals for or operator

is_admin = True

if not is_admin:
    print("Access Denied for non administrators")
else:
    print("Welcome, Administrator")