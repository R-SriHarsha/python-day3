#write a python program to print a range of armstrong numbers using stringss an function

def rangearm(n,m):
    for i in range(n,m+1):
        num=0
        s=str(i)
        l=len(s)
        for j in s:
            num+=int(j)**l

        if num==int(i):
            print(i)
n,m=map(int,input().split(" "))
rangearm(n,m)
        
            
