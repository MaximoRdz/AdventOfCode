import re
from collections import defaultdict, deque

with open("day-19/input.txt", "r") as file:
    workflow, _ = file.read().split("\n\n")

workflow_dict = defaultdict(list)
for w in workflow.split("\n"):
    key, other = w[:-1].split("{")
    instructions = other.split(",")
    workflow_dict[key] = instructions


def compare(xmas_key, limit_num, op, xmas_dict):
    if op == ">":
        return xmas_dict[xmas_key] > limit_num
    if op == "<":
        return xmas_dict[xmas_key] < limit_num

def check_if_included(saved_ratings, new_ratings):
    # having x = [a, b], y = [c, d]
    # is     w = [e, f], z = [g, h] contained in it?
    for current_ratings in saved_ratings:
        result = 0
        for s in "xmas":
            ca, cb = current_ratings[s]
            na, nb = new_ratings[s]
            result +=  (ca <= na <= cb and ca <= nb <= cb)
        if result == 4:
            return True
    return False


# [A, B] convention both inclusive
INT_MIN = 1
INT_MAX = 4000
ratings = {s: (INT_MIN, INT_MAX) for s in "xmas"}



state = ("in", ratings)

q = deque()
q.append(state)
accepted_intervals = []
while q:
    key, ratings = q.pop()
    if key == "A" and not check_if_included(accepted_intervals, ratings):
        accepted_intervals.append(ratings)
        continue
    if key == "R":
        continue
    # for each operation in the workflow instructions
    # we keep both paths True and False
    for ins in workflow_dict[key]:
        if not (">" in ins or "<" in ins):
            q.append((ins, ratings.copy()))
        else:
            limit = int(re.findall("\d+", ins)[0])
            xmas_key = ins[0]
            next_key = ins.split(":")[1]
            a, b = ratings[xmas_key]
            if a<=limit<=b:
                if "<" in ins:
                    left = (a, limit-1)
                    right = (limit, b)

                    left_ratings = ratings.copy()
                    left_ratings[xmas_key] = left

                    right_ratings = ratings.copy()
                    right_ratings[xmas_key] = right

                    q.append((next_key, left_ratings.copy()))
                    ratings = right_ratings # continue with the false same key

                if ">" in ins:
                    left = (a, limit)
                    right = (limit+1, b)

                    left_ratings = ratings.copy()
                    left_ratings[xmas_key] = left

                    right_ratings = ratings.copy()
                    right_ratings[xmas_key] = right
                    q.append((next_key, right_ratings.copy()))
                    ratings = left_ratings  # continue with the false same key

ans = 0
for intervals in accepted_intervals:
    ncomb = 1
    for value in intervals.values():
        ncomb *= value[1]+1-value[0]
    ans += ncomb
print("Solution Part 2: ", ans)
