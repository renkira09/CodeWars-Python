"""
  ## Counting Sheep ... - 8 Kyu ##
  Consider an array/list of sheep where some sheep may be missing from their place. 
  We need a function that counts the number of sheep present in the array (true means present).

  For example,

  [True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True]
  The correct answer would be 17.

  Hint: Don't forget to check for bad values like null/undefined
"""

def count_sheeps(sheep):
  # TODO May the force be with you
  # Case 1
  # i = 0
  # for s in sheep:
  #   i = i+1 if s else i+0
  # return i

  # Case 2
  return sum([1 for s in sheep if s])

  # Solution
  # return sheep.count(True)

print(count_sheeps([True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True]))