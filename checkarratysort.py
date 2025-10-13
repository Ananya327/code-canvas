def check_array(a):
    n=len(a)
    for i in range(1,n):
        
        if a[i]>=a[i-1]:
            pass
        else:
            return False
            break
    return True




a=[5,6,7,18]
print(check_array(a))