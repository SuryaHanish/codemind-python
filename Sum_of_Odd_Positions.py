n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(n):
    if(i%2==1):
        sum=sum+a[i]
print(sum)

