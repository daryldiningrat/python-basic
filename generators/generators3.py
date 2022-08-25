import re


def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(1000):
    print(x)


#def fib_list(number):
#    a = 0
#    b = 1
#    result = []
#    for i in range(number):
#        result.append(a)
#        temp = a
#        a = b
#        b = temp + b
#    return result
#
#print(fib_list(100000))