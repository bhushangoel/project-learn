# classes in python created by using class keyword, pass is a keyword in python which tells the interpreter do nothing
cars = []


# self points to the current instance of class, if we want to call add_student from inside the class we can use self.add_student()
# __init__ is the constructor function, that executes initially
# self is an instance attribute, which is common for a particular instance
# similarly we can have the class attributes, which will be common to the whole class and all the instances of that class
class Car:
    car_type = "Sedan"  # class attribute

    def __init__(self, name, color):
        self.name = name
        self.color = color
        cars.append(self)

    def __str__(self):
        return "Car name: " + self.name

    def get_car_type(self):
        return self.car_type


# bmw is now an object made from Car class
bmw = Car("BMW", "Red")
print(bmw, bmw.color, bmw.get_car_type(), Car.car_type)

audi = Car("Audi", "Black")
print(audi, audi.get_car_type())
