# What Is Functional Programming?

A pure function is a function whose output value follows solely from its input values, without any observable side effects. In functional programming, a program consists entirely of evaluation of pure functions. Computation proceeds by nested or composed function calls, without changes to state or mutable data.

The functional paradigm is popular because it offers several advantages over other programming paradigms. Functional code is:


- High level: You’re describing the result you want rather than explicitly specifying the steps required to get there. Single statements tend to be concise but pack a lot of punch.

- Transparent: The behavior of a pure function depends only on its inputs and outputs, without intermediary values. That eliminates the possibility of side effects, which facilitates debugging.

- Parallelizable: Routines that don’t cause side effects can more easily run in parallel with one another.

## Advantages of pure functions

- Clear and Understandable
- Easy to Extend
- Easy to Maintain
- Memory Efficient
- DRY Code

## __Map__

`map()` function returns a map object(which is an iterator) 
 of the results after applying the given function to each 
 item of a given iterable (list, tuple etc.)

 __Syntax :__

 `map(func, iter)`

 __Parameters :__

 - func : It is a function to which map passes each element of given iterable.
 - iter : It is a iterable which is to be mapped.
 
 __NOTE__ : You can pass one or more iterable to the map() function.

 __Example :__

  
```python
# Python program to demonstrate working
# of map.
# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
```

__Output :__

```
[5, 7, 9]
```


## __Filter__

The `filter()` method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

__syntax :__

`filter(function, sequence)`

__Parameters:__

- function: function that tests if each element of a 
sequence true or not.
- sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.
- Returns:
returns an iterator that is already filtered. 

__Example :__

```python
# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
  
  
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
  
# using filter function
filtered = filter(fun, sequence)
  
print('The filtered letters are:')
for s in filtered:
    print(s)
```

__Output :__

```
The filtered letters are:
e
e
```

## __Zip__

Python `zip()` method takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 

It is used to map the similar index of multiple containers so that they can be used just using a single entity. 

__Syntax :__

`zip(*iterators)` 

__Parameters :__
 Python iterables or containers ( list, string etc ) 

__Return Value :__
 Returns a single iterator object, having mapped values from all the 
containers.

__Example :__

```python

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)
 
print(set(mapped))
```

__Output :__

```
{('Shambhavi', 3), ('Nikhil', 1), ('Astha', 2), ('Manjeet', 4)}
```

## __Reduce__

The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

__Working :__  

- At first step, first two elements of sequence are picked and the result is obtained.
- Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
- This process continues till no more elements are left in the container.
- The final returned result is returned and printed on console.

__Example :__

```python

# python code to demonstrate working of reduce()
 
# importing functools for reduce()
import functools
 
# initializing list
lis = [1, 3, 5, 6, 2, ]
 
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
```

__Output :__

```
The sum of the list elements is : 17
The maximum element of the list is : 6
```

## __Lambda__

Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 

__Python Lambda Function__

__Syntax :__

`lambda arguments: expression`

- This function can have any number of arguments but only one expression, which is evaluated and returned.
- One is free to use lambda functions wherever function objects are required.
- You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
- It has various uses in particular fields of programming besides other types of expressions in functions.

__Example :__ Lambda Function Example

Difference Between Lambda functions and def defined function are as follows: 

Let’s look at this example and try to understand the difference between a normal def defined function and lambda function. This is a program that returns the cube of a given value:  

```python

# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y
 
# using the normally
# defined function
print(cube(5))
 
# using the lambda function
print(lambda_cube(5))
```

__Output :__

```
125
125
```

As we can see in the above example both the cube() function and lambda_cube() function behave the same and as intended. Let’s analyze the above example a bit more:

- Without using Lambda: Here, both of them return the cube of a given number. But, while using def, we needed to define a function with a name cube and needed to pass a value to it. After execution, we also needed to return the result from where the function was called using the return keyword.
- Using Lambda: Lambda definition does not include a “return” statement, it always contains an expression that is returned. We can also put a lambda definition anywhere a function is expected, and we don’t have to assign it to a variable at all. This is the simplicity of lambda functions.