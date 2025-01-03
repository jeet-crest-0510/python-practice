import itertools     

# temp = itertools.count(start=10, step=2)
# print(temp)
# print(next(temp))
# print(next(temp))

# l = [[next(temp)for i in range(4)]for i in range(4)]
# print(l)

def display(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]<10:
                print('0' + str(mat[i][j]) , end = ' ')
            else:
                print(mat[i][j], end = ' ')
            
        print()
    print()

n = int(input('Enter the number: '))
iter = itertools.count(1)
matrix = [[next(iter) for x in range(n)] for x in range(n)]

display(matrix)

if n%2==0:
    for i in range(n):
        if i%2 == 1:
            matrix[i][:] = matrix[i][::-1]

display(matrix)
