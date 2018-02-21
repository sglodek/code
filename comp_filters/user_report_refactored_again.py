def parse_groups(file_path='/etc/group'):
    with open(file_path, "r") as group_list:
        group_list = group_list.read().split("\n")
        group_list.pop()
        group_list = list(line.split(":") for line in group_list)
        group_list = list(filter(lambda x: x[3] != "", group_list))
        return group_list

def parse_users(passwd_file='/etc/passwd'):
    with open(passwd_file, "r") as user_list:
        user_list = user_list.read().split("\n")
        user_list.pop()
        user_list = list(line.split(":") for line in user_list)
        user_list = list(filter(lambda x: int(x[2]) >= 1000, user_list))
        return user_list

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
        for user in users:
                account = """
                Account Name: {}
                    UID: {}
                    GID: {}
                    Home Dir: {}
                    Shell: {}
                    Supplimentary Groups: {}
                    """.format(user[0], user[2], user[3], user[5], user[6], user[7])

                output.write(account)
                print(account)

def main():
    groups = parse_groups()
    users = parse_users()
    sup_groups = get_sup_groups(users, groups)
    gen_user_report(sup_groups)

if __name__ == "__main__":
    main()