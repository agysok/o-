y=15 
x=20



def setup():
    size(500,600)
def draw():
    background(250,184,0)
    global y,x
    noStroke()
    ellipse(y,x,50,50)
    y=y+15
    x=x+20
    if x>600 and y>500:
        x=10
    if y==500:
        y=19
