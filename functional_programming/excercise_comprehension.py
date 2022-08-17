from cmath import e


some_list = ['a', 'b', 'c', 'd', 'e', 'c', 
                'a', 'y', 'w', 'h', 'w', 'z']


# Traditional Way
duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)


# Comprehension Way
"""
using sets comprehensiun in order to get unique values
and turn them to list
"""

duplicates_list = list({value for value in some_list
                    if some_list.count(value) > 1})

print(duplicates_list)