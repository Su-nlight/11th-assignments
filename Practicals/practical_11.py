import sys
emailid=list()
username=list()
domain=list()
try:
    n=int(input("Enter number of n students: "))
except ValueError:
    print("N given is not defined.")
    sys.exit(0)
except:
    print("Runtime Error")
    sys.exit(0)

for i in range(n):
    emailid.append(input("Enter Email id of student no.{} : ".format(i+1)).strip())
    username.append(emailid[i].split("@")[0])
    domain.append(emailid[i].split("@")[-1])
emailid,username,domain=tuple(emailid),tuple(username),tuple(domain)
print(emailid,username,domain)
#Write a program to read email IDs of n number of students and store them in a tuple.
#Create two new tuples, one to store only the usernames from the email IDs and second to store
#domain names from the email IDs. Print all three tuples at the end of the program.