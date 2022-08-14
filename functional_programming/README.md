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