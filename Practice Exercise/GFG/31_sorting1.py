def countSort(arr):
        # code here
        dict = {}
        s = ''
        
        for a in arr:
            if a not in dict:
                dict[a] = 1
            else:
                dict[a] += 1
                
        dict1 = sorted(dict)
        
        for d in dict1:
            s += d*dict[d]
        
        return s

arr = "geeksforgeeks"
s = countSort(arr)
print('Array: ' + arr)
print('Sorted Array: ' + s)