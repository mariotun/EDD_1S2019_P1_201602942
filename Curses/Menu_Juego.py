 
import sys
sys.path.insert(0,'Structures')
import Lista_Circular_doble
#from Structures import Lista_Circular_doble 
#from Structures.Cola import *
import curses
import time
import csv
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

options=["1.Play","2.Scoreboard","3.User Selection","4.Reports","5.Bulk Loading","6.Exit "]
lcd=Lista_Circular_doble.Circular_Doubly_Linked_List()

'''lcd=Lista_Circular_doble.Circular_Doubly_Linked_List()
lcd.add(Lista_Circular_doble.NodeLCD("mario"))
lcd.add(Lista_Circular_doble.NodeLCD("karla"))
lcd.add(Lista_Circular_doble.NodeLCD("sofia"))
lcd.print_Circular_Doubly_Linked_List()'''



def Options_Menu(stdscr):

    
  #  stdscr.clear()
    h,w=stdscr.getmaxyx()

    for i ,row in enumerate(options):
        x=w//2 -len(row)//2
        y=h//2 -len(options) + i
        stdscr.addstr(y,x,row)


    while 1:

        number=stdscr.getch()
        #stdscr.clear()

        if number == 49:
            stdscr.addstr(15,15,"Ingresando a Opcion numero 1 (Play)...")
            #stdscr.refresh()
            #time.sleep(3)
            #exit()
        elif number == 50:
            stdscr.addstr(15,15,"Ingresando a Opcion numero 2 (Scoreboard)...")
           
            
        elif number == 51:
            stdscr.addstr(15,15,"Ingresando a Opcion numero 3 (User Selection)...")
            stdscr.refresh()
            time.sleep(5)
            stdscr.clear()
            stdscr.refresh()
            lcd.print_Circular_Doubly_Linked_List()
           # stdscr.refresh()
            stdscr.addstr(20,5,"PRESIONE x PARA SALIR...")
            stdscr.getch()

           # stdscr.refresh()


            
        elif number==52:
            stdscr.addstr(15,15,"Ingresando a Opcion numero 4 (Reports)...")

        elif number==53:
            
            stdscr.addstr(15,15,"Se esta leyendo el archivo de usuarios (Bulk Loading)...")
            stdscr.refresh()
            time.sleep(5)
            with open('Curses/Users.csv') as archivo:

                leer = csv.reader(archivo, delimiter=',')
                lineas = 0
                escribir_otro=""
                #lcd=Lista_Circular_doble.Circular_Doubly_Linked_List()
    
                for fila in leer:
                    if lineas == 0:
         
                        lineas += 1
                    else:
                        #if int(fila[1]) >= 15 and int(fila[1]) <= 30 : 
                        #print(f'\tEl Juego {fila[0]} demoro {fila[1]} minutos')
           
                        lcd.add(Lista_Circular_doble.NodeLCD(fila[0]))
            
                        lineas+= 1
                
                #lcd.print_Circular_Doubly_Linked_List()
                stdscr.refresh()
                stdscr.addstr(15,15,"--->se ingresaron usuarios a la aplicacion...")
                #stdscr.refresh()
                #lcd.print_Circular_Doubly_Linked_List()


        elif number==54:
            stdscr.addstr(15,15,"Se esta cerrando en Juego...")
            exit()
        elif number==120: 
            stdscr.clear() 
            stdscr.refresh()  
            Options_Menu(stdscr)
            
        #Options_Menu(stdscr)
        stdscr.refresh()
'''
def bulk_loading(self):

    with open('/home/mario/Escritorio/practica1/Users.csv') as archivo:

        leer = csv.reader(archivo, delimiter=',')
        lineas = 0
        escribir_otro=""
        lcd=Lista_Circular_doble.Circular_Doubly_Linked_List()
    
        for fila in leer:
            if lineas == 0:
         
                lineas += 1
            else:
                #if int(fila[1]) >= 15 and int(fila[1]) <= 30 : 
                #print(f'\tEl Juego {fila[0]} demoro {fila[1]} minutos')
           
                lcd.add(Lista_Circular_doble.NodeLCD(fila[0]))
            
                lineas+= 1
'''

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





'''
stdscr=curses.initscr()
stdscr.border(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)




stdscr.addstr(0,25,"Main Menu")
stdscr.refresh()
time.sleep(3)


curses.noecho()
curses.nocbreak()
stdscr.keypad(False)

curses.endwin() '''


'''
import sys,os
import curses

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        title = "Curses example"[:width-1]
        subtitle = "Written by Clay McLeod"[:width-1]
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()

'''
