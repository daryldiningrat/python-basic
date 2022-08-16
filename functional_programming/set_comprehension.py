# list, set and dictionary
from loguru import logger

"""
sets only allow numbers that not duplicate.
only unique items
"""

my_list = {char for char in 'hello'}
my_list3 = {num**2 for num in range(0,50)}
my_list4 = {num**2 for num in range(0,50)
            if num % 2 == 0}




print(my_list)
logger.info("----------------Expression for each item------------------")
print(my_list3)
logger.info("----------------Expression for each item and add an option to get Even number------------------")
print(my_list4)