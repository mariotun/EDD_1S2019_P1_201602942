
import curses
#from curses import textpad
import csv
import time
#import random
import sys
sys.path.insert(0,'Structures')
import Lista_Circular_doble
from lista_doble import Doubly_Linked_List,NodeLD
import Snake


from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

lcd=Lista_Circular_doble.Circular_Doubly_Linked_List()
#ld=lista_doble.Doubly_Linked_List()
#ld=Doubly_Linked_List()
#nod=Lista_Circular_doble.NodeLCD(" ")



def one_play(stdscr):# <<<<<-------------------------METHOD CALLED one_play------------------------->>>>>

    #stdscr=curses.initscr()
    #stdscr.border(0)
    #curses.curs_set(0)
    stdscr.clear()
    Snake.Boody(stdscr)

           
    #stdscr.refresh()
     

def two_scoreboard(stdscr):# <<<<<-------------------------METHOD CALLED two_scoreboard------------------------->>>>>

    stdscr=curses.initscr()
    stdscr.border(0)
    curses.curs_set(0)
    stdscr.addstr(2,35,"SCOREBOARD")

    Snake.col.printQueue()
    time.sleep(3)

    stdscr.getch()
    stdscr.refresh()

def three_userselection(stdscr):# <<<<<-------------------------METHOD CALLED three_userselection------------------------->>>>>
	
    
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
                #stdscr.addstr(5,5,dato.posx)
    		else:
                    stdscr.addstr(10,35,temp.user)   
                    lcd.set_user(temp.user)
                    temp=temp.next
                

    		
    		

    	elif direction == KEY_RIGHT:
    		#stdscr.addstr(10,5,"ha presionado la tecla derecha")
    		if temp is None:
    			stdscr.addstr(5,5,"La lista esta vacia")
    		else:
    			     #stdscr.addstr(10,15,"<---")
                    stdscr.addstr(10,35,temp.user)
                    lcd.set_user(temp.user)
                    temp=temp.previous
                    
                

    	elif direction == 120:
    		a=120


		

    #lcd.print_Circular_Doubly_Linked_List()
   
    #stdscr.addstr(20,5,"PRESIONE x PARA SALIR...")
    #stdscr.getch()
    stdscr.refresh()


def four_reports(stdscr):# <<<<<-------------------------METHOD CALLED four_reports------------------------->>>>>

    stdscr=curses.initscr()
    stdscr.border(0)
    curses.curs_set(0)
    stdscr.addstr(5,30,"REPORTS:")
    stdscr.addstr(20,5,"PRESIONE x PARA SALIR...")
    report=["a.Snake Report","b.Score Report","c.Scoreboard Report","d.Users Report"]

    b=48

    ha,wa=stdscr.getmaxyx()

    for i ,row in enumerate(report):
        xa=wa//2 -len(row)//2
        ya=ha//2 -len(report) + i
        stdscr.addstr(ya,xa,row)

    while b != 120:

        report_type=stdscr.getch()

        if report_type==97:
            print("m")
            Snake.ld.graph_snake()

        elif report_type==98:
            print("m")
            Snake.pil.graph_stack_score()

        elif report_type==99:
            print("m")
            Snake.col.graph_Queue_scoreboard()

        elif report_type==100:
            print("m")
            lcd.graph_list_user()

        elif report_type==120:
            b=120




    #stdscr.getch()
    stdscr.refresh()


def five_bulkloading(stdscr):# <<<<<-------------------------METHOD CALLED five_bulkloading------------------------->>>>>

    stdscr=curses.initscr()
    stdscr.border(0)
    curses.curs_set(0)
    '''stdscr.clear()
    curses.curs_set(0)
    curses.echo()
    stdscr.keypad(True)
    stdscr.addstr(2,3,"Ingrese el Nombre del Archivo:")
    stdscr.addstr(2,35," "*15,curses.A_UNDERLINE)
    nombreArchivo=stdscr.getstr(2,35)
    arch="Curses/ {}".format(str(nombreArchivo))
    stdscr.addstr(2,3,arch)
    time.sleep(2)'''

     
    try:
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
    
    except:
        print("no entro en leer")
        pass
	    #stdscr.refresh()           
        #stdscr.addstr(15,15,"--->se ingresaron usuarios a la aplicacion...")   
    


