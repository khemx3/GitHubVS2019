import turtle

class Disk(object):

    def __init__(self,name="",xpos=0,ypos=0,height=20,width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        pass 

    def newpos(self,xpos,ypos):
        pass
        
    def cleardisk(self):
        pass

class Pole(object):

    def __init__(self,name="",xpos=0,ypos=0,thick=10,length=100):
        pass

    def showpole(self):
       pass

    def pushdisk(self,disk):
        pass


    def popdisk(self):
        pass
       
class Hanoi(object):

    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        pass

    def move_disk(self,start,destination):
        pass

    def move_tower(self,n,s,d,w):
        pass
    def solve(self):
        pass



h = Hanoi()
h.solve()
        

