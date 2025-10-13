def Remove_duplicate_element(a):
    n=len(a)
    # b=set(a)
    # return list(b)
    b=[]
    for i in a:
        if i not in b:
             
            b.append(i)
    return b
    
        








a=[2,3,4,5,1,3,2,4,1,6]
print(Remove_duplicate_element(a))