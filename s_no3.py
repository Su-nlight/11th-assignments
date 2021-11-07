name=input("Enter Your Name:")
b_s=float(input("Enter Your Basic Salary:"))
pf=((12/100)*b_s)
hra=((10/100)*b_s)
gross=(b_s+hra-pf)

if gross>=100000:
    it=((30/100)*gross)

elif gross<100000 and gross>=80000:
    it=((20/100)*gross)

elif gross<80000 and gross>=50000:
    it=((10/100)*gross)

elif gross<=50000:
    it=0


net=(gross-it)

print("Name = " + name+"\nBasic Salary = " +str(b_s) +"\n P. F. = " +str(pf)+"\n H. R. A. = " +str(hra) + "\n Gross = " +str(gross) +"\n I. T. = " +str(it) +"\n Net = " +str(net))
