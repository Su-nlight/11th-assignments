'''Q). Write a program to input name of a student, total marks of a student out of 
hundred if it is greater than or equal to 50 display passed otherwise display Failed '''

name=input("Enter your Name:")
marks=int(input("Enter your Marks Out of Hundered:"))

if marks>=50:
  print("Passed")

elif marks<50:
  print("Failed")

else:
  print("Invalid Marks")
