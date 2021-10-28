num = int(input("Please enter the number: "))

if num > 1:

   for i in range(2,(num//2)+1):
      if (num % i) == 0:
         print(num,"is not a prime number")
         print(i,"times",num//i,"is",num)
         temp=0
         break;
      else:
         temp=1
         
if temp==1:
  print(num, "is a prime number")