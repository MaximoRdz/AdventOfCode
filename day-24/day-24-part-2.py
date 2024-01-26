with open("day-24/example.txt", "r") as file:
    data = file.readlines()   
particles = [
    tuple(
        [int(n) for n in line.replace("@", ",").replace(" ", "").split(",")]
        ) for line in data
    ] 


def get_sign(a):
    if a==0:
        return 0
    elif a>0:
        return 1
    else:
        return -1
    
RX = [float("-inf"), float("inf")]
RY = [float("-inf"), float("inf")]
RZ = [float("-inf"), float("inf")]
def update_range(p, v, r):
    if get_sign(v)==1:
        r[0] = max(r[0], p)
    elif get_sign(vxa)==-1:
        r[1] = min(r[1], p)
        
for A in particles:
    xa, ya, za, vxa, vya, vza  = A
    update_range(xa, vxa, RX)
    update_range(ya, vya, RY)
    update_range(za, vza, RZ)

    print(RX, RY, RZ)



