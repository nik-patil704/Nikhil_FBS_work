feet = int(input("Enter distant in feet:"))
inches = int(input("Enter distant in inches:"))

total_inches = (feet * 12)+ inches
total_cm = total_inches *2.54

meters = int(total_cm // 100)
centimeters = int(total_cm % 100)
print(f"{meters} meters and {centimeters} centimeters")