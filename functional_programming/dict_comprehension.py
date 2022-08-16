"""
Like List Comprehension, Python allows dictionary comprehensions.
 We can create dictionaries using simple expressions.
A dictionary comprehension takes the form 
{key: value for (key, value) in iterable}
"""
simple_dict = {
    'a':1,
    'b':2,
    'c':3
}

my_dict = {k:v**4 for k, v in simple_dict.items()}

my_dict2 = {k:v**4 for k, v in simple_dict.items()
            if v%2 ==0}

my_dict3 = {num:num**4 for num in [1,2,3]}

print(my_dict)
print(my_dict2)
print(my_dict3)
