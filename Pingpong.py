import turtle
#import mm.py

#Setup
wn = turtle.Screen() #wn is now turtle.Screen() 
wn.title('Ping Pong by @_Lunatic1337') # Titles the game .exe
wn.bgcolor('black') #color
wn.setup(width=1337, height=1080) #Sets res.
wn.tracer(0) #stops auto updating

#Player 1 paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0) #animation speed
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #Stretch paddle
paddle_a.penup()
paddle_a.goto(-350, 0) #set paddle starting position

#Player 2 paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0) #animation speed
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #Stretch paddle
paddle_b.penup()
paddle_b.goto(350, 0) #set paddle starting position

#Ball
ball = turtle.Turtle()
ball.speed(0) #animation speed
ball.shape('circle')
ball.color('white')
ball.penup() #dont draw line 
ball.goto(0, 0)
ball.dx = 0.2 #ball xy ms
ball.dy = -0.2

#pen
pen = turtle.Turtle()
pen.speed(0) #animspeed
pen.color('white')
pen.penup() 
pen.hideturtle()
pen.goto(0,260) #sets position of score
pen.write('Player A:0  Player B:0', align='center', font=('Courier',24,'normal')) #Player text count

#Score
scoreA = 0 #Sets default value to score
scoreB = 0

#paddle move
def paddleAUp(): #ms of paddles
    y = paddle_a.ycor()
    y +=20 #sets how much the paddle will move
    paddle_a.sety(y)
def paddleADown():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddleBUp():
    y = paddle_b.ycor()
    y +=20 
    paddle_b.sety(y)
def paddleBDown():
    y = paddle_b.ycor()
    y -=20 
    paddle_b.sety(y)

#OnKeyPress
wn.listen()
wn.onkeypress(paddleAUp, 'w') #left paddle
wn.onkeypress(paddleADown, 's')
wn.onkeypress(paddleBUp, 'Up') #right paddle
wn.onkeypress(paddleBDown, 'Down')

#Game loop
while True:
    wn.update() #this updates screen

    #Ball MS
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290: #checks y cordinates
        ball.sety(290) #makes it so the ball bounces back
        ball.dy *= -1
    if ball.ycor() < -290: #checks other paddle
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390: #checks x cordinates
        ball.setx(390)
        ball.dx *= -1
        scoreA +=1 #add 1 point ot score
        pen.clear() #clear previous text and insert new score text
        pen.write('Player A:{}  Player B:{}'.format(scoreA, scoreB), align='center', font=('Courier',24,'normal'))
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write('Player A:{}  Player B:{}'.format(scoreA, scoreB), align='center', font=('Courier',24,'normal'))

    #collision check
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40  and ball.ycor() >  paddle_b.ycor() -40): #checks if the ball hit the paddle
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40  and ball.ycor() >  paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
