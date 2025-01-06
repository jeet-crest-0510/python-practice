arr = [10, 20, 30, 40, 45, 50, 55, 60]

def binary_search_iterative(arr, element):
    
    low = 0
    high = len(arr) - 1

    while(low <= high):
        mid = (low + high)//2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

search = 20

index = binary_search_iterative(arr, search)

if index == -1:
    print("Element not found")
else:
    print(f'Element {search} is present at index {index}')