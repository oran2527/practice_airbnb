#!/usr/bin/python3
"""module point 6 cmd class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """do_EOF function"""
        return True

    def do_quit(self, line):
        """do_QUIT function"""
        return True

    def help_quit(self):
        """help_quit function"""
        print("Quit command to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
