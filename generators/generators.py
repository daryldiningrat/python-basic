def generator_function(num):
    """
    The yield statement suspends a function’s execution and 
    sends a value back to the caller, but retains enough state 
    to enable the function to resume where it left off. 
    When the function resumes, it continues execution immediately 
    after the last yield run. 
    This allows its code to produce a series of values over time, 
    rather than computing them at once and sending them back
    like a list.
    """
    for i in range(num):
        yield i*2

for item in generator_function(10000):
    print(item)
