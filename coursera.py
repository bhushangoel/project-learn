class A():
    msg = 'class message'

    '''Instance method, takes self (instance object) as an argument
        To call this we need to create an instance of the class'''
    def foo(self, msg):
        self.message = msg
        print(self.message)

    '''It can directly access the methods or variables declared on the class, it takes current class (cls) as argument'''
    @classmethod
    def cFoo(cls):
        print(cls.msg)



# creating instance
a = A()
# calling instance method using instance name
a.foo('called from instance')
# calling instance method directly using class name but we need to pass the instance as an argument
A.foo(a, 'called directly using class name')

# calling class method directly
A.cFoo()
# calling class method using instance
a.cFoo()

str = 'name'
print(str, id(str))