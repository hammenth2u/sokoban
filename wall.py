from entity import Entity
class Wall(Entity):
    def __init__(self,posX,posY):
        Entity.__init__(self,self.posX,self.posY,"#")