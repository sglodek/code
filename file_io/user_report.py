def main():
    users = parse_accounts()
    groups = parse_groups()
    gen_user_report(users,groups)

def parse_accounts(file_path='/etc/passwd'):
    with open(file_path) as passwd_file:
        passwd_contents = passwd_file.read()
        passwd_lines = []
        passwd_lines = passwd_contents.split("\n")
        users = []
        for user in passwd_lines:
            users.append(user.split(":"))
        return users
        
def parse_groups(file_path='/etc/group'):
    with open(file_path) as group_file:
        group_contents = group_file.read()
        group_lines = []
        group_lines = group_contents.split("\n")
        groups = []
        for group in group_lines:
            groups.append(group.split(":"))
        return groups


def gen_user_report(users, groups, output_file='user_report.txt'):
    for i in range(0, len(users)-1):
        supp_groups = []
        for b in range(0, len(groups)-1):
            if users[i][0] in groups[b][3]:
                supp_groups.append(groups[b][0])
        users[i].append(supp_groups)
    with open(output_file, 'a') as output:
        for i in range(0, len(users) - 1):
            if int(users[i][2]) >= 1000:
                account = """
                Account Name: {}
                    UID: {}
                    GID: {}
                    Home Dir: {}
                    Shell: {}
                    Supplimentary Groups: {}
                    """.format(users[i][0], users[i][2], users[i][3], users[i][5], users[i][6], users[i][7])

                output.write(account)

if __name__ == "__main__":
    main()

