# Write a program to input names of n students and store them in a tuple. Also, input a name
# from the user and find if this student is present in the tuple or not.
def isempty(tocheck):
    if tocheck.strip() == "": return True
    else: return False

class students:
    name = []
    def __init__(self):
        try:
            self.n = int(input("Enter value of n: "))
            self.add_name()
            self.name = tuple(self.name)
            print(self.name)
        except ValueError:
            print("Provided value of n is not valid, retry again...")
            students()
    def does_exists(self, name1):
        if name1 in self.name: return True
        else: return False
    def add_name(self):
        for i in range(self.n):
            newname = input("Enter name of student {}: ".format(i + 1))
            if isempty(newname) == True:
                print("The name entered is blank so it is not acceptable")
                i -= 1
                print(i)
                continue
            if self.does_exists(name1=newname) == True:
                print("User already does exist in the tuple")
                i -= 1
                print(i)
                continue
            else:
                self.name.append(newname)
                print(newname, "is added to the tuple")

students()