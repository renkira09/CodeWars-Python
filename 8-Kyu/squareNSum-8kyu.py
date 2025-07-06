"""
    ## Square (n) Sum - 8 Kyu ##
    Complete the square sum function so that it squares each number passed into it and then sums the results together.

    For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""

def square_sum(numbers):
    #your code here
    # Case 1
    # x = 0
    # for no in numbers:
    #     x += no**2
    # return x

    # Case 2
    return sum(n**2 for n in numbers)

    # Solution
    # return sum(x * x for x in numbers) 


print(square_sum([1, 2, 2]))
print(square_sum([3, 3, 3]))