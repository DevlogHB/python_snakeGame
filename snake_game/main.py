from turtle import Screen, Turtle;
from snake import Snake;
from food import Food;
from scoreboard import Scoreboard;
import time;

# 초기 화면 설정
screen = Screen();
screen.setup(500,500);
screen.bgcolor("black");
screen.title("Snake Game"); 
screen.tracer(0);

# snake, food 클래스 설정
snake = Snake();
food = Food();
scoreboard = Scoreboard();

# 키 설정
screen.listen();
screen.onkey(snake.move_up,"Up");
screen.onkey(snake.move_down,"Down");
screen.onkey(snake.move_left,"Left");
screen.onkey(snake.move_right,"Right");

is_game = True;

# 자동 움직임 설정
while is_game:
    screen.update();   
    time.sleep(0.1);
    snake.move_snake();

    # food와 snake 거리 체크(음식을 먹으면 뱀이 커짐)
    if snake.head.distance(food) < 15:
        food.refresh();
        snake.extend();
        scoreboard.increase_score();

    # 벽과 충돌 감지
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() <-240:
        scoreboard.reset();
        snake.reset();
        
    # 뱀 꼬리 충돌 감지
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset();
            snake.reset();



screen.exitonclick();