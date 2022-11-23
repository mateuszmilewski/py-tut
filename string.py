# testing the string

def charsTest():
    py = 'Python'

    print(py)
    print(py[0])
    print(py[-1])
    # second from last
    print(py[-2])
    # from 2 to 5
    print(py[2:5])
    # character from the beginning to position 2 (excluded)
    print(py[:2])
    # so now interesting 
    print(py[:2] + py[2:]) # will give us Python


    # note
    # Python strings cannot be changed — they are immutable. 
    # Therefore, assigning to an indexed position in the string results in an error

    # so if we want to change it then you need to create a new one
    jy = 'J' + py[1:]
    print(jy)


    # length of the string
    print(len(py))
    print(len(jy))




def sideQuest(foo):
    foo()



# to run any function - you need to add () 
# this is just additional check for me how passing functions are friendly...
sideQuest(charsTest)