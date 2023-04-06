# importing
import os
import subprocess

# shell
class Shell:
    def __init__(self):
        self.cwd = os.getcwd()

    def execute(self, command):
        # split command
        command = command.split()

        # cd: change directory
        if command[0] == "cd":
            if len(command) == 1:
                self.cwd = os.path.expanduser("~")
            else:
                self.cwd = os.path.expanduser(command[1])
            return

        # ls: list files
        if command[0] == "ls":
            if len(command) == 1:
                print(os.listdir(self.cwd))
            else:
                if command[1] == "-la":
                    print(os.listdir(self.cwd))
                else:
                    print("ls: invalid option")
            return

        # cat: print file content
        if command[0] == "cat":
            if len(command) == 1:
                print("cat: missing file operand")
            else:
                if command[1] == "-la":
                    print("cat: invalid option")
                else:
                    try:
                        with open(command[1], "r") as f:
                            print(f.read())
                    except FileNotFoundError:
                        print("cat: {}: No such file or directory".format(command[1]))
            return

        # bc: calculator 
        if command[0] == "bc":
            if len(command) == 1:
                print("bc: missing file operand")
            else:
                if command[1] == "-la":
                    print("bc: invalid option")
                else:
                    try:
                        with open(command[1], "r") as f:
                            print(subprocess.check_output(["bc"], stdin=f))
                    except FileNotFoundError:
                        print("bc: {}: No such file or directory".format(command[1]))
            return

        # ps: process status
        if command[0] == "ps":
            if len(command) == 1:
                print("ps: missing file operand")
            else:
                if command[1] == "-aux":
                    print(subprocess.check_output(["ps", "aux"]))
                else:
                    print("ps: invalid option")
            return

        # grep: search for pattern
        if command[0] == "grep":
            if len(command) == 1:
                print("grep: missing file operand")
            else:
                if command[1] == "term":
                    print(subprocess.check_output(["ps", "aux"]).decode("utf-8").split(" ")[-1])
                else:
                    print("grep: invalid option")
            return

        # exit: exit shell
        if command[0] == "exit":
            exit()

        # support IO redirection: input from file to process
        if ">" in command:
            if command[0] == "ls":
                if command[1] == "-la":
                    with open(command[2], "w") as f:
                        f.write(str(os.listdir(self.cwd)))
                else:
                    print("ls: invalid option")
            elif command[0] == "cat":
                if command[1] == "-la":
                    print("cat: invalid option")
                else:
                    try:
                        with open(command[1], "r") as f:
                            with open(command[2], "w") as g:
                                g.write(f.read())
                    except FileNotFoundError:
                        print("cat: {}: No such file or directory".format(command[1]))
            elif command[0] == "bc":
                if command[1] == "-la":
                    print("bc: invalid option")
                else:
                    try:
                        with open(command[1], "r") as f:
                            with open(command[2], "w") as g:
                                g.write(str(subprocess.check_output(["bc"], stdin=f)))
                    except FileNotFoundError:
                        print("bc: {}: No such file or directory".format(command[1]))
            elif command[0] == "ps":
                if command[1] == "-aux":
                    with open(command[2], "w") as f:
                        f.write(str(subprocess.check_output(["ps", "aux"])))
                else:
                    print("ps: invalid option")
            elif command[0] == "grep":
                if command[1] == "term":
                    with open(command[2], "w") as f:
                        f.write(str(subprocess.check_output(["ps", "aux"]).decode("utf-8").split(" ")[-1]))
                else:
                    print("grep: invalid option")
            else:
                print("{}: command not found".format(command[0]))
            return

        # invalid command
        print("{}: command not found".format(command[0]))

# main
if __name__ == "__main__":
    shell = Shell()
    while True:
        command = input("$ ")
        shell.execute(command)
