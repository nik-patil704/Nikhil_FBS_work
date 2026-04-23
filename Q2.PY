# Write a program to input any alphabet and check whether it is vowel or consonant.
# Program to check vowel or consonant

char = input("Enter an alphabet: ")

# Convert to lowercase for easy comparison
char = char.lower()

# Check if input is a single alphabet
if len(char) == 1 and char.isalpha():
    if char in ['a', 'e', 'i', 'o', 'u']:
        print("It is a vowel.")
    else:
        print("It is a consonant.")
else:
    print("Invalid input! Please enter a single alphabet.")