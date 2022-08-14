
my_list = [1,2,3]
def multiply_by2(item):
    """
    map() function returns a map object(which is an iterator) 
    of the results after applying the given function to each 
    item of a given iterable (list, tuple etc.)

    map(func, iter)

    Parameters :
    fun : It is a function to which map passes each element of given iterable.
    iter : It is a iterable which is to be mapped.

    NOTE : You can pass one or more iterable to the map() function.
    """
    return item*2

print(list(map(multiply_by2, my_list)))