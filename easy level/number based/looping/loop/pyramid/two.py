n = int(input())

for i in range(1, n):
    # Left spaces
    print("  " * (n - i), end="")

    
    for j in range(1, i + 1):
        print("*", end=" ")

    
    print("  " * (2 * (n - i) - 1), end="")

    # Right triangle
    for j in range(1, i + 1):
        print("*", end=" ")

    print()