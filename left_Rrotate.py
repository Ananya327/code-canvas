def Left_Rotate(arr):
    n=len(arr)
    a=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]

    arr[n-1]=a



    return arr




arr=[1,2,3,4,5]
print(Left_Rotate(arr))