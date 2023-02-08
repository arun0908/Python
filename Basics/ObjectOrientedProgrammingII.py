class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add nother Cat
class Tom(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Tom('Tom', 12), Sally('Sally', 5), Simon('Simon', 2)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()

print('===============================')


class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog('tom', 5)
dog2 = Dog('nibbles', 2)
dog3 = Dog('brutus', 8)

# multiple arguments can be passed without mentioning each and every one of them using the *args keyword


def Oldestdog(*args):
    return max(args)


print(f'The oldest dog is {Oldestdog(dog1.age,dog2.age,dog3.age)} years old')
