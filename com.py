n=int(input("Enter number:"))
i,fact=1
s,s2=0 
if n<0:
 print("Error")
 
else:
 while i<=n:
  fact*=i
  s+=fact
  s2+=i
  i+=1
  
 print("Factorial is {0}\nSum of each step in factorial is {1}\n Sum till nth natural number is ".format(fact, s, s2))