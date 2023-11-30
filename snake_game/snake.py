from turtle import Turtle;

START_POSITIONS = [(0, 0), (-20, 0)];
MOVE_DISTANCE = 20;
UP = 90;
DOWN = 270;
LEFT = 180;
RIGHT = 0;

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position);

    def add_segment(self, position):
        new_segment = Turtle("square");
        new_segment.color("white");
        new_segment.penup();
        new_segment.goto(position);
        self.segments.append(new_segment);
    
    # 음식을 먹으면 뱀 꼬리 추가
    def extend(self):
        self.add_segment(self.segments[-1].position());
    
    def move_snake(self):
        for num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[num-1].xcor()
            new_y = self.segments[num-1].ycor()
            self.segments[num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE);
    
    # 초기화
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000) # 화면에서 제외
        self.segments.clear();
        self.create_snake();
        self.head = self.segments[0];

    # 상하좌우 움직임 체크
    def move_headCheck(self, move, r_move):
        if self.head.heading() != r_move:
            self.head.setheading(move);
    
    def move_up(self):
        self.move_headCheck(UP,DOWN);
    
    def move_down(self):
        self.move_headCheck(DOWN,UP);

    def move_left(self):
        self.move_headCheck(LEFT,RIGHT);
        
    def move_right(self):
        self.move_headCheck(RIGHT,LEFT);

