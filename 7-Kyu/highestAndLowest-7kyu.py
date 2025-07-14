"""
    ## Highest and Lowest - 7 Kyu ##
    In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

    Examples
    high_and_low("1 2 3 4 5") # return "5 1"
    high_and_low("1 2 -3 4 5") # return "5 -3"
    high_and_low("1 9 3 4 -5") # return "9 -5"

    Notes
    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first.
"""

def high_and_low(numbers):
    # ...
    # Case 1
    numbers = [int(i) for i in numbers.split()]
    numbers = str(max(numbers)) + " " + str(min(numbers))
    return numbers

    # Solution
    # nn = [int(s) for s in numbers.split(" ")]
    # return "%i %i" % (max(nn),min(nn))

    # Solution 2
    # numlist = numbers.split(" ")
    # i = 0
    # highest = int(numlist[0])
    # lowest = int(numlist[0])
    # while i < len(numlist):
    #     numlist[i] = int(numlist[i])
    #     if numlist[i] > highest:
    #         highest = numlist[i]
    #     if numlist[i] < lowest:
    #         lowest = numlist[i]
    #     i += 1
    # highest = str(highest)
    # lowest = str(lowest)
    # return  highest+" "+lowest

# high_and_low("1 2 3 4 5")
print(high_and_low("1 2 3 4 5"))
print(high_and_low("1 2 -3 4 5"))
print(high_and_low("1 9 3 4 -5"))
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))