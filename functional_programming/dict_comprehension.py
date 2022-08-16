"""
Like List Comprehension, Python allows dictionary comprehensions.
 We can create dictionaries using simple expressions.
A dictionary comprehension takes the form 
{key: value for (key, value) in iterable}
"""
simple_dict = {
    'a':1,
    'b':2
}

my_dict = {key:value**2 for key, value in simple_dict.items()}

print(my_dict)