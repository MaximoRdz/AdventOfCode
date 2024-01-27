
example = [87, 6, 7, 29, 31, 0, 1,  
           69, 69, 65, 64, 65, 63, 68, 
           69, 69, 65, 64, 65, 63, 68,   # tf = 15
           69, 69, 65, 64, 65, 63, 68, 
           69, 69, 65, 64, 65, 63, 68,
           69, 69, 65, 64, 65, 63, 68, 
           69, 69, 65, 64, 65, 63, 68, 
           69, 69, 65, 64, 65, 63, 68, 
           69, 69, 65, 64, 65, 63, 68,
           69, 69, 65, 64, 65, 63, 68,
           69, 69, 65, 64, 65, 63, 68, 
           69, 69, 65, 64, 65, 63, 68, 
           69, 69, 65, 64, 65, 63, 68, 
           69, 69, 65, 64, 65, 63, 68,
           69, 69, 65, 64, 65,
           ]



visited = set()
visited.add(example[0])
i = 1

cycle = []
while i<len(example):
    current = example[i]

    if current in visited:
        cycle.append(current)
        if len(cycle) > 4 and cycle[0]==cycle[-2] and cycle[1]==cycle[-1]:
            print("Cycle found", cycle[:-2])
            T = len(cycle[:-2]) 
            print("Period: ", T)
            tf = i-2
            print("tf: ", tf)
            break
    else:
        cycle.clear()

    i += 1
    visited.add(current)

N = len(example)-1
print("Last index: ", N)
print("Total left values to compute: ", N-tf)
cycles = (N-tf)//T
print("Complete cycles contained: ", cycles)
ans = N - (tf+1+T*cycles)
print(ans)
print("Solution: ", cycle[ans])






    
