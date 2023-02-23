from ModuleII import test2
import random
from collections import Counter, defaultdict
# from ModuleII import test


# test() Trying to call this gives you an import error, as the method is provided as part of the if __name__=='__main__' block, which prevents it
# from being imported as python cannot find the method.
# test2()
# help(random) # prints the purpose of the random module in python
# print(dir(random)) # prints the list of available methods in the random module in python.

demo_list = [1, 1, 2, 3, 1, 4, 4, 1, 2, 3,
             2, 5, 3]  # list of repeating variables
# counter object, a counter is similar to a dictionary which outputs the count of every variable in the iterable and produces a dict like object
c = Counter(demo_list)
map = {}
for i in c:
    map[i] = c[i]
print(c, map)  # {1: 4, 2: 3, 3: 3, 4: 2, 5: 1}
# trying to access an element not present in the map
try:
    # this generates a keyerror, because there is no variable 6 in the dictionary
    print(map[6])
except KeyError as err:
    print('key not found', err)
# in a defaultdict, we can avoid the error of not having a key by using the default value, in this case int, so whenever there is no value it outputs 0
dict = defaultdict(int)
for i in map:
    dict[i] = map[i]
print(dict)
print(dict[6])
