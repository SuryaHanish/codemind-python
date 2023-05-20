n=int(input())
t=0
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2!=0:
        t+=1
if t<=2:
    print("YES")
else:
    print("NO")