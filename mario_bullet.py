# cook your dish here
for i in range(int(input())):
    x,y,z=map(int , input().split())

    d=y/x
    if d>z:print(0)
    else:print(z-d)