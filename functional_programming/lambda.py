from functools import reduce

"""
Python Lambda Functions are anonymous function means that 
the function is without a name. As we already know that the def 
keyword is used to define a normal function in Python. 
Similarly, the lambda keyword is used to define an anonymous function in Python. 

syntax : lambda arguments: expression
"""
my_list = [1,2,3]

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))