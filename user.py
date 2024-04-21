# user.py

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def update_email(self, new_email):
        self.email = new_email
