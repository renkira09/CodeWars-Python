"""
    ## Find Array - 7 Kyu ##
    You are given two arrays arr1 and arr2, where arr2 always contains integers.
    
    Write a function such that:
    For arr1 = ['a', 'a', 'a', 'a', 'a'], arr2 = [2, 4] the function returns ['a', 'a']
    For arr1 = [0, 1, 5, 2, 1, 8, 9, 1, 5], arr2 = [1, 4, 7] the function returns [1, 1, 1]
    For arr1 = [0, 3, 4], arr2 = [2, 6] the function returns [4]
    For arr1=["a","b","c","d"] , arr2=[2,2,2], the function returns ["c","c","c"]
    For arr1=["a","b","c","d"], arr2=[3,0,2] the function returns ["d","a","c"]

    Note that when an element inside arr2 is greater than the index of the last element 
    of arr1 no element of arr1 should be added to the resulting array. If either arr1 or 
    arr2 is empty, you should return an empty arr (empty list in python, empty vector in c++). 
    Note for c++ use std::vector arr1, arr2.
"""

def find_array(arr1, arr2):
    # Case 1
    # x = []
    # for i in arr2:
    #     if i > len(arr1)-1:
    #         continue
    #     x.append(arr1[i])
    # print(x)
    # return x

    # Case 2
    x = [arr1[i] for i in arr2 if i <= len(arr1)-1]
    print(x)
    # return [arr1[i] for i in arr2 if i <= len(arr1)-1]

    # Solution
    # return [ arr1[i] for i in arr2 if i< len(arr1) ]


find_array(['a', 'a', 'a', 'a', 'a'], [2, 4])
find_array([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7])
find_array([0, 3, 4], [2, 6])
find_array(["a","b","c","d"], [2,2,2])
find_array(["a","b","c","d"], [3,0,2])