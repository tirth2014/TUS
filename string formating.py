class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        print("hello, my name is {} and age is {}...name: %s".format(self.name, self.age) % self.name)

        def heel():
            print("heel")


ob = Person("Tirth", 21)
ob.fun()

print('{2} {1} {0}'.format('one',
                           'two', 'three'))
