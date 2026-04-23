num = int(input("Enter a three-digit number: "))

# Extract digits
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

# Calculate sum
digit_sum = hundreds + tens + ones

print("Sum of digits:", digit_sum)