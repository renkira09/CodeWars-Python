"""
    ## Hello, Name or World! - 8 Kyu ##
    Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given 
    (or passed as an empty String).
    Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

    Examples:
    * With `name` = "john"  => return "Hello, John!"
    * With `name` = "aliCE" => return "Hello, Alice!"
    * With `name` not given 
    or `name` = ""        => return "Hello, World!"
"""

def hello(name=""):
    # Case 1
    # if name:
    #     return f"Hello, {name}!"
    # else:
    #     return "Hello, World!"
    
    # Case 2
    return f"Hello, {name.capitalize()}!" if name else "Hello, World!"

    # Solution
    # return f"Hello, {name.title() or 'World'}!"

print(hello("Kira"))
print(hello("renkira"))
print(hello(""))
print(hello())