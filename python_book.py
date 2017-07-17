'''
1. take element X and check whether it is divisible by any element of array A
2. if yes, then keep on dividing till it is no more divisible and check for prime number
3. if no, print no
'''

def main(arr, q1, q2, q3):
    a = arr.pop()
    def recurse(a):
        q1/a

    recurse(a)

'''composite class'''
# class Other(object):
#     def one(self):
#         print('one')
#
#     def two(self):
#         print("two")
#
#
# class Another(object):
#     def __init__(self):
#         self.other = Other()
#
#     def callOne(self):
#         self.other.one()
#
# tryme = Another()
# tryme.callOne()

'''inheritance'''
# class Animal(object):
#     def __init__(self, sound):
#         print('init called')
#         self.sound = sound
#
#     def makeSound(self):
#         print(self.sound)
#
#
# dog = Animal("bark")
#
# dog.makeSound()
#
# class Reptile(Animal):
#     def __init__(self, sound):
#         print('reptile init', Animal)
#         self.sound = sound
#
#
# snake = Reptile("fiss")
# '''
#     see, we don't have makeSound method in Reptile class but still we are able to call that, why ? because we have inherited this
#     Reptile class from Animal class, which has the makeSound method defined
# '''
# snake.makeSound()