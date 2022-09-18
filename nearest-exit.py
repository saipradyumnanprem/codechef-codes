#python 3 code
t = int(input())
for i in range(t):
    seat = int(input())
    dr = seat - 1
    dl = 100 - seat
    
    if dl > dr:
        print("LEFT")
    else:
        print("RIGHT")
