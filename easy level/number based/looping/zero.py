n = int(input("Enter a number: "))

result = 0
place = 1

while n > 0:
    rem = n % 10

    if rem != 0:
        result = result + (rem * place)
        place = place * 10

    n = n // 10

print("Number after removing zeros:", result)