def automorphic(n):
    s=n*n
    sn=str(n)
    ss=str(s)
    if ss.endswith(sn):
        return True
    return False
    
num=int(input())
if automorphic(num):
    print("Automorphic Number")
else :
    print("Not an Automorphic Number")