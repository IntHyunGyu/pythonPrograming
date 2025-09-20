import turtle as t

distance = int(input("거북이가 움직일 거리를 입력하세요 : "))

if distance == 0:
    print("잘못된 입력입니다")
    exit()

t.shape("turtle")
t.forward(distance)
t.left(120)
t.forward(distance)
t.left(120)
t.forward(distance)

t.exitonclick()