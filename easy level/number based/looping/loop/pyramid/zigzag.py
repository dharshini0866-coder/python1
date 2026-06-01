n = int(input())

for i in range(3):
    for j in range(2 * n - 1):
        if (i == 0 and (j == n - 1 or j == 0 or j == 2 * n - 2)) or \
           (i == 1 and (j == 1 or j == n - 1 or j == n + 1 or j == 2 * n - 3)) or \
           (i == 2 and (j == 2 or j == n - 1 or j == 2 * n - 4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()