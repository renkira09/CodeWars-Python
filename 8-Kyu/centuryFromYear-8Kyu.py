import math

def century(year):
    # Finish this :)
    century = math.ceil(year/100)
    print(century)
    return century

# other solution
def century2(year):
    print((year + 99) // 100)
    return (year + 99) // 100

century(1705) # Expected: 18
century2(1705) # Expected: 18
century(1900) # Expected: 19
century2(1900) # Expected: 19
century(1601) # Expected: 17
century2(1601) # Expected: 17
century(2000) # Expected: 20
century2(2000) # Expected: 20
century(2742) # Expected: 28
century2(2742) # Expected: 28
