h,m=map(int,input().split(":"))
ang=abs((h*30)-((11/2)*m))
res=360-ang
print(min(ang,res))