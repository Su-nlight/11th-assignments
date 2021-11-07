n=int(input("Enter number:"))
s=0
try:
 if n>0 or n=0:
  print("Error")
 
 else:
  for i in range(1,n+1):
   s+=(1/i)
  
  print("sum of harmonic series is ",s)
  
except:
 print("Integer not defined.")
