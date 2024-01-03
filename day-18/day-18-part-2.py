
with open("day-18/input.txt", "r") as file:
    data = file.read().splitlines()

directions = {"0": (0, 1) , "1": (1, 0), "2": (0, -1), "3": (-1, 0)}

START = (0, 0)
vertices = []
vertices.append(START)

ci, cj = START

boundary = 0
for line in data:
    _, _, color = line.split()

    _, *distance, d = color[1:-1]

    dir_i, dir_j = directions[d]
    length = int("".join(distance), 16)     # hexadecimal str number to decimal int
    boundary += length

    ni, nj = ci + length*dir_i, cj + length*dir_j
    if (ni, nj) == START:
        break
    vertices.append((ni, nj))
    ci, cj = ni, nj


def shoelace_formula(vertices):
    area = 0
    for i, vertex in enumerate(vertices):
        try:
            area += vertex[0] * (vertices[i-1][1] - vertices[i+1][1])
        except:
            area += vertex[0] * (vertices[i-1][1] - vertices[0][1])
    return 0.5 * area
    

def interior_points(A, b):
    return int(A - 0.5*b + 1)

A = shoelace_formula(vertices)
print("Polygon Area: ", A)
print("Shoelace + Picks Th: ", interior_points(A, boundary) + boundary)