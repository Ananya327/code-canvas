def consigativenumber(a, target):
    n = len(a)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += a[j]
            if total == target:
                return True
    return False



a=[1,2,3,5,2]

target=84
print(consigativenumber(a,target))