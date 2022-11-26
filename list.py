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


list()

#side quest call
simpleFib()