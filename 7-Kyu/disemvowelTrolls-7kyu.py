"""
    ## Disemvowel Trolls - 7 Kyu ##
    Trolls are attacking your comment section!
    A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
    Your task is to write a function that takes a string and return a new string with all vowels removed.

    For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

    Note: for this kata y isn't considered a vowel.
"""

def disemvowel(s):
    for i in ["a","i","u","e","o","A","I","U","E","O"]:
        s = s.replace(i, "") if i in s else s
    return s

    # Solution
    # return "".join(c for c in string if c.lower() not in "aeiou")

    # Solution 2
    # for i in "aeiouAEIOU":
    #     s = s.replace(i,'')
    # return s

print(disemvowel("This website is for losers LOL!"))
# disemvowel("This website is for losers LOL!")