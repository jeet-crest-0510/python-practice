def returnSum(dict):
    sum = 0
    for k in dict:
        sum+=dict[k]
    return sum

dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))
print("Size of Dict: " + str(dict.__sizeof__()))