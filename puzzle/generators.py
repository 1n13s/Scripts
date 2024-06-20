import random

def create_cubes (num: int):
    result = []
    for x in range(num):
        result.append(x**3)
    return result

def gen_create_cubes (num: int):
    for x in range(num):
        yield x**3

def print_result (result: list):
    for num in result:
        print(num)

#Problem one
def gensquares(num: int):
    for x in range(num):
        yield f"Square of {x} is {x**2}"

"""for result in gensquares(10):
    print(result)"""

#Problem two
def rand_num(low,high,num):
    for x in range(num):
        yield random.randint(low,high)

"""for result in rand_num(0,568,10):
    print(result)"""

#Problem 3
s = "hello"
s_gen = iter(s)
print(next(s_gen))

#Problem 4




