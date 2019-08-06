 
#import sys
#sys.path.insert(0,'Structures')
#import Lista_Circular_doble
import Options

import curses
import time
import csv
#from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

options=["1.Play","2.Scoreboard","3.User Selection","4.Reports","5.Bulk Loading","6.Exit "]
#lcd=Lista_Circular_doble.Circular_Doubly_Linked_List()
#opt=Options.menu()
'''lcd=Lista_Circular_doble.Circular_Doubly_Linked_List()
lcd.add(Lista_Circular_doble.NodeLCD("mario"))
lcd.add(Lista_Circular_doble.NodeLCD("karla"))
lcd.add(Lista_Circular_doble.NodeLCD("sofia"))
lcd.print_Circular_Doubly_Linked_List()'''



def Options_Menu(stdscr):

    
  #  stdscr.clear()


    h1,w1=stdscr.getmaxyx()

    for i ,row in enumerate(options):
        x1=w1//2 -len(row)//2
        y1=h1//2 -len(options) + i
        stdscr.addstr(y1,x1,row)


    while 1:

        number=stdscr.getch()
        #stdscr.clear()

        if number == 49:
            stdscr.addstr(15,15,"Ingresando a Opcion numero 1 (Play)...")
            stdscr.clear()
            stdscr.refresh()

            Options.one_play(stdscr)
           
            stdscr.clear()
            Main_Menu(stdscr)
            stdscr.refresh()
            
            
        elif number == 50:
            stdscr.addstr(15,15,"Ingresando a Opcion numero 2 (Scoreboard)...")
            stdscr.clear()
            stdscr.refresh()

            Options.two_scoreboard(stdscr)
           
            stdscr.clear()
            Main_Menu(stdscr)
            stdscr.refresh()


        elif number == 51:
            stdscr.addstr(15,15,"Ingresando a Opcion numero 3 (User Selection)...")
            #stdscr.refresh()
            #time.sleep(5)
            stdscr.clear()
            stdscr.refresh()

            Options.three_userselection(stdscr)
          
            stdscr.clear()
            Main_Menu(stdscr)
            stdscr.refresh()
            
        elif number==52:
            stdscr.addstr(15,15,"Ingresando a Opcion numero 4 (Reports)...")
            stdscr.clear()
            stdscr.refresh()
            
            Options.four_reports(stdscr)
           
            #stdscr.getch() 
            stdscr.clear()
            Main_Menu(stdscr)
            stdscr.refresh()

        elif number==53:
            
            stdscr.addstr(15,15,"Se esta leyendo el archivo de usuarios (Bulk Loading)...")
            
            stdscr.refresh()
            time.sleep(3)

            Options.five_bulkloading(stdscr)

            
           
           
            stdscr.clear()
            Main_Menu(stdscr)
            stdscr.refresh()
            
               


        elif number==54:
            stdscr.addstr(15,15,"Se esta cerrando en Juego...")
            exit()
        elif number==120: 
            stdscr.clear() 
            stdscr.refresh()  
            Options_Menu(stdscr)
       
    

def Main_Menu(stdscr):

    stdscr=curses.initscr()
    stdscr.border(0)
    curses.curs_set(0)

    
    h,w=stdscr.getmaxyx()
    title="Main Menu"
    x=w//2 - len(title)//2
    #y=h//2
    stdscr.addstr(0,x,title)

    Options_Menu(stdscr)

        


    
    stdscr.getch()
    stdscr.refresh()
    
curses.wrapper(Main_Menu)





