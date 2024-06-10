import os

userslist = ["Alpha", "Beta", "Gamma"]

print("Adding users to the list")
print("************************")

# Loop to add users from the list
for user in userslist:
    # Check if the user exists
    exitcode = os.system(f"net user {user} > nul 2>&1")
    if exitcode != 0:
        print(f"User {user} does not exist. Adding it.")
        print("************************")
        print()
        # Add the user
        os.system(f"net user {user} /add")
    else:
        print(f"User {user} already exists!")
        print("************************")
        print()