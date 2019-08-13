import os

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

	def dequeue_all(self):

		aux=None
		temp=self.first
		

		if self.first is None:
			print("NO hay datos aun")

		else:

			while temp != self.last:
				aux=self.first
				self.first=aux.next

				temp=temp.next

	
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
			print(".")


	def graph_Queue_scoreboard(self):

		cadena=""
		aux=self.first

		if self.first != None:

			cadena+="\n"
			cadena+="cola1[\n"
			cadena+="label=\"{"
			cadena+="\n"

			while aux != None:

				cadena+="("
				cadena+=str(aux.user)
				cadena+=","
				cadena+=str(aux.score)
				cadena+=")"
				cadena+="| \n"

				aux=aux.next

			cadena+="}\" \n"
			cadena+="]; \n"
			cadena+="}"


		else:
			cadena+=str(aux)
			cadena+="[label=\"null\"];\n}"
			print("VACIO")




		f=open("Scoreboard_Queue.dot","w")
		f.write("digraph cola_puntajes{\n label=Cola_Puntaje_Usuarios; \n labelloc=t; \n")
		f.write("node[margin=0.3 fontcolor=black shape=record];\n")
		#f.write("{rank=same;\n")

		f.write(cadena)
		
		#f.write("} }")
		f.close()

		os.system("dot Scoreboard_Queue.dot -Tpng -o Scoreboard_Queue.png")
		os.system("xdg-open Scoreboard_Queue.png")







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



	