"""
    ## Training Time - 7 Kyu ##
    Task
    Create a function shuffleIt. The function accepts two or more parameters. The first parameter arr is an array of numbers, followed by an arbitrary number of numeric arrays. Each numeric array contains two numbers, which are indices for elements in arr (the numbers will always be within bounds). For every such array, swap the elements. Try to use all your new skills: arrow functions, the spread operator, destructuring, and rest parameters.

    Example:

    shuffleIt([1,2,3,4,5],[1,2]) should return [1,3,2,4,5]
    shuffleIt([1,2,3,4,5],[1,2],[3,4]) should return [1,3,2,5,4]
    shuffleIt([1,2,3,4,5],[1,2],[3,4],[2,3]) should return [1,3,5,2,4]
"""
def shuffle_it(arr, *args):
    #your code here
    print("-"*15)

    # # Case 2
    # for arg in args:
    #     dump = []
    #     for a in arg[::-1]:
    #         dump.append(arr[a])
    #         arr.pop(a)
    #     x,y = dump
    #     arr.insert(arg[0], x)
    #     arr.insert(arg[1], y)

    # Case 3
    for arg in args:
        dump = [arr[a] for a in arg[::-1]]
        x,y = arg
        arr[x] = dump[0]
        arr[y] = dump[1]

    return arr

    # Solution
    # for x,y in T:
    #     A[x],A[y]=A[y],A[x]
    # return A


print(shuffle_it([1,2,3,4,5],[1,2]))
print(shuffle_it([1,2,3,4,5],[1,2],[3,4]))
print(shuffle_it([1,2,3,4,5],[1,2],[3,4],[2,3]))
print(shuffle_it([1,2,3,4,5],[1,2],[3,4],[2,3],[4,4]))

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    # print(arguments)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# cheeseshop("Limburger", 
#            "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")