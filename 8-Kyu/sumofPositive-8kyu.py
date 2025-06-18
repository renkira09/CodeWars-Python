"""
    ## Sum of Positive - 8 Kyu ##
    You get an array of numbers, return the sum of all of the positives ones.

    Example
    [1, -4, 7, 12] => 1 + 7 + 12 = 20
    
    Note
    If there is nothing to sum, the sum is default to 0.
"""

def positive_sum(arr):
    # Your code here
    # Case 1
    # a = 0
    # for i in arr:
    #     if i > 0:
    #         a+=i
    # print(a)
    
    # Case 2
    # a = 0
    # for i in arr:
    #     a += i if i > 0 else 0
    # print(a)

    # Case 3
    a = sum([i for i in arr if i > 0])
    print(a)
    # return sum([i for i in arr if i > 0])

    # Solution
    # return sum(x for x in arr if x > 0)

arr = [1, -4, 7, 12]
positive_sum(arr)