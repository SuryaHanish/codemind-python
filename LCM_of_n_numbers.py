import math
n=int(input())
A = list(map(int,input().split()))
print(math.lcm(*A))