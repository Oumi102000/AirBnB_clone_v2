#!/usr/bin/python3
"""
Defines AirBnB console module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quit command to exit the HBNB console"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the HBNB program"""
        print("")
        return True

    def emptyline(self):
        """Overrides the cmd emptyline method, do nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
