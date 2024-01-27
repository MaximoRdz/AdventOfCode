import sympy


with open("day-24/input.txt", "r") as file:
    data = file.readlines()   

# Faster Approach
particles = [
    tuple(
        [int(n) for n in line.replace("@", ",").split(",")]
        ) for line in data
    ] 

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
equations = []

for i, (sx, sy, sz, vx, vy, vz) in enumerate(particles):
    equations.append(
        (xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr)
    )
    equations.append(
        (yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr)
    )
    if i < 2:
        # At least 4 eqns so not so many solutions are found.
        continue

    answers = [ans for ans in sympy.solve(equations) if all(x%1==0 for x in ans.values())]

    if len(answers) == 1:
        print("Solution Part 2: ", sum(answers[0][p] for p in [xr, yr, zr]), f"Iterations: {i}")
        break

# First solution.

# xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
# equations = []

# for sx, sy, sz, vx, vy, vz in particles:
#     equations.append(
#         (xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr)
#     )
#     equations.append(
#         (yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr)
#     )

# answer = sympy.solve(equations)
# print("Solution Part 2: ", sum(answer[0][p] for p in [xr, yr, zr]))

