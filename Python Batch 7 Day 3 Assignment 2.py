# Using for loop print all the prime numbers between 1 to 200 using FOR loop and RANGE function
for i in range(1,201):
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)