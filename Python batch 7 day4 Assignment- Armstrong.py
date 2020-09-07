# Print the first Armstrong number in the range of 1042000 to 702648265
# and exit the loop as soon as you encounter the first Armstrong number

#num = input("Enter the number")

for num in range(1042000,702648265):
    num = str(num)
    order = len(num)
    num = int(num)
    sum = 0
    temp = num
    while(temp>0):
        digit = temp%10
        sum = sum+digit ** order
        temp = temp//10
    if num == sum:
        print(num, "is an Armstrong number")
        break;
    else:
        print(num, "is not an Armstrong number")


