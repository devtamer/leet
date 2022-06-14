
# first class functions
def multiply(a,b):
    return a*b
mult = multiply
def product(x,y):
    return mult(x,y)
def proveprod(a,b,func):
    return func(a,b)

print(mult(2,3))
print(product(6,2))
print(proveprod(9,4, product))

def decorator_fun(main_func):
    def wrapper_func():
        print("Wrapper Function")
        return main_func()
    return wrapper_func

@decorator_fun
def display()
