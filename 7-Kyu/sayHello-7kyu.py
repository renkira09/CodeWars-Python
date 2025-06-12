"""
    ## Say Hello! - 7 Kyu ##
    Say hello!
    Write a function to greet a person. Function will take name as input and greet the person by saying hello. 
    Return null/nil/None if input is empty string or null/nil/None.

    Example:
    greet("Niks") == "hello Niks!"
    greet("")    == None # Return None if input is empty string
    greet(None)  == None # Return None if input is None
"""

def greet(name):
    # your code here
    if name != '' and name is not None:
        return f"hello {name}!"
    else:
        return None
    
    # Solution
    # return f"hello {name}!" if name else None

greet(input("Your Name: "))