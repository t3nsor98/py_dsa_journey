class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def bark(self):       # Method
        print(f"{self.name} says woof!")

# Creating an object (instance) of the class
my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy says woof!


# Inheritance
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof!")    