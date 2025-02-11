# def sum(a, b):
#     return a + b

# print(sum(1, 2))


# mysum = lambda a, b: a + b
# print(mysum(1, 2))

# print((lambda a,b: a+b) (1, 2))

# # Example of lambda function in another function
# def power(n):
#     return lambda a: a ** n

# print(power(2)(3))

def sum_num(a):
    return sum(a)

def HigherOrderFunction(f, lst):
    var = f(lst)
    return var

result = HigherOrderFunction(sum_num, [1, 2, 3, 4, 5])
print(result)

