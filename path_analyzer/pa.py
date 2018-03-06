import sys
import os
import subprocess
paths = os.getenv("PATH").split(":")

def main():
    if sys.argv[1] == "cmd":
        command_path(sys.argv[2])
    elif sys.argv[1] == "rep":
        report(sys.argv[2])
    else:
        print("ya done goofed son")

def command_path(command):
    for path in paths:
        if os.path.isdir(path):
            if command in os.listdir(path):
                print(path)

    man = subprocess.run("man -P cat " + command, stdin=subprocess.PIPE, shell=True)
    print(man)

def report(stuff):
    command_dict = {}
    print(paths)
    for path in paths:
        if os.path.isdir(path):
            for item in os.listdir(path):
                if os.path.isfile(path + "/" + item):
                    command_dict.setdefault(item, []).append(path)

    print(command_dict)

if __name__ == "__main__":
    cmd_or_rep = sys.argv[1]
    #command = sys.argv[2]
    main()