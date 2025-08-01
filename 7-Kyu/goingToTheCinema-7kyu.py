"""
    ## Going to the Cinema - 7 Kyu ##
    My friend John likes to go to the cinema. He can choose between system A and system B.

    System A : he buys a ticket (15 dollars) every time
    System B : he buys a card (500 dollars) and a first ticket for 0.90 times the ticket price, 
    then for each additional ticket he pays 0.90 times the price paid for the previous ticket.
    Example:
    If John goes to the cinema 3 times:

    System A : 15 * 3 = 45
    System B : 500 + 15 * 0.90 + (15 * 0.90) * 0.90 + (15 * 0.90 * 0.90) * 0.90 ( = 536.5849999999999, no rounding for each ticket)
    John wants to know how many times he must go to the cinema so that the final result of System B, when rounded up to the next dollar, will be cheaper than System A.

    The function movie has 3 parameters: 
    card (price of the card), ticket (normal price of a ticket), perc (fraction of what he paid for the previous ticket) 
    and returns the first n such that ceil(price of System B) < price of System A.
    More examples:
    movie(500, 15, 0.9) should return 43 
        (with card the total price is 634, with tickets 645)
    movie(100, 10, 0.95) should return 24 
        (with card the total price is 235, with tickets 240)
"""


import math


def movie(card, ticket, perc):
    # your code
    # Case 1
    # a = ticket
    # b1 = ticket * perc
    # b2 = card + b1
    # x = 1
    # while True:
    #     b1 = b1 * perc
    #     b2 = b2 + b1
    #     a = a + ticket
    #     x += 1
    #     if math.ceil(b2) < a:
    #         break
    # return x

    # Case 1
    a = ticket
    b1 = ticket * perc
    b2 = card + b1
    x = 1
    while True:
        b1 = b1 * perc
        b2 = b2 + b1
        a = a + ticket
        x += 1
        if math.ceil(b2) < a:
            break
    return x

    # Solution
    # while card + ticket*perc*(1-perc**n)/(1-perc) - ticket*n > -1: 
    #     n += 1
    # return n

# Solution 2
# from itertools import takewhile, count, accumulate
# def movie(card, ticket, perc):
#     sys_b = accumulate(ticket*perc**n for n in count(1))
#     sys_a = accumulate(ticket for m in count(1))
#     return sum(1 for a in takewhile(lambda x: round(x[0] + card + 0.49) >= x[1], zip(sys_b, sys_a))) + 1


# print(movie(500, 15, 0.9))
print(movie(100, 10, 0.95))