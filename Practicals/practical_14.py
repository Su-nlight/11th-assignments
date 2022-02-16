#Write a Python program to create a dictionary of frequency of letters from a string.
data=input("Enter String to create frequency dictionary of: ")
freqdic=dict()
new=dict()
for i in data:
    if i in freqdic:
        freqdic[i]+=1
    else:
        freqdic[i]=1

temp=sorted(freqdic.keys())
for x in temp:
    new[x]=freqdic[x]
freqdic=new
print(freqdic)