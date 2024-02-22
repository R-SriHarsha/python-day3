#factorial of a number using recursion and strong numbers
'''
def fact(n):
    if n<1:
        return 1
    
    return n*fact(n-1)



def strong(n):
    s=str(n)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum==n:
        print("Strong number")
    else:
        print("weak number")




n=int(input())
strong(n)
'''


#strong numbers in a given range

def fact(n):
    if n<1:
        return 1
    
    return n*fact(n-1)



def strong(n):
    s=str(n)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum==n:
        print(n)




n,m=map(int,input().split())
for k in range(n,m+1):
    strong(k)
    



