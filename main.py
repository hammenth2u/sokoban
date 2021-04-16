import curses
import time
import player
import sys

listWall = [[2,0], [2,1], [2,2], [2,3], [2,4], [2,5],[2,6],[2,7], [2,8], [2,9], [2,10],[2,11], [2,12], [2,13], [2,14], [2,15], [2,16], [2,17], [2,18], [2,19], [2,20], [3,0], [3,20], [4,0], [4,20],[5,0], [5,20],[6,0], [6,1], [6,2], [6,3], [6,4], [6,5],[6,6],[6,7], [6,8], [6,9], [6,10],[6,11], [6,12], [6,13], [6,14], [6,15], [6,16],[6,17],[6,18], [6,19], [6,20],  [5,7]]
joueur = player.Player(4,4)
listCible = [[4,6], [4,9]]
listCaisse = [[4,5], [4,13]]
joueurPos = [joueur.posX,joueur.posY]

presenceCaisse = False
 
def resetMap(stdscr):
    stdscr.clear()
    listWall = [[2,0], [2,1], [2,2], [2,3], [2,4], [2,5],[2,6],[2,7], [2,8], [2,9], [2,10],[2,11], [2,12], [2,13], [2,14], [2,15], [2,16], [2,17], [2,18], [2,19], [2,20], [3,0], [3,20], [4,0], [4,20],[5,0], [5,20],[6,0], [6,1], [6,2], [6,3], [6,4], [6,5],[6,6],[6,7], [6,8], [6,9], [6,10],[6,11], [6,12], [6,13], [6,14], [6,15], [6,16],[6,17],[6,18], [6,19], [6,20],  [5,7]]
    
    joueurPos = [4,4]
    joueur.posX = 4
    joueur.posY = 4
    listCible = [[4,6], [4,9]]
    listCaisse = [[4,5], [4,13]]

    for wall in listWall:
        stdscr.addstr(wall[0],wall[1], f"#" )    

    for cible in listCible:
        stdscr.addstr(cible[0],cible[1], f"O" )    

    for caisse in listCaisse:
        stdscr.addstr(caisse[0],caisse[1], f"X" )        
    
    stdscr.addstr(joueur.posX, joueur.posY, "P")




def haut(stdscr):
    joueurPos = [joueur.posX,joueur.posY]
    joueurNextPos = [joueur.posX  - 1, joueur.posY]
    joueurNext2Pos = [joueur.posX  - 2, joueur.posY]
    


    if not (joueurNextPos in listCaisse):
        if not (joueurNextPos in listWall):
            stdscr.addstr(joueur.posX, joueur.posY,  " ")
            joueur.posX = joueur.posX - 1

            for cible in listCible:
                stdscr.addstr(cible[0],cible[1], f"O" )    

            stdscr.addstr( joueur.posX, joueur.posY, "P")
            stdscr.refresh()
            joueurPos = [joueur.posX,joueur.posY]
    else:
        if not (joueurNext2Pos in listWall):
            stdscr.addstr(joueur.posX, joueur.posY,  " ")
            stdscr.addstr(joueur.posX - 1, joueur.posY,  " ")
            joueur.posX = joueur.posX - 1

            for cible in listCible:
                stdscr.addstr(cible[0],cible[1], f"O" )    

            stdscr.addstr( joueur.posX, joueur.posY, "P")
            stdscr.addstr( joueur.posX - 1, joueur.posY, "X")
            stdscr.refresh()
            joueurPos = [joueur.posX,joueur.posY]

            i = listCaisse.index(joueurNextPos)
            listCaisse[i] = [joueur.posX - 1, joueur.posY]

            if listCaisse[i] in listCible:
                if len(listCaisse) > 0:
                    del listCaisse[i]  
                    longueur = len(listCaisse)
                    if longueur == 0:
                        stdscr.addstr(20, 0, f"Partie gagnée !")         
                

              
    

def bas(stdscr):
    joueurPos = [joueur.posX,joueur.posY]
    joueurNextPos = [joueur.posX  + 1, joueur.posY]
    joueurNext2Pos = [joueur.posX  + 2, joueur.posY]
    

    if not (joueurNextPos in listCaisse):
        if not (joueurNextPos in listWall):
            stdscr.addstr(joueur.posX, joueur.posY,  " ")
            joueur.posX = joueur.posX + 1

            for cible in listCible:
                stdscr.addstr(cible[0],cible[1], f"O" )    

            stdscr.addstr( joueur.posX, joueur.posY, "P")
            stdscr.refresh()
            joueurPos = [joueur.posX,joueur.posY]
    else:
        if not (joueurNext2Pos in listWall):
            stdscr.addstr(joueur.posX, joueur.posY,  " ")
            stdscr.addstr(joueur.posX + 1, joueur.posY,  " ")
            joueur.posX = joueur.posX + 1

            for cible in listCible:
                stdscr.addstr(cible[0],cible[1], f"O" )    

            stdscr.addstr( joueur.posX, joueur.posY, "P")
            stdscr.addstr( joueur.posX + 1, joueur.posY, "X")
            stdscr.refresh()  
            joueurPos = [joueur.posX,joueur.posY]   

            i = listCaisse.index(joueurNextPos)
            listCaisse[i] = [joueur.posX + 1, joueur.posY]  

            if listCaisse[i] in listCible:
                if len(listCaisse) > 0:
                    del listCaisse[i]   
                    longueur = len(listCaisse)
                    if longueur == 0:
                        stdscr.addstr(20, 0, f"Partie gagnée !")            



def gauche(stdscr):
    joueurPos = [joueur.posX,joueur.posY]
    joueurNextPos = [joueur.posX  , joueur.posY - 1]
    joueurNext2Pos = [joueur.posX  , joueur.posY - 2]
    

    if not (joueurNextPos in listCaisse):
        if not (joueurNextPos in listWall):
            stdscr.addstr(joueur.posX, joueur.posY,  " ")
            joueur.posY = joueur.posY - 1

            for cible in listCible:
                stdscr.addstr(cible[0],cible[1], f"O" )    

            stdscr.addstr( joueur.posX, joueur.posY, "P")
            stdscr.refresh()
            joueurPos = [joueur.posX,joueur.posY]
    else:
        if not (joueurNext2Pos in listWall):
            stdscr.addstr(joueur.posX, joueur.posY,  " ")
            stdscr.addstr(joueur.posX , joueur.posY - 1,  " ")
            joueur.posY = joueur.posY - 1

            for cible in listCible:
                stdscr.addstr(cible[0],cible[1], f"O" )    

            stdscr.addstr( joueur.posX, joueur.posY, "P")
            stdscr.addstr( joueur.posX , joueur.posY - 1, "X")
            stdscr.refresh()  
            joueurPos = [joueur.posX,joueur.posY] 

            i = listCaisse.index(joueurNextPos)
            listCaisse[i] = [joueur.posX, joueur.posY - 1]

            if listCaisse[i] in listCible:
                if len(listCaisse) > 0:
                    del listCaisse[i]   
                    longueur = len(listCaisse)
                    if longueur == 0:
                        stdscr.addstr(20, 0, f"Partie gagnée !")         



def droite(stdscr):  
    joueurPos = [joueur.posX,joueur.posY]
    joueurNextPos = [joueur.posX  , joueur.posY + 1]
    joueurNext2Pos = [joueur.posX  , joueur.posY + 2]
    

    if not (joueurNextPos in listCaisse):
        if not (joueurNextPos in listWall):
            stdscr.addstr(joueur.posX, joueur.posY,  " ")
            joueur.posY = joueur.posY + 1

            for cible in listCible:
                stdscr.addstr(cible[0],cible[1], f"O" )    

            stdscr.addstr( joueur.posX, joueur.posY, "P")
            stdscr.refresh()
            joueurPos = [joueur.posX,joueur.posY]
    else:
        if not (joueurNext2Pos in listWall):
            stdscr.addstr(joueur.posX, joueur.posY,  " ")
            stdscr.addstr(joueur.posX , joueur.posY + 1,  " ")
            joueur.posY = joueur.posY + 1

            for cible in listCible:
                stdscr.addstr(cible[0],cible[1], f"O" )    

            stdscr.addstr( joueur.posX, joueur.posY, "P")
            stdscr.addstr( joueur.posX , joueur.posY + 1, "X")
            stdscr.refresh()     
            joueurPos = [joueur.posX,joueur.posY]  

            i = listCaisse.index(joueurNextPos)
            listCaisse[i] = [joueur.posX, joueur.posY + 1]  

            if listCaisse[i] in listCible:
                if len(listCaisse) > 0:
                    del listCaisse[i]   
                    longueur = len(listCaisse)
                    if longueur == 0:
                        stdscr.addstr(20, 0, f"Partie gagnée !")

                                          




def main(stdscr):
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
 
    
    stdscr.addstr(0,0,f"Hello bienvenue dans le jeu sokoban")
        

    resetMap(stdscr)

    while True:
        entry = stdscr.getch()

        for cible in listCible:
            stdscr.addstr(cible[0],cible[1], f"O" ) 
    
        if entry == curses.KEY_UP:
            haut(stdscr)
        if entry == curses.KEY_DOWN:
            bas(stdscr)
        if entry == curses.KEY_LEFT:
            gauche(stdscr)
        if entry == curses.KEY_RIGHT:
            droite(stdscr)  
        if entry ==  32:
            resetMap(stdscr) 
        if entry ==  27 or entry == ord('q') or entry == ord('Q'):
            sys.exit()


    curses.endwin()

if __name__ == "__main__":

    curses.wrapper(main)