
s=input("Enter string:")
c=0
f=0
l=0
d=0

for i in s:
  if i.isupper():
    c+=1
  if i.islower():
    f+=1
  if i.isalpha():
    l+=1
  if i.isdigit():
    d+=1

print("No of uppercase letters = {}\n No of lowercase letters = {} /n No of alphabets ={} /n No of digits = {}" .format(c,f,l,d))
