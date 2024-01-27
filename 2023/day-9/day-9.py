

with open("day-9/input.txt", "r") as file:
    data = file.read().split("\n")

histories = []
for line in data:
    histories.append([int(x) for x in line.split()])




def next_sequence(sequence):
    new_seq = [sequence[i]-sequence[i-1] for i in range(1, len(sequence))]
    return new_seq

def find_next(cur_seq, reverse=False, max_steps=1e6):
    history_sequences = [cur_seq]
    step = 0
    while sum(cur_seq):
        cur_seq = next_sequence(cur_seq)
        history_sequences.append(cur_seq)
        step += 1
        if step == max_steps:
            print("MAXIMUM STEPS REACHED")
            break
    if reverse:
        ans = 0
        for i in reversed(range(1, len(history_sequences))):
            ans = history_sequences[i-1][0]-ans
            
    else:
        ans = 0
        for i in reversed(range(1, len(history_sequences))):
            ans += history_sequences[i-1][-1]

    return ans


last_numbers = [find_next(seq) for seq in histories]
print("part 1: ", sum(last_numbers))

last_numbers = [find_next(seq, reverse=True) for seq in histories]
print("part 2: ", sum(last_numbers))
    