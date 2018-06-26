def sieve(limit):
    num_list = []
    prime_list = []
    for i in range(2, limit+1):
        if i not in num_list:
            if i%2 != 0:
                prime_list.append(i)
                for j in range(i*i, limit+1, i):
                    num_list.append(j)
    print(prime_list)

input1 = int(input("Enter a limit: \n"))
sieve(input1)
