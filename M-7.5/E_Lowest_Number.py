n=int(input())
a=list(map(int,input().split()))

min=100000
for i in range(len(a)):
    if min > a[i]:
        min = a[i]
        ind = a.index(a[i]) + 1


print(f'{min} {ind}')
