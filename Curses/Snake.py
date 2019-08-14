

import curses 
from curses import textpad
import time
import random
import Food
import Options
import sys
sys.path.insert(0,'Structures')
from lista_doble import Doubly_Linked_List,NodeLD
from Pila import Stack,NodeStack
from Cola import NodeQueue,Queue
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import Lista_Circular_doble
ld=Doubly_Linked_List()
fd=Food.Food_Snake()
pil=Stack()
col=Queue()

		
def dar_comida(stdscr):
	fd=Food.Food_Snake()

	tipo=random.randint(1,60)

	if tipo <=10:
		stdscr.addstr(int(fd.get_ycomida()),int(fd.get_xcomida()),"*")

	else:
		stdscr.addstr(int(fd.get_ycomida()),int(fd.get_xcomida()),"+")




def Boody(stdscr):
	#ld=Doubly_Linked_List()

	try:
		seguir=0
		if Options.lcd.get_user() is "n":
			stdscr=curses.initscr()
			stdscr.border(0)
			curses.curs_set(0)
			curses.echo()
			stdscr.keypad(True)
			#print("no hay usuario seleccionado")
			stdscr.addstr(2,3,"NO se ha selecionado un Usuario!!!!")
			stdscr.addstr(5,3,"Ingrese un Nombre:")
			
			stdscr.addstr(5,22," "*15,curses.A_UNDERLINE)
			usuario_nuevo=stdscr.getstr(5,22)
			curses.noecho()
			#curses.curs_set(0)
			#stdscr.keypad(False)#para probar
			
			if usuario_nuevo.isalpha() is True:
				stdscr.addstr(7,3,"Nombre Correcto :)")
				stdscr.addstr(9,3,usuario_nuevo)
				Options.lcd.add(Lista_Circular_doble.NodeLCD(str(usuario_nuevo)))
			#time.sleep(1)
				seguir=1
				stdscr.getch()
				stdscr.clear()
			else:
				stdscr.addstr(8,3,"Debe ser solo un nombre escrita de forma correcta,Gracias :(")
				stdscr.getch()
				stdscr.clear()
			#stdscr.addstr(6,6,"Ingrese su Nombre:")

			time.sleep(3)


		if seguir==1 or Options.lcd.get_user() is not "n":
			seguir=0
			ld.remove_all()
			pil.pop_all()
			#col.dequeue_all()
			stdscr.keypad(True)
			stdscr=curses.initscr()
			curses.curs_set(0)
			stdscr.border(0)
			stdscr.nodelay(1)

	

			stdscr.addstr(1,4,"Name:")
			stdscr.addstr(1,10,Options.lcd.get_user())
			#stdscr.addstr(1,10,usuario_nuevo)
			score=0
			score2=0
			score_total=0
			score_text="Score: {}".format(score)
			stdscr.addstr(1,35,score_text)

			aumento=1
			cont=0
			rapido=300
	

    

			al,an= stdscr.getmaxyx()
			box = [[3,3], [al-2, an-3]]
			textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

			puntox=an//2
			puntoy=al//2

    
			ld.add_first(NodeLD(puntox+1,puntoy))
			ld.add_first(NodeLD(puntox,puntoy))
			ld.add_first(NodeLD(puntox-1,puntoy))
	
	
			salida=KEY_LEFT

			face=ld.head

    
			while face is not None:
				stdscr.addstr(int(face.posy),int(face.posx),"#")
				face=face.next
      

			alimento=fd.pintar_comida(stdscr)
			fd.pintar_obstaculos(stdscr)
    
			while salida != 120:

		
				stdscr.timeout(rapido)
				tecla=stdscr.getch()

        
				if tecla is not  -1: 

					salida=tecla  


				if salida == curses.KEY_RIGHT:
					puntox=puntox+1
			


				elif salida== curses.KEY_LEFT:
					puntox=puntox-1
			
            
				elif salida == curses.KEY_DOWN:
					puntoy=puntoy+1
			
           
				elif salida == curses.KEY_UP:
					puntoy=puntoy-1
			

        
		
				ld.add_first(NodeLD(puntox,puntoy))

				if (puntoy == fd.get_obsy()) and (puntox == fd.get_obsx()):

					print("Game Over")
					score_total=score+score2
					col.enqueue(NodeQueue(Options.lcd.get_user(),str(score_total)))
					time.sleep(2)
					#ld.graph_snake()
					salida=120

		

				if (puntoy == fd.get_ycomida()) and (puntox == fd.get_xcomida() and score < 15):
					#alimento=fd.pintar_comida(stdscr)
					#ast="*"
					#mas="+"
					score_text="Score: {}".format("   ")
					stdscr.addstr(1,35,score_text)

					if alimento == '*':
						score=score-1
						stdscr.refresh()
						score_text="Score: {}".format(score)
						stdscr.addstr(1,35,score_text)
						stdscr.addstr(int(ld.get_lasty()),int(ld.get_lastx())," ")
						pil.pop()

						if score < 0:
							nada="nad2"
						else:
							ld.remove_last()
				

					elif alimento == '+':
						score+=1
						stdscr.refresh()
						score_text="Score: {}".format(score)
						stdscr.addstr(1,35,score_text)
						ld.add_first(NodeLD(puntox,puntoy))
						pil.push(NodeStack(puntox,puntoy))

			





					alimento=fd.pintar_comida(stdscr)	


				if (puntoy == fd.get_ycomida()) and (puntox == fd.get_xcomida() and score >= 15):

					rapido=85
					score_text2="Score: {}".format("   ")
					stdscr.addstr(1,35,score_text2)

					if alimento == '*':
						score2=score2-1
						stdscr.refresh()
						#score_text2="Score: {}".format("   ")
						#stdscr.addstr(1,35,score_text2)
						score_text2="Score: {}".format(score2)
						stdscr.addstr(1,35,score_text2)
						stdscr.addstr(int(ld.get_lasty()),int(ld.get_lastx())," ")
						pil.pop()
						ld.remove_last()
				

					elif alimento == '+':
						score2+=1
						stdscr.refresh()
						#score_text2="Score: {}".format("   ")
						#stdscr.addstr(1,35,score_text2)
						score_text2="Score: {}".format(score2)
						stdscr.addstr(1,35,score_text2)
						ld.add_first(NodeLD(puntox,puntoy))
						pil.push(NodeStack(puntox,puntoy))

			

					alimento=fd.pintar_comida(stdscr)

			


				stdscr.addstr(int(ld.get_lasty()),int(ld.get_lastx())," ")
				ld.remove_last()
        		#stdscr.addstr(ld.remove_last(),," ")
        
				face=ld.head
				while face != None:

					stdscr.addstr(int(face.posy),int(face.posx),"#")
            		#print(ld.head.posy,end=",")
            		#print(ld.head.posx)
					face=face.next
					stdscr.refresh()

				stdscr.refresh()





	except curses.error :
		print("error")
