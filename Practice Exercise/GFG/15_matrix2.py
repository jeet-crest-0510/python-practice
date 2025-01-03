
# Using list comprehension + groupby()
from itertools import groupby

test_list = [1, 3, 5, 1, 3, 2, 5, 4, 2]

print("The original list : " + str(test_list))

# Group similar elements into Matrix
res = [list(val) for key, val in groupby(sorted(test_list))]

print("Matrix after grouping : " + str(res))
