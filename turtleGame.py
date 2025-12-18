import turtle
import random

# 화면 설정
wn = turtle.Screen()
wn.title("turtle game")
wn.bgpic("img/minimap.gif")  # 배경 GIF 유지
wn.setup(width=450, height=450)
wn.tracer(0)

# 점수 표시
score = 0
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 200)
score_turtle.write(f"score: {score}", align="center", font=("Arial", 16, "bold"))

# 플레이어 설정
wn.register_shape("img/minion.gif")  # 플레이어 이미지
player = turtle.Turtle()
player.shape("img/minion.gif")
player.penup()
player.goto(0, -175)
player.shapesize(stretch_wid=0.5, stretch_len=0.5)
player.speed(0)

PLAYER_SPEED = 15

# 장애물 설정
obstacles = []
OBSTACLE_SPEED = 4
COLORS = ["red", "blue", "magenta", "orange", "purple", "cyan"]

# 게임 상태
GAME_RUNNING = True

# 플레이어 이동
def move_left():
    if GAME_RUNNING:
        x = player.xcor() - PLAYER_SPEED
        if x > -225:
            player.setx(x)

def move_right():
    if GAME_RUNNING:
        x = player.xcor() + PLAYER_SPEED
        if x < 225:
            player.setx(x)

def move_up():
    if GAME_RUNNING:
        y = player.ycor() + PLAYER_SPEED
        if y < 225:
            player.sety(y)

def move_down():
    if GAME_RUNNING:
        y = player.ycor() - PLAYER_SPEED
        if y > -225:
            player.sety(y)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")

# 충돌 체크
def check_collision(obj):
    return player.distance(obj) < 20

# 점수 업데이트
def update_score():
    score_turtle.clear()
    score_turtle.write(f"score: {score}", align="center", font=("Arial", 16, "bold"))

# 장애물 생성
def spawn_obstacle():
    if not GAME_RUNNING:
        return
    for _ in range(random.randint(1, 4)):
        x = random.randint(-225, 225)
        y = 225
        color = random.choice(COLORS)
        obstacle = turtle.Turtle()
        obstacle.shape("circle")  # 원으로 변경
        obstacle.color(color)
        obstacle.shapesize(stretch_wid=1.5, stretch_len=1.5)
        obstacle.penup()
        obstacle.goto(x, y)
        obstacles.append(obstacle)
    wn.ontimer(spawn_obstacle, random.randint(800, 1500))

# 장애물 이동
def move_obstacles():
    global score, OBSTACLE_SPEED
    if not GAME_RUNNING:
        return
    for obs in obstacles[:]:
        y = obs.ycor() - OBSTACLE_SPEED
        obs.sety(y)
        if check_collision(obs):
            game_over()
            return
        if y < -225:
            obs.hideturtle()
            obstacles.remove(obs)
            score += 1
            update_score()
            if score % 5 == 0:
                OBSTACLE_SPEED += 1
    wn.update()
    wn.ontimer(move_obstacles, 20)

# 게임 종료
def game_over():
    global GAME_RUNNING
    GAME_RUNNING = False
    for obs in obstacles:
        obs.hideturtle()
    obstacles.clear()
    player.hideturtle()
    score_turtle.clear()
    score_turtle.goto(0, 0)
    score_turtle.write(f"Game Over! final Score : {score}\n enter R ", align="center", font=("Arial", 18, "bold"))

# 게임 재시작
def restart_game():
    global score, OBSTACLE_SPEED, GAME_RUNNING
    for obs in obstacles:
        obs.hideturtle()
    obstacles.clear()
    score = 0
    OBSTACLE_SPEED = 4
    GAME_RUNNING = True
    player.showturtle()
    player.goto(0, -175)
    score_turtle.clear()
    score_turtle.goto(0, 200)
    update_score()
    spawn_obstacle()
    move_obstacles()

wn.onkey(restart_game, "r")

# 게임 시작
spawn_obstacle()
move_obstacles()
wn.mainloop()
