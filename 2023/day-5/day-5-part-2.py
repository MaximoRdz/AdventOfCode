
with open("day-5/input.txt", "r") as file:
    almanac = file.read()

seeds, *paragraphs = almanac.split("\n\n")

_, seeds = seeds.split(":")
seeds = seeds.split()
seed_ranges = [(int(seeds[i]), int(seeds[i])+int(seeds[i+1])) 
               for i in range(0, len(seeds), 2)]


def get_almanac_ranges(paragraphs):
    almanac_ranges = {}

    for i, p in enumerate(paragraphs):
        p_lines = p.split("\n")[1:]
        almanac_ranges[i] = [tuple([int(num) for num in line.split()]) for line in p_lines]

    return almanac_ranges

almanac_ranges = get_almanac_ranges(paragraphs)

def map_ranges(lo, hi, map_ins):
    # interval [lo, hi) inclusive exclusive criteria

    ans = []  # list of overlapping ranges
    for dst, src, L in map_ins:
        D = dst - src  # interval shift distance

        if not ((hi < src) or (lo > src+L)):
            # overlaps
            ans.append((max(lo, src), min(hi, src+L), D))
    
    for i, interval in enumerate(ans):
        # return the simplest to compute destination ranges
        l, r, D = interval
        # print("first", (l+D, r+D), "D: ", D)
        yield (l+D, r+D)

        # return all the not overlapping values in between consecutive
        # intervals F(x) = x
        if (i < len(ans)-1) and (r < ans[i+1][0]):
            # print("second", (r, ans[i+1][0]))
            yield(r, ans[i+1][0])

    if len(ans) == 0:
        # not even one overlapped all x -> x
        # print("third", (lo, hi))
        yield (lo, hi)
        return     
    # start and end edge cases can cause troubles
    if ans[0][0] > lo:
        # not overlapping left to first range
        # print("fourth", (lo, ans[0][0]))
        yield (lo, ans[0][0])
    if ans[-1][1] < hi:
        # not overlapping right to last range
        # print("fifth", (ans[-1][1], hi), "D: ", ans[-1][-1])
        yield (ans[-1][1], hi)



ans = 1 << 60

for lo, hi in seed_ranges:
    current_ranges = [(lo, hi)]
    # print("--------------", current_ranges)
    # print("--------------")

    new_ranges = []

    for almanac_step in almanac_ranges.values():
        # print("step ")
        # print(almanac_step)
        for lo, hi in current_ranges:
            for new_range in map_ranges(lo, hi, almanac_step):
                new_ranges.append(new_range)
                # print(new_range)
            # print("new ranges: ", new_ranges)
        current_ranges, new_ranges = new_ranges, []
    
    for lo, hi in current_ranges:
        ans = min(ans, lo)
        print(ans)




# print(ans)



