def uniquele(a):
    
    unique=[]
    for lst in a:
        if a.count(lst)==1:
            unique.append(lst)
    return unique


a=[1,2,3,4,5,8,1,2,3,3]
print(uniquele(a))