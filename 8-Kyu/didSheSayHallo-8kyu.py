"""
    ## Did she say hallo? - 8 Kyu ##
    You received a whatsup message from an unknown number. 
    Could it be from that girl/boy with a foreign accent you met yesterday evening?
    Write a simple function to check if the string contains the word hallo in different languages.

    These are the languages of the possible people you met the night before:
    hello - english
    ciao - italian
    salut - french
    hallo - german
    hola - spanish
    ahoj - czech republic
    czesc - polish
    
    Notes
    you can assume the input is a string.
    to keep this a beginner exercise you don't need to check if the greeting is a subset of word (Hallowen can pass the test)
    function should be case insensitive to pass the tests
"""

def validate_hello(greetings):
    #your code here
    # Case 1
    # if "hello" in greetings.lower():
    #     # print(True)
    #     return True
    # elif "ciao" in greetings.lower():
    #     # print(True)
    #     return True
    # elif "salut" in greetings.lower():
    #     # print(True)
    #     return True
    # elif "hallo" in greetings.lower():
    #     # print(True)
    #     return True
    # elif "hola" in greetings.lower():
    #     # print(True)
    #     return True
    # elif "ahoj" in greetings.lower():
    #     # print(True)
    #     return True
    # elif "czesc" in greetings.lower():
    #     # print(True)
    #     return True
    # else:
    #     # print(False)
    #     return False

    # Case 2
    # if "hello" in greetings.lower() or "ciao" in greetings.lower() or "salut" in greetings.lower() or "hallo" in greetings.lower() or "hola" in greetings.lower() or "ahoj" in greetings.lower() or "czesc" in greetings.lower():
    #     # print(True)
    #     return True
    # else:
    #     # print(False)
    #     return False

    # Case 3
    greetings = greetings.lower()
    if "hello" in greetings or "ciao" in greetings or "salut" in greetings or "hallo" in greetings or "hola" in greetings or "ahoj" in greetings or "czesc" in greetings:
        # print(True)
        return True
    else:
        # print(False)
        return False
    
    # Solution
    # return any(x in greetings.lower() for x in ['hello','ciao','salut','hallo','hola','ahoj','czesc'])

    # Solution 2
    # g = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    # for s in g:
    #     if s in greetings.lower():
    #         return True
    # return False

# Solution 3
# from re import compile, search, I

# REGEX = compile(r'hello|ciao|salut|hallo|hola|ahoj|czesc', I)


# def validate_hello(greeting):
#     return bool(search(REGEX, greeting))

greeting = input("Send Message: ")
validate_hello(greeting)