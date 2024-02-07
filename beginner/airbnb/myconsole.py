#!/usr/bin/python3

import cmd
import os

class MyCmd(cmd.Cmd):
    """
    simple command line interface for the game.
    """

    prompt = "console>>> "

    def do_greet(self, line):
        """
        greet the user.
        """
        print("hello, world!")

    def do_EOF(self, line):
        """
        exit the program.
        """
        return True

    def default(self, line):
        """
        handle unknown commands.
        """
        print("unknown command: " + line)

    def do_quit(self, line):
        """
        quits the program
        """
        return True

    def do_clear(self, line):
        """
        clears the screen
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        return False

    def emptyline(self):
        """
        handle empty line input.
        """
        pass

if __name__ == "__main__":
    MyCmd().cmdloop()

