# Object-Oriented Program

__What is object-oriented programming?__

Object-oriented programming (OOP) is a computer programming model that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.

OOP focuses on the objects that developers want to manipulate rather than the logic required to manipulate them. This approach to programming is well-suited for programs that are large, complex and actively updated or maintained. This includes programs for manufacturing and design, as well as mobile applications; for example, OOP can be used for manufacturing system simulation software.

The organization of an object-oriented program also makes the method beneficial to collaborative development, where projects are divided into groups. Additional benefits of OOP include code reusability, scalability and efficiency.

## __Inheritance__

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

__Example__

- Create a Parent Class

Any class can be a parent class, so the syntax is the same as creating any other class:

Create a class named Person, with firstname and lastname properties, and a printname method:

```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```

- Create a Child Class

To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

```python
class Student(Person):
  pass
```

Now the Student class has the same properties and methods as the Person class.

Use the Student class to create an object, and then execute the printname method:

```python
x = Student("Mike", "Olsen")
x.printname()
```

## __init__

 `__init__` is a magic method or dunder method that has attribute

## Self in python class

self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.

## @classmethod

In Python, the @classmethod decorator is used to declare a method in the class as a class method that can be called using `ClassName.MethodName()`. The class method can also be called using an object of the class.

The `@classmethod` is an alternative of the `classmethod()` function. It is recommended to use the `@classmethod` decorator instead of the function because it is just a syntactic sugar.

- Declares a method
- it can access class attributes, but not the instance attributes.
- it can be called using the `ClassName.MethodName()` or `object.MethodName()`
- it can be used to declare a factory method that returns objects of the class.

```python
class Student:
    name = 'unknown' # class attribute
    def __init__(self):
        self.age = 20  # instance attribute

    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=',cls.name)
```

Above, the Student class contains a class attribute name and an instance attribute age. The `tostring()` method is decorated with the `@classmethod` decorator that makes it a class method, which can be called using the Student.tostring(). Note that the first parameter of any class method must be cls that can be used to access the class's attributes. You can give any name to the first parameter instead of cls.


## @staticmethod

- Declares a static method
- it cannot access either class attributes or instance attributes.
- it can be called using the `ClassName.MethodName()` or `object.MethodName()`
- it cannot return an object of the class

