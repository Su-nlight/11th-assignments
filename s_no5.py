print("Choice are: \n 1 --> Area of circle \n 2 --> Area of Reactangle \n 3 --> Circumference of Circle \n 4 --> Area of Square")
ch=int(input("Enter your Choice: "))

try:
  if ch==1:
       rad=int(input("Enter Radius of Circle"))
       ar=((22/7)*(rad**2))
       print("Area of circle is "+ str(ar))

  elif ch==2:
       l=int(input("Enter Length of Rectangle: "))
       b=int(input("Enter Breadth of Rectangle: "))
       ar=(l*b)
       print("Area of Rectangle is "+ str(ar))

  elif ch==3:
       rad=int(input("Enter Radius of Circle: "))
       cir=((22/7)*(rad*2))
       print("Circumference of circle is "+ str(cir))

  elif ch==4:
       s=int(input("Enter Side of Square: "))
       ar=(s**2)
       print("Area of Rectangle is "+ str(ar))

  else:
       print("Invalid choice")
except:
  print("Error")
