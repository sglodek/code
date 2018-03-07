import sys
import os
import subprocess
import json
import argparse

opsys = sys.platform

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", choices=["cmd", "rep"], help="cmd or rep")
    parser.add_argument("y", help="command")
    args = parser.parse_args()


    if args.x == "cmd":
        generate_command_info(args.y)
    elif args.x == "rep":
        generate_report(args.y)

def generate_command_info(command):
    if opsys == "linux":
        paths = os.getenv("PATH").split(":")
        print("List of Paths:")
        for path in paths:
            if os.path.isdir(path):
                if command in os.listdir(path):
                    print(path)

        man = subprocess.run(["man", "-P", "cat", command], stdout=subprocess.PIPE, universal_newlines=True)
        print(man.stdout)
        
    elif opsys == "windows":
        paths = os.getenv("PATH").split(";")
        for path in paths:
            if os.path.isdir(path):
                if command in os.listdir(path):
                    print(path)

def generate_report(stuff):
    if opsys == "linux":
        paths = os.getenv("PATH").split(":")
        command_dict = {}
        for path in paths:
            if os.path.isdir(path):
                for item in os.listdir(path):
                    if os.path.isfile(path + "/" + item):
                        command_dict.setdefault(item, []).append(path)

        if sys.argv[2] == "term":
            print_report(command_dict)
        elif sys.argv[2] == "file":
            write_report(command_dict)

    elif opsys == "windows":
        pass

def write_report(command_dict):
    with open("report.json", 'w') as f:
        json.dump(command_dict, f)

def print_report(command_dict):
    for item in command_dict:
        print("""
        Command: {}
        Path:{}
        """.format(item, command_dict[item]))

if __name__ == "__main__":
    main()