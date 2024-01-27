from itertools import combinations


with open("day-24/input.txt", "r") as file:
    data = file.readlines()   
particles = [
    tuple(
        [int(n) for n in line.replace("@", ",").split(",")]
        ) for line in data
    ] 


def intersection(A, B):
    xa, ya, vxa, vya = A[0], A[1], A[3], A[4]
    xb, yb, vxb, vyb = B[0], B[1], B[3], B[4]

    if (vya/vxa==vyb/vxb) and (xa!=xb or ya!=yb):
        return ()
    
    xs = (vyb/vxb * xb - vya/vxa * xa - (yb - ya)) / (vyb/vxb - vya/vxa)

    if (xs - xa)/vxa < 0 or (xs - xb)/vxb < 0:
        return ()

    ys = ya + vya/vxa * (xs - xa)

    return xs, ys


XRANGE = 200000000000000, 400000000000000
YRANGE = 200000000000000, 400000000000000


def in_range(pt, interval):
    return interval[0] < pt < interval[1]


ans = 0
for A, B in combinations(particles, 2):
    pt = intersection(A, B)
    if pt and in_range(pt[0], XRANGE) and in_range(pt[1], YRANGE):
        ans += 1

print("Solution part 1: ", ans)
