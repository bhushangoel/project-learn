# function
car = []


def addCar():
    name = input("Enter your favorite car: ")
    car.append(name)


addCar()
print(car)


# variable argument function
def var_args(*args):
    print('args', args, len(args))


var_args("abc", "def", 14, True)


def var_args2(**kwargs):
    print('args', kwargs)


var_args2(first="abc", second="def", third=14, fourth=True)

# yield keyword
carArr = []


def read_file():
    try:
        f = ["bmw", "audi"]
        for car1 in read_cars(f):
            carArr.append(car1)
    except Exception as error:
        print("Could not locate file - {0}".format(error))


def read_cars(f):
    print(f)
    for line in f:
        yield line  # try to replace yield with return and observe the result


read_file()
print(carArr)


# lambda functions
def double(x):
    return x * 2


d = double(5)
print(d)

# its a one line function, mainly used in the case where we need to pass a function as a parameter of another function
triple = lambda x: x * 3

t = triple(5)
print(t)
