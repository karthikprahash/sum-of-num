# sum-of-num
N=int(input())
n=list(map(int,input().split()))[:N]
s=0
for i in n:
    s=i+s
print(s)
