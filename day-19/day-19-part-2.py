from collections import defaultdict, deque

with open("day-19/example.txt", "r") as file:
    workflow, _ = file.read().split("\n\n")

workflow_dict = defaultdict(list)
for w in workflow.split("\n"):
    key, other = w[:-1].split("{")
    instructions = other.split(",")
    workflow_dict[key] = instructions


def compare(a, b, op, xmas_dict):
    if op == ">":
        return xmas_dict[a] > b
    if op == "<":
        return xmas_dict[a] < b
    
def update_state(s, state):
    if "<" in s or ">" in s:
        op = "<" if "<" in s else ">"
        a, other = s.split(op)
        b, c = other.split(":")
        b = int(b)
        return a, b, c, op
    return s


# [A, B) convention
INT_MIN = 1
INT_MAX = 4000 + 1
path_init = {s: (INT_MIN, INT_MAX) for s in "xmas"}




def allowed_states(current_state, key):
    if key == "A":
        return current_state
    if key == "R":
        return 0

    for constrain in workflow_dict[key]:
        op_ans = update_state(constrain, current_state)
        if op_ans == False:
            continue
        elif op_ans == "A" or op_ans == "R":
            ans = op_ans
            break
        else:

            break

