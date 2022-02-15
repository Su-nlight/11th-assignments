#Write a program using a user defined  function that displays sum of first n natural numbers, where n is passed as an argument.
def sum0nnum(n):
    summ=0
    for x in range(1,n+1):
        summ+=x
    return summ

n=input("Enter nth number: ")
print(sum0nnum(int(n)))
