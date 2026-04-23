import random

# Step 1: Set correct credentials
correct_userid = "admin"
correct_password = "1234"

# Step 2: Take input from user
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Step 3: Verify credentials
if userid == correct_userid and password == correct_password:
    print("Login Successful!")

    # Step 4: Generate 4-digit random number
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    # Step 5: Ask user to re-enter captcha
    user_captcha = int(input("Enter the captcha: "))

    # Step 6: Verify captcha
    if user_captcha == captcha:
        print("Verification Successful!")
    else:
        print("Verification Failed!")

else:
    print("Invalid User ID or Password")