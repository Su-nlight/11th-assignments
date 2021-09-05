#Q). Write a program to input name and marks of 3 subjects and display their Total.

name=input("Enter Your Name:")
sub1=input("Enter Marks of Subject 1:")
sub2=input("Enter Marks of Subject 2:")
sub3=input("Enter Marks of Subject 3:")

total= int(sub1) + int(sub2) + int(sub3)

print("Total Marks of " + name + " are:" + str(total))
