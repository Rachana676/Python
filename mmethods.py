import os
from operatoroperation import *

ov1=oper()
ov2=oper()

ov1.getelements()
ov2.getelements()

while True:

	print("1. OVERLOAD + OPERATOR")
	print("2. OVERLOAD - OPERATOR")
	print("3. OVERLOAD * OPERATOR")
	print("4. OVERLOAD // OPERATOR")

	ch=int(input("ENTER YOUR CHOICE: "))

	if ch==1:
		print("OVERLOAD + OPERATOR")
		print(ov1+ov2)

	elif ch==2:
		print("OVERLOAD - OPERATOR")
		print(ov1-ov2)

	elif ch==3:
		print("OVERLOAD * OPERATOR")
		print(ov1*ov2)

	elif ch==4:
		print("OVERLOAD // OPERATOR")
		print(ov1//ov2)

	else:
		print("INVALID CHOICE!!!")
