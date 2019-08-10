
import curses
from curses import textpad
import csv
import time
import random
import sys
sys.path.insert(0,'Structures')
import Lista_Circular_doble
import lista_doble


from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

lcd=Lista_Circular_doble.Circular_Doubly_Linked_List()
ld=lista_doble.Doubly_Linked_List()
#nod=Lista_Circular_doble.NodeLCD(" ")






def one_play(stdscr):# <<<<<-------------------------METHOD CALLED one_play------------------------->>>>>

    stdscr=curses.initscr()
    #stdscr.border(0)
    curses.curs_set(0)
    stdscr.addstr(1,4,"Name:")
    stdscr.addstr(1,35,"Score:")
    stdscr.addstr(1,55,"Press  'g' to Play")
    score=0
    salida=48
    stdscr.addstr(1,43,str(score))
    #dato=ld.head
    
    al,an= stdscr.getmaxyx()
    box = [[3,3], [al-2, an-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    puntox=an//2
    puntoy=al//2

  

    ld.add_first(lista_doble.NodeLD(puntoy,puntox+1))
    ld.add_first(lista_doble.NodeLD(puntoy,puntox))
    ld.add_first(lista_doble.NodeLD(puntoy,puntox-1))

    face=ld.head

    while face is not None:
        stdscr.addstr(int(ld.head.posx),int(ld.head.posy),"#")
        #print(face.posy,end=",")
        #print(face.posx)
        face=face.next
        ld.head=ld.head.next
    
    
    while salida != 120:

        tecla=stdscr.getch()

        if tecla in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP,120]:
            posicion=tecla


            #face=ld.head
            #tail=ld.last
        
        #stdscr.addstr(puntoy,puntox," ")

        if posicion == curses.KEY_RIGHT:
            puntox=puntox+1
            ld.add_first(lista_doble.NodeLD(puntoy,puntox))


        elif posicion== curses.KEY_LEFT:
            puntox=puntox-1
            ld.add_first(lista_doble.NodeLD(puntoy,puntox))
            
            
        elif posicion == curses.KEY_DOWN:
            puntoy=puntoy+1
            ld.add_first(lista_doble.NodeLD(puntoy,puntox))
            
           
        elif posicion== curses.KEY_UP:
            puntoy=puntoy-1
            ld.add_first(lista_doble.NodeLD(puntoy,puntox))

        elif posicion==120:
            salida=120


        
        #ld.remove_last()
        
        while ld.head != None:
            stdscr.addstr(int(ld.head.posx),int(ld.head.posy),"#")
            #print(face.posy,end=",")
            #print(face.posx)
            ld.head=ld.head.next

        

  
    

    #stdscr.getch()
    stdscr.refresh()

def two_scoreboard(stdscr):# <<<<<-------------------------METHOD CALLED two_scoreboard------------------------->>>>>

    stdscr=curses.initscr()
    stdscr.border(0)
    curses.curs_set(0)
    stdscr.addstr(5,5,"two")

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
            

        elif report_type==98:
            print("m")

        elif report_type==99:
            print("m")

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
    


