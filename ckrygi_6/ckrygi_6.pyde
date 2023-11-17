y=80
x=50
x=60


def setup():
    size(600,700)
def draw(): 
    global x,y
    fill(y,x,800) #красный 1 
    ellipse(100,100,50,50)
    global x,y
    fill(y,x,122) #красный 2
    ellipse(200,200,50,50)
    global x,y
    fill(y,x,255) # синий 3
    ellipse(300,300,50,50)
    global x,y
    fill(y,x,0) # желтый 4
    ellipse(400,400,50,50)
    global x,y
    fill(y,x,255) # голубой 5
    ellipse(500,500,50,50)
    global x,y
    fill(x,y,255) # фиолетовый 6
    ellipse(560,600,50,50)
  
    

    x=x+1
    y=y+1
    x=x+1
