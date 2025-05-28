import random, copy

# Set up the grid dimensions
rows, cols = 50, 50
size = (rows, cols)

rounds = [0]

ppuln = [[0 for _ in range(size[0])] for _ in range(size[1])]
ppuln[size[0]//2][size[1]//2] = 1
ppuln_hist = [ppuln]

nghb_stat = [[False for _ in range(size[0])] for _ in range(size[1])]
infect_stat = [[[] for _ in range(size[0])] for _ in range(size[1])]
infect_stat[size[0]//2][size[1]//2].append(rounds[0])
recovery_stat = [[0 for _ in range(size[0])] for _ in range(size[1])]

infecting_probility = 0.95
recovered_infecting_nbp = 0.75              # naive bayes probility of being infected given recovered (assume with exponential effects on the numbers of infected times)
medical_consultation_probility = 0.75
treatment_duration = 5
immune_system_recovery_rate = 1 - 0.15      # meaning 15% better than yesterday
immune_probilistic_threshold = 0.1          # to be considered as recovered to healthy


cured_list = []

def cured(infct_stt):
    if treatment_duration == 1:
        return True
    assert infct_stt != []
    assert infct_stt[-1] == rounds[0]
    temp_cnt = 1
    while infct_stt[len(infct_stt)-1 - temp_cnt] == infct_stt[-1] - temp_cnt:
        temp_cnt += 1
        if temp_cnt == treatment_duration:
            return True
    return False      

def get_current_infected_days(infct_stt):
    temp_cnt = 1
    while infct_stt[len(infct_stt)-1 - temp_cnt] == infct_stt[-1] - temp_cnt:
        temp_cnt += 1
    return temp_cnt

def updating(ppln):
    for i in range(size[0]):
        for j in range(size[1]):
            infected_found = False
            for a in range(-1,2):
                for b in range(-1,2):
                    if size[0] > a+i >= 0 and size[1] > b+j >= 0:
                        if ppln[a+i][b+j] == 1:
                            nghb_stat[i][j] = True
                            infected_found = True
            if not infected_found:
                nghb_stat[i][j] = False

    ppln_cp = copy.deepcopy(ppln)
    rounds[0] += 1
    for i in range(size[0]):
        for j in range(size[1]):
            if ppln[i][j] == 0 and nghb_stat[i][j]:
                dice = random.randint(1, 100)
                if dice <= 100*(1-(recovered_infecting_nbp**recovery_stat[i][j])*infecting_probility): #C.MD
                    continue
                else:
                    ppln_cp[i][j] = 1
                    infect_stat[i][j].append(rounds[0])
            elif ppln[i][j] == 1:
                infect_stat[i][j].append(rounds[0])
                dice = random.randint(1, 100)
                if dice <= 100*medical_consultation_probility:
                    if not cured(infect_stat[i][j]):
                        continue
                    else:
                        ppln_cp[i][j] = 0
                        recovery_stat[i][j] += 1
                else:
                    infected_days = get_current_infected_days(infect_stat[i][j])
                    if immune_system_recovery_rate**infected_days < immune_probilistic_threshold:
                        ppln_cp[i][j] = 0
                        recovery_stat[i][j] += 1

    return ppln_cp

for _ in range(100):
    ppuln = updating(ppuln)
    ppuln_hist.append(ppuln)



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
draw_grid(rows=size[0], cols=size[1], size=5, ppln=ppuln_hist[-1])

