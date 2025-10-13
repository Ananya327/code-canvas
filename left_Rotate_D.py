def Left_Rotate_D(arr,d):
    j=0
    n=len(arr)
    d=d%n
    temp=[]
    for i in range(n):
        temp[i]=arr[i]
    
    for i in range(d,n):
        arr[i-d]=arr[i]


    for i in range(n-d):
        arr[i]=temp[i-(n-d)]


arr=[1,2,3,4,5,6,7]
d=3
print(Left_Rotate_D(arr,d))