# Samuel Gest
# M03 Lab-Case Study: Lists Functions, and Classes
# this program takes user input for a car and its specific attributes, then outputs the data entered


# New class called Vehicle
class Vehicle:
    # function initializing attributes 
    def __init__(self, type_):
        self.type_ = type_


# New class that inherits above class attributes
class Automobile(Vehicle):
    # initializing attributes
    def __init__(self, type_, year, make, model, doors, roof):
        super().__init__(type_)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # function to print prompts for user to input information
    def info(self):
        return print(f'Vehicle type: {self.type_}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}')

# takes user input for attributes
year = input("Year:")
make = input("Make:")
model = input("Model:")
doors = input("Number of Doors (2 or 4):")
roof = input("Type of Roof (Solid or Sunroof):")

# outputs user input
Automobile("Car", year, make, model, doors, roof).info()
