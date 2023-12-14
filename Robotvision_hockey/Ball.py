class Ball:
    def __init__(self,y,x,h,w,ball_h,ball_w):#
        self.y=y
        self.x=x
        self.vec=[-1,2]
        self.h=h
        self.w=w
        self.ball_h=ball_h
        self.ball_w=ball_w
    def move(self):
        self.y+=self.vec[0]
        self.x+=self.vec[1]
        if self.y-self.ball_h<0:
            self.y=self.ball_h+1
            self.vec[0]*=-1
        if self.y+self.ball_h>=self.h:
            self.y=self.h-self.ball_h-1
            self.vec[0]*=-1
        if self.x-self.ball_w<0:
            self.x=self.ball_w+1
            self.vec[1]*=-1
        if self.x+self.ball_w>=self.w:
            self.x=self.w-self.ball_w-1
            self.vec[1]*=-1
            
        
    def collision(self,vec):
        self.vec=vec
        
        