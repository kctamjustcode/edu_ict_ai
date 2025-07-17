import copy, random, math

length_states = 500
actions = [-1, 0, 1]
policy_prob = [0.505, 0.05, 0.445]     # under a policy based on randomness

alpha = 0.005
dcf = 0.05

#print((-1)*math.inf)

def R(t, s, a):
    if a == 1:
        return 10*a*math.log(t+1)/(abs(s)+1)**2
    elif a == 0:
        return 0
    elif a == -1:
        return 5*a*math.log(t+1)/(abs(s)+1)**2
    if s == 100:            # states := index of a row of length [-100, 100]
        return math.inf
    elif s == -100:
        return (-1)*math.inf
    
def v_pi_fctr(s, t):
    return sum([policy_prob[i]*dcf**t*R(t+1, s, actions[i]) for i in range(len(actions))])

def v_pi(s):
    return sum([v_pi_fctr(s, t) for t in range(length_states)])


# It estimates the state value function of a finite-state Markov decision process (MDP) under a policy π
# The algorithm starts by initializing a table V(s) arbitrarily, with one value for each state of the MDP. A positive learning rate α is chosen.
states = [0]
def state_nxt(s):   # equivalent to policy function, to be altered
    dice = random.randint(1, 1000)
    '''
    v_neigh = [v_pi(s-1), v_pi(s), v_pi(s+1)]   # this defines the policy by maximal argument; if so, always take +1...
    nxt = v_neigh.index(max(v_neigh))-1   # mulitple max is not handled yet
    '''
    # this defines a policy by randomness
    if dice <= 525:
        nxt = -1
    elif 525 < dice <= 575:
        nxt = 0
    elif 575 < dice:
        nxt = 1
    return s + nxt

for _ in range(length_states-1):
    states += [state_nxt(states[-1])]

print(states[-1])
print('states: ', states[:100])
v_values = [v_pi(states[i]) for i in range(length_states)]
v_values_def = copy.deepcopy(v_values)
print("by defin: ", v_values_def[:100])


updates = 500   # then we repeatedly evaluate the policy π
for _ in range(updates):
    v_values_cp = copy.deepcopy(v_values)
    for i in range(length_states-1):
        # the -alpha + alpha* part is known as the TD error
        v_values_cp[i] = (1-alpha)*v_values[i] + alpha*(R(i+1, states[i], states[i+1]-states[i]) + dcf*v_values[i+1])
    v_values = v_values_cp

for k in range(200):
    #assert (states[k+1]-states[k])*v_values[k] >= 0
    print("state: ", states[k], "action: ", states[k+1]-states[k], "by defin: ", v_values_def[k], 'updating: ', v_values[k])
