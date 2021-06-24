s1={2,4,6,8,10}
print(s1)

s2=set()
n=int(input("ENTER THE NUMBER OF ELEMENTS IN SET-2: "))
print("ENTER THE ELEMENTS: ")
for i in range(0,n):
    ele=(input())
    s2.add(ele)
print(s2)


while True:

    print("1. LENGTH")
    print("2. ADD A NEW VALUE")
    print("3. ADD MULTIPLE VALUES")
    print("4. POP A VALUE")
    print("5. UNION")
    print("6. INTERSECTION")
    print("7. SET DIFFERENCE")
    print("8. SYMMETRIC DIFFERENCE")
    print("9. CLEAR THE SETS")
    print("10. DELETE THE SET")

    ch=int(input("ENTER YOUR CHOICE: "))

    if ch==1:
        print("LENGTH OF SET-1: ",len(s1))
        print("LENGTH OF SET-2: ",len(s2))

    elif ch==2:
        val=int(input("Enter a value: "))
        s1.add(val)
        print("SET-1: ",s1)

    elif ch==3:
        s1.update([1,2,3,4])
        print(s1)

    elif ch==4:
        print(s1)
        print(s2)
        s1.pop()
        s2.pop()
        print("AFTER PERFORMONG POP OPERATION: ",s1)
        print("AFTER PERFORMONG POP OPERATION: ",s2)

    elif ch==5:
        s3=s1.union(s2)
        print("UNION OF 2 SETS: ",s3)

    elif ch==6:
        s3=s1.intersection(s2)
        print("INTERSECTION OF 2 SETS: ",s3)

    elif ch==7:
        s3=s1-s2
        print("SET DIFFERENCE IS: ",s3)

    elif ch==8:
        s3=s1^s2
        print("SYMMETRIC DIFFERENCE IS: ",s3)

    elif ch==9:
        s1.clear()
        s2.clear()
        print("SET-1: ",s1)
        print("SET-2: ",s2)

    elif ch==10:
        del(s1)
        del(s2)
        print(s1)
        print(s2)

    else:
        pirnt("INVALID CHOICE!!")
