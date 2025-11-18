import turtle
import random

class polygon:
    def __init__(self,num_sides = 3, num_insides = 0):
        self.num_sides = num_sides
        self.num_insides = num_insides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = self.get_new_color()
        self.border_size = random.randint(1, 10)


    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def drawing(self):
        self.draw_polygon()
        for i in range(self.num_insides):
            reduction_ratio = 0.618
            turtle.penup()
            turtle.forward(self.size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(self.size*(1-reduction_ratio)/2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]

    # adjust the size according to the reduction ratio
            self.size *= reduction_ratio
            self.draw_polygon()
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

    # draw a polygon at a random location, orientation, color, and border line thickness
    ## num_sides = random.randint(3, 5) # triangle, square, or pentagon
    ## size = random.randint(50, 150)
    ## orientation = random.randint(0, 90)
    ## location = [random.randint(-300, 300), random.randint(-200, 200)]
    ## color = get_new_color()
    ## border_size = random.randint(1, 10)
    ## draw_polygon(num_sides, size, orientation, location, color, border_size)
choose_num = input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: ")
choice = int(choose_num)
if choice == 1:
    for i in range(30):
        shape = polygon(3, 0)
        shape.draw_polygon()
elif choice == 2:
    for i in range(30):
        shape = polygon(4, 0)
        shape.draw_polygon()
elif choice == 3:
    for i in range(30):
        shape = polygon(5, 0)
        shape.draw_polygon()
elif choice == 4:
    for i in range(30):
        shape = polygon(random.randint(3, 5), 0)
        shape.draw_polygon()
elif choice == 5:
    for i in range(30):
        shape = polygon(3, 2)
        shape.draw_polygon()
elif choice == 6:
    for i in range(30):
        shape = polygon(4, 2)
        shape.draw_polygon()
elif choice == 7:
    for i in range(30):
        shape = polygon(5, 2)
        shape.draw_polygon()
elif choice == 8:
    for i in range(30):
        shape = polygon(random.randint(3, 5), 2)
        shape.draw_polygon()
elif choice == 9:
    for i in range(30):
        shape = polygon(random.randint(3, 5), random.randint(0, 1))
        shape.draw_polygon()

turtle.done()
