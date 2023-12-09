x=200
y1=4
y=3
y3=4
y2=4
y4=5
y5=7
y6=4
y7=9
y8=8
y9=10
y10=11
y11=12
y21=122
img=0



def setup(): 
   size(500,600)
   img = loadImage('dla burgera.jpg')
def draw():
    global y21
    global y11
    global y10
    global y7
    global y8
    global y6
    global y5
    global y4
    global y3
    global y2
    global y1, y,img
    global x
    fill(196,196,196)
    background(255,255,255)
    noStroke()
    ellipse(250,400,250,60)#x тень
    fill(240,184,116)
    ellipse(250,y,250,80)#x булочка 1
    y=y+1.1
    if y>370:
        noLoop()
        ellipse(250,379,250,80)
    loop
    fill(80,46,33)
    ellipse(250,y1,250,70)#x котлета
    y1=y1+1.1
    if y1>358:
        noLoop()
    fill(235,250,40)
    rect(130,y2,250,50) #x сырочек
    y2=y2+1.1
    if y2>300:
        noLoop()
        rect(180,280,250,70)
    loop
    fill(108,198,30)
    ellipse(130,y3,50,50) #x купасточка
    y3=y3+1.1
    if y3>300:
        noLoop()
        ellipse(130,300,50,50)
    loop
    ellipse(170,y4,50,50)#x купасточка
    y4=y4+1.1
    if y4>300:
        noLoop()
        ellipse(130,300,50,50)
    loop
    ellipse(210,y5,50,50)#x купасточка
    y5=y5+1.1
    if y5>300:
        noLoop()
        ellipse(130,300,50,50)
    loop
    ellipse(250,y6,50,50)#x купасточка
    y6=y6+1.1
    if y6>300:
        noLoop()
        ellipse(130,300,50,50)
    loop
    ellipse(290,y7,50,50)#x купасточка
    y7=y7+1.1
    if y7>300:
        noLoop()
        ellipse(130,300,50,50)
    loop
    ellipse(320,y8,50,50)#x купасточка
    y8=y8+1.1
    if y8>300:
        noLoop()
        ellipse(130,300,50,50)
    loop
    ellipse(370,y10,50,50)#x купасточка
    y10=y10+1.1
    if y10>300:
        noLoop()
        ellipse(130,300,50,50)
    loop
    ellipse(350,y11,50,50) #x купасточка
    y11=y11+1.1
    if y11>300:
        noLoop()
        ellipse(130,300,50,50)
    loop
    fill(71,129,21)
    fill(255,5,14)
    ellipse(250,y21,250,80) #x помидор часть 1 
    y21=y21+1

   

       #ellipse(250,260,250,80)
    loop
    fill(224,77,82)
    ellipse(250,260,230,60) #xпомидор часть 2
    fill(240,184,116)
    ellipse(250,230,250,120)
    fill(0,0,0)
