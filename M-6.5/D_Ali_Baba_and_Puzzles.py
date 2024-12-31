a,b,c,x=map(int,input().split())
 
if a+b-c == x :
    print('YES')
elif a-b+c == x :
    print('YES')
elif a+b*c == x :
    print('YES')
elif a*b+c == x :
    print('YES')
elif a*b-c == x :
    print('YES')
elif a-b*c == x :
    print('YES')
else:
    print('NO')