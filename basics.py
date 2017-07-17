name = "Bhushan"
lastname = "Goel"

# string format functions
final = "My Name is {0} {1}".format(name, lastname)
final2 = f"My Name is {name} {lastname}"

print(final, final2)

# boolean
python = True
java = False

# control flow statements
number = 50
if number != 5 and java:
    print('yey')

# list or arrays
car_names = ["BMW", "AUDI", "MERCEDES"]

# add item at the end
car_names.append("PORCHE")

# check if value exists in car_names
value = "BMW" in car_names

# delete from car_names
del car_names[2]

# slicing array ==> [start:end]
car_names_tmp = car_names[1:]
print(car_names, value, len(car_names), car_names_tmp)

# for loop
for name in car_names:
    print("{0} is a luxury car".format(name))

# range (start, end, incrementBy)
x = 0
for index in range(0, 6, 1):  # [5,7,9]
    x += 1
    print("value of x: {0}".format(x))

# dictionaries
car = {
    "name": "BMW",
    "type": "sedan"
}

print(car["name"])
print(car.get("power", "unknown"))
print(car.keys())
print(car.values())

#exception handling
try:
    car['power']
except KeyError as error:
    print("Error occured {0}".format(error))

print("but this code executes...")

