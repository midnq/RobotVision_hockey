class Player:
    def __init__(self,y,x):
        self.y=y
        self.x=x
        self.vec=[0,0]
    
    def move(self,y,x):
        self.vec=[y-self.y,x-self.x]
        self.y = y
        self.x = x

