from collections import defaultdict, deque

with open("day-19/input.txt", "r") as file:
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

        if compare(a, b, op, xmas_dict):
            return c
        return False
    return s


workflow_dict = defaultdict(list)
for w in workflow.split("\n"):
    key, other = w[:-1].split("{")
    instructions = other.split(",")
    workflow_dict[key] = instructions

def classifiy_rating(rating_values):
    START = "in"
    wq = deque([START])
    ans = -1
    while wq:
        key = wq.popleft()
        for s in workflow_dict[key]:
            op_ans = operation(s, rating_values)
            if op_ans == False:
                continue
            elif op_ans == "A" or op_ans == "R":
                ans = op_ans
                break
            else:
                wq.append(op_ans)
                break
    return ans

result = defaultdict(int)

for rating in ratings.split("\n"):
    rating_values = ratings_to_dict(rating)
    if classifiy_rating(rating_values) == "A":
        for key, value in rating_values.items():
            result[key] += value

print("Solution Part 1: ", sum(result.values()))