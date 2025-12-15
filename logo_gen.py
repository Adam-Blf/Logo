import turtle

def draw_logo():
    t = turtle.Turtle()
    t.speed(2)
    t.color("blue")
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
    turtle.done()

if __name__ == "__main__":
    print("Drawing logo...")
    # Uncomment to run GUI
    # draw_logo() 
