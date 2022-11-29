class C:
    def f(self):
        print('foobar')


i = C()
i.f()



class C2:
    cv = 'cv'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.list = [] # correct way of making instance array

    def addElement(self, element):
        self.list.append(element)

i2 = C2("abc")
print(i2.cv, i2.name)
i2.addElement('element oooo')

print(i2.list)




# additional test between class var and instance var
class Test:
    a = 'a'
    b = 'b'

i1 = Test()
print(i1.a, i1.b)
i2 = Test()
i2.a = 'aaa'
# this is now intersting class var become instance var!
print(i1.a, i2.a)
