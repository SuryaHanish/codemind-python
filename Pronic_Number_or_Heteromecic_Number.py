def pronic(n):
    for i in range(1, n):
        if i*(i+1)==n:
            return True
    return False
        
num = int(input())
if pronic(num):
    print("YES")
else :
    print("NO")