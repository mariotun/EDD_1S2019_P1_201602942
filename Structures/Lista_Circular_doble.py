class NodeLCD:#CLASS CALLED NodeLCD

	def __init__(self,user):#CONSTRUCTOR 

		self.user=user
		self.next=None
		self.previous=None

class Doubly_Linked_List:#CLASS CALLED Doubly_Linked_List

	def __init__(self):#CONSTRUCTOR 
		
		self.first=None
		self.last=None

	def add(self,nodelcd):#METHOD CALLED ADD

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

		print("Entered Node")
