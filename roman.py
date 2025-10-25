def roman_no(s):
    n=len(s)
    roman={"I":1,"V":5,"X":10,"L":50,"C":100}
    total=0
    for i in range(n):
        for j in range(i+1,n):
            if roman[ s[i]]>=roman[s[j]]:
                total=roman[s[i]]+roman[s[j]]
            else:
                total=roman[s[i]]-roman[s[j]]
    total=total+roman[s[-1]]
    return total



print(roman_no("III"))