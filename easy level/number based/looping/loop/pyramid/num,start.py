n = int(input())

num = 1

for i in range(1, n + 1):
    if i % 2 != 0:  # Odd rows
        for j in range(i):
            print(num, end=" ")
        num += 1
    else:  # Even rows
        for j in range(i):
            print("*", end=" ")
    print()