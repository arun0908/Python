from functools import reduce


# Pure Function
# The below function is said to be pure as it always returns an exprected and same output for the same input everytime, and does
# not effect the outside world, such as printing the result(effects by displaying it on screen) instead of returning, or using the
# new array in a global scope.
def MultiplyByTwo(array):
    new_array = []
    for _ in array:
        new_array.append(_*2)
    return new_array


print(MultiplyByTwo([1, 2, 3]))
print('=============================================')


# Map(). Map is a function provided in python, which takes in a function as an input and an iterable and returns a map object as
# output. As per the functional programming paradigm, it seperates the data aspect of the code and logic aspect of the code.
def MultiplyByThree(item):
    return item*3


# Map returns a map object and its location in the memory. Function provided as part of map, must be predefined and does not take
# inbuilt functions. They dont modify the input and return a new output.
new_list = list(map(MultiplyByThree, [1, 3, 9]))
print(new_list)
print('=============================================')


# Filter. Filter is similar to map and takes in a function and an iterable but filters out stuff and returns a True or false condition
# and based on true or false for each item, they are filtered by the filter function. They dont modify the input and return a new output.
def is_odd(item):
    return item % 2 != 0


odd = list(filter(is_odd, [1, 2, 3, 4, 5]))
print(odd)  # [1,3,5]
odd2 = list(map(is_odd, [1, 2, 3, 4, 5]))
print(odd2)  # [True,False,True,False,True]
print('=============================================')


# Zip. Zip is used to zip all the variables in the first and second iterable as a tuple, by combining first element from both the lists,
# second one from both the lists, third, etc. For example it can be used to combine username and emails for example
zip_list = list(zip([1, 2, 3, 4], [1, 4, 9, 16]))
print(zip_list)  # [(1,1),(2,4),(3,9),(4,16)]
print('=============================================')


# Reduce. Reduce is a function in python which is seldom used. It is similar to other map and filter functions and takes in a function as,
# an input along with a iterable object and an initial value for the function. It returns an integer value as an output.
def sums(sum, item):
    # This returned value is used as the sum param for the next iteration of the iterable object.
    return sum + item


reduce_list = [1, 2, 4, 3, 6]
print(f'Output of reduce function is : {reduce(sums,reduce_list,0)}')
