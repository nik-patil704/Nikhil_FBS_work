total_amount = 0

for i in range(5):
    age = int(input(f"Enter age of person {i+1}: "))
    ticket = int(input(f"Enter ticket amount for person {i+1}: "))

    if age < 12:
        final_amount = ticket * 0.70   # 30% discount
    elif age > 59:
        final_amount = ticket * 0.50   # 50% discount
    else:
        final_amount = ticket          # full amount

    total_amount += final_amount

print(f"Total amount to be paid for all: {total_amount}")