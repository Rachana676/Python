class employee:
    
    raise_amount=1.04

    def __init__(self, first=None, last=None, basic=None):
        self.first=first
        self.last=last
        self.basic=basic

    def getdata(self):
        self.first=input("Enter 1st name: ")
        self.last=input("Enter last name: ")
        self.basic=int(input("Enter basic salary: "))

    def display(self):
        print("FIRST NAME: ",self.first)
        print("LAST NAME: ",self.last)
        print("BASIC SALARY: ",self.basic)

class manager(employee):
    
    r_amount=1.10

    def raise_amount(self):
        print("AFTER RAISE SALARY: ",self.basic*self.r_amount)

class developer(employee):
    
    r_amount=1.05

    def raise_amount(self):
        print("AFTER RAISE SALARY: ",self.basic*self.r_amount)

m=manager()
d=developer()

while True:

    print("1. ENTER MANAGER INFO")
    print("2. ENTER DEVELOPER INFO")
    print("3. EXIT")

    ch=int(input("Enter your choice: "))

    if ch==1:
        m.getdata()
        print("MANAGER INFO")
        m.display()
        m.raise_amount()

    elif ch==2:
        d.getdata()
        print("DEVELOPER INFO")
        d.display()
        d.raise_amount()

    elif ch==3:
        break
