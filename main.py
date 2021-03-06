from sys import argv
from cli import *
from helpers import *
from commands import *

if __name__ == "__main__":

    # empty args
    if len(argv)==1:
        # help
        help()
        exit()

    # command decomposition
    command, args = argv[1], argv[2:]

    if command in commands:
        try:
            if command == commands[0]:
                # help
                help()
            elif command == commands[1]:
                # command 1
                output("o","Command1")
                command1(args)
            elif command == commands[2]:
                # command 2
                output("o","Command2")
                command2(args)

            # healthy finish
            output("o", "Completed")
        except Exception as e:
            output("o", "Aborted")
            output("e", e)
    else:
        output("e", "Unrecognised command: " + command)
        help()
