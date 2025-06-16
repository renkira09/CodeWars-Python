"""
    ## Reversed Strings - 8 Kyu ##
    Complete the solution so that it reverses the string passed into it.

    'world'  =>  'dlrow'
    'word'   =>  'drow'
"""

def solution(string):
    # Case 1
    a = [i for i in string]
    a.reverse()
    a = ''.join(a)
    print(a)
    # return a

    # Case 2
    # a = ""
    # for i in string:
    #     a = ''.join(i+a)
    # print(a)
    # return a

    # Solution
    # return str[::-1]


solution("world")
solution("word")