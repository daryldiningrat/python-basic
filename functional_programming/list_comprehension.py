# list, set and dictionary
from loguru import logger
# Using this list comprehension
my_list = [char for char in 'hello']

# instead of this
my_list2 = []

for char in 'hello':
    my_list2.append(char)

#
my_list3 = [num**2 for num in range(0,50)]
my_list4 = [num**2 for num in range(0,50)
            if num % 2 == 0]




print(my_list)
print(my_list2)
logger.info("----------------Expression for each item------------------")
print(my_list3)
logger.info("----------------Expression for each item and add an option to get Even number------------------")
print(my_list4)