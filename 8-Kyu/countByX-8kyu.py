"""
    ## Count by X - 8 Kyu ##
    Create a function with two arguments that will return an array of the first n multiples of x.
    Assume both the given number and the number of times to count will be positive numbers greater than 0.
    Return the results as an array or list ( depending on language ).

    Examples --> output
    x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
    x = 2, n = 5  --> [2,4,6,8,10]
"""

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    # Case
    array = []
    a = 0
    while n:
        a += 1
        if a % x == 0:
            array.append(a)
        if n == len(array):
            break
    # print(array)
    return array

    # Solution
    # return [i * x for i in range(1, n + 1)]

    # Solution 2
    # arr = []
    # for num in range(1, n+1):
    #     result = x * num
    #     arr.append(result)
    # return arr



count_by(1,10)
count_by(2,5)
