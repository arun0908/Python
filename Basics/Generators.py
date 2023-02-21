from time import time


# A generator function, which takes in the input as nums and includes the yield keyword which pauses the flow of the function code.
def generator_function(num):
    for item in range(num):
        # In the first iteration, the value of item = 0, and once it encounters yield(item), the program is paused. When we provide a next keyword
        # then the program resumes for another iteration and again stops with item = 1
        yield (item)


# creating a variable which holds the output of this generator function, which is a generator object. So this generator object is an iterable and
# it can be iterated over.
g = generator_function(100)
# This prints the location in memory of the generator object
print(g)
# The use of next keyword resumes the generator_function program and it assigns the value as per the code to g and outputs it.
print(next(g))
# Now the value of item in the function code is 1 and the next keyword outputs this and then resumes the flow of the program again.
print(next(g))
# Now when we try to print g again, without the use of the next keyword, we get the same output, which is the objects location in the memory.
print(g)
print(next(g))

# Instead of using the next keyword each time, what we can do is use a for loop, which loops through the iterable object and we can print it.
for i in generator_function(10):
    print(i, end=',')
print('===============================================')


# Code to understand the power of generators in python and its use insted of lists of any other kind of iterables.
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    print('1')
    for i in range(10000000):
        i*5


@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i*5


long_time()
long_time2()
print('===============================================')

# Custom generator function, which allows us to create a generator of our own type similar to the range generator.


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            iterator*5
            next(iterator)
        except StopIteration:
            break


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # this line allows us to use the current number as the starting point for the iteration
        MyGen.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(1, 100)
for i in gen:
    print(i, end=' ')
print('===============================================')


# Fibonacci series using generators
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(16):
    print(x)
print('===============================================')


# Fibonacci series using lists instead of generators.
def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


print(fib2(16))
