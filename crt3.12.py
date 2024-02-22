#to print odd composite numbers in a range
#without count

def oddcomp(n,m,l):
    for i in range(n,m+1):
        if i%2!=0:
            for j in range(2,i):
                if i%j==0:
                    l.append(i)
                    break
n,m=map(int,input().split())
l=[]
oddcomp(n,m,l)
print(l)
print(sum(l))


#with counting factors
'''
def oddcomp(n,m,l):
    for i in range(n,m+1):
        if i%2!=0:
            count=0
            for j in range(1,i+1):
                if i%j==0:
                    count+=1
                if(count>2):
                    
                    l.append(i)
                    break
                
n,m=map(int,input().split())
l=[]
oddcomp(n,m,l)
print(l)
print(sum(l))
'''



#without taking list as a parameter
'''
def composite(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
        return 1
    else:
        return 0

a,b=int(input(),int(input()))
l=[]
for i in range(a,b+1):
    if i%2!=0:
        flag=composite(i)
        if flag==1:
            l.append(i)
        

'''

