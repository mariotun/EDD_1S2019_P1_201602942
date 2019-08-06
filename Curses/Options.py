
import curses
import csv
import time
import sys
sys.path.insert(0,'Structures')
import Lista_Circular_doble
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

lcd=Lista_Circular_doble.Circular_Doubly_Linked_List()
#nod=Lista_Circular_doble.NodeLCD(" ")






def one_play(stdscr):

    stdscr=curses.initscr()
    stdscr.border(0)
    curses.curs_set(0)
    stdscr.addstr(5,5,"one")

    stdscr.getch()
    stdscr.refresh()

def two_scoreboard(stdscr):

    stdscr=curses.initscr()
    stdscr.border(0)
    curses.curs_set(0)
    stdscr.addstr(5,5,"two")

    stdscr.getch()
    stdscr.refresh()

def three_userselection(stdscr):
	

    stdscr=curses.initscr()
    #stdscr.border(0)
    curses.curs_set(0)

    a=48
    stdscr.addstr(20,5,"PRESIONE x PARA SALIR...")
    stdscr.addstr(10,15,"-->")
    stdscr.addstr(10,60,"<--")
    temp=lcd.first
    #aux=lcd.last

    while a != 120:

    	direction=stdscr.getch()

    	
    	if direction == KEY_LEFT:
    		#stdscr.addstr(10,5,"ha presionado la tecla izquierda")
    		#temp=lcd.first
    		
    		#print(temp.user)
    		if temp is None:
    			stdscr.addstr(5,5,"La lista esta vacia")
    		else:
    			#stdscr.addstr(10,15,"-->")
    			stdscr.addstr(10,35,temp.user)
    			temp=temp.next
    		
    		

    	elif direction == KEY_RIGHT:
    		#stdscr.addstr(10,5,"ha presionado la tecla derecha")
    		if temp is None:
    			stdscr.addstr(5,5,"La lista esta vacia")
    		else:
    			#stdscr.addstr(10,15,"<---")
    			stdscr.addstr(10,35,temp.user)
    			temp=temp.previous

    	elif direction == 120:
    		a=120


		

    #lcd.print_Circular_Doubly_Linked_List()
   
    #stdscr.addstr(20,5,"PRESIONE x PARA SALIR...")
    #stdscr.getch()
    stdscr.refresh()

def four_reports(stdscr):

    stdscr=curses.initscr()
    stdscr.border(0)
    curses.curs_set(0)
    stdscr.addstr(5,5,"four")

    stdscr.getch()
    stdscr.refresh()

def five_bulkloading(stdscr):

    stdscr=curses.initscr()
    stdscr.border(0)
    curses.curs_set(0)
     
    
    with open('Curses/Users.csv') as archivo:

        leer = csv.reader(archivo, delimiter=',')
        lineas = 0
        escribir_otro=""
                #lcd=Lista_Circular_doble.Circular_Doubly_Linked_List()
    
        for fila in leer:
            if lineas == 0:
         
               lineas += 1

            else:

            	lcd.add(Lista_Circular_doble.NodeLCD(fila[0]))
            	#lcd.add(nod(fila[0]))
            	lineas+= 1
    
	    
	    #stdscr.refresh()           
        #stdscr.addstr(15,15,"--->se ingresaron usuarios a la aplicacion...")   
    

    