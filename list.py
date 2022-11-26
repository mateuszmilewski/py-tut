def list():
    list1 = [1, 2, 3, 4, 5, 6]
    print(list1[0])
    # same as for string
    print(list1[-1])
    print(list1[2:])
    print(list1[3:5]) # element #3 and #4 -> #5 doesnt count

    list2 = list1[:] # copy of the list
    print(list2)
    # this mod affects only number 1
    list1[2] = 123

    print(list1)
    print(list2)


    # now this is different -> this is kind of the reference copy
    # so change in list3 affects data in list
    list3 = list1
    list3[2] = 111

    print(list1)
    print(list2)
    print(list3)


    list4 = list1[:]
    list4.append(666)

    print('check for this list4')
    print(list1)
    print(list4)


    # quick loop
    print('quick loop')
    words = ['cat', 'window', 'defenestrate']
    for word in words:
        print(word, len(word))



    # colletion
    coll = {
        'key1': 1,
        'key2': 2,
        'key3': 3,
        'key4': 4
    }

    for k, v in coll.items():
        print(k, v)
        print(coll[k])
    

    #list, range # this is somehow doesnt work properly
    #print('list and range')
    #rng1 = range(5)
    #print(rng1)
    #list5 = list(rng1)
    #print('end of the list and range')

    print('print(sum(range(4)))')
    print(sum(range(4))) # 0 + 1 + 2 + 3



# side quest
def simpleFib():

    print("simple Fib test here : ")

    a, b = 0, 1 # something like a Ruby lang
    while a < 10:
        print(a)
        a, b = b, (a + b)


def interestingExample(num, l = []):
    print('interesting exmaple')
    #
    l.append(num)
    print(l)
    return l





list()

#side quest call
simpleFib()

l = [17]
# 17 will be lost - always overwriting
l = interestingExample(1)
l = interestingExample(2)
l = interestingExample(1)

print('list list ', l)


def moreOnLists():
    l = [2,5,7]
    l.append(1)
    l.insert(1,23)
    l.remove(5)
    l.extend([3,3])

    print('more on lists ', l)

moreOnLists()



def sq():

    print('list 1 -> ')
    a = []
    for x in range(20):
        a.append(x**2)
    print(a)

    print('list 2 ->')
    a = []
    #a = list((1)) this is not wokring list ...
    #a = list(map(lambda x: x**2, range(10)))
    result1 = map( lambda x: x**2 , range(10))
    print(result1, result1.__doc__)
    print(dir(result1))
    print( 'result1.__eq__.__doc__ ->' )
    print( result1.__eq__.__doc__ )
    print( 'result1.__iter__.__doc__ ->' )
    print( result1.__iter__.__doc__ )


    # nice one here
    listlist = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    # this below is the same but i really like this one above
    #combs = []
    #for x in [1,2,3]:
    #   for y in [3,1,4]:
    #       if x != y:
    #        combs.append((x, y))
    #
    #combs
    #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    print('list list ')
    print( listlist )


    nextTestList = [-4, -2, 0, 2, 5, 7]
    output1 = [x * 2 for x in nextTestList]
    print('output1 from [x * 2 for x in nextTestList]')
    print(output1)

    output2 = [abs(x) for x in output1]
    print('output2 = abs(x) for x in output1')
    print(output2)

sq()