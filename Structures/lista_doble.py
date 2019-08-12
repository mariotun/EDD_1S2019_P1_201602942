import os
import curses

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

		
	def graph_snake(self):
		#print("hola")

		otro=" "
		unoPrimero=self.head
		dosPrimero=self.head

		#unoUltimo=self.last
		#dosUltimo=self.last
		

		if self.head != None:

			while unoPrimero != None:

				otro+=str(unoPrimero)
				otro+="[label=\"("
				otro+=str(unoPrimero.posx)
				otro+=","
				otro+=str(unoPrimero.posy)
				otro+=")\"];\n"

				unoPrimero=unoPrimero.next
				

		else: 
			
			otro+=str(unoPrimero)
			otro+="[label=\"null\"]"
			print("VACIO")


		while dosPrimero != None:

			otro+=str(dosPrimero)

			if dosPrimero.next != None:
				otro+="->"

			dosPrimero=dosPrimero.next

		#cadena+=str(self.first)
			
		
		otro+="\n"
		otro+="[dir=both style=tapered arrowsize=0.5 penwidth=1 color=black];\n"


		f=open("snake_list.dot","w")
		f.write("digraph Lista_Snake{\n label=Posicion_Snake; \n labelloc=t; \n")
		f.write("node[margin=0.3 fontcolor=black shape=box];\n")
		f.write("{rank=same;\n")

		f.write(otro)
		
		f.write("} }")
		f.close()

		os.system("dot snake_list.dot -Tpng -o snake_list.png")
		os.system("xdg-open snake_list.png")




	def remove_last(self):


		temporal=self.last
		temporal2=None

		self.last=self.last.previous
		self.last.next=None

		temporal2=temporal
		temporal=temporal.previous

		return temporal2.posy


	def get_lasty(self):
		yget=self.last
		return yget.posy



	def get_lastx(self):
		xget=self.last
		return xget.posx


	'''	
	def print_sanke(stdscr):

    	stdscr=curses.initstr()
    	#stdscr.border(0)
    	curses.curs_set(0)
    	stdscr.addstr(5,5,"two")

    	pr=self.head

        while pr != None:

            stdscr.addstr(int(pr.posx),int(pr.posy),"#")
            #print(face.posy,end=",")
            #print(face.posx)
            pr=pr.next

    	stdscr.getch()
    	stdscr.refresh()
		'''
	def remove_all(self):

		temporal=self.last
		temporal2=None

		while temporal != self.head:
		
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
list2.remove_all()
'''print(list2.remove_last())
print(list2.remove_last())
print(list2.remove_last())'''
list2.print_linkedlist()


	 