from collections import defaultdict

with open("day-19/example.txt", "r") as file:
    workflow, ratings = file.read().split("\n\n")

def ratings_to_dict(rating):
    vars = defaultdict(int)
    for r in rating[1:-1].split(","):
        key, _, *value = r
        vars[key] = int("".join(value))
    return vars

def compare(a, b, op, xmas_dict):
    if op == ">":
        return xmas_dict[a] > b
    if op == "<":
        return xmas_dict[a] < b
    
def operation(s, xmas_dict):
    if "<" in s or ">" in s:
        op = "<" if "<" in s else ">"
        a, other = s.split(op)
        b, c = other.split(":")
        b = int(b)

        if not compare(a, b, op, xmas_dict):
            return c
        return True
    return s


workflow_dict = defaultdict(list)
for w in workflow.split("\n"):
    key, other = w[:-1].split("{")
    instructions = other.split(",")
    workflow_dict[key] = instructions

ratings = ratings.split("\n")
for rating in ratings[0:1]:
    rating_values = ratings_to_dict(rating)

START = "in"
current_key = START
ans = 0
while ans != "A" or ans != "R":
    for s in workflow_dict[current_key]:
        print(s, ": ", operation(s, rating_values))

