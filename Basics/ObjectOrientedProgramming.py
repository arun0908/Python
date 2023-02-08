class PlayerCharecter:
    # Class object attribute
    membership = True

    # Constructor
    def __init__(self, name, age):
        # the class object attribute can only be referred using self. If membership is entered directly without self, there is an error.
        # It can also be referred using PlayerCharecter.membership as it is a class object attribute if we try to reference the name
        # variable using PlayerCharecter.name it throws an error and does not recognize it, as the class does not have any variable called
        # name
        if self.membership & (age > 18):
            # The addition of the _ denotes that this variable is to considered private as per convention and not used to assign anything else.
            self._name = name
            self.age = age

    # Method of the class common to any instance of the class
    def jump(self, distance):
        self.distance = distance
        # any attribute being referred in the class needs to have the self keyword, which indicates that the attribute belonging to
        # the object
        print(f'{self._name} can jump {self.distance} m')

    def speak(self):
        print(f'I am player {self._name}, and i am {self.age} years old')

    # The @classmethod is a decorator, which is used to indicate that this method belongs to the class. It takes in a mandate parameter
    # which is cls similar to self. It can be accessed similar to a class object attribute by calling the classname. way.
    @classmethod
    def addThings(cls, num1, num2):
        return cls('Teddy', num1+num2)


player1 = PlayerCharecter('Mike', 22)
player2 = PlayerCharecter('Jake', 41)
# Here we are calling the addthings method in Playercharecter class using the class method concept.
player3 = PlayerCharecter.addThings(2, 3)
player1.jump(10)
player2.jump(20)
# We are calling the speak method which is abstracted from the user, but he is able to access the method
# player2.speak = 'Helloo' This would change the definition of the speak method which would make it a string and next time the speak is
# called as a method it would throw an error. This would be a wrong implementation of Abstraction.
player2.speak()
print('============================== \n')


# Parent class used for inheritance
class User():
    # This method has been commented as part of HybridChar object creation which calls constructors of 2 parent classes and each call their
    # super class which is User's constructor and pass email again, which leads to error.

    # def __init__(self, email):
    #     self.email = email

    def sign_in(self):
        print('The user is signed in')

    def attack(self):
        print('User attack method to demonstrate polymorphism')


# Child class/sub class which dervies from the User class which is the parent class
class Wizard(User):
    # We are creating another constructor which is specific to the Wizard class and overrrides the constructor of the User class.
    # So if we want to call the constructor of the user class we have 2 methods. One is by using the class name or using the super keyword.
    def __init__(self, name, power, email):
        # User.__init__(self, email)  # 1 method
        # super().__init__(email)  # 2 method
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Wizard {self.name} can attack with a power of {self.power}')

    # def display_email(self):
    #     print(f'I own the email address {self.email}')


# Class is derived by passing the class name inside the paranthesis of the child class
class Archer(User):
    def __init__(self, name, arrow_count, email):
        # User.__init__(self, email)
        # super().__init__(email)
        self.name = name
        self.arrow_count = arrow_count

    def attack(self):
        print(
            f'Archer {self.name} can attack with a total of {self.arrow_count} arrows')

    # def display_email(self):
    #     print(f'I own the email address {self.email}')


# Multiple inheritance
class HybridChar(Wizard, Archer):

    # Passing of parameters seperately and calling the constructors of each parent class, ensures that there are no variables left out
    # for calling the methods of each class. By default, the Wizard class takes precedence and params are passed to it first.
    def __init__(self, name, power, arrows, email):
        Archer.__init__(self, name, arrows, email)
        Wizard.__init__(self, name, power, email)


wizard1 = Wizard('Gandalf', 1000, 'gandalf@wizrd.com')
archer1 = Archer('Hawk Eye', 100, 'hawkeye@archer.com')
hybrid1 = HybridChar('Hulk', 10000, 100, 'hulk@green.com')
wizard1.attack()
archer1.attack()
wizard1.sign_in()
print('============================== \n')
print(hybrid1.attack())
print('============================== \n')
# This checks whether the given object is an instance of the class given
print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True

# Object is the default and base class from which any class/object inherits in python.
print(isinstance(wizard1, object))  # True

# Polymorphism, which changes the method definition based on the class which calls it.
print('============================== \n')
for _ in [wizard1, archer1]:
    _.attack()

print('============================== \n')
# wizard1.display_email()
# archer1.display_email()

# Introspection of an object can be done by using the dir keyword which helps us to determing the methods avaiable to an object
print('============================== \n')
print(dir(wizard1))
