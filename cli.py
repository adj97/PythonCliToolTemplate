def help():
    print_message = [
        "Welcome to {0}, a cli tool for <description>",
        "Commands include: " + ", ".join(commands),
        "usage: {0} <command> [parameters]"
    ]
    print('\n'.join(print_message))

commands = [
    "help",
    "command1",
    "command2"
]