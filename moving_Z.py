def moving_Zero(a):
    j=0
    n=len(a)
    b=[]
    c=[]
    for i in a:
        if i!=0:
            b.append(i)
        else:
            c.append(i)
    a=b+c
    return a
        
    # for i in range(n):
    #     if a[i]==0:
    #         j=i
    #         break

    # for i in range(j+1,n):
    #     if a[i]!=a[j]:
    #         a[i],a[j]=a[j],a[i]
    #         j=j+1
    
    # return a



a=[1,8,0,5,5,2,9,0,0,0,7,7,4]
print(moving_Zero(a))