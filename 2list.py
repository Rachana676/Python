l1=[]
ele1=int(input("ENTER NO. OF ELEMENTS IN LIST-1: "))
print("ENTER THE ELEMENTS: ")
for i in range(0,ele1):
    n=input()
    l1.append(n)
print(l1)

l2=[]
ele2=int(input("ENTER NO. OF ELEMENTS IN LIST-2: "))
print("ENTER THE ELEMENTS: ")
for i in range(0,ele2):
    n=input()
    l2.append(n)
print(l2)

while True:

    print("1. CONCATENATION")
    print("2. FIND LENGTH")
    print("3. FIND THE MINIMUM AND MAXIMUM VALUE")
    print("4. CHECK MEMBERSHIP")
    print("5. APPEND")
    print("6. ITERATION")
    print("7. REPETITION")
    print("8. REVERSE")
    print("9. SLICING")
    print("10. DELETE THE LIST")

    ch=int(input("ENTER YOUR CHOICE: "))

    if ch==1:
        l3=l1+l2;
        print(l3)

    elif ch==2:
        print("LENGTH OF LIST-1: ",len(l1))
        print("LENGTH OF LIST-2: ",len(l2))

    elif ch==3:
        print("MINIMUM, MAXIMUM VALUE OF LIST-1: ",min(l1),max(l1))
        print("MINIMUM, MAXIMUM VALUE OF LIST-2: ",min(l2),max(l2))

    elif ch==4:
        print("ENTER THE ELEMENT TO CHECK THE MEMBERSHIP: ")
        ele=input()
        print( "element" ,ele, "present in the list -> ",(ele in l1))

    elif ch==5:
        print(l1)
        print(l2)
        m=int(input("ENTER THE VALUE TO BE APPENDED IN LIST-1: "))
        n=int(input("ENTER THE VALUE TO BE APPENDED IN LIST-2: "))
        l1.append(m)
        l2.append(n)
        print("UPDATED LIST-1: ",l1)
        print("UPDATED LIST-2: ",l2)

    elif ch==6:
        for i in l1:
            print(i)
        for i in l2:
            print(i)

    elif ch==7:
        n=int(input("ENTER THE NO OF TIMES THE LIST IS TO BE REPEATED: "))
        print(l1*n)

    elif ch==8:
        print("REVERSED LIST IS: ",l1[::-1],l2[::-1])

    elif ch==9:
        n=int(input("ENTER THE INDEX: "))
        print(l1[n])
        print(l2[n])

    elif ch==10:
        del l1
        del l2
        print(l1)
        print(l2)
        
