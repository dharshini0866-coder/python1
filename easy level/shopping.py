amount = int(input())
if amount >= 5000:
    final_amount = amount - (amount * 10 // 100)
else:
    final_amount = amount
print(final_amount)