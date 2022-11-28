class C:
    def f(self):
        print('foobar')


i = C()
i.f()



class C2:
    cv = 'cv'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

i2 = C2("abc")
print(i2.cv, i2.name)