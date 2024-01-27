a = 2
b = 4

print(int.__lt__(a, b))
print(int.__gt__(a, b))
a = 4
print(int.__lt__(a, b) or int.__eq__(a, b))


operator = {
    "<": int.__lt__, 
    ">": int.__gt__
}

print("Function in dict 10 < 4: ", operator["<"](10, 4))

