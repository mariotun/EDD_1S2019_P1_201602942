
class NodeQueue:#CLASS CALLED NodeQueue

	def __init__(self,user,score):#CONSTRUCTOR 

		self.user=user
		self.score=score
		self.next=None

class Queue:#CLASS CALLED Queue

	def __init__(self):#CONSTRUCTOR

		self.first=None
		self.last=None
		print("example")

	def enqueue(self,nodenew):#METHOD CALLED enqueue

		if self.first == None:

			self.first=nodenew
			self.first.next=None
			self.last=self.first

		else:
			self.last.next=nodenew
			nodenew.next=None
			self.last=nodenew

		print("Node entered to queue")


	def dequeue(self):#METHOD CALLED dequeue

		aux=None

		if self.first is None:
			print("queue empty")

		else:
			aux=self.first
			self.first=aux.next
			print("Node deleted in queue")

	
	def printQueue(self):#METHOD CALLED printQueue

		aux=self.first

		if self.first != None:

			while aux != None:

				print('[',end='')
				print(aux.user,end=',')
				print(aux.score,end='')
				print(']',end='')
				print('-->',end='')

				aux=aux.next

			print("\n")

		else:
			print("queue empty")



#-------Example to use the Queue-------

'''
co=Queue()#CREATE A NEW Queue
co.enqueue(NodeQueue("mario",5))#ADD ELEMENT 1
co.enqueue(NodeQueue("raul",7))#ADD ELEMENT 2
co.enqueue(NodeQueue("carlos",23))#ADD ELEMENT 3
co.enqueue(NodeQueue("sofia",8))#ADD ELEMENT 4
co.printQueue()#PRINT THE Queue
co.dequeue()#DELETE ELEMENT
co.dequeue()#DELETE ELEMENT
co.printQueue()#PRINT THE Queue

'''



	