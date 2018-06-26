input1 = int(input("enter 2 numbers: \n"))
input2 = int(input())

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a, a)

r = gcd(input1, input2)
print(r)