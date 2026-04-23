amount = int(input("Enter amount: "))

# List of currency notes (Indian denominations)
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

total_notes = 0

print("Notes required:")

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        total_notes += count
        print(note, ":", count)

print("Minimum number of notes =", total_notes)