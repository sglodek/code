def split_group_line(line):
    return line.split(":")

def parse_groups(file_path='/etc/group'):
    with open(file_path, "r") as group_list:
        group_list = group_list.read().split("\n")
        group_list.pop()
        group_list = list(split_group_line(line) for line in group_list)
        return group_list

def is_user_account(user_data):
    if int(user_data[2]) >= 1000:
        return True

def get_user_accounts(passwd_file='/etc/passwd'):
    with open(passwd_file, "r") as user_list:
        user_list = user_list.read().split("\n")
        user_list.pop()
        user_list = list(split_group_line(line) for line in user_list)
        user_list = list(filter(is_user_account, user_list))
        new_dict = {}
        for user in user_list:
            new_dict[user[0]] = user
        return new_dict


def get_sup_groups_test(users, groups):
    group_dict = {}
    for group in groups:
        for user in group[3].split(","):
            if user in users:
                group_dict.setdefault(user, [])
                group_dict[user].append(group[0])
    return group_dict

def get_sup_groups(users, groups):
        for user in users:
            supp_groups = []
            for group in groups:
                if user[0] in group[3]:
                    supp_groups.append(group[0])
            user.append(supp_groups)
        return users

def gen_user_report(users, output_file='user_report.txt'):
    with open(output_file, 'w') as output:
        for i in range(0, len(users)):
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

def main():
    groups = parse_groups()
    users = get_user_accounts()
    #sup_groups = get_sup_groups(users, groups)
    sup_groups = get_sup_groups_test(users, groups)
    gen_user_report(sup_groups, users)

if __name__ == "__main__":
    main()