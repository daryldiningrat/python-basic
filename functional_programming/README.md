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

## Map

`map()` function returns a map object(which is an iterator) 
 of the results after applying the given function to each 
 item of a given iterable (list, tuple etc.)

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