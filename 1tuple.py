t1=tuple(input("ENTER TUPLE-1 VALUES: "))
t2=tuple(input("ENTER TUPLE-2 VALUES: "))
print(t1)
print(t2)

while True:
    print("1. CONCATENATE")
    print("2. FIND LENGTH")
    print("3. FIND MINIMUM VALUE")
    print("4. FIND MAXIMUM VALUE")
    print("5. SLICING")
    print("6. RANGE SLICING")
    print("7. REPETITION")
    print("8. REVERSE")
    print("9. ITERATING THROUGH STRING")
    print("10. DELETE THE TUPLE")

    ch=int(input("ENTER THE CHOICE: "))

    if ch==1:
        print(t1+t2)

    elif ch==2:
        print(len(t1))
        print(len(t2))

    elif ch==3:
        print("MIN VALUE: ",min(t1))
        print("MIN VALUE: ",min(t2))

    elif ch==4:
        print("MIN VALUE: ",max(t1))
        print("MIN VALUE: ",max(t2))

    elif ch==5:
        n=int(input("Enter the index: "))
        print(t1[n])
        print(t2[n])

    elif ch==6:
        r1=int(input("Enter range-1: "))
        r2=int(input("Enter range-2: "))
        print(t1[r1:r2])
        print(t2[r1:r2])

    elif ch==7:
        n=int(input("Enter the no of times the tuple is to be repeated: "))
        print(t1*n)
        print(t2*n)

    elif ch==8:
        print("Reversed tuple: ",t1[::-1],t2[::-1])

    elif ch==9:
        for i in t1:
            print(i)
        for i in t1:
            print(i)

    elif ch==10:
        del t1
        del t2
        print(t1)
        print(t2)

    else:
        print("INVALID CHOICE!!!")
