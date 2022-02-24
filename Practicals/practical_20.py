data=dict()
value=dict()
n=int(input("Enter number of students you want to enter: "))

for x in range(n):
    admn = int(input("Enter Admission number of student no.{}: ".format(x + 1)))
    value["name"]=input("Enter Name of student no.{}: ".format(x + 1))
    value["class"]=int(input("Enter Class of student no.{} in numeric: ".format(x+1)))
    value["section"]=input("Enter Section of student no.{}: ".format(x + 1))
    value["percentage"]=float(input("Enter percentage of student no.{}: ".format(x + 1)))
    data[admn]=value
    value=dict()

for i in data.keys():
    print("\nAdmission number: ",i)
    for j in data[i].keys():
        print("\t{} is {}".format(j,data[i][j]))
