# Make a function for prime numbers and use filter to filter out all the prime numbers from 1- 2500
def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

fltrObj=filter(isPrime, range(1,2501))
print ('Prime numbers between 1-2500:',list(fltrObj))