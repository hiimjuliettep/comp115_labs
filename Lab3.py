import turtle

window = turtle.Screen()

def draw_steps(num_steps):
    pen = turtle.Turtle()
    pen.speed(1)
    for _ in range(num_steps):
        pen.forward(10)
        pen.left(90)
        pen.forward(10)
        pen.right(90)
    pen.shape("blank")
    pen.clear()

def draw_triangle(side_length):
    pen = turtle.Turtle()
    pen.speed(1)
    exterior_angle = 360 / 3  
    for _ in range(3):
        pen.forward(side_length)
        pen.left(exterior_angle)
    pen.shape("blank")
    pen.clear()


#Exercise 1

def draw_sq(side_length):
    pen = turtle.Turtle()
    pen.speed(1)
    exterior_angle = 360 / 4 
    for _ in range(4):
        pen.forward(side_length)
        pen.left(exterior_angle)
    pen.shape("blank")
    pen.clear()

#Exercise 2

def draw_reg_polygon(num_sides, side_length):
    pen = turtle.Turtle()
    pen.speed(1)
    exterior_angle = 360 / num_sides
    for n in range(num_sides):
        pen.forward(side_length)
        pen.right(exterior_angle)
    pen.shape("blank")
    pen.clear()
    
#draw_reg_polygon(6, 20)
        
#Exercise 3

def draw_rectangle(length, width):
    pen = turtle.Turtle()
    pen.speed(1)
    for n in range(2):
        pen.forward(length)
        pen.left(90)
        pen.forward(width)
        pen.left(90)
    pen.shape("blank")
    pen.clear()
    
#draw_rectangle(20, 10)

#Exercise 4

def draw_circles(num_circles):
    radius = 10
    radius_increase = 5
    pen = turtle.Turtle()
    pen.speed(1)
    for _ in range(num_circles):
        pen.circle(radius)
        radius += radius_increase
    pen.shape("blank")
    pen.clear()
    
draw_circles(5)
   