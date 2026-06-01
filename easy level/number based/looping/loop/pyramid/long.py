n = int(input())

# Upper half including middle row
for i in range(n):
    # Leading spaces
    print("  " * i, end="")

    # Stars
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()

# Lower half
for i in range(n - 2, -1, -1):
    # Leading spaces
    print("  " * i, end="")

    # Stars
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()