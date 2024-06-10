import os

userslist = ["Alpha1", "Beta1", "Gamma1"]
group_name = "Administrators"  # Replace with the desired group name

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

    # Add the user to the group
    os.system(f"net localgroup {group_name} {user} /add")
    print(f"Adding user {user} to the {group_name} group...")

    # Check if the user is added to the group
    result = os.popen(f"net localgroup {group_name} | findstr /i \"{user}\"").read()
    if result:
        print(f"User {user} is added to the {group_name} group.")
    else:
        print(f"Failed to add user {user} to the {group_name} group.")
    print("************************")
    print()