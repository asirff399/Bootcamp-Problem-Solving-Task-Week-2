n=int(input())
a=list(map(int,input().split()))

for i in range(n // 2):
    tmp = a[i]
    a[i] = a[n-1-i]
    a[n-1-i] = tmp

print(*a)
