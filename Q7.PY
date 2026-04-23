correct_userid = "nikhil.12"
correct_password = "nikhil@24"

userid = input("Enter uder id:")
password = input("Enter password:")

if userid == correct_userid and password == correct_password:
    print("login successful")
else:
    print("Invalid user id or password")