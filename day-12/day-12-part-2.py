

with open("day-12/input.txt","r") as file:
    data = file.read().split("\n")

records = []
for line in data:
    record, values = line.split(" ")
    values = [int(v) for v in values.split(",")]
    records.append([record, values])


def is_block_valid(cfg, blocks):
    # there must be enough springs left
    # all of the elements up to the length of that block must be #
    # the next element must be a dot to split the blocks
    if (blocks[0] <= len(cfg)) and ("." not in cfg[:blocks[0]]) and (len(cfg) == blocks[0] or cfg[blocks[0]] != "#"):
        return True
    return False

cache = {}
def count(cfg, blocks):
    # cfg: configuration (str)
    # base cases of the recursion:
    if cfg in cache:
        return cache[cfg]
    if cfg == "": 
        # empty configuration can only be valid if there are no
        # blocks expected, "" and ( ) in that case it'd be valid
        return 1 if blocks == () else 0
    
    key = (cfg, blocks)
    if key in cache:
        return cache[key]

    if blocks == (): 
        # if there are no more blocks but we still have a not empty 
        # cfg
        return 0 if "#" in cfg else 1
    
    result = 0
    # ? can only be a . or a #
    if cfg[0] in ".?":
        # Treat ? as a dot (first possibilty)
        # if ? is a dot remove this dot a check the rest of the str
        result += count(cfg[1:], blocks)
    
    if cfg[0] in "#?":
        # treat ? as a # (second possibility)
        # this is the start of a block
        if is_block_valid(cfg, blocks):
            # we start a valid block
            result += count(cfg[blocks[0]+1:], blocks[1:])

    cache[key] = result
    return result

ans = 0 
for record, values in records:
    record = "?".join([record]*5)
    values *= 5 
    ans += count(record, tuple(values))
    cache.clear()

    

print("Solution Part 2: ", ans)
print(cache)
