def calcAns(a, b):
    marks = a //10
    
    markScored = marks * b
    
    return markScored
    
    
    
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a,b = input().split()
        a= int(a)
        b = int(b)
        ans = calcAns(a, b)
        print(ans)
        
