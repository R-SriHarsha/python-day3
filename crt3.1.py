# write a python program to print the smallest vovel repeating odd no of  times in a given string

st=input()
vow="aeiouAEIOU"

s2=""
for i in st:
    if i in vow:
        if st.count(i)%2!=0:
            s2+=i
if len(s2)==0:
    print("not found")
else:
    print(min(s2))
            

    

        

        
    
        

        
