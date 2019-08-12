

import curses 
from curses import textpad
import time
import random
import Food
import sys
sys.path.insert(0,'Structures')
from lista_doble import Doubly_Linked_List,NodeLD
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

ld=Doubly_Linked_List()
fd=Food.Food_Snake()

		
def dar_comida(stdscr):
	fd=Food.Food_Snake()

	tipo=random.randint(1,60)

	if tipo <=10:
		stdscr.addstr(int(fd.get_ycomida()),int(fd.get_xcomida()),"*")

	else:
		stdscr.addstr(int(fd.get_ycomida()),int(fd.get_xcomida()),"+")




def Boody(stdscr):
	#ld=Doubly_Linked_List()
	ld.remove_all()
	stdscr=curses.initscr()
	curses.curs_set(0)
	stdscr.nodelay(1)
	stdscr.addstr(1,4,"Name:")
	#stdscr.addstr(1,35,"Score:")
	stdscr.addstr(1,55,"Press  'g' to Play")
	score=0
	score2=0
	score_total=0
	score_text="Score: {}".format(score)
	stdscr.addstr(1,35,score_text)

	aumento=1
	cont=0
	rapido=300
	#salida=48
	#stdscr.addstr(1,43,str(score))
    #dato=ld.head

    

	al,an= stdscr.getmaxyx()
	box = [[3,3], [al-2, an-3]]
	textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

	puntox=an//2
	puntoy=al//2

    
	ld.add_first(NodeLD(puntox+1,puntoy))
	ld.add_first(NodeLD(puntox,puntoy))
	ld.add_first(NodeLD(puntox-1,puntoy))
	
	#Food.food(stdscr)funciona que esta en otro archivo pero no es una clase
	#Food(stdscr) si funciona con el metodo que esta hasta arriba



	

	salida=KEY_LEFT

 	#ld.graph_snake()

	face=ld.head

    
	#try:
	while face is not None:
		stdscr.addstr(int(face.posy),int(face.posx),"#")
		
        #print(face.posy,end=",")
        #print(face.posx)
		face=face.next
        #ld.head=ld.head.next
    #ld.graph_sake()
    #except curses.error:
     #   pass


	#dar_comida(stdscr)<<<<<<<<<<<
	alimento=fd.pintar_comida(stdscr)
	fd.pintar_obstaculos(stdscr)
    
	while salida != 120:

		
		stdscr.timeout(rapido)
		tecla=stdscr.getch()

        #if tecla in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP,120,103]:
            #posicion=tecla
		if tecla is not  -1: 

			salida=tecla  


		if salida == curses.KEY_RIGHT:
			puntox=puntox+1
			'''ld.add_first(NodeLD(puntox,puntoy))
            ld.remove_last()'''


		elif salida== curses.KEY_LEFT:
			puntox=puntox-1
			'''ld.add_first(NodeLD(puntox,puntoy))
            ld.remove_last()'''
            
		elif salida == curses.KEY_DOWN:
			puntoy=puntoy+1
			'''ld.add_first(NodeLD(puntox,puntoy))
            ld.remove_last()'''
           
		elif salida == curses.KEY_UP:
			puntoy=puntoy-1
			'''ld.add_first(NodeLD(puntox,puntoy))
            ld.remove_last()'''

        
		
		ld.add_first(NodeLD(puntox,puntoy))

		if (puntoy == fd.get_obsy()) and (puntox == fd.get_obsx()):

			print("Game Over")
			#ld.graph_snake()
			salida=120

		

		if (puntoy == fd.get_ycomida()) and (puntox == fd.get_xcomida() and score < 15):
			#alimento=fd.pintar_comida(stdscr)
			#ast="*"
			#mas="+"

			if alimento == '*':
				score=score-1
				stdscr.refresh()
				score_text="Score: {}".format(score)
				stdscr.addstr(1,35,score_text)
				stdscr.addstr(int(ld.get_lasty()),int(ld.get_lastx())," ")
				ld.remove_last()
				

			elif alimento == '+':
				score+=1
				stdscr.refresh()
				score_text="Score: {}".format(score)
				stdscr.addstr(1,35,score_text)
				ld.add_first(NodeLD(puntox,puntoy))

			





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
				ld.remove_last()
				

			elif alimento == '+':
				score2+=1
				stdscr.refresh()
				#score_text2="Score: {}".format("   ")
				#stdscr.addstr(1,35,score_text2)
				score_text2="Score: {}".format(score2)
				stdscr.addstr(1,35,score_text2)
				ld.add_first(NodeLD(puntox,puntoy))

			

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



