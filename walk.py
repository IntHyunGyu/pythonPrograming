import turtle as t
import random

t.shape("turtle")
t.speed(1)

for x in range(500):
    a = random.randint(1,360)
    b = random.randint(5,20)
    t.setheading(a)
    t.forward(b)

