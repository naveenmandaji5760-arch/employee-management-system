print("Login Module")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "admin123":
    print("Welcome User")
else:
    print("Invalid Credentials")