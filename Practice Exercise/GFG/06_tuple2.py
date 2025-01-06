# Python3 code to demonstrate working of 
# Maximum and Minimum K elements in Tuple
# Using slicing + sorted()

# initializing tuple
test_tup = (5, 20, 3, 7, 6, 8)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# initializing K 
K = 2

# Maximum and Minimum K elements in Tuple
# Using slicing + sorted()
test_tup = list(test_tup)
temp = sorted(test_tup)
res = tuple(temp[:K] + temp[-K:])

# printing result 
print("The extracted values : " + str(res)) 
