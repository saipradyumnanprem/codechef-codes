def height(a, b):
    if a > b:
        return 1
    else:
        return 2
    
    
    
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = input().split()
        a = int(a)
        b = int(b)
        f = height(a,b)
        if f == 1:
            print("A")
        else:
            print("B")
