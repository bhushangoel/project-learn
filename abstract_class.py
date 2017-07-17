'''
Abstract class acts as a blueprint for other classes, 
abstract methods can only be present inside abstract classes.
Abstract methods needs to pass from a function body.
Class which extends abstract class should have the abstract methods
'''

from abc import ABCMeta, abstractmethod, ABC
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r=1):
        print(r)
        self.radius = r

    def setRadius(self, r):
        self.radius = r

    def area(self):
        a = math.pi * math.pow(self.radius, 2)
        print(a)
        return a

    def perimeter(self):
        p = 2 * math.pi * self.radius
        print('p: ', p)
        return p


# c2 = Circle()

# c2.perimeter()

class A():
    count = 0

    def increaseCount(self):
        z = self.count + 1
        print(z)
        return z


a = A()
b = A()

a.count = 10
# print(a.count)
# print(a.count)
# print(b.count)

def factorial(n):
    print('n:', n)
    if n == 1:
        return 1

    aa = n * factorial(n-1)
    print(n, aa)
    return aa

ans = factorial(4)

# print(ans)