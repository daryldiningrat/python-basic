from functools import reduce

my_list = [1,2,3]

def accumulator(acc, item):
    """
    The reduce(fun,seq) function is used to 
    apply a particular function passed in its argument 
    to all of the list elements mentioned in 
    the sequence passed along.
    This function is defined in “functools” module.
    """
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 10))