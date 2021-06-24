d={}

class emp:

    def sal(self,name,addr,pan,basic,tds=0):
        self.name=name
        self.addr=addr
        self.pan=pan
        self.basic=basic
        self.hra=0.2*basic
        self.da=0.5*basic
        self.ta=0.1*basic
        self.tds=tds
        self.pf=0.12*basic
        self.Esi=0.04*basic
        netsal=self.basic+self.hra+self.da+self.ta-(self.pf+self.tds+self.Esi)
        return netsal
    
    def get_d(self):
        name=input("ENTER NAME:  ")
        addr=input("ENTER THE ADDRESS: ")
        pan=input("ENTER THE PAN NUMBER: ")
        basic=int(input("ENTER THE BASIC PAY: "))
        tds=int(input("ENTER THE TDS: "))
        self.netsal=self.sal(name,addr,pan,basic,tds)
        
    def display(self):
        print("NAME: ",self.name)
        print("ADDRESS: ",self.addr)
        print("PAN NO.: ",self.pan)
        print("BASIC PAY: ",self.basic)
        print("TDS: ",self.tds)
        print("DA : ",self.da)
        print("TRAVELLING ALLOWANCE: ",self.ta)
        print("HOME RENT ALLOWANCE: ",self.hra)
        print("PROVIDENT FUND: ",self.pf)
        print("EMPLOYEE STATE INSURANCE: ",self.Esi)
        print("NET SALARY: ",self.netsal)
    def search(self,name):
        for k,v in d.items():
            print("k==",k)
            print("v==",v)
            if k==name:
                print(v.__dict__)
while True:
    print("1. ENTER EMPLOYEE DETAILS")
    print("2. DISPLAY EMPLOYEE DETAILS")
    print("3. UPDATE")
    print("4. SEARCH")
    
    ch=int(input("ENTER YOUR CHOICE: "))

    if ch==1:
        print("EMPLOYEE DETAILS")
        e=emp()
        e.get_d()

    elif ch==2:
        print("DISPLAY")
        e.display()
        
    elif ch==3:
        print("UPDATE")
        d.update({e.name:e})
        print(d)

    elif ch==4:
        print("SEARCH")
        e.search(input("ENTER EMPLOYEE'S NAME: "))

    else:
        exit()
