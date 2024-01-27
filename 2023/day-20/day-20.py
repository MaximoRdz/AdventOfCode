# modules communicate using pulses: lo and hi

# % flip flop module -> either on or off (default off)
# hi to % ignored
# lo to % -> on turns off and sends lo 
#            off turns on and sends hi

# & conjunction module -> remember the type of the most recent pulse
# received from each inputs (default all lo)
# a (lo), b (lo), ... -> &module 
# a (hi), same -> &module if all hi emits lo if not emits hi 

# broadcaster emits to all outputs the input signal

# button module emits lo to the broadcaster
# after pushing you can only push again once all the modules have
# finished their task

# Pulses are processed in the order they are sent
# pulse to a, b, c then a emits apl1 and apl2
# they order should be a, b, c, apl1, apl2, bpl1, cpl1, cpl2, cpl3, ...


from heapq import heappop, heappush

with open("day-20/input.txt", "r") as file:
    data = file.read().splitlines()

system = {}
modules = set()
for line in data:
    key, connections = line.split(" -> ")
    connections = connections.split(", ")
    modules = modules.union(set(connections))
    if key == "broadcaster":
        system[key] = {"type": "bc", "in": ["btn"], "out": connections}
        continue
    system[key[1:]] = {"type": key[0], "in": [], "out": connections}

# add dead end modules
for mod in modules:
    if mod not in system.keys():
        system[mod] = {"type": None, "in": [], "out": []}

# input connections
for key, io_dict in system.items():
    for con in io_dict["out"]:
        system[con]["in"].append(key)

class FlipFlop:
    state = -1      # off by default
    def __init__(self, ouput):
        self.output = ouput
    def update_state(self, pulse):
        self.state *= pulse
    def process_pulse(self, input, pulse):
        if pulse == 1:
            # hi ignored
            return False
        self.update_state(pulse)
        return self.output, self.state
    
class Conjunction:
    def __init__(self, input, output):
        self.last_pulses = {inp: -1 for inp in input}
        self.output = output
    def process_pulse(self, input, pulse):
        self.last_pulses[input] = pulse
        if len(self.last_pulses) == sum(self.last_pulses.values()):
            # all hi
            return self.output, -1
        return self.output, 1

class Broadcaster:
    def __init__(self, output):
        self.output = output
    def process_pulse(self, input, pulse):
        return self.output, pulse

class DeadEndModule:
    def process_pulse(self, input, pulse):
        return False

system_state = {}
for key in system.keys():
    if system[key]["type"] == "bc":
        system_state[key] = Broadcaster(system[key]["out"])
    elif system[key]["type"] == "%":
        system_state[key] = FlipFlop(system[key]["out"])
    elif system[key]["type"] == "&":
        system_state[key] = Conjunction(system[key]["in"], system[key]["out"])
    else:
        system_state[key] = DeadEndModule()

def get_system_stamp(system_state):
    stamp = []
    for key in system_state.keys():
        if system[key]["type"] == "bc":
            continue
        elif system[key]["type"] == "%":
            stamp.append((key, system_state[key].state))
        elif system[key]["type"] == "&":
            stamp.append((key, system_state[key].last_pulses))
        else:
            continue
    return tuple(stamp)

def push_btn():
    start_btn = (0, "btn", "broadcaster", -1) # priority, emisor, receptor, pulse 
                                                                        # lo(-1) hi(1)
    heap = []
    heappush(heap, start_btn)
    count_low, count_high = 0, 0
    while heap:
        p, emisor, receptor, pulse = heappop(heap)
        if pulse == 1: 
            count_high += 1
        else:
            count_low += 1
        # process pulse between em and re
        module_response = system_state[receptor].process_pulse(emisor, pulse)
        if module_response:
            new_receptors, new_pulse = module_response
            for new_receptor in new_receptors:
                heappush(heap, (p+1, receptor, new_receptor, new_pulse))
    return count_low, count_high

count_low, count_high = 0, 0
stamp_init = get_system_stamp(system_state)
stamp_next = 0

i = 0
while stamp_init != stamp_next and i < 1000:
    cl, ch = push_btn()
    count_low += cl
    count_high += ch
    stamp_next = get_system_stamp(system_state)
    i += 1

N = 1000
print("Solution Part 1: ", (N//i)**2 * count_low * count_high)








