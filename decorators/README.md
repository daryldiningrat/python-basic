# __Decorators__

Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.

> First Class Objects
In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.

Properties of first class functions:

- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures such as hash tables, lists, and so on

Consider the below examples for better understanding.

__Example :__

What if a function returns something or an argument is passed to the function?

In all the above examples the functions didn’t return anything so there wasn’t an issue, but one may need the returned value.

```python
def hello_decorator(func):
	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))
```

__Output :__

```
before Execution
Inside the function
after Execution
Sum = 3
```

In the above example, you may notice a keen difference in the parameters of the inner function. The inner function takes the argument as *args and **kwargs which means that a tuple of positional arguments or a dictionary of keyword arguments can be passed of any length. This makes it a general decorator that can decorate a function having any number of arguments.