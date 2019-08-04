
class NodeStack:#CLASS CALLED NodeStack

	def __init__(self,x=None,y=None):#CONSTRUCTOR 

		self.x=x
		self.y=y
		self.next=None

class Stack:#CLASS CALLED Stack

	def __init__(self):#CONSTRUCTOR 

		self.first=None

	def push(self,nodestack):#METHOD CALLED push

		nodestack.next=self.first
		self.first=nodestack
		print("Node entered to Stack")

	def pop(self):#METHOD CALLED pop

		aux=None

		if self.first is None:
			print("Stack Empty")

		else:
			aux=self.first
			self.first=aux.next
			print("Node deleted in Stack")


	def print_stack(self):#METHOD CALLED print_stack

		a=self.first
		

		if self.first != None:
			while a != None:
				print('[',end='')
				print(a.x,end=',')
				print(a.y,end='')
				print(']',end='')
				print('-->',end='')
				a=a.next
			print(" \n")

		else:
			print("Stack Empty") 


#-------Example to use the Stack-------

pi=Stack()#CREATE A NEW Stack
pi.push(NodeStack(2,2))#ADD ELEMENT 1
pi.push(NodeStack(5,6))#ADD ELEMENT 2
pi.push(NodeStack(1,7))#ADD ELEMENT 3
pi.push(NodeStack(9,1))#ADD ELEMENT 4
pi.push(NodeStack(4,3))#ADD ELEMENT 5
pi.print_stack()#PRINT THE Stack
pi.pop()#DELETE ELEMENT
pi.pop()#DELETE ELEMENT
pi.print_stack()#PRINT THE Stack
		