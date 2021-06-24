class oper:

	def __init__(self):
		self.alist=[]

	def getelements(self):
		n=int(input("ENTER THE SIZE OF LIST: "))
		print("ENTER",n," ELEMENTS: ")
		for i in range(0,n):
			ele=int(input())
			self.alist.append(ele)
		print(self.alist)
	
	def __add__(self,other):
		if len(self.alist)==len(other.alist):
			new_list=[]
			for i in range(0,len(self.alist)):
				new_list.append(self.alist[i]+other.alist[i])
			return new_list
		else:
			print("2 LISTS SHOULD BE OF SAME SIZE!!")

	def __sub__(self,other):
		if len(self.alist)==len(other.alist):
			new_list=[]
			for i in range(0,len(self.alist)):
				new_list.append(self.alist[i]-other.alist[i])
			return new_list
		else:
			print("2 LISTS SHOULD BE OF SAME SIZE!!")

	def __mul__(self,other):
		if len(self.alist)==len(other.alist):
			new_list=[]
			for i in range(0,len(self.alist)):
				new_list.append(self.alist[i]*other.alist[i])
			return new_list
		else:
			print("2 LISTS SHOULD BE OF SAME SIZE!!")

	def __floordiv__(self,other):
		if len(self.alist)==len(other.alist):
			new_list=[]
			for i in range(0,len(self.alist)):
				new_list.append(self.alist[i]//other.alist[i])
			return new_list
		else:
			print("2 LISTS SHOULD BE OF SAME SIZE!!")
	
