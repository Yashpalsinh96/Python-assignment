max_tries = 3
   
username = input("Enter your username: ")
password = input("Enter your password: ")

for _ in range(max_tries):
    retype_password = input("Re-type your password: ") 

    if retype_password == password:
        print("Login successful!")
        break   
    else:
        print("Incorrect password. Try again")

else:
    print("Too many incorrect attempts. Exiting.")
