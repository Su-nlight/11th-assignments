Tuple1=eval(input("Enter values of tuple se[perated by comma(,): "))

ele=int(input("Enter element to be searched: "))

for i in range(len(Tuple1)):
    if Tuple1[i]==ele:
        print("{} in Tuple is found at index={}".format(ele,i))
    else:
        print("{} in tuple is provided is not found".format(ele))