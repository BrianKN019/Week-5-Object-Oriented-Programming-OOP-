# Canvas Assignment 1: Design Your Own Class! 🗷️

# Part 1: Creating a Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand  # Public attribute
        self.model = model
        self.__price = price  # Private attribute (encapsulation)

    # Method to display smartphone details
    def display_details(self):
        return f"Smartphone: {self.brand} {self.model}, Price: ${self.__price}"

    # Method to update the price
    def update_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Error: Price must be greater than zero.")

# Inheritance: Adding a specialized class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def display_details(self):
        base_details = super().display_details()
        return f"{base_details}, GPU: {self.gpu}"

# Create objects for the classes
phone1 = Smartphone("Apple", "iPhone 15", 1200)
phone2 = GamingSmartphone("Asus", "ROG Phone 6", 1500, "Adreno 730")

# Display details
print(phone1.display_details())
print(phone2.display_details())

# Update price of phone1
phone1.update_price(1100)
print(phone1.display_details())

# Activity 2: Polymorphism Challenge! 🎭

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Create objects for each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Demonstrate polymorphism
vehicles = [car, plane, boat]
for vehicle in vehicles:
    print(vehicle.move())
