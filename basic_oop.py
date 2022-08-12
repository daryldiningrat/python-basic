from pydoc import plain

# This is a constructor
class PlayerCharater:
    
    # Class Object Attribute
    membership = True

    # This is a method
    def __init__(self, name, age):
        """
        __init__ is a magic method or dunder method that has attribute
        self: the self is used to represent the instance of the class.
              with this keyword, you can access the attributes and
              methods of the class in python. it binds the attributes
              with the given arguments. The reason why we use self that
              python does not use the '@' syntax to refer to instance attributes
        name: -> str 
        age: -> int
        """
        if self.membership:
            self.name = name # Attribute
            self.age = age # Attribute
    
    def run(self):

        return 'run'
    
    def shout(self):
        print(f'my name is {self.name} and my age is {self.age}')

        return None
    
    @classmethod
    def adding_things(cls, num1, num2):
        """
        - Declares a method.
        - The first parameter must be cls, which can be used to access class attributes.
        - it can access class attributes, but not the instance attributes.
        - it can be called using the ClassName.MethodName() or object.MethodName().
        - it can be used to declare a factory method that returns objects of the class.
        """
        return cls('Buriza', num1 + num2)


# Save class as an object
player1 = PlayerCharater('Daryl', 25) # instance an object
player2 = PlayerCharater('Diningrat', 25) # instance an object
player3 = PlayerCharater.adding_things(5,10)


# You can access method in class
print(player1.membership)
print(player1.run())
print(player1.name)
print(player2.name)

print(player1.shout())

print(player1.adding_things(5,5))

print(player3.age)