from turtle import Turtle
MOVE_DISTANCE = 20
ALLOWED_HEADINGS = {
            "north": [(0, 180), 90],
            "south": [(0, 180), 270],
            "east": [(90, 270), 0],
            "west": [(90, 270), 180],
        }

class Snake:
    def __init__(self):
        self.snakes = []
        self.move = 20
        for i in range(3):
            snake = self.create_snake()
            snake.setx(i*(-20))
            self.snakes.append(snake)
        self.head = self.snakes[0]
        self.body = self.snakes[1:] 
    
    def create_snake(self):
        snake = Turtle()
        snake.speed('slowest')
        snake.penup()
        snake.shape('square')
        snake.color('white')
        return snake
    
    def move_snake(self):
        self.move_body()
        self.move_head()        

    def move_body(self):
        for i in range(len(self.body) - 1, -1, -1):
            if i == 0:
                position_to_go = self.head.pos()
            else:
                position_to_go = self.body[i-1].pos()
            self.body[i].goto(position_to_go)

    def move_head(self):
        self.head.fd(MOVE_DISTANCE)
        
    def create_new_segment(self):
        new_segment = self.create_snake()
        last_body_segment = self.body[len(self.body) - 1]
        x = last_body_segment.xcor()
        y = last_body_segment.ycor()
        new_segment.setpos(x,y)
        self.body.append(new_segment)
        self.snakes.append(new_segment)

    def turn(self, direction):        
        heading = self.head.heading()
        if heading in ALLOWED_HEADINGS[direction][0]:
            self.head.setheading(ALLOWED_HEADINGS[direction][1])

    def turn_north(self):
        self.turn("north")
            
    def turn_south(self):
        self.turn("south")
            
    def turn_east(self):
        self.turn("east")
        
    def turn_west(self):
        self.turn("west")