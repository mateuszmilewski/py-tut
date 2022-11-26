def fooConstruct(num):
    """
        doc string
        this is a bit simple foo quasi-foo-constructor based on lambda expression
    """
    return lambda x: x + 2 * num

foo = fooConstruct(17)

print(foo(1))
print(foo(2))


foo = fooConstruct(-100)
print(foo(1))
print(foo(2))


print( fooConstruct.__doc__)
