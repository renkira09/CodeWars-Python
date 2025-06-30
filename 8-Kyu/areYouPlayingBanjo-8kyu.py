"""
    ## Are You Playing Banjo? - 8 Kyu ##
    Create a function which answers the question "Are you playing banjo?".
    If your name starts with the letter "R" or lower case "r", you are playing banjo!

    The function takes a name as its only argument, and returns one of the following strings:
    name + " plays banjo" 
    name + " does not play banjo"

    Names given are always valid strings.
"""

def are_you_playing_banjo(name):
    # Implement me!
    # Case 1
    # if name[0].lower() == "r":
    #     print("OKe")
    # else:
    #     print("Zannen:P")
    
    # Case 2
    # if name.lower().startswith('r'):
    #     print("Yeay!")
    # else:
    #     print("Arara:)")

    # Case 3
    oke = f"{name} plays banjo" if name[0].lower() == "r" else f"{name} does not play banjo"
    print(oke)
    return f"{name} plays banjo" if name[0].lower() == "r" else f"{name} does not play banjo"

    # Solution
    # if name[0].lower() == 'r':
    #     return name + ' plays banjo'
    # else:
    #     return name + ' does not play banjo'

    # Solution 2
    # return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";

are_you_playing_banjo("Renkira")
are_you_playing_banjo("renkira")
are_you_playing_banjo("Akira")
are_you_playing_banjo("akira")
are_you_playing_banjo("Fid")
are_you_playing_banjo("Nur")