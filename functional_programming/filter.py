my_list = [1,2,3]

def only_odd(item):
    """
    The filter() method filters the given sequence 
    with the help of a function that tests each 
    element in the sequence to be true or not.
    """
    return item % 2 != 0

print(list(filter(only_odd, my_list)))