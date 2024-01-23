

with open("day-23/example.txt", "r") as file:
    data = file.read().splitlines()

# ##############
# ###S####   ###     
# ### #### #####     
# ###  i   ##### 
# ##### ######## 
# ##############
    
# Path contraction: Since the map is mazze-like we can 
# contract the graph to take into account only point of 
# interest (i) (that is points with more than 2 neighbors)  
# and the distance between them

interest_points = set()

st = 0, data[0].find(".")
nd = -1, data[-1].find(".")

interest_points.add(st)
interest_points.add(nd)

for i, line in enumerate(data):
    for j, c in enumerate(line):
        pass