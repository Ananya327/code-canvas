def Remove_duplicate_element(a):
    n=len(a)
    # b=set(a)
    # return len(list(b))
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return(len(b))
    
        
a=[1,2,2,2,1,1,3,2,3,1,4]
print(Remove_duplicate_element(a))