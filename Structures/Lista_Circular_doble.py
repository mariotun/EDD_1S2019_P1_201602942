#import file
import os
import curses


class NodeLCD:#CLASS CALLED NodeLCD

	def __init__(self,user):#CONSTRUCTOR 

		self.user=user
		self.next=None
		self.previous=None

class Circular_Doubly_Linked_List:#CLASS CALLED Circular_Doubly_Linked_List
	
	#first=None
	#last=None

	def __init__(self):#CONSTRUCTOR 
		
		self.first=None
		self.last=None

		
		
		#primero=self.first
		#ultimo=self.last

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

		#print("Node entered to Circular Doubly Linked List")


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
	
	def escribir(self):

		cadena=" "
		codigo=0
		unoPrimero=self.first
		unoUltimo=self.last
		DosPrimero=self.first

		if self.first != None:

			while unoPrimero!=unoUltimo:

				cadena+=str(codigo)
				cadena+="[label=\""
				cadena+=unoPrimero.user
				cadena+="\"];\n"

				unoPrimero=unoPrimero.next
				codigo+=1

		else: 
			#stdscr.addstr(5,5,"La lista esta vacia")
			cadena+=str(unoPrimero)
			cadena+="[label=\"null\"]"
			print("VACIO")


		return cadena


	def graph_list_user(self):

		cadena=" "
		codigo=0
		codigonuevo=0
		unoPrimero=self.first
		dosPrimero=self.first

		unoUltimo=self.last
		dosUltimo=self.last
		

		if self.first != None:

			while unoPrimero!=unoUltimo:

				cadena+=str(unoPrimero)
				cadena+="[label=\""
				cadena+=unoPrimero.user
				cadena+="\"];\n"

				unoPrimero=unoPrimero.next
				

		else: 
			
			cadena+=str(unoPrimero)
			cadena+="[label=\"null\"]"
			print("VACIO")


		while dosPrimero != dosUltimo:

			cadena+=str(dosPrimero)

			if dosPrimero != dosUltimo:
				cadena+="->"
				dosPrimero=dosPrimero.next

		cadena+=str(self.first)
			
		
		cadena+="\n"
		cadena+="[dir=both style=tapered arrowsize=0.5 penwidth=1 color=black];\n"


		f=open("user_list.dot","w")
		f.write("digraph Lista_Simple{\n label=Lista_de_Usuarios; \n labelloc=t; \n")
		f.write("node[margin=0.3 fontcolor=black shape=box];\n")
		f.write("{rank=same;\n")

		f.write(cadena)
		
		f.write("} }")
		f.close()

		os.system("dot user_list.dot -Tpng -o user_list.png")
		os.system("xdg-open user_list.png")
		
		



#-------Example to use the list-------
'''
lcd=Circular_Doubly_Linked_List()#CREATE A NEW Circular_Doubly_Linked_List
lcd.add(NodeLCD("mario"))#ADD ELEMENT 1
lcd.add(NodeLCD("raul"))#ADD ELEMENT 2
lcd.add(NodeLCD("carlos"))#ADD ELEMENT 3
lcd.add(NodeLCD("sofia"))#ADD ELEMENT 4
lcd.add(NodeLCD("alejandra"))#ADD ELEMENT 5
lcd.print_Circular_Doubly_Linked_List()#PRINT THE LIST '''

