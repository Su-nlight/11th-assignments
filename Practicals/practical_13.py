numbers=tuple()
n=int(input("Enter how many numbers you want in your list: "))

for i in range(n):
    num=int(input(":"))
    numbers+=(num,)

print("The numbers in the Tuple are: ",numbers)
print("\nThe Maximum number is ",max(numbers))
print("\nThe minimun number is ",min(numbers))

mean=sum(numbers)/len(numbers)

print("\nThe mean of numbers is ",mean)