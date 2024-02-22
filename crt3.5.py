#
length,digit=map(int,input().split(" "))

s=input()

for i in range(len(s)):
    if int(s[i])<digit:
        print(s[:i]+str(digit)+s[i:])
        break
else:
    print(s+str(digit))
