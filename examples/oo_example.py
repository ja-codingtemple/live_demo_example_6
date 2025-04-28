'''
Attributes / properties are variables inside of a class.
Methods are functions inside of a class.
'''

# BASE CLASS ( PARENT CLASS / SUPERCLASS ) 
class Animal:
    # To run this method and create an instance of the class, you must type the name of the class followed by (). Ex: Animal()
    def __init__(self, name):
        self.name = name
        self.living = True
        self.legCount = 4
        self.location = "Home"
        print(name + " has been created.")
        
    def walk(self, destination):
        self.location = destination
        print(f"{self.name} walks to {self.location}.")
        
# SUBCLASSES (CHILD CLASSES) -- These inherit from the parent class Animal.
class Dog(Animal):
    def bark(self, target):
        print(f"{self.name} barks at {target}.")
        
class Cat(Animal):
    def highjump(self, target):
        print(f"{self.name} does a very high jump onto {target}.")

'''
INSTANTIATING THE ANIMAL CLASS & ACCESSINGS ITS PROPERTIES / METHODS
'''
print("\nINSTANTIATING THE ANIMAL CLASS & ACCESSINGS ITS PROPERTIES / METHODS:")

# Here we create two Animal objects.
animal1 = Animal("Fluffy")
animal2 = Animal("Snowball")

# Here we print out the values of various object attributes.
print(animal1.name + " " + animal2.name)
print(f"{animal1.name} {animal2.name}")

# Here we call the class method walk()
animal1.walk("the dog park")
animal2.walk("the better dog park")

# Finally, we print the animal locations.
print(animal1.location)
print(animal2.location)

'''
INSTANTIATING THE SUBCLASSES & ACCESSING THEIR PROPERTIES / METHODS
'''
print("\nINSTANTIATING THE SUBCLASSES & ACCESSING THEIR PROPERTIES / METHODS")
dog1 = Dog("Peanut")
dog1.walk("the dog park")
dog1.bark("the other dogs")

cat1 = Cat("Moon")
cat1.walk("the food bowl")
cat1.highjump("the kitchen counter")