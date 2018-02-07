with open("/etc/passwd") as passwd_file:
    passwd_contents = passwd_file.read()
    passwd_lines = []
    passwd_lines = passwd_contents.split("\n")
    users = []
    for user in passwd_lines:
        users.append(user.split(":"))

with open("/etc/group") as group_file:
    group_contents = group_file.read()
    group_lines = []
    group_lines = group_contents.split("\n")
    groups = []
    for group in group_lines:
        groups.append(group.split(":"))

for i in range(0, len(users)-1):
    supp_groups = []
    for b in range(0, len(groups)-1):
        if users[i][0] in groups[b][3]:
            supp_groups.append(groups[b][0])
    users[i].append(supp_groups)

print(users)
for i in range(0, len(users) - 1):
    account = """
    Account Name: {}
        UID: {}
        GID: {}
        Home Dir: {}
        Shell: {}
        Supplimentary Groups: {}
        """.format(users[i][0], users[i][2], users[i][3], users[i][5], users[i][6], users[i][7])

    print(account)

