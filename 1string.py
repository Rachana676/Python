a=input("ENTER THE 1st STRING: ")
b=input("ENTER THE 2nd STRING: ")

while True:

    print("1. CONCATENATION")
    print("2. FIND LENGTH")
    print("3. REPETITION")
    print("4. LOWERCASE")
    print("5. UPPERCASE")
    print("6. CAPITALIZE")
    print("7. SWAP THE CASE")
    print("8. REVERSE")
    print("9. COUNT OCCURANCE OF A CHAR")
    print("10. SPLIT")

    ch=int(input("ENTER YOUR CHOICE: "))

    if ch==1:
        c=a+b
        print("CONCATENATED STRING IS: ",c)

    elif ch==2:
        print("LENGTH OF 1st STRING IS: ",len(a))
        print("LENGTH OF 2nd STRING IS: ",len(b))

    elif ch==3:
        n=int(input("ENTER THE NO OF TIMES THE STRING IS TO BE REPEATED: "))
        print(a*n)
        print(b*n)

    elif ch==4:
        print("STRING 1 IN LOWERCASE: ",a.lower())
        print("STRING 2 IN LOWERCASE: ",b.lower())

    elif ch==5:
        print("STRING 1 IN UPPERCASE: ",a.upper())
        print("STRING 2 IN UPPERCASE: ",b.upper())

    elif ch==6:
        print("CAPITALIZED STRING-1: ",a.capitalize())
        print("CAPITALIZED STRING-2: ",b.capitalize())

    elif ch==7:
        print(a.swapcase())
        print(b.swapcase())

    elif ch==8:
        print("STRING-1 REVERSED: ",a[::-1])
        print("STRING-2 REVERSED: ",b[::-1])

    elif ch==9:
        n=input("Enter the alphabet to be counted: ")
        print(a.count(n))
        print(b.count(n))

    elif ch==10:
        print(a.split())
        print(b.split())

    else:
        print("INVALID CHOICE!!!")

    
