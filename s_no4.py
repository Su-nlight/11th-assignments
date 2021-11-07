no1=int(input("Enter number one:"))
no2=int(input("Enter number Two:"))
no3=int(input("Enter number Three:"))
st="Greatest number among all is: "

if no1>no2 and no1>no3:
    print(st +str(no1))

elif no2>no1 and no2>no3:
    print(st +str(no2))

elif no3>no2 and no3>no2:
    print(st +str(no3))
