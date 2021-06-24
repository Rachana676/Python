class student:

    def __init__(self, usn=None, name=None, age=None):
        self.usn=usn
        self.name=name
        self.age=age

    def getdata(self):
        self.usn=input("ENTER THE USN: ")
        self.name=input("ENTER THE NAME: ")
        self.age=int(input("ENTER THE AGE: "))

    def display(self):
        print("USN: ",self.usn)
        print("NAME: ",self.name)
        print("AGE: ",self.age)

class UGstudent(student):

    def __init__(self, sem=None, fee=None, stipend=None):
        self.sem=sem
        self.fee=fee
        self.stipend=stipend

    def UG_getdata(self):
        self.sem=int(input("ENTER THE SEMESTER: "))
        self.fee=int(input("ENTER THE FEE: "))
        self.stipend=int(input("ENTER THE STIPEND: "))

    def UG_display(self):
        print("SEMESTER: ",self.sem)
        print("FEE: ",self.fee)
        print("STIPEND: ",self.stipend)

class PGstudent(student):

    def __init__(self, sem=None, fee=None, stipend=None):
        self.sem=sem
        self.fee=fee
        self.stipend=stipend

    def PG_getdata(self):
        self.sem=int(input("ENTER THE SEMESTER: "))
        self.fee=int(input("ENTER THE FEE: "))
        self.stipend=int(input("ENTER THE STIPEND: "))

    def PG_display(self):
        print("SEMESTER: ",self.sem)
        print("FEE: ",self.fee)
        print("STIPEND: ",self.stipend)


s1=UGstudent()
s1.getdata()
s1.UG_getdata()
s1.display()
s1.UG_display()

s2=PGstudent()
s2.getdata()
s2.PG_getdata()
s2.display()
s2.PG_display()
