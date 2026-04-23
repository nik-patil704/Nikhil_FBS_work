# Input 5 subject marks from user and display grade(eg.First class,Second class ..)#include <stdio.h>
# Input marks for 5 subjects
marks = []
for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

# Calculate percentage
percentage = sum(marks) / 5

print(f"Percentage = {percentage}")

# Determine grade
if percentage >= 60:
    print("Grade: First Class")
elif percentage >= 50:
    print("Grade: Second Class")
elif percentage >= 40:
    print("Grade: Third Class")
else:
    print("Grade: Fail")
