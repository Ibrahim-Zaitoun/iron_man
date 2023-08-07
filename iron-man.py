face_one = [
  [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),(-40, -20), (0, -20)],

  [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),(40, 120), (0, 120)]
]

face_two = [
  [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),(-80, -230), (-64, -210), (0, -210)],
  
  [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),(100, -46), (50, -40), (40, -30), (0, -30)]
]

face_three = [
  [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),(0, -250)],
  
  [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),(0,-220)]
]

start_point_1= (0,120)
start_point_2= (0,-30)
start_point_3= (0,-220) 

import turtle 

turtle.screensize(canvwidth=500, canvheight=600, bg="black")
wn = turtle.Screen()
wn.bgpic(r"D:\python\Code\projects\fire4.PNG")
wn.setup(width=500,height=600)


iron= turtle.Turtle()
iron.hideturtle()

def draw(face,start_point):      
    iron.penup()
    iron.goto(start_point)
    iron.pendown()
    iron.begin_fill()

    for tup in face:
        for point in tup:
            iron.goto(point)

    iron.end_fill()
    iron.penup()  
       
draw(face_one,start_point_1)
draw(face_two,start_point_2)    
draw(face_three,start_point_3)        

turtle.done()



