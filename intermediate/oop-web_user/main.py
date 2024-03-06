#!/usr/bin/python3
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

    def __str__(self):
        return f"User ID: {self.id}, Username: {self.username}"

user_1 = User("32896639", "Shem Ogata")
print(user_1)
