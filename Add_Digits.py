def digits(n):
    su=0
    while n>0:
        rem=n%10
        su=su+rem 
        n=n//10
    if su>9:
        su=digits(su)
    return su
n=int(input())
x=digits(n)
print(x)
