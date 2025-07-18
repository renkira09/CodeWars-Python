"""
    ## Beginner Series #1 School Paperwork - 8 Kyu ##
    Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
    Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

    Example:
    n= 5, m=5: 25
    n=-5, m=5:  0
    Waiting for translations and Feedback! Thanks!
"""

def paperwork(n, m):
    # Happy Coding! ^_^
    # Case 1
    # if n < 0:
    #     return 0
    # elif m < 0:
    #     return 0
    # else:
    #     return m*n

    # Case 2
    # return 0 if n<0 else (0 if m<0 else m*n)

    # Case 3
    return m*n if n>=0 and m>=0 else 0

    # Solution
    # return n * m if n > 0 and m > 0 else 0
    
print(paperwork(5, 5))
print(paperwork(-5, 5))
print(paperwork(5, -5))
    