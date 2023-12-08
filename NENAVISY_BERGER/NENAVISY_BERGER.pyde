x=250
y1=4
y=3
img=0


def setup(): 
   size(500,600)
   img = loadImage('dla burgera.jpg')
def draw():
    global y1, y,img
    global x
    image(0,0,img)
    fill(196,196,196)
   
    background(255,255,255)
    noStroke()
    ellipse(250,400,250,60)#x тень
    fill(240,184,116)
    ellipse(250,y,250,80)#x булочка 1
    y=y+2
    if y>370:
        noLoop()
    fill(80,46,33)
    ellipse(250,y1,250,70)#x котлета
    y1=y1+1
    if y1>370:
        noLoop()
    fill(235,250,40)
    rect(130,300,250,50) #x сырочек
    fill(108,198,30)
    ellipse(130,300,50,50) #x купасточка
    ellipse(170,300,50,50)#x купасточка
    ellipse(210,300,50,50)#x купасточка
    ellipse(250,300,50,50)#x купасточка
    ellipse(290,300,50,50)#x купасточка
    ellipse(230,300,50,50)#x купасточка
    ellipse(270,300,50,50)#x купасточка
    ellipse(320,300,50,50)#x купасточка
    ellipse(370,300,50,50)#x купасточка
    ellipse(350,300,50,50) #x купасточка
    fill(71,129,21)
    fill(255,5,14)
    ellipse(250,260,250,80) #x помидор часть 1 
    fill(224,77,82)
    ellipse(250,260,230,60) #xпомидор часть 2
    fill(240,184,116)
    ellipse(250,230,250,120)
    fill(0,0,0)
