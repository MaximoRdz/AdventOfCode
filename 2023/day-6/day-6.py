import math
import numpy as np

def second_order(a, b, c):
    radicant = b**2 - 4*a*c
    if radicant >= 0:
        return (-b - math.sqrt(radicant))/(2*a), (-b + math.sqrt(radicant))/(2*a)
    else: 
        return None
    
    
def distance(dt, T):
    return dt*(T-dt)
distance = np.vectorize(distance)



with open("day-6/input.txt", "r") as file:
    data = file.read().split("\n")


T_array = [int(t) for t in data[0].split(":")[1].split()]
R_array = [int(r) for r in data[1].split(":")[1].split()]

ans = 1
for T, R in zip(T_array, R_array):

    sol_1, sol_2 = second_order(1, -T, R)
    t_arr = np.arange(math.floor(sol_1), math.ceil(sol_2)+1)
    x_arr = distance(t_arr, T)
    ans *= len(x_arr[(x_arr > R)])

print("Part 1: ", ans)

