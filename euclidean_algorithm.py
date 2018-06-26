input1 = int(input("enter 2 numbers: \n"))
input2 = int(input())
input3 = int(input())
input4 = int(input())

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a, a)

def egcd(a,b):
    x,y,u,v = 0,1,1,0
    while a!=0:
        q,r = b // a, b%a
        m,n = x-u*q, y-v*q
        b,a,x,y,u,v=a,r,u,v,m,n
    my_gcd = b
    return my_gcd

def egcd2(a,b,x,y):
    if a == 0:
        x = 0
        y = 1
        return b
    x1 = 1
    y1 = 1# to store values of recursive call
    my_gcd = egcd2(b%a, a, x1, y1)

    #update x and y using results of recursive call
    x = y1 - (b/a) * x1
    y = x1
    return my_gcd

r = gcd(input1, input2)
print(r)

r2 = egcd(input1,input2)
print(r2)

r3 = egcd2(input1, input2, input3, input4)
print(r3)
