import turtle

def draw():

    window = turtle.Screen()
    window.bgcolor("black")
    #Create turtle tina - T
    tina = turtle.Turtle()
    tina.setpos(-300, 200)
    tina.shape("turtle")
    tina.color("pink")
    tina.speed(2)
    #Draw T
    tina.forward(100)
    tina.backward(50)
    tina.right(90)
    tina.forward(100)
    #Create turtle ed - E
    ed = turtle.Turtle()
    ed.setpos(-175, 200)
    ed.shape("turtle")
    ed.color("purple")
    ed.speed(2)
    #Draw E
    ed.forward(50)
    ed.backward(50)
    ed.right(90)
    ed.forward(50)
    ed.left(90)
    ed.forward(25)
    ed.backward(25)
    ed.right(90)
    ed.forward(50)
    ed.left(90)
    ed.forward(50)
    #Create turtle Abi - A
    abi = turtle.Turtle()
    abi.setpos(-100, 0)
    abi.shape("turtle")
    abi.color("red")
    abi.speed(2)
    #Draw A
    abi.left(70)
    abi.forward(100)
    abi.right(140)
    abi.forward(100)
    abi.backward(50)
    abi.right(110)
    abi.forward(35)
    #Create turtle matt - M
    matt = turtle.Turtle()
    matt.setpos(0, 0)
    matt.shape("turtle")
    matt.color("green")
    matt.speed(2)
    #Draw M
    matt.left(90)
    matt.forward(100)
    matt.right(135)
    matt.forward(50)
    matt.left(90)
    matt.forward(50)
    matt.right(135)
    matt.forward(100)
    #Create turtle omar - O
    omar = turtle.Turtle()
    omar.shape("turtle")
    omar.color("white")
    omar.speed(2)
    omar.setpos(150, 0)
    omar.circle(50, 360)
    
    
    
    window.exitonclick()

draw()
