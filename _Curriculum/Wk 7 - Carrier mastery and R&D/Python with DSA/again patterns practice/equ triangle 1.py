n = 5

for i in range(1, n + 1):

    # spaces
    for j in range(1, n - i + 1):
        print(" ", end="")

    # stars
    for j in range(1, 2 * i):
        print("*", end="")

    print()