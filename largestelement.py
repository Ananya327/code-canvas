def largest(a):
    n=len(a)
    # a.sort()
    # return a[n-1]
    max=a[0]
    for i in range(n):
        if max<a[i]:
            max=a[i]
    return max




a=[3,2,4,5,6,1,3,4]
print(largest(a))