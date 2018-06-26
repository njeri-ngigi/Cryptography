input1 = int(input("Enter number: "))
input2 = int(input("Enter exponential: "))
input3 = int(input("Enter modulus: "))

def mod_exp(a,b,c):
    d = pow(a, b) % c
    print(d)
    return d

def mod_exp2(a,b,c):
    d = pow(a,b,c)
    print(d)
    return d

def mod_exp3(a,b,p):
    result = 1 #Initialze result
    a = a % p
    while (b>0):
        #if b is odd
        if ((b&1) == 1):
            result = (result*a) % p
        
        #if b is even 
        b = b >> 1
        a = (a*a) % p
    print(result)
    return result

mod_exp(input1, input2, input3)
mod_exp2(input1, input2, input3)
mod_exp3(input1, input2, input3)
