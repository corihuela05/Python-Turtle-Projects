import turtle
t=turtle.Turtle()
screen=turtle.Screen()

def midline(t,length):
        t.fd(length/2)
        t.bk(length)
        t.fd(length/2)
       
#midline(t,100)

def spiral(t,length,mutiplier,numlines,angle):
    newlength=length
    colors=['blue','green','purple','orange']
    for i in range(numlines):
            for color in colors:
                    t.color(color)
                    midline(t,newlength)
                    newlength=newlength*mutiplier
                    t.left(angle)
       
      

spiral(t,50,1.1,10,12)
