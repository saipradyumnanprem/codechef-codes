t = int(input())
for i in range(t):
    x1,x2,x3,x4 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    x3 = int(x3)
    x4 = int(x4)
    
    if x1 == x2 == x3 == x4:
        print("IN")
    else:
        print("OUT")
