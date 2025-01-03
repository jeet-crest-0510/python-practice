set = {5,2,7,4,5,6}

print(set)

set.pop()

print('Pop() : ' + str(set))

set.discard(7)

print('Discard(): ' + str(set))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7}

print(set1)
print(set2)

print('Intersection os both sets: ' + str(set1 & set2))
print('Union os both sets: ' + str(set1 | set2))
print('Difference os both sets: ' + str(set1 - set2))

a = [1, 2, 3, 4]
b = [5, 6, 3, 8]

# Check for at least one common element
if any(item in b for item in a):
    print("Common elements exist.")
else:
    print("No common elements.")