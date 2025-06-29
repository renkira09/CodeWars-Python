"""
    ## String Ends With - 7 Kyu ##
    Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

    Examples:
    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

def solution(text, ending):
    # your code here...
    # # Case 1
    # print("-"*10)
    # res = False
    # for x in range(len(ending)):
    #     if text[-(x+1)] == ending[-(x+1)]:
    #         res = True
    #     else:
    #         res = False
    # print(res)

    # # Case 2
    # text = [x if text[-(x+1)] == ending[-(x+1)] else None for x in range(len(ending))]
    # if text[0] != None:
    #     print(True)
    # else:
    #     print(False)

    # Case 3
    # for x in range(len(ending)):
    #     if ending[::-1][x] == text[::-1][x]:
    #         print(text[::-1])
    #     else:
    #         print("?"*5)
    
    # Case 4
    # [ print(True) if ending[::-1][x] == text[::-1][x] else print(False) for x in range(len(ending))]
    # [ print(False) for x in range(len(ending)) if ending[::-1][x] != text[::-1][x]]

    # Case 5
    for x in range(len(ending)):
        if x > len(text)-1:
            print(False)
            return False
        if ending[::-1][x] != text[::-1][x]:
            print(False)
            return False
    print(True)
    return True

    # Solution
    # return string.endswith(ending)

    # Solution 2
    # return ending in string[-len(ending):]

    # Solution 3
    # return string[-(len(ending))::] == ending
        


solution('abc', 'bc')
solution('abc', 'd')
solution("abc",     "abcd")
solution("ails", "fails")