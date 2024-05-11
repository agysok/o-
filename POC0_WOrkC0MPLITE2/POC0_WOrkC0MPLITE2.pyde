n=-120
y=10

def setup():
    size(380,600)
def draw():
    global y,n
    push()
    background(231,237,230)
    noStroke()
    fill(229,173,30) #цвет пола
    rect(0,370,400,80) #пол
    fill(216,155,0) #цвет части двери 1
    rect(300,220,80,150) # часть двери 1
    fill(237,178,29) #цвет части двери 2
    rect(311,230,60,140) #часть двери 2
    fill(41,41,41) # цвет ручки от двери
    rect(315,290,10,10) #ручка от двери
    fill(0,0,0) #цвет первой ножки кровати 
    rect(0,360,20,35) #первая ножка кровати
    fill(0,0,0) #часть кровати
    rect(0,330,90,35) #часть кровати
    fill(255,3,3) #цвет одеяла
    rect(0,320,90,35) #одеяло
    fill(255,255,255)
    rect(0,310,40,40)
    fill(255,255,255) #цвет части окна 1
    rect(20,30,150,150) #чать окна 1
    fill(0,185,255) #цвет части окна 2
    rect(25,35,60,140) #часть окна 2
    fill(0,185,255) #цвет окна часть 3
    rect(105,35,60,140) #окно часть 3
    fill(170,170,170) #цвет окна часть 4
    rect(90,79,10,27) #окно часть 4
    fill(60,255,3) #цвет травы
    rect(25,125,60,50) #трава
    fill(185,137,13) #цвет тени от стола
    rect(0,450,1000,500) #сама тень
    fill(152,112,11) #цвет стола
    rect(81,520,220,40) #сам стол
    fill(197,198,196) #цвет лютры 1
    rect(170,0,50,60) #часть лютры 1
    fill(255,255,8) #цвет люстры 2
    rect(120,20,150,40) #часть люстры 2
    fill(255,255,255) #цвет люстры 3
    rect(175,40,40,20) #часть люстры 3
    fill(203,503,199)
    rect(90,100,200,60)
    fill(31,130,203)#цвет корпуса
    rect(90,100,200,450)#корпус
    fill(18,109,198)#2 часть
    rect(125,100,130,450)#
    fill(31,130,203)
    rect(85,160,5,50)
    fill(2,36,70)
    ellipse(190,170,110,110)
    fill(0,0,0)
    ellipse(190,170,90,90)
    fill(7,15,57)
    rect(147,145,85,50)
    fill(13,14,21)
    ellipse(165,160,20,20)
    fill(251,255,198)
    ellipse(165,160,10,10)
    fill(13,14,21)
    ellipse(215,160,20,20)
    fill(17,82,46)
    ellipse(215,160,10,10)
    fill(0,0,0)
    ellipse(215,160,5,5)
    fill(148,198,170)
    ellipse(213,158,2,2)
    fill(148,198,170)
    ellipse(217,160,2,2)
    fill(4,10,41) # цвет камеры
    ellipse(165,185,20,20) # камера с лево внизу
    fill(7,72,23)#цвет блик
    ellipse(165,185,10,10)# блики
    fill(144,193,156) #цвет блик
    ellipse(165,185,5,5) #блики
    fill(4,10,41) # цвет камеры
    ellipse(215,185,20,20) # камера с право внизу
    fill(41,70,56) # цвет блик
    ellipse(215,185,10,10) # блики
    fill(110,111,110) # цвет блик
    ellipse(215,185,5,5) # блики
    fill(4,10,41) # цвет камеры
    ellipse(190,170,30,30) #камера по середине
    fill(15,52,34)# цвет блик
    ellipse(190,170,20,20)# блики
    fill(25,36,31)#цвет блик
    ellipse(190,170,10,10)#блики
    fill(240,250,245)#цвет блик
    ellipse(190,170,5,5)#блики 
    fill(83,95,165) 
    translate(width/2, height/2)#надпись поко
    rotate(radians(-90))#надпись поко
    textSize(48)# надпись поко
    textAlign(CENTER, CENTER)#надпись поко
    text("POCO", 0, 0)#надпись поко
    pop()
    fill(0,0,0)
    ellipse(200,y,100,200)
    rect(150,n,100,70)
    n=n+5
    y=y+5
   
    if y>800 and n>800:

        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(224,254,0)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(224,254,0)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(224,254,0)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(224,254,0)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(224,254,0)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(224,254,0)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(224,254,0)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(224,254,0)
        strokeWeight(random(30))
        
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(224,254,0)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        fill(252,144,28)
        point(random(380),random(600))
        strokeWeight(2)
        stroke(252,144,28)
        strokeWeight(random(30))
        
        
        
