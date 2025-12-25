# L Local Scope variables Declared in functions and classes
def my_func():
    my_var = 10
    print(my_var) 

my_func()

# E variables defined in enclosing or nested functions 
def outerfunc():
    msg = 'Hello There!'

    def innerfunc():
        print(msg)

    innerfunc()

outerfunc()

# however outerfunctions cannot print or access the variables declared in inner scope as out_func is calling res variable before inner function is called

def out_func():
    msg = 'Hello there!'
    # print(res)

    def inner_func():
        res = "How are you?"
        print(msg)
    inner_func()

out_func()

# but there is a way to do it lets do it now

def out_func():
    msg = "Hello There!"
    res = "" # declaring res as empty string in the enclosing scope
    def in_func():
        print(msg)
        nonlocal res # nonlocal allows modification of an enclosing variable
        res = 'How are you?'
        
    in_func()
    print(res)
out_func()

# global scope let us use variables on global level in program its not bound to any function or class for exmaple

my_var = 100

def show_var():
    print(my_var)

show_var()

print(my_var)

# if you want to make a variable globally accessible here it is

my_var = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var)
    print(my_var_2)

show_vars()

print(my_var_2)

# also you can use global keyword to make modifications in global variable for example

var_word = 100

def change_var():
    global var_word
    var_word = 200

change_var() 

print(var_word) # My Var is now modified using global keyword

# and finally according to LEGB rule built in scope refers to all of pythons built in functions modules and keywords and are available anywhere in your program

print(str(45))
print(type(3.14))
print(isinstance(4, str))