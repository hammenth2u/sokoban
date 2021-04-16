import curses
import time
import player
import target
import wall

def main(stdscr):
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    joueur = player.Player(3,4)
    target_one = target.Target(4,6) 
    
    while True:
        entry = stdscr.getch()
        stdscr.addstr(0,0,f"Hello bienvenue dans le jeu sokoban")
        

        stdscr.addstr(2,0, f"#########################")
        stdscr.addstr(3,0, f"#                       #")
        stdscr.addstr(4,0, f"#                       #")
        stdscr.addstr(5,0, f"#                       #")
        stdscr.addstr(6,0, f"#                       #")
        stdscr.addstr(7,0, f"#                       #")
        stdscr.addstr(8,0, f"#                       #")
        stdscr.addstr(9,0, f"#                       #")
        stdscr.addstr(10,0, f"#########################")

        

        # stdscr.addstr(joueur.posX, joueur.posY, "P")
        stdscr.addstr(target_one.posX, target_one.posY, "O")



        # stdscr.clear()
        # h, w = stdscr.getmaxyx()
        
        # stdscr.addstr(0, 0, f"{str(h)}, {str(w)}")
        if entry == curses.KEY_UP:
            joueur.movePlayer(curses.KEY_UP, stdscr)
        if entry == curses.KEY_DOWN:
            joueur.movePlayer(curses.KEY_DOWN, stdscr)
        if entry == curses.KEY_LEFT:
            joueur.movePlayer(curses.KEY_LEFT, stdscr)
        if entry == curses.KEY_RIGHT:
            joueur.movePlayer(curses.KEY_RIGHT, stdscr)


    curses.endwin()

if __name__ == "__main__":

    curses.wrapper(main)