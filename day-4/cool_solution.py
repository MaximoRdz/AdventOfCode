from collections import defaultdict

with open("day-4/input.txt", "r") as myfile:
    lines = myfile.read().splitlines()



correct_numbers = 0
N = defaultdict(int)  # cards of each type
for i, line in enumerate(lines):
    N[i] += 1     # one original card
    id_, card = line.split(":")
    winners, numbers = card.strip().split("|")
    winners = [int(x) for x in winners.split()]
    numbers = [int(x) for x in numbers.split()]

    # number of correct numbers per card = length of the intersection
    intersection = set(winners) & set(numbers)
    val = len(intersection)
    if intersection:
        correct_numbers += 2**(val - 1)
    for j in range(val):
        N[i+1+j] += N[i]
    
print("Part 1: ", correct_numbers)
print("Part 2: ", sum(N.values()))

