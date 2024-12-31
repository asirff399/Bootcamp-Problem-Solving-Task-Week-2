n=int(input())
a=list(map(int,input().split()))
x=int(input())

f=False
for i in a:
    if i == x:
        index=a.index(i)
        f=True

if f is True:
    print(index)
else:
    print(-1)
    
