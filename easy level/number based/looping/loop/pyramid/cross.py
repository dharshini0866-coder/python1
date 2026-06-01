n = int(input())

# Upper half including middle row
for i in range(n):
    for j in range(2 * n - 1):
        if j == i or j == (2 * n - 2 - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(n - 2, -1, -1):
    for j in range(2 * n - 1):
        if j == i or j == (2 * n - 2 - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()