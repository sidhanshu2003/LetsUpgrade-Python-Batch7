# Make a Lambda function for capitalizing the whole sentence passed using arguments
# And Map all the sentences in the list, with the Lambda function
#["Hey this is sai", i am in mumbai",...]
#o/p
#["Hey This Is Sai", I Am In Mumbai",...]

lst = ["Hey this is sai, i am in mumbai,..."]
checkCapitalizeLambda = map(lambda lst: lst.title(),lst)
print(list(checkCapitalizeLambda))