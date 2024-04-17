import turtle

t = turtle.Turtle()

window = turtle.Screen()

#Exercise 1

def draw_circles(t, size, circle_count, decrease_amnt):
    for num in range(circle_count):
        t.circle(size)
        size = size - (decrease_amnt)

draw_circles(t, size = 20, circle_count=5, decrease_amnt = 5)

#Exercise 2
  
def draw_special(t, size, repeat, circle_count, decrease_amnt):
    for _ in range(repeat):
        draw_circles(t, size, circle_count, decrease_amnt)
        t.right(360 / repeat)
        
draw_special(t, size = 20, repeat = 5, circle_count = 10, decrease_amnt = 5)

#Exercise 3

def draw_picture(t, size, repeat, circle_count, decrease_amnt):
    colours = ['white', 'yellow', 'blue', 'orange', 'pink']
    for n in range(repeat):
        t.color(colours[n % len(colours)])
        draw_circles(t, size, circle_count, decrease_amnt)
    draw_special(t, size, circle_count, repeat, decrease_amnt)

draw_picture(t, size = 10, repeat = 6, circle_count = 5, decrease_amnt = 5)
        
    
    
    
    