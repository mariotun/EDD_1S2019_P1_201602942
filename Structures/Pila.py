import os


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
		#print("Node entered to Stack")

	def pop(self):#METHOD CALLED pop

		aux=None

		if self.first is None:
			print(" ")

		else:
			aux=self.first
			self.first=aux.next
			#print("Node deleted in Stack")


	def pop_all(self):

		aux=None
		temp=self.first

		if self.first is None:
			print("NO hay datos aun")

		else:

			while temp != None:
				aux=self.first
				self.first=aux.next

				temp=temp.next


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

	def graph_stack_score(self):

		cadena=" "
		aux=self.first

		if self.first != None:

			cadena+="\n"
			cadena+="pila1[\n"
			cadena+="label=\"{"
			cadena+="\n"

			while aux!=None:

				cadena+="|"
				cadena+="("
				cadena+=str(aux.x)
				cadena+=","
				cadena+=str(aux.y)
				cadena+=")"
				cadena+="\n"

				aux=aux.next

			cadena+="}\" \n"
			cadena+="];\n"
			cadena+="}"

		else:
			cadena+=str(aux)
			cadena+="[label=\"null\"];\n}"
			print("VACIO")


		f=open("Score_Stack.dot","w")
		f.write("digraph pila_puntos{\n label=Pila_Puntaje_Juego; \n labelloc=t; \n")
		f.write("node[margin=0.3 fontcolor=black shape=record];\n")
		#f.write("{rank=same;\n")

		f.write(cadena)
		
		#f.write("} }")
		f.close()

		os.system("dot Score_Stack.dot -Tpng -o Score_Stack.png")
		os.system("xdg-open Score_Stack.png")













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
		