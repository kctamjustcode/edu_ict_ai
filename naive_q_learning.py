import copy

q_values = [[0, 0, 0] for _ in range(500)]
alpha = 0.05
discount_factor = 0.03

def R(t, A):
    if A == 2:
        return 10*t
    elif A == 1:
        return 0
    elif A == 0:
        return -10*t

q_values_cp = copy.deepcopy(q_values)

updates = 50
for t in range(updates):
    for i in range(500-1):
        for j in range(3):
            q_values_cp[i][j] = (1-alpha) * q_values[i][j] + alpha * (R(i+1, j) + discount_factor*max(q_values[i+1]))
    q_values = q_values_cp

print("updated q-values: ", q_values_cp)
