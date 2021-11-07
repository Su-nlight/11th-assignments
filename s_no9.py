n=int(input("Enter number:"))
s=0
try:
 if n<0 or n==0:
  print("Error")
 
 else:
  for i in range(1,n+1):
   s+=((i*((-1)**(i-1))))
  
  print("sum of series is ",s)
  
except:
 print("Integer not defined.")
