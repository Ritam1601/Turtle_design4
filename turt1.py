import turtle as t
t.speed('fastest')
t.bgcolor('black')
t.hideturtle()
t.color('white')
t.pensize(3)
t.pencolor('#00EEEE')
for i in range(72):
	t.penup()
	t.fd(220)
	t.rt(90)
	t.pendown()
	for i in range(2):
		t.fd(220)
		t.rt(90)
	t.penup()
	t.fd(220)
	t.rt(90)
	t.rt(5)
t.rt(90)
t.pensize(8)
t.fd(200)
t.lt(90)
t.pendown()
t.pencolor('red')
t.circle(200)
t.penup()
t.lt(90)
t.fd(20)
t.rt(90)
t.pendown()
t.pencolor('yellow')
t.circle(180)
t.exitonclick()