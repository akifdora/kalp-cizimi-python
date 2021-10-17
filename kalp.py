import turtle

ok = turtle.Turtle()
ok.speed(0)

def donus():
    for i in range(200):
        ok.right(1)
        ok.forward(1)

def kalp():
    ok.fillcolor('red')
    ok.begin_fill()
    ok.left(140)
    ok.forward(113)
    donus()
    ok.left(120)
    donus()
    ok.forward(112)
    ok.end_fill()

def yazi():
    ok.up()
    ok.setpos(-50, 95)
    ok.down()
    ok.color('white')
    ok.write("çok tatlısın", font=("Poppins", 12, "bold"))

kalp()
yazi()
ok.ht()
