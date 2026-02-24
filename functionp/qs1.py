# using func calc sum of any num of values
def sum(n) :
    ans = n + sum(n-1)
    if n==0 :
        return 0
    return ans
n = int(input("enter the number"))
print(sum(n))