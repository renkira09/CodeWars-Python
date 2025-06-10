def digitize(n):
    # return [int(i) for i in str(n)][::-1]
    print([int(i) for i in str(n)][::-1])

def digitize2(n):
    result = []
    while n >= 1:
        print("result => ",result)
        print("before -> ",n)
        result.append(n%10)
        n //= 10
        print("after -> ",n)
    # return result
    print(result)

digitize(987654321)
digitize2(987654321)