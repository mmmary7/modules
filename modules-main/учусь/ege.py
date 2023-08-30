print("a b c")
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            if (not a and b and c) or (not a and not b and c) or (not a or not b or not c) == 1:
                print(a, b, c)
