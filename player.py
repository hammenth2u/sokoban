import curses
class Player :   

    def __init__(self, posX, posY, maxPosX, maxPosY, minPosX, minPosY):
        self.posX = posX
        self.posY = posY
        


    def movePlayer(self, key, stdscr) :
        
        if key == curses.KEY_UP : 
            stdscr.addstr(self.posY,self.posX,  " ")
            self.posY = self.posY - 1
            stdscr.addstr( self.posY,self.posX, "P")
            stdscr.refresh()
        if key == curses.KEY_DOWN : 
            stdscr.addstr(self.posY,self.posX,  " ")
            self.posY = self.posY + 1
            stdscr.addstr( self.posY,self.posX, "P")
            stdscr.refresh()
        if key == curses.KEY_RIGHT : 
            stdscr.addstr(self.posY,self.posX,  " ")
            self.posX = self.posX + 1
            stdscr.addstr( self.posY,self.posX, "P")
        if key == curses.KEY_LEFT : 
            stdscr.addstr(self.posY,self.posX,  " ")
            self.posX = self.posX - 1
            stdscr.addstr( self.posY,self.posX, "P")