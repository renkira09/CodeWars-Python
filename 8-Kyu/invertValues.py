"""
    ## Invert Values - 8 Kyu ##
    Given a set of numbers, return the additive inverse of each. 
    Each positive becomes negatives, and the negatives become positives.

    [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
    [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
    [] --> []
    You can assume that all values are integers. Do not mutate the input array.
"""

def invert(lst):
    arr = []
    for x in lst:
        a = -x if x > 0 else -1*x
        arr.append(a)
    return arr

    # Solution
    # return [-x for x in lst]

    # Solution
    # return list(map(lambda x: -x, lst))

invert([1, 2, 3, 4, 5])
invert([1, -2, 3, -4, 5])
invert([])