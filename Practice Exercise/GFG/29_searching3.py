arr = [10, 20, 30, 40, 45, 50, 55, 60]

def binary_search_recursive(arr, element, low = 0, high = len(arr)):

    if low > high:
        return -1

    mid = (low + high) // 2
    
    if arr[mid] == element:
        return mid
    elif arr[mid] < element:
        return binary_search_recursive(arr, element, mid+1, high)
    else:
        return binary_search_recursive(arr, element, low, mid-1)


search = 55

index = binary_search_recursive(arr, search)

if index == -1:
    print("Element not found")
else:
    print(f'Element {search} is present at index {index}')