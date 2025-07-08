"""
    ## How Many Times Should I Go? - 7 Kyu ##
    Lot of museum allow you to be a member, for a certain amount amount_by_year you can have unlimitted acces to the museum.

    In this kata you should complete a function in order to know after how many visit it will be better to take an annual pass. 
    The function take 2 arguments annual_price and individual_price.
"""

def how_many_times(annual_price, individual_price):
    # code here
    # Case 1
    # x = annual_price/individual_price+0.4
    # return round(x)

    # Case 2
    return round(annual_price/individual_price+0.49)

# Solution
# from math import ceil
# def how_many_times(ap, ip):
#     return ceil(ap/ip)

print(how_many_times(40, 15))
print(how_many_times(30, 10))
print(how_many_times(80, 15))
print(how_many_times(143, 132))