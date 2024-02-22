#print sum of n natural numbers using recursion
def sumofnnatural(n):
    if n<1:
        return 1
    else:
        
        return n+sumofnnatural(n-1)
        

print(sumofnnatural(int(input())))
    
    
