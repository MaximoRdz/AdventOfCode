import math

with open("day-6/input.txt", "r") as file:
    data = file.read()

T = int(data.split("\n")[0].split(":")[1].replace(" ", ""))
R = int(data.split("\n")[1].split(":")[1].replace(" ", ""))

def second_order(a, b, c):
    radicant = b**2 - 4*a*c
    if radicant >= 0:
        return (-b - math.sqrt(radicant))/(2*a), (-b + math.sqrt(radicant))/(2*a)
    else: 
        return None
    
t1, t2 = second_order(1, -T, R)

def distance(dt, T):
    return dt*(T-dt)

def is_record(t, T, R):
    if distance(t, T) - R > 0:
        return True
    else:
        return False


ans = (math.ceil(t2)-1)+1 - (math.floor(t1)+1)
print("solution part 2: ", ans)