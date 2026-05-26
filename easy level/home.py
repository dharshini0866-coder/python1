U = int(input())
if U <= 100:
    bill = U * 2
elif U <= 200:
    bill = (100 * 2) + ((U - 100) * 3)
else:
    bill = (100 * 2) + (100 * 3) + ((U - 200) * 5)

# Print total bill
print(bill)