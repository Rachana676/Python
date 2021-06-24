while True:
    print ("1. ENTER SOURCE FILE NAME AND DESTINATION FILE NAME ")
    print ("2. OPEN A FILE IN READ AND WROTE MODE")
    print ("3. WRITE TO A FILE")
    print ("4. READ CONTENT OF THE FILE")
    print ("5. COPY THE CONTENT TO NEW FILE ")
    print ("6. CLOSING THE FILE")

    ch = int(input("Enter the Choice "))

    if ch == 1:
        sname=input("Enter Existing file name ")
        dname=input("Enter new file name ")
        print ("Two Files Created ")

    elif ch == 2:
        try:         
            A = open(sname,"r")
            B = open(dname,"w")
        except FileNotFoundError: 
            print ("-"*60)
            print ("FileNotFoundError: File Note Found ")
            print ("-"*60)
        except NameError: 
            print ("-"*60)
            print ("NameError: Plz Create The File Before Opening it ")
            print ("-"*60)
        else:
            print ("-"*60)
            print("Operation Done succussfully ")
            print ("-"*60)

    elif ch == 3:
        try:
            a = A.read()
            B.write(a)
        except NameError:
            print ("-"*60)
            print ("NameError: Plz Open the file first ")
            print ("-"*60)
        else:
            print ("-"*60)
            print ("File successfully copied ")
            print ("-"*60)
            A.close()
            B.close()

    elif ch == 4:
        try:
            B.read()
        except ValueError:          
            print ("-"*60)
            print ("ValueError: Plz Open the file first ")
            print ("-"*60)

    elif ch == 5:
        try:
            A = open(sname,"r")
            B = open(dname,"w")
            str1=A.read()
            B.write(str1)
        except IOError: 
            print ("-"*60)
            print ("Error: can\'t find file or read data ")
            print ("-"*60)
        else:
            print ("File successfully copied ")
            A.close()
            B.close()

    elif ch==6:
        try:
            print(A/B)
        except TypeError:
            print ("-"*60)
            print ("TypeError: Cannot do this Operation ")
            print ("-"*60)
      
