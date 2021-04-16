import curses
class Player :   

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        



    # def setposY(self, newLocated):
    #     self._located = newLocated
    # located = property(_getlocated, _setlocated)


    # def movePlayer(self, key, stdscr) :
    #     if 2 < self.posX < 23 and 3 < self.posY < 9:
    #         if key == curses.KEY_UP : 
    #             stdscr.addstr(self.posY,self.posX,  " ")
    #             self.posY = self.posY - 1
    #             stdscr.addstr( self.posY,self.posX, "P")
    #             stdscr.refresh()
    #         if key == curses.KEY_DOWN : 
    #             stdscr.addstr(self.posY,self.posX,  " ")
    #             self.posY = self.posY + 1
    #             stdscr.addstr( self.posY,self.posX, "P")
    #             stdscr.refresh()
    #         if key == curses.KEY_RIGHT : 
    #             stdscr.addstr(self.posY,self.posX,  " ")
    #             self.posX = self.posX + 1
    #             stdscr.addstr( self.posY,self.posX, "P")
    #         if key == curses.KEY_LEFT : 
    #             stdscr.addstr(self.posY,self.posX,  " ")
    #             self.posX = self.posX - 1
    #             stdscr.addstr( self.posY,self.posX, "P")