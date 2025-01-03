test_list = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]
 
print("The original list : " + str(test_list))
 
# pairing each 1st col with next rows in Matrix
res = {test_list[0][i]: test_list[i+1]  for i in range(len(test_list) - 1)}

print("The Assigned Matrix : " + str(res))