#!/usr/bin/python3

import cmd

class UserMan(cmd.Cmd):
    """Simple CRUD command for managing users"""

    def __init__(self):
        super().__init__()
        self.users = {}

    def do_create(self, line):
        """Create a new user. Syntax: create <id> <name>"""
        args = line.split()
        if len(args) == 2:
            user_id, name = args
            if user_id.isdigit():
                user_id = int(user_id)
                self.users[user_id] = name
                print(f"User created: ID={user_id}, Name={name}")
            else:
                print("Error: User ID must be a digit.")
        else:
            print("Error: Invalid input. Syntax: create <id> <name>")

    def do_read(self, line):
        """Read user details by ID. Syntax: read <id>"""
        args = line.split()
        if len(args) == 1:
            user_id = args[0]
            if user_id.isdigit():
                user_id = int(user_id)
                if user_id in self.users:
                    name = self.users[user_id]
                    print(f"User found: ID={user_id}, Name={name}")
                else:
                    print("Error: User ID not found.")
            else:
                print("Error: User ID must be a digit.")
        else:
            print("Error: Invalid input. Syntax: read <id>")

    def do_update(self, line):
        """Update user name by ID. Syntax: update <id> <new_name>"""
        args = line.split()
        if len(args) == 2:
            user_id, new_name = args
            if user_id.isdigit():
                user_id = int(user_id)
                if user_id in self.users:
                    self.users[user_id] = new_name
                    print(f"User updated: ID={user_id}, New Name={new_name}")
                else:
                    print("Error: User ID not found.")
            else:
                print("Error: User ID must be a digit.")
        else:
            print("Error: Invalid input. Syntax: update <id> <new_name>")

    def do_destroy(self, line):
        """Delete a user by ID. Syntax: destroy <id>"""
        args = line.split()
        if len(args) == 1:
            user_id = args[0]
            if user_id.isdigit():
                user_id = int(user_id)
                if user_id in self.users:
                    del self.users[user_id]
                    print(f"User deleted: ID={user_id}")
                else:
                    print("Error: User ID not found.")
            else:
                print("Error: User ID must be a digit.")
        else:
            print("Error: Invalid input. Syntax: destroy <id>")

    def do_list(self, line):
        """List all users"""
        for user_id, name in self.users.items():
            print(f"ID={user_id}, Name={name}")

if __name__ == '__main__':
    UserMan().cmdloop()

