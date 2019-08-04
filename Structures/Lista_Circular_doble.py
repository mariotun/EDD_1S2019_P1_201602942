class NodeLCD:#CLASS CALLED NodeLCD

	def __init__(self,user):#CONSTRUCTOR 

		self.user=user
		self.next=None
		self.previous=None

class Circular_Doubly_Linked_List:#CLASS CALLED Circular_Doubly_Linked_List

	def __init__(self):#CONSTRUCTOR 
		
		self.first=None
		self.last=None

	def add(self,nodelcd):#METHOD CALLED add

		if self.first is None:
			
			self.first=nodelcd
			self.last=nodelcd
			self.first.next=self.first
			self.first.previous=self.last

		else:
			
			self.last.next=nodelcd
			nodelcd.previous=self.last
			nodelcd.next=self.first
			self.last=nodelcd
			self.first.previous=self.last

		print("Node entered to Circular Doubly Linked List")


	def print_Circular_Doubly_Linked_List(self):#METHOD CALLED print_Circular_Doubly_Linked_List

		if self.first is None:
			
			print("Circular Doubly Linked List Empy")

		else:
			temp=self.first

			while temp.next is not self.first:
				print(temp.user,end='')
				print('-->',end=" ")
				temp=temp.next

			print(temp.user,end='')
			print('-->',end='')
			temp=temp.next
			print(temp.user)
	

#-------Example to use the list-------

lcd=Circular_Doubly_Linked_List()#CREATE A NEW Circular_Doubly_Linked_List
lcd.add(NodeLCD("mario"))#ADD ELEMENT 1
lcd.add(NodeLCD("raul"))#ADD ELEMENT 2
lcd.add(NodeLCD("carlos"))#ADD ELEMENT 3
lcd.add(NodeLCD("sofia"))#ADD ELEMENT 4
lcd.add(NodeLCD("alejandra"))#ADD ELEMENT 5
lcd.print_Circular_Doubly_Linked_List()#PRINT THE LIST

