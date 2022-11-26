class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(p):
    if p.x == 0 and p.y == 0:
        print(f' point x= ={p.x} , y= ={p.y}')
    elif p.x == 2 and p.y == 1:
        print(f'point x= {p.x} , y= {p.y} .  2121')
        #print('test2')
    elif p.x > 10 and p.y > 10:
        print(f'point with big numbers x= {p.x} , y= {p.y}')
    else:
        print('not a point or not defined Point ', p)


where_is( Point(0, 0) )
where_is( Point(2, 1) )
where_is( Point(3, 3) )
where_is( Point(30, 13) )