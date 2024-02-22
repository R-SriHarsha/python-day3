#comparing input with given string
'''
s1="codeforces"
s=input()
count=0

for i in range(len(s1)):
    
    if s[i]!=s1[i]:
        count+=1


print(s1)
print(s)
print(count)

'''

#comparing given two strings
print("give two input strings of ten characters")
s1=input()
s2=input()
count=0
if len(s1)!=len(s2):
    print("lengths must be equal")
else:
    for i in range(len(s1)):
    
        if s2[i]!=s1[i]:
            count+=1

    print(s1)
    print(s2)
    print(count)


