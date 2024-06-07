# CLASSES AND OBJECTS
# Define a class named 'Car'
class Car:
    def __init__(self, brand, model, year):
        # Initialize the Car object with brand, model, and year attributes
        self.brand = brand
        self.model = model
        self.year = year
    
    # Method to display car details
    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes and methods
print(my_car.brand)  
my_car.display_details()

# Encapsulation
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute
    # Public method to access private attributes
    def get_details(self):
        return f"Name: {self.__name}, Age: {self.__age}"
    # Public method to set private attributes
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age")

# Create an object of the Person class
person = Person("Alice", 30)
# Accessing private attribute via public method
print(person.get_details())
# Using setter method to update private attribute
person.set_age(35)
print(person.get_details()) 

# Inheritance
# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # To be implemented by subclasses

# Derived class
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create objects of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method
print(dog.name, "says", dog.speak())  
print(cat.name, "says", cat.speak())  

# Polymorphism
# Base class
class Shape:
    def draw(self):
        pass  # To be implemented by subclasses

# Derived class for circles
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

# Derived class for rectangles
class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

# Function to demonstrate polymorphism
def draw_shape(shape):
    shape.draw()

# Create objects of Circle and Rectangle
circle = Circle()
rectangle = Rectangle()

# Using the function with different types of shapes
draw_shape(circle)     
draw_shape(rectangle)  


# Abstraction
from abc import ABC, abstractmethod
# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
# Derived class implementing abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Create an object of the Rectangle class
rectangle = Rectangle(4, 5)

# Accessing methods
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())


# Composition
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print("Engine started")
class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine  # Car has an Engine
    def start(self):
        print(f"{self.brand} {self.model} is starting.")
        self.engine.start()
# Create an Engine object
engine = Engine(150)
# Create a Car object with an Engine
car = Car("Honda", "Civic", engine)
# Start the car
car.start()

