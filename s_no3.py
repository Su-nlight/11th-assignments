s=int(input("Enter Side of Square:"))
l=int(input("Enter Length of Rectangle:"))
b=int(input("Enter Breadth of Rectangle:"))
ch=int(input("Enter your Choice:"))

if ch==1:
  ar1=s**2
  ar2=l*b
  print("Area of Square = "+ str(ar1) +" \n Area of Rectangle = " + str(ar2)
        
elif ch==2:
  per1=4*s
  per2=2*(l+b)
  print("Perimeter of Square" + str(per1) +"\n Perimeter of Rectangle" + str(per2)
        
else:
  print("Invalid choice")
