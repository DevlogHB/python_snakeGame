from turtle import Turtle;
import random;

# food 클래스 생성(Turtle 상속)
class Food(Turtle):

    def __init__(self):
        super().__init__();
        self.shape("circle");
        self.penup();
        self.shapesize(0.5, 0.5);
        self.color("blue");
        self.speed("fastest");
        food_x =random.randint(-230, 230);
        food_y =random.randint(-230, 230);
        self.goto(food_x, food_y);
        self.refresh();
    
    def refresh(self):
        food_x =random.randint(-230, 230);
        food_y =random.randint(-230, 230);
        self.goto(food_x, food_y);