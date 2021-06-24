class Person:

    def Hello(self, name=None, age=None):
        self.name=name
        self.age=age

        if self.name!=None and self.age!=None:
            print("Hello %s, your age is %s"%(self.name,self.age))

        elif self.name!=None:
            print("Hello ",self.name)

        else:
            print("Hello!!")

p1=Person()

p1.Hello()
p1.Hello("RVCE")
p1.Hello("RVCE",58)
