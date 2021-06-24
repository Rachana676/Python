class student:

    def __init__(self, usn=None, name=None, age=None):
        self.usn=usn
        self.name=name
        self.age=age

    def getdata(self):
        self.usn=input("ENTER USN: ")
        self.name=input("ENTER NAME: ")
        self.age=int(input("ENTER AGE: "))

    def display(self):
        print("USN: ",self.usn)
        print("NAME: ",self.name)
        print("AGE: ",self.age)

class derived1(student):

    def __init__(self, sem=None, sub1=None, sub2=None, sub3=None, sub4=None, sub5=None):
        self.sem=sem
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.sub4=sub4
        self.sub5=sub5

    def dgetdata(self):
        self.sem=int(input("ENTER SEMESTER: "))
        self.sub1=int(input("ENTER SUBJECT-1 MARKS: "))
        self.sub2=int(input("ENTER SUBJECT-2 MARKS: "))
        self.sub3=int(input("ENTER SUBJECT-2 MARKS: "))
        self.sub4=int(input("ENTER SUBJECT-2 MARKS: "))
        self.sub5=int(input("ENTER SUBJECT-2 MARKS: "))

class derived2(derived1):

    def ddisplay(self):

        self.total=self.sub1+self.sub2+self.sub3+self.sub4+self.sub5
        self.percent=self.total/5

        print("STUDENT DETAILS!!")
        print("SEMESTER: ",self.sem)
        print("SUBJECT-1: ",self.sub1)
        print("SUBJECT-2: ",self.sub2)
        print("SUBJECT-3: ",self.sub3)
        print("SUBJECT-4: ",self.sub4)
        print("SUBJECT-5: ",self.sub5)
        print("TOTAL: ",self.total)
        print("PERCENTAGE: ",self.percent)

s1=derived2()

s1.getdata()
s1.dgetdata()
s1.ddisplay()
    
