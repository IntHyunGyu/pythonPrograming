import random
import turtle as t

playing = False
score = 0 # 점수

# 악당 거북이
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

# 먹이
ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

# 점수 표시용
scoreT = t.Turtle()
scoreT.color("White")
scoreT.hideturtle()
scoreT.up()
scoreT.goto(200,200)
scoreT.write(f"Score: {score}", False, "right", ("Arial", 16, "normal"))

# 초기 셋팅
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def game():
    global score
    global playing

    t.forward(10)

    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)

    speed = max(15, score + 5)

    te.forward(speed)

    if t.distance(te) < 12:
        scoreT.clear()
        text = "Score: " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    if t.distance(ts) <= 12:
        score += 1
        scoreT.clear()
        scoreT.write(f"Score: {score}", False, "right", ("Arial", 16, "normal"))
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        ts.goto(start_x, start_y)

    if playing:
        t.ontimer(game, 100)

def play_start():
    global score
    global playing

    if not playing:
        playing = True
        score = 0
        t.clear()
        te.goto(0, 200)
        ts.goto(0, -200)

        game()

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.onkey(play_start, "space")

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")

t.listen()
t.mainloop()
