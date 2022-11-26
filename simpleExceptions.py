try:
    x = 10
except ValueError:
    print('we have exception')

try:
    raise Exception('text1', 'text2')
except Exception as inst:
    print(inst)
    print(type(inst))
    