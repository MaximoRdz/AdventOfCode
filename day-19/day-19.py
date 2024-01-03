from collections import defaultdict

with open("day-19/example.txt", "r") as file:
    workflow, ratings = file.read().split("\n\n")


def string_to_dict(rating):
    vars = defaultdict(int)
    for r in rating[1:-1].split(","):
        key, _, *value = r
        vars[key] = int("".join(value))
    
    return vars



ratings = ratings.split("\n")
for rating in ratings:
    print(string_to_dict(rating))

