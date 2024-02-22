#write a python program to make encryption and decryption with a key value using functions
def encryption(s,key):
    aval=0
    se=""
    for i in s:
        aval=ord(i)
        aval+=key
        se+=chr(aval)
    print(se)
    

def decryption(s,key):
    bval=0
    sd=""
    for i in s:
        bval=ord(i)
        bval-=key
        sd+=chr(bval)
    print(sd)

s=input("enter a string:")
key=int(input("enter a key:"))
l=int(input("enter 1 for encryption, 2 for decryption"))
if(l==1):
    encryption(s,key)
elif(l==2):
    decryption(s,key)
else:
    print("error: wrong input!")

