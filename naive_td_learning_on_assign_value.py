import copy, math, random

def move(s, q):
    ind = math.inf
    if q > 2500:
        ind = s.index(1)
    else:
        old = s.index(1)
        others = list(range(3))
        others.remove(old)
        odds = random.randint(0, 1)
        ind = others[odds]
    return ind

def R(t, s):
    if t % 3 == s[t].index(1):
        return math.exp(8)+t
    else:
        try:
            return -100
        except:
            print('ws')
    '''
    if s.index(1) == 2:
        return 10*t
    elif s.index(1) == 1:
        return 0
    elif s.index(1) == 0:
        return -10*t
    '''

state_length = 50
v_values = [0 for _ in range(state_length)]
states = [[0,1,0] for _ in range(state_length)]
last_state = [0,0,0]
last_state[(state_length-1)%3] = 1
states[-1] = last_state
second_last_state = [0,0,0]
second_last_state[(state_length-2)%3] = 1
states[-2] = second_last_state
verf = [False for _ in range(state_length)]
v_values[-1] = R(state_length-1, states)
print('normal test: ',states[49].index(1) == 49%3)

alpha = 0.15
discount_factor = 0.003

v_values_cp = copy.deepcopy(v_values)

updates = 10000
for t in range(updates):
    for i in range(state_length-2, -1,-1):
        v_values[i]= (1-alpha) * v_values[i] + alpha * (R(i+1, states) + discount_factor*v_values[i+1])
    for i in range(state_length-2,-1,-1):
        reset_state = [0,0,0]
        rest_ind = (move(states[i+1], v_values[i+1]) - 1)%3
        reset_state[rest_ind] = 1
        states[i] = reset_state

for i in range(state_length): 
    verf[i] = (states[i].index(1) == i %3)


print("updated q-values: ", v_values)
print(states)

for i in range(state_length):
    if verf[i] == True:
        print(i)
        print(v_values[i])
print(verf)