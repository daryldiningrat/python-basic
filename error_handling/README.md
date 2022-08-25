# __Error Handling__

## __Try and Except Statement – Catching Exceptions__

Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.

__Example:__ Let us try to access the array element whose index is out of bound and handle the corresponding exception.

```python
# Python program to handle simple runtime error
#Python 3
  
a = [1, 2, 3]
try: 
    print ("Second element = %d" %(a[1]))
  
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
  
except:
    print ("An error occurred")
```

__Output :__
```
Second element = 2
An error occurred
```

In the above example, the statements that can cause the error are placed inside the try statement (second print statement in our case). The second print statement tries to access the fourth element of the list which is not there and this throws an exception. This exception is then caught by the except statement.

## __Catching Specific Exception__

A try statement can have more than one except clause, to specify handlers for different exceptions. Please note that at most one handler will be executed. For example, we can add IndexError in the above code. The general syntax for adding specific exceptions are – 

```python
try:
    # statement(s)
except IndexError:
    # statement(s)
except ValueError:
    # statement(s)
```

__Example:__ Catching specific exception in Python

```python
# Program to handle multiple errors with one
# except statement
# Python 3
  
def fun(a):
    if a < 4:
  
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
  
    # throws NameError if a >= 4
    print("Value of b = ", b)
      
try:
    fun(3)
    fun(5)
  
# note that braces () are necessary here for 
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
```
__output :__

```
ZeroDivisionError Occurred and Handled
```

If you comment on the line fun(3), the output will be 
```
NameError Occurred and Handled
```

The output above is so because as soon as python tries to access the value of b, NameError occurs. 

## __Try with Else Clause__

In python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

__Example:__ Try with else clause

```python

# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
  
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
```
__Output :__

```
-5.0
a/b result in 0 
```

## __Finally Keyword in Python__

Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after normal termination of try block or after try block terminates due to some exception

__Syntax:__

```python
try:
    # Some Code.... 

except:
    # optional block
    # Handling of exception (if required)

else:
    # execute if no exception

finally:
    # Some code .....(always executed)
```

__Example :__
```python
# Python program to demonstrate finally
  
# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)
  
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
  
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
```

__Output :__
```
Can't divide by zero
This is always executed
```

## __Raising Exception__

The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception).

```python

# Program to depict Raising Exception
  
try: 
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not
```
The output of the above code will simply line printed as “An exception” but a Runtime error will also occur in the last due to the raise statement in the last line. So, the output on your command line will look like 

```
Traceback (most recent call last):
  File "/home/d6ec14ca595b97bff8d8034bbf212a9f.py", line 5, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there
```