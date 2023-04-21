# Importing turtle
import turtle

# Forming a Screen
wd = turtle.Screen()
wd.bgcolor("White")
wd.title("Logo - Coding Ninjas")


#Initialising the turtle object
tt = turtle.Turtle()

# Setting pen for drawing the circle
tt.color("Orange")
tt.width(32)

# Drawing the C shape of the logo
tt.backward(60)
for x in range(180):
    tt.backward(1)
    tt.right(1)
tt.backward(60)

# Setting pen for drawing the eyes
tt.color("Black")
tt.width(5)

# Positioning the pen to draw left eye
tt.up()
tt.left(90)
tt.forward(45)
tt.right(90)
tt.forward(80)

#Drawing the left Eye
tt.down()
tt.left(75)
tt.begin_fill()
tt.circle(15,180)
tt.end_fill()
tt.hideturtle()

#Repositioning for the right eye
tt.up()
tt.right(75)
tt.forward(20)

# Drawing the right eye
tt.down()
tt.right(75)
tt.begin_fill()
tt.circle(15,180)
tt.end_fill()

# Finish by turtle.done() command
turtle.done()
