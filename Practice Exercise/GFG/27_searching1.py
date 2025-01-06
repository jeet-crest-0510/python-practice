arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

search = 'J'

def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
        
    return -1

index = linear_search(arr, search)
if index == -1:
    print("Element not found!!")
else:
    print(f'Element {search} is present at index {index}')


