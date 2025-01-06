n = int(input('Enter size of Pattern: '))
alpha = 65

for i in range(n):
    print(" "*(n-i), end = " ")
    for j in range(i+1):
        print(chr(alpha), end =" ")
        alpha+=1
    alpha=65
    print()