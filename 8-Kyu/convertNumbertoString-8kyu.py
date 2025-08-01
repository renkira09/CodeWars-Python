"""
    ## Convert a Number to a String - 8 Kyu ##
    We need a function that can transform a number (integer) into a string.

    What ways of achieving this do you know?

    Examples (input --> output):
    123  --> "123"
    999  --> "999"
    -100 --> "-100"
"""

def number_to_string(num):
    # Return a string of the number here!
    # Case 1
    # num = str(num)
    # return num

    # Case 2
    return f"{num}"

    # Case 3
    # return str(num)

print(number_to_string(123))
print(number_to_string(999))
print(number_to_string(-100))