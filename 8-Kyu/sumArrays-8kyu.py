"""
    ## Sum Arrays - 8 Kyu ##
    Write a function that takes an array of numbers and returns the sum of the numbers. 
    The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

    Examples
    Input: [1, 5.2, 4, 0, -1]
    Output: 9.2

    Input: []
    Output: 0

    Input: [-2.398]
    Output: -2.398

    Assumptions
    You can assume that you are only given numbers.
    You cannot assume the size of the array.
    You can assume that you do get an array and if the array is empty, return 0.

    What We're Testing
    We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
    Advanced users may find this extremely easy and can easily write this in one line.
"""

def sum_array(a):
    # Case 1 - basic
    # x = 0
    # for i in a:
    #     x += i
    # print(x)
    # return x

    # Case 2 - failed
    # x = []
    # b = [ x+a[i] for i in range(len(a)) ]
    # print(x)
    # return x

    # Case 3 - pro
    # x = sum(a)
    # print(x)
    # return x

    # Case 4
    x = 0
    n = len(a)
    while n > 0:
        n -= 1
        x += a[n]
    print("==>",x)
    # return x

    # Solution
    # return lambda a: sum(a)


sum_array([1, 5.2, 4, 0, -1])
sum_array([])
sum_array([-2.398])