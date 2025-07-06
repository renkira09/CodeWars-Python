"""
    ## Friend or Foe - 7 Kyu ##
    friends name in it.

    If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, 
    you can be sure he's not...

    Input = ["Ryan", "Kieran", "Jason", "Yous"]
    Output = ["Ryan", "Yous"]

    Input = ["Peter", "Stephen", "Joe"]
    Output = []
    Input strings will only contain letters.
    Note: keep the original order of the names in the output.
"""

def friend(x):
    #Code
    # Case 1
    # r = []
    # for s in x:
    #     if len(s) == 4:
    #         r.append(s)
    # return r

    # Case 2
    return [s for s in x if s.isalpha() and len(s) == 4]

    # Solution
    # return [f for f in x if len(f) == 4]

print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
print(friend(["Peter", "Stephen", "Joe"]))
print(friend(["Peter", "Stephen", "Joe3"]))