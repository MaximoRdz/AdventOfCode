# SETS DATA STRUCTURES PYTHON
# Unordered collection with no duplicate elements.
# sets support mathematical operations like: 
# union, intersection, difference, symmetric difference
# +, -, subsets, ...

a = set("abracadabra")
b = set("alacazam")

print(f"\na: 'abracadabra'; set of a: {a}")
print(f"\nb: 'alacazam'; set of b: {b}")

print("\nLetters in a but not in b: a-b: ", a-b)
print("\nLetters in a or b or both: a|b: ", a|b)
print("\nLetters in both a and b: a&b: ", a&b)
print("\nLetters in a and b but not both: a ^ b: ", a^b)

print("\na^b = (a|b) - (a&b): ", (a|b) - (a&b))

print("{1, 2, 3}.issubset({1, 2, 3, 4}", {1, 2, 3}.issubset({1, 2, 3, 4}))
print("{1, 2} <= {1, 2, 3}", {1, 2} <= {1, 2, 3})

