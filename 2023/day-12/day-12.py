import time
from itertools import product


with open("day-12/input.txt","r") as file:
    data = file.read().split("\n")

damaged_records = []
for line in data:
    record, values = line.split(" ")
    values = [int(v) for v in values.split(",")]
    damaged_records.append([record, values])

def possible_arrangements(record, value):
    N = record.count("?")

    ans = 0 

    for comb in product([" ", "#"], repeat=N):
        new_record = record
        for n, c in enumerate(comb):
            new_record = new_record.replace("?", c, 1)
        out_value = list(map(lambda x: len(x), new_record.split()))
        if out_value == value:
            ans += 1
    return ans
start = time.time()
arrs = []
for record, value in damaged_records:
    arrs.append(possible_arrangements(record.replace(".", " "), value))

print("Solution Part 1: ", sum(arrs))
print(f"Runtime: {(time.time()-start):.2f} s")
 
 