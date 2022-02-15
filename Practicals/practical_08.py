#Write a program using a user defined function calcFact() to calculate and display the factorial of a number num passed as an argument.
def calcFact(num):
    product=1
    for x in range(1,num+1):
        product*=x 
    return product
n=input("Enter natural number till you want factorial: ")
try:
    n=int(n)
    if n<0:
        print("negative value not accepatble")
    else: 
        print(calcFact(n))
except ValueError:
    print("Value Error")