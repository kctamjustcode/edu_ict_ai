import random, copy

size = (50, 50)
ppuln = [[0 for _ in range(size[0])] for _ in range(size[1])]
nghb_stat = [[False for _ in range(size[0])] for _ in range(size[1])]

rounds = [0]

def infecting(a, b):
    ppuln[a][b] = 1
    return 1
    
def wind_direction():
    return 1

def updating(ppln):
    for i in range(size[0]):
        for j in range(size[1]):
            for a in range(-1,2):
                for b in range(-1,2):
                    if size[0] > a+i >= 0 and size[1] > b+j >= 0:
                        if ppuln[a+i][b+j] == 1:
                            nghb_stat[i][j] = True
                            #break
    ppln_cp = copy.deepcopy(ppln)
    for i in range(size[0]):
        for j in range(size[1]):
            if ppln[i][j] == 0 and nghb_stat[i][j]:
                dice = random.randint(1, 100)
                if dice <= 95: # infectious probability threshold
                    continue
                else:
                    ppln_cp[i][j] = 1
    rounds[0] += 1
    return ppln_cp


ppuln[size[0]//2][size[1]//2] = 1
for _ in range(50):
    ppuln = updating(ppuln)
print(ppuln)
#print(nghb_stat)


import turtle


def draw_square(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_grid(rows, cols, size, ppln):
    screen = turtle.Screen()
    screen.tracer(0)  # Disable animation
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    colors = ["lightblue", "lightgreen"]  # Alternating colors

    for row in range(rows):
        for col in range(cols):
            x = col * size - 200
            y = -row * size + 200
            t.goto(x, y)
            color = colors[ppln[row][col]]  # Alternate colors
            draw_square(t, size, color)

    screen.onkey(screen.bye, "q")
    screen.listen()

    t.hideturtle()
    screen.mainloop()

# Customize grid size and square size
draw_grid(rows=size[0], cols=size[1], size=5, ppln=ppuln)


