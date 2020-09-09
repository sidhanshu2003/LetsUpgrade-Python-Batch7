# Write a program to identify sublist [1,1,5] is there in the given list in the same order, if yes
# print "It's a Match" if no then print "It's Gone" in function

lst = [1, 5, 6, 4, 1, 2, 3, 5]
sub_lst1 = [1, 1, 5]

print("List : " + str(lst))
print("Sublist1 : " + str(sub_lst1))

# using issubset() to check subset of list
flag = 0
if (set(sub_lst1).issubset(set(lst))):
    flag = 1

if (flag):
    print("It's a match")
else:
    print("It's gone")
