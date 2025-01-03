# Inputing Natural Number
number = int(input("Enter the Natural Number: "))

# j ranges from 1 to n
for j in range(1, number+1):

	# Initializing List
	a = []

	# i loop ranges from 1 to j
	for i in range(1, j+1):
		print(i, end=" ")
		if(i < j):
			print("+", end=" ")
		a.append(i)
	print("=", sum(a))

print()
