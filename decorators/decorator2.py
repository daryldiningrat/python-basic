# Decorator

from loguru import logger


def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')
    return wrap_func

@my_decorator
def hello():
    print('Hello, World!')

@my_decorator
def bye():
    print('Bye, World!')

hello()
bye()

"""
 Also can be use like this
 remove `@my_decorator` if you prefer call decorator like below
"""

#hello2 = my_decorator(hello)
#bye2 = my_decorator(bye)

#hello2()
#bye2()