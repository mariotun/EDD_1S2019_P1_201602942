class NodeLD:
	def __init__(self,posx,posy):
		self.posx=posx
		self.posy=posy
		self.next=None
		self.previous=None


class Doubly_Linked_List:
	def __init__(self):

		self.head=None
		self.last=None

    
	'''def add(self,nodeld):

		if self.head is None:
			self.head=nodeld

		else:
			aux=self.head
			while aux.next is not None:
				aux=aux.next

			aux.next=nodeld
			nodeld.previous=aux'''

	'''def add(self,nodeld):

		if self.head is None:

			self.head=nodeld
			self.head.next=None
			self.head.previous=None
			self.last=self.head
		else:

			self.last.next=nodeld
			nodeld.next=None
			nodeld.previous=self.last
			self.last=nodeld'''
	def add_first(self,nodeld):

		if self.head is None:
			self.head=nodeld
			self.head.next=None
			self.head.previous=None
			self.last=self.head
		else:
			self.head.previous=nodeld
			nodeld.next=self.head
			nodeld.previous=None
			self.head=nodeld





	def remove_last(self):

		'''temporal=self.head
		temporal2=None

		self.head=self.head.next
		self.head.previous=None

		temporal2=temporal
		temporal=temporal.next`'''

		temporal=self.last
		temporal2=None

		self.last=self.last.previous
		self.last.next=None

		temporal2=temporal
		temporal=temporal.previous

		



	def print_linkedlist(self):
		
		if self.head is None:
			print("The linkedlist is Empty")

		else:
			aux=self.head

			while aux is not None:
				print("[",end="")
				print(aux.posx,end=",")
				print(aux.posy,end="")
				print("]",end="")
				print("-->",end="")
				aux=aux.next
			print("\n")	
			#print(aux.x)


list2 = Doubly_Linked_List()      #create a new DoubleLinkedList
list2.add_first(NodeLD(2,4)) 
list2.add_first(NodeLD(4,2)) 
list2.add_first(NodeLD(3,1)) 
list2.add_first(NodeLD(5,1)) 
list2.add_first(NodeLD(2,2)) 
list2.add_first(NodeLD(7,8)) 
list2.print_linkedlist()
list2.remove_last()
list2.remove_last()
list2.remove_last()
list2.print_linkedlist()


	 