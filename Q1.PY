# Input from user
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Convert to total seconds
total_seconds = (hours * 3600) + (minutes * 60) + seconds

# Output result
print("Total seconds:", total_seconds)