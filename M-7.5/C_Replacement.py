n=int(input())
a=list(map(int,input().split()))

for i in range(len(a)):
    if a[i] > 0:
        a[i] = 1
    elif a[i] < 0:
        a[i] = 2

print(*a)