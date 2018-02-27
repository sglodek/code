def split_group_line(line: str) -> list:
    """
    >>> split_group_line("hello:world") #doctest: +NORMALIZE_WHITESPACE
    ['hello', 'world']
    """
    return line.split(":")

def parse_groups(file_path='/etc/group') -> list:
    """
    >>> parse_groups("group") #doctest: +NORMALIZE_WHITESPACE
    [['wireshark', 'x', '983', 'sglodek']] 
    """

    with open(file_path, "r") as group_list:
        group_list = group_list.read().split("\n")
        group_list.pop()
        group_list = list(split_group_line(line) for line in group_list)
        return group_list

def is_user_account(user_data: list) -> bool:
    """
    >>> is_user_account([0,0,1001]) #doctest: +NORMALIZE_WHITESPACE
    True

    """
    if int(user_data[2]) >= 1000:
        return True

def get_user_accounts(passwd_file='/etc/passwd') -> list:
    """
    >>> get_user_accounts("passwd") #doctest: +NORMALIZE_WHITESPACE
    [['sglodek', 'x', '1002', '1002', '', '/home/sglodek', '/bin/bash']] 
    """
    with open(passwd_file, "r") as user_list:
        user_list = user_list.read().split("\n")
        user_list.pop()
        user_list = list(split_group_line(line) for line in user_list)
        user_list = list(filter(is_user_account, user_list))
        return user_list

def get_sup_groups(users: list, groups: list) -> list:
    """
    >>> users = [['sglodek', 'x', '1002', '1002', '', '/home/sglodek', '/bin/bash']]
    >>> groups = [['wireshark', 'x', '983', 'sglodek']]
    >>> get_sup_groups(users, groups) #doctest: +NORMALIZE_WHITESPACE
    [['sglodek', 'x', '1002', '1002', '', '/home/sglodek', '/bin/bash', ['wireshark']]]
    """
    for user in users:
        supp_groups = []
        for group in groups:
             if user[0] in group[3]:
                 supp_groups.append(group[0])
        user.append(supp_groups)
    return users

def gen_user_report(users: list, output_file='user_report.txt'):
    """
    >>> users = [['sglodek', 'x', '1002', '1002', '', '/home/sglodek', '/bin/bash', ['wireshark']]]
    >>> gen_user_report(users) #doctest: +NORMALIZE_WHITESPACE
    """
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
    sup_groups = get_sup_groups(users, groups)
    gen_user_report(sup_groups)

if __name__ == "__main__":
    main()