def insertion_sort(arr):

    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            j=i
            while j>=0 and arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                j -= 1
    return arr

arr = [5,4,2,7,1]
print(f'Array is: {arr}')

s = insertion_sort(arr)
print(f'Sorted Array is: {s}')