numbarr = [2,3,6,8]

def plus():
    value = 0
    for n in numbarr:
        value += n
    print(value)
    if value % 2 == 0:
        print('This number is even')
    else:
        print('This number is odd')
    

plus()