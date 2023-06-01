def reverse(n):
    negative=False
    if n<0:
        negative=True
        n=abs(n)
    rev=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n=n//10
        
    if negative:
        rev=-rev
    return rev
    
n=int(input())
rev=reverse(n)
print(rev)