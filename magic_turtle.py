import turtle
def draw_square():
    tush = turtle.Pen()
    window  = turtle.Screen()
    window.bgcolor('grey')

    count = 1
    for i in range (1,130):
        for count in range (1 , 5,1):
            tush.forward(100)
            tush.right(90)
            tush.speed(1000)
        tush.right(3)    

draw_square()
    
