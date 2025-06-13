"""
    ## Triangular Treasure - 7 Kyu ##
    Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.

    1st (1)   2nd (3)    3rd (6)
    *          **        ***
                *         **
                          *
    You need to return the nth triangular number. You should return 0 for out of range values:

    For example: (Input --> Output)

    0 --> 0
    2 --> 3
    3 --> 6
    -10 --> 0
"""

# Gagal memahami soal
def triangular(n):
    ...
    # a = ['*' for x in range(n) for i in range(x) ]
    # print(a)

    # # Case 1
    # a = n
    # while n > 0:
    #     while a > 0:
    #         print(' * '*a)
    #         a -= 1
    #     break

    # Case 2
    # if n <= 0:
    #     return  0
    # n += 1
    # for x in range(n):
    #     n-=1
    #     print(' * '*n)

    # # Case 3
    # if n > 0:
    #     a = ['*'*n if n != n else n-1 for x in range(n)]
    #     print(a)
    #     # return ['*'*n, n-=1 for x in range(n)]
    # else:
    #     return 0

    # Case 4
    # if n > 0:
    #     return ['*'*(n-x) for x in range(n)]
    # else:
    #     return 0
    
    # Solution
    return n * (n + 1) // 2 if n > 0 else 0
    
    

triangular(0)
triangular(2)
triangular(3)
triangular(-10)