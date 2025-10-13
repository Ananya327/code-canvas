def Left_Rotate_D(arr, d):
    n = len(arr)
    d = d % n  # handle cases when d > n
    
    temp = []
    for i in range(d):  # store first d elements
        temp.append(arr[i])
    
    # Shift remaining elements to the left
    for i in range(d, n):
        arr[i - d] = arr[i]
    
    # Put back temp elements at the end
    for i in range(d):
        arr[n - d + i] = temp[i]
    
    return arr

# Example
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
print(Left_Rotate_D(arr, d))
