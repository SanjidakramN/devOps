def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
    
def HigherOrderFunction(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
   
res = HigherOrderFunction('absolute')
res = HigherOrderFunction('cube')
res = HigherOrderFunction('square')
print(res(-5))
   