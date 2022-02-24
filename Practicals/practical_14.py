t1=eval(input("Enter elements of first tuple seperated by comma(,): "))
t2=eval(input("Enter elements of second tuple seperated by comma(,): "))

print("values before swaping\nFirst Tuple: {}\nSecond Tuple: {}".format(t1,t2))

t2,t1=t1,t2

print("values before swaping\nFirst Tuple: {}\nSecond Tuple: {}".format(t1,t2))
