def  seclargest(a):
    n=len(a)
    # a.sort()
    # if a[n-1]!=a[n-2]:
    #         second=a[n-2]
    # return second
    max=a[0]
    secondmax=a[0]
    for i in range(n):
        if max<a[i]:
            max=a[i]
   

    for i in range(n):
        if secondmax<a[i] and a[i]<max:
            secondmax=a[i]
    return secondmax




a=[3,2,4,5,6,1,3,4]
print(seclargest(a))